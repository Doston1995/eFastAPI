from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    id         :Optional[str]
    username   :Optional[str]
    password   :Optional[str]
    office     :Optional[str]
    is_staff   :Optional[bool]
    
    class Config:
        orm_mode = True
        schema_extra = {
            'example' :{
                'username'   :'Doston',
                'password'   :'123',
                'office'     :'Toshkent',
                'is_staff'   : False,
            }
        }