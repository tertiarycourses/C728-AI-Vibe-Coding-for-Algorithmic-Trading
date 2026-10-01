"""C728 Lab 4 checkpoint. Run from any directory; core dependencies are in ../trading_core.py."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from trading_core import prices,validate,indicators,backtest,metrics,plot,np,pd
out=Path(__file__).resolve().parent
d=indicators(prices()); changed=prices(); changed.loc[700:,"close"]*=2
assert indicators(changed).signal.iloc[:700].equals(d.signal.iloc[:700])
assert d.signal.iloc[:49].eq(0).all()
d[["date","signal"]].to_csv(out/"signals.csv",index=False)
print("Signals verified: future perturbation does not change earlier signals")
