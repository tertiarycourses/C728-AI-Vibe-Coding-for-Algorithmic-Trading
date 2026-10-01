"""C728 Lab 2 checkpoint. Run from any directory; core dependencies are in ../trading_core.py."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from trading_core import prices,validate,indicators,backtest,metrics,plot,np,pd
out=Path(__file__).resolve().parent
import argparse
p=argparse.ArgumentParser(); p.add_argument("--csv"); p.add_argument("--url"); args=p.parse_args()
if args.csv and args.url: p.error("Choose csv OR url")
d=validate(pd.read_csv(args.csv or args.url)) if args.csv or args.url else validate(prices())
d.to_csv(out/"prices.csv",index=False)
for broken in [pd.concat([d,d.tail(1)]),d.assign(close=-1)]:
    try: validate(broken)
    except ValueError: pass
    else: raise AssertionError("Bad data accepted")
print(f"Validated {len(d)} rows; rejected duplicate and negative-price fixtures")
