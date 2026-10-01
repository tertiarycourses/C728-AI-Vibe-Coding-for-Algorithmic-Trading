"""C728 Lab 3 checkpoint. Run from any directory; core dependencies are in ../trading_core.py."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from trading_core import prices,validate,indicators,backtest,metrics,plot,np,pd
out=Path(__file__).resolve().parent
d=indicators(prices()); assert d.slow.iloc[:49].isna().all()
assert np.isclose(d.fast.iloc[19],d.close.iloc[:20].mean())
plot(d,out/"indicators.png"); d.to_csv(out/"indicators.csv",index=False)
print("Indicators verified: 49 slow-window warm-up rows")
