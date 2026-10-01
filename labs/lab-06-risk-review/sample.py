"""C728 Lab 6 checkpoint. Run from any directory; core dependencies are in ../trading_core.py."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from trading_core import prices,validate,indicators,backtest,metrics,plot,np,pd
out=Path(__file__).resolve().parent
import json
d=backtest(prices()); m=metrics(d)
assert m["max_drawdown"]<=0
known=pd.Series([1.,1.2,.9,1.3]); assert np.isclose((known/known.cummax()-1).min(),-.25)
json.dump(m,open(out/"metrics.json","w"),indent=2); plot(d,out/"risk.png")
print(json.dumps(m,indent=2)); print("Known drawdown fixture: -25%")
