"""C728 reproducible research utilities. Synthetic observations only by default."""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def prices():
    rng=np.random.default_rng(728)
    returns=rng.normal(0.0003,0.012,756)
    return pd.DataFrame({"date":pd.bdate_range("2023-01-02",periods=756),"close":100*np.cumprod(1+returns)})

def validate(df):
    df=df.copy(); df["date"]=pd.to_datetime(df["date"],errors="raise")
    df["close"]=pd.to_numeric(df["close"],errors="raise")
    if df.empty or df["date"].isna().any() or df["date"].duplicated().any() or not df["date"].is_monotonic_increasing:
        raise ValueError("Dates must be nonempty, unique and ascending")
    if not np.isfinite(df["close"]).all() or (df["close"]<=0).any():
        raise ValueError("Close must be finite and positive")
    return df

def indicators(df,fast=20,slow=50):
    if not 1<fast<slow: raise ValueError("Require 1 < fast < slow")
    d=validate(df); d["fast"]=d.close.rolling(fast).mean(); d["slow"]=d.close.rolling(slow).mean()
    d["signal"]=((d.fast>d.slow)&d.slow.notna()).astype(float)
    return d

def backtest(df,fast=20,slow=50,cost_bps=10):
    if cost_bps<0: raise ValueError("Cost must be nonnegative")
    d=indicators(df,fast,slow); d["return"]=d.close.pct_change().fillna(0)
    d["position"]=d.signal.shift(1).fillna(0)
    d["turnover"]=d.position.diff().abs().fillna(d.position.abs())
    d["net_return"]=d.position*d["return"]-d.turnover*cost_bps/10000
    d["equity"]=(1+d.net_return).cumprod(); d["benchmark"]=(1+d["return"]).cumprod()
    d["drawdown"]=d.equity/d.equity.cummax()-1
    return d

def metrics(d):
    r=d.net_return; vol=r.std(ddof=1)
    return {"total_return":float(d.equity.iloc[-1]-1),"sharpe_rf0":float(np.sqrt(252)*r.mean()/vol) if vol>0 else 0.,"max_drawdown":float(d.drawdown.min()),"turnover":float(d.turnover.sum())}

def plot(d,path):
    fig,axs=plt.subplots(3,1,figsize=(10,7),sharex=True)
    axs[0].plot(d.date,d.close,label="Synthetic close",color="#155e75")
    for c in ["fast","slow"]:
        if c in d: axs[0].plot(d.date,d[c],label=c)
    axs[0].legend(); axs[0].set_ylabel("Price")
    if "equity" in d:
        axs[1].plot(d.date,d.equity,label="Strategy, net"); axs[1].plot(d.date,d.benchmark,label="Buy and hold"); axs[1].legend()
        axs[2].fill_between(d.date,d.drawdown,0,color="#b91c1c",alpha=.4); axs[2].set_ylabel("Drawdown")
    else:
        axs[1].plot(d.date,d.close.pct_change()); axs[1].set_ylabel("Daily return")
        axs[2].plot(d.date,d.get("signal",pd.Series(0,index=d.index))); axs[2].set_ylabel("Signal")
    fig.suptitle("C728 • Synthetic teaching data • No forecast"); fig.tight_layout(); fig.savefig(path,dpi=150); plt.close(fig)
