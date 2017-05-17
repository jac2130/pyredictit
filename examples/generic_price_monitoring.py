from time import sleep
from pyredictit import pyredictit
import sys, os
sys.path.append(os.path.abspath("../../vars"))
from env_vars import *

pyredictit_api = pyredictit()
pyredictit_api.create_authed_session(username=user_name,password=password)
long_sell_contracts = pyredictit_api.search_for_contracts(market='politics', buy_sell='sell', type_='long')


my_contract = long_sell_contracts[0]
print(my_contract.name)
print(my_contract.type_)
while True:
    pyredictit_api.monitor_price_of_contract(contract=my_contract, monitor_type='generic',
                                             number_of_shares=0, trigger_price=0.00)
    sleep(30)
    
"""
>>> PENCE.TIEBREAK.033117
>>> Yes
>>> 76¢
>>> 76¢
"""
