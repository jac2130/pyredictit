from pyredictit import pyredictit
import sys, os
sys.path.append(os.path.abspath("../../vars"))
from env_vars import *

pyredictit_api = pyredictit()
pyredictit_api.create_authed_session(username=user_name,password=password)

pyredictit_api.current_gain_loss()

#>>> $0.00
