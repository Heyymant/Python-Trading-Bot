from msilib.schema import SelfReg
from pickletools import optimize
from typing import Dict, List ,Union ,Optional
from sqlalchemy import false

from sympy import re, symbols


# str = None is equivalent t0 Optional[str]
class Portfolio():
    def __init__(self , account_number : Optional[str]) -> None:
        self.account_number = account_number
        self.positions ={}
        self.position_count = 0
        self.market_values = 0.0
        self.profit_loss = 0.0
        self.rist_tolrennce = 0.0
    
    def add_position(self, symbol : str, asset_type : str, quantity : int = 0, 
    purchase_price : float = 0.0, purchase_date : float = 0.0 ) ->Dict :
    
        self.positions[symbol] = {}
        self.positions[symbol]['symbol'] = symbol
        self.positions[symbol]['quantity'] = quantity
        self.positions[symbol]['purchase_data'] = purchase_date
        self.positions[symbol]['purchase_price'] = purchase_price
        self.positions[symbol]['asset_type'] = asset_type

        return self.positions

        # for adding positions 

    def add_positions(self , positions : List(Dict)) -> Dict :

        if isinstance (positions , List) :
            for position in positions :
                self.add_positions (
                    symbol = position['symbol'],
                    asset_type = position["asset_type"],
                    quantity = position.get('quantity ', 0),
                    purchase_price = position.get('purchase_price', 0.0),
                    purchase_date = position.get('purchase_date',0.0)
                )
            return self.positions

        else :
            return TypeError("Position must be a type of dictionary")

            #  for removing positions

    def remove_positions(self , symbol : str) -> tuple[bool, str] :
        if symbol in self.positions :
            del self.positions[symbol]
            return (True , "{Symbol} was successfully removed from the portfolio".format(symbol = symbol))
        else :
            return ('{Symbol} did not exist in the portfolio' .format(symbol = symbol))

    def in_portfolio(self, symbol : str ) -> bool :
        if symbol in self.positions:
            return True
        else :
             False
    
    def is_profitable(self, symbol : str , current_price = str) -> bool :
         
         purchase_price = self.positions[symbol]['purchase_price']

         if purchase_price >= current_price :
             return True
         elif purchase_price < current_price :
             return False 


    def total_allocation (self) :
        pass

    def risk_exposure(self) :
        pass

    def total_market_value(self) :
        pass