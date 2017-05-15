from pyredictit import pyredictit
import sys, os
sys.path.append(os.path.abspath("../../vars"))
from env_vars import *

pyredictit_api = pyredictit()
pyredictit_api.create_authed_session(username=user_name,password=password)
pyredictit_api.current_gain_loss()
pyredictit_api.money_invested()
pyredictit_api.money_available()

"""
>>> You've lost $2.26.
>>> You have $39.22 currently invested in contracts.
>>> You have $0.22 available.
""
