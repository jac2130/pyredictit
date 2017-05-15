from time import sleep
from pyredictit import pyredictit
import sys, os
sys.path.append(os.path.abspath("../../vars"))
from env_vars import *

pyredictit_api = pyredictit()
pyredictit_api.create_authed_session(username=user_name,password=password)

pyredictit_api.get_my_contracts()

my_contract = pyredictit_api.my_contracts[0]
my_contract.get_current_volume()
print(my_contract.name)
print(my_contract.type_)
print(my_contract.volume)

"""
>>> PENCE.TIEBREAK.033117
>>> Yes
>>> There have been 595 shares traded today.
"""
