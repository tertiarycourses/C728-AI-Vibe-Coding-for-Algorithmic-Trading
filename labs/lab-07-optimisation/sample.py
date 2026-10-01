"""C728 Lab 7 checkpoint. Run from any directory; core dependencies are in ../trading_core.py."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from trading_core import prices,validate,indicators,backtest,metrics,plot,np,pd
out=Path(__file__).resolve().parent
import json
raw=prices(); split=504; rows=[]
for fast in [10,20,30]:
    for slow in [40,50,60]:
        m=metrics(backtest(raw.iloc[:split],fast,slow)); rows.append({"fast":fast,"slow":slow,**m})
ranking=pd.DataFrame(rows).sort_values("sharpe_rf0",ascending=False)
best=ranking.iloc[0]; fast=int(best.fast); slow=int(best.slow)
# Carry historical indicator context, then score holdout only; begin holdout flat.
d=backtest(raw,fast,slow); hold=d.iloc[split:].copy(); hold.iloc[0,hold.columns.get_loc("turnover")]=abs(hold.position.iloc[0])
hold["net_return"]=hold.position*hold["return"]-hold.turnover*.001
hold["equity"]=(1+hold.net_return).cumprod(); hold["drawdown"]=hold.equity/hold.equity.cummax()-1
ranking.to_csv(out/"training-grid.csv",index=False)
json.dump({"selected_on_training":{"fast":fast,"slow":slow},"holdout_once":metrics(hold)},open(out/"holdout.json","w"),indent=2)
print("9 train-only candidates; 252 untouched holdout observations")
