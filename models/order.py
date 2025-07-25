from datetime import datetime
import json
from uuid import uuid4

class Order:
    def __init__(
        self, 
        id: str,
        user_id: str,
        created_at: datetime,
        updated_at: datetime,
        ):
        self.id          = id
        self.user_id     = id
        self.created_at  = created_at
        self.updated_at  = updated_at
        
    
    def to_dict(self)-> dict:
        return {
            "id": self.id,          
            "user_id": self.user_id,            
            "created_at": self.created_at.strftime("%Y-%m-%dT%H:%M:%SZ"),  
            "updated_at": self.updated_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        
    @classmethod
    def from_dict(cls , data: dict):
        return cls(
            id=data['id'],
            user_id=data['user_id'],
            created_at=datetime.strptime(data['created_at'], "%Y-%m-%dT%H:%M:%SZ"),
            updated_at_at=datetime.strptime(data['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
        )
        
    @classmethod
    def load_orders(cls):
        with open("datebase/orders.json") as jsonfile:
            try:
                data =  json.load(jsonfile)   
                
                orders = []
                for item in data:
                    orders.append(cls.from_dict(item)) 
                
                print(orders)
    
            except:
                return []
            
    @classmethod 
    def save_orders(cls , orders):
        with open("database/orders.json" , "w") as jsonfile:
            data = [order.to_dict() for order in orders]
            json.dump(data, jsonfile, indent=2)
            
    @classmethod
    def create_order(cls , user_id):
            order = cls(
            str(uuid4()),
            user_id,
            datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            )
            
            orders = cls.load_orders()
            orders.append(order)
            cls.save_orders(orders)