"""C728 Lab 5 checkpoint. Run from any directory; core dependencies are in ../trading_core.py."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from trading_core import prices,validate,indicators,backtest,metrics,plot,np,pd
out=Path(__file__).resolve().parent
d=backtest(prices()); assert d.position.equals(d.signal.shift(1).fillna(0))
assert (d.net_return<=d.position*d["return"]+1e-12).all()
flat=backtest(pd.DataFrame({"date":pd.bdate_range("2024-01-01",periods=100),"close":100.}))
assert flat.equity.eq(1).all()
d.to_csv(out/"backtest.csv",index=False); plot(d,out/"backtest.png")
print("Backtest verified: lag, costs and flat-price fixture")
