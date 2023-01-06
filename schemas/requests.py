from pydantic import BaseModel
from typing import Optional

class CreateRequest(BaseModel):
    pinpp      :Optional[str]
    
    class Config:
        orm_mode = True
        schema_extra = {
            'example' :{
                'pinpp'   :'31234567891234',
            }
        }


class ShowRequest(BaseModel):

    id        :Optional[str]
    pinpp     :Optional[str]
    create_at :Optional[str]
    user_id   :Optional[str]

    class Config:
        orm_mode = True