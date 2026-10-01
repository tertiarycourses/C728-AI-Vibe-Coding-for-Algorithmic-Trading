"""C728 Lab 1 checkpoint. Run from any directory; core dependencies are in ../trading_core.py."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from trading_core import prices,validate,indicators,backtest,metrics,plot,np,pd
out=Path(__file__).resolve().parent
d=validate(prices()); assert len(d)==756
print("Python environment OK; 756 deterministic observations")
d.head(10).to_csv(out/"preview.csv",index=False)
