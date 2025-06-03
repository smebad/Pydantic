# Pydantic Model Validator Example

## What is a Model Validator in Pydantic?

A **Model Validator** in Pydantic is used to perform **custom validation** that goes beyond individual fields. It allows you to validate or transform the model **as a whole**, which is especially useful when validation logic depends on multiple fields together.

You use `@model_validator` with `mode="after"` to validate after the entire model has been parsed, meaning all fields are already available for logic checks.

## Why Use Model Validators?

* To enforce business rules that involve **multiple fields**.
* To ensure **consistency** and **integrity** in the model.
* To apply transformations or defaults based on multiple field values.

## Code Explanation

```python
from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    # Model-level validation: runs after all field values are available
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        # Patients older than 60 must have an emergency contact
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model

# Function to simulate updating patient data

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

# Creating patient data dictionary
patient_info = {
    'name': 'ebad',
    'email': 'mohammadebad1@hotmail.com',
    'age': '65',  # Pydantic will coerce this string to an integer
    'weight': 68.7,
    'married': False,
    'allergies': ['milk', 'dust'],
    'contact_details': {
        'phone': '1234567890',
        'emergency': '656565'  # This field satisfies the custom validator
    }
}

# Creating the Patient object, which will run all validators
patient1 = Patient(**patient_info)

# Updating patient data
update_patient_data(patient1)
```

## What I did in `model_validator.py`

* I defined a `Patient` model using Pydantic's `BaseModel`.
* I included fields like name, email, age, weight, marital status, allergies, and contact details.
* I used a `model_validator` to ensure that patients over the age of 60 must have an emergency contact in their `contact_details`.
* I created a dictionary with patient information and passed it into the model using unpacking (`**patient_info`).
* I called a function to print out patient data to simulate usage.

## What I Learned

* How to use Pydantic's `@model_validator` for complex, cross-field validation.
* That `model_validator(mode='after')` is executed **after** all fields are validated and type-coerced.
* How Pydantic automatically converts compatible types (e.g., `'65'` to `65` for `int`).
* How to raise custom error messages based on business rules.
