from typing import Optional
from pydantic import BaseModel

class Owner(BaseModel):
    ownerid:str
    ownername:str
    ownerlastname:str
    ownerusername:str
    ownerpassword:str
    owneremail:str
    
    
class Address(BaseModel):
    addressid:str
    addressmainstreet:str
    addressbackstreet:str
    addresssector:str
    
class Parkingland(BaseModel):
    ownerid:str
    plid:str
    addressid:str
    plsize:int
    plpropertydocument: Optional[str]  # Marcar como opcional
    
class Parkinglot(BaseModel):
    ownerid:str
    plid:str
    plotid:str
    plotstatus:str
    plotlength:float
    plotwidth:float
    
    
    