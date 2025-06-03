from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'karachi', 'state': 'sindh', 'pin': '75290'}

address1 = Address(**address_dict)

patient_dict = {'name': 'ebad', 'age': 28, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(exclude_unset=True)

print(temp)
print(type(temp))