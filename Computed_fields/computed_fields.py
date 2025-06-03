from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float # for kilograms
    height: float # for meters
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field # decorator for computed fields
    @property
    def bmi(self) -> float: # body mass index
        bmi = round(self.weight/(self.height**2),2) # calculating BMI
        return bmi



def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('BMI', patient.bmi)
    print('updated')

patient_info = {'name':'ebad', 'email':'mohammadebad1@hotmail.com', 'age': '28', 'weight': 68.7, 'height': 1.74, 'married': False, 'allergies': ['milk', 'dust'], 'contact_details':{'phone':'123456789', 'emergency':'656565'}}

patient1 = Patient(**patient_info) 

update_patient_data(patient1)