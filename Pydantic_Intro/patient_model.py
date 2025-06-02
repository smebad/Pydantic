from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Ebad', 'Syed'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'ebad', 'email':'mohammadebad1@hotmail.com', 'linkedin_url':'https://www.linkedin.com/in/syed-ebad-ml', 'married': False, 'allergies': ['milk'],  'age': '28', 'weight': 68.5,'contact_details':{'phone':'12345678'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)