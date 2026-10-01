"""C728 Lab 8 checkpoint. Run from any directory; core dependencies are in ../trading_core.py."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from trading_core import prices,validate,indicators,backtest,metrics,plot,np,pd
out=Path(__file__).resolve().parent
import argparse,json,os,urllib.request
p=argparse.ArgumentParser(); p.add_argument("--paper-account",action="store_true"); args=p.parse_args()
if args.paper_account:
    # Read-only account connection: no order endpoint exists in this sample.
    key=os.environ.get("APCA_API_KEY_ID"); secret=os.environ.get("APCA_API_SECRET_KEY")
    if not key or not secret: raise SystemExit("Set paper credentials locally in environment variables")
    req=urllib.request.Request("https://paper-api.alpaca.markets/v2/account",headers={"APCA-API-KEY-ID":key,"APCA-API-SECRET-KEY":secret})
    try:
        with urllib.request.urlopen(req,timeout=15) as response: account=json.load(response)
        print("Paper connection OK; status:",account.get("status","UNKNOWN"))
    except Exception: raise SystemExit("Paper account read failed; check network and paper credentials")
seen=set(); events=[]
def submit(order_id,qty,stale=False,halt=False):
    reason="duplicate" if order_id in seen else "halted" if halt else "stale" if stale else "limit" if qty>10 or qty<=0 else "simulated"
    if reason=="simulated": seen.add(order_id)
    events.append({"order_id":order_id,"quantity":qty,"status":reason}); return reason
assert submit("demo-1",1)=="simulated"
assert submit("demo-1",1)=="duplicate"
assert submit("demo-2",1,stale=True)=="stale"
assert submit("demo-3",11)=="limit"
assert submit("demo-4",1,halt=True)=="halted"
(out/"events.jsonl").write_text("\n".join(json.dumps(e) for e in events)+"\n")
print("5 monitored events: simulated, duplicate, stale, limit, halted; no real orders")
