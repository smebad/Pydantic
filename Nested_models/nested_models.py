from pydantic import BaseModel

class Address(BaseModel):  

    city: str 
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'karachi', 'state': 'sindh', 'pin': '75290'}

address1 = Address(**address_dict)

patient_dict = {'name': 'ebad', 'gender': 'male', 'age': 28, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(include={'name', 'address'}) # include only name and address

print(type(temp))

