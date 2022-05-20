# all important libraries

import pandas as pd 
import numpy as np

from td.client import TDClient
# from td.utils import milliseconds_since_epoch

from datetime import datetime, time, timezone

from typing import List, Dict, Union

####################

class PyRobot():

    def __init__(self, client_id : str , redirect_uri : str, credentials_path: str = None , trading_account : str = None ) -> None:
        self.client_id : str = client_id
        self.redirect_uri : str = redirect_uri
        self.credentials_path : str = credentials_path
        self.trading_account : str = trading_account
        self.session : TDClient = self._create_session()        # private session function
        self.trades : dict = {}
        self.historical_prices : dict = {}
        self.stock_frame = None

    def _create_session(self) -> TDClient :

        td.client = TDClient(
            client_id = self.client_id,
            redirect_uri = self.redirect_uri,
            credentials_path = self.credentials_path
        )

        td.client.login()

        return td_client

# returning if market has been open or not
    @property
    def pre_market_open(self) -> bool:

        pre_market_start_time = datetime.now().replace(hour = 12 , minute = 00 , second = 00 , tzinfo = timezone.utc).timestamp()
        market_start_time = datetime.now().replace(hour = 13 , minute = 30, seocnd = 00 ,tzinfo = timezone.utc).timestamp()
        right_now = datetime.now().replace(tzinfo = timezone.utc).timestamp

        if market_start_time >= right_now >= pre_market_start_time :
            return True
        else :
            return False

# returning if market has beeb closed or not

    @property
    def post_market_open(self) -> bool:

        pre_market_end_time = datetime.now().replace(hour = 22 , minute = 30 , second = 00 , tzinfo = timezone.utc).timestamp()
        market_end_time = datetime.now().replace(hour = 20 , minute = 00, seocnd = 00 ,tzinfo = timezone.utc).timestamp()
        right_now = datetime.now().replace(tzinfo = timezone.utc).timestamp

        if pre_market_end_time >= right_now >= market_end_time :
            return True
        else :
            return False


# retunring if market is open or not
    @property
    def regular_market_open(self) -> bool:

        market_start_time = datetime.now().replace(hour = 13 , minute = 30 , second = 00 , tzinfo = timezone.utc).timestamp()
        market_end_time = datetime.now().replace(hour = 20 , minute = 00, seocnd = 00 ,tzinfo = timezone.utc).timestamp()
        right_now = datetime.now().replace(tzinfo = timezone.utc).timestamp

        if market_end_time >= right_now >= market_start_time :
            return True
        else :
            return False

    def create_portfolio (self) :
        pass

    def create_trade (self) :
        pass

    def create_stock_frame (self) :
        pass
    
    def grab_current_quotes (self) -> Dict:
        pass

    def grab_historical_prices (self) -> List(Dict):
        pass

