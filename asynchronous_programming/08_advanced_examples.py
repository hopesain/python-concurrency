#### FIND THE ADVANCED EXAMPLES IN THIS FILE ###

"""
*** first example ***
Let's say we have a list of items. Possibly 20 items, basically orders, as in food orders at a restaurant. 
Assuming we have 20 customers in the room, the waiter gets five orders then hands over to the chef, 
as the chef is preparing the first five meals, he goes back to the customers and gets another five orders, 
when he hands over the second five orders, the first five, have already been prepared 
then he goes to deliver the first five and takes another five orders.

The cycle continues until all 20 orders are served. 
"""

import asyncio
from dataclasses import dataclass
from typing import List

@dataclass
class Order:
    id: int
    meal: str

    