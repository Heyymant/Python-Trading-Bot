# all important libraries

import pandas as pd 
import numpy as np

from td.client import TDClient
# from td.utils import milliseconds_since_epoch

from datetime import datetime, time, timezone

from typing import List, Dict, Union

####################

class PyRobot():

    def __init__(self, client_id : str , rediredct_uri : str, credentials_path: str = None , trading_account : str = None ) -> None:
        self.client_id : str = client_id
        self.redirect_uri : str = rediredct_uri
        self.credentials_path : str = credentials_path
        self.trading_account : str = trading_account
        self.session : TDClient = self._create_session()        # private session function