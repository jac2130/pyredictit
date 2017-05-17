from pyredictit import pyredictit
import json
import sys, os
sys.path.append(os.path.abspath("../../vars"))
from env_vars import *

pyredictit_api = pyredictit()
pyredictit_api.create_authed_session(username=user_name,password=password)
long_sell_contracts = pyredictit_api.search_for_contracts(market='politics', buy_sell='sell', type_='long')

out = {}
for contract in long_sell_contracts:
    #print('------')
    #for item in dir(contract):
    
    cont=contract.__dict__    
    market= cont["market"]
    if not market in out.keys():
        out[market]={}
        out[market]["outcomes"]={}
        
    if cont["name"] == "Long":
        out[market]["outcomes"][cont["cid"]] = {"outcome": "yes"}
        #print("outcome: " + "yes")
    else:
        out[market]["outcomes"][cont["cid"]]={"outcome": cont["name"]}
        
    for key in list(set(cont.keys())- set(["name", "market", "cid"])):
        out[market]["outcomes"][cont["cid"]][key]=str(cont[key])
        
with open("bets.json", "w") as f:
    f.write(json.dumps(out))        
