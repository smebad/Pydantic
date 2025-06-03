# Pydantic Field Validators Example

## What is a Field Validator in Pydantic?

Field validators are methods in Pydantic models that allow you to add custom logic for validating or transforming the values of individual fields. They provide more control beyond basic type checking.

You define a field validator using the `@field_validator()` decorator, specifying the field name(s) to which the validation applies. These methods can:

* Enforce custom constraints
* Clean or modify values (e.g., capitalizing names)
* Raise custom errors

## How Field Validators Help

* Ensure input is correct before further processing.
* Prevent runtime issues by catching bad data early.
* Help maintain consistency and correctness in data models.

## Explanation of the Provided Code

```python
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str  # Patient's name
    email: EmailStr  # Must be a valid email address
    age: int  # Must be an integer
    weight: float  # Patient's weight
    married: bool  # Marital status
    allergies: List[str]  # List of allergies
    contact_details: Dict[str, str]  # Contact details (e.g., phone number)

    # Validator to restrict email domain
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'icloud.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value

    # Validator to transform the name to uppercase
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    # Validator to ensure age is between 0 and 100 (exclusive)
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')

# Function to print patient data

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

# Sample patient data
patient_info = {
    'name': 'ebad',
    'email': 'mohammadebad1@hotmail.com',
    'age': '28',  # Will be coerced to int automatically
    'weight': 68.7,
    'married': False,
    'allergies': ['dust'],
    'contact_details': {'phone': '1234567890'}
}

# Create a Patient instance (runs all validations)
patient1 = Patient(**patient_info)

# Call the function to print details
update_patient_data(patient1)
```

## What I Did and What I Learned

In this file (`field_validator.py`), I practiced using Pydantic's `@field_validator` to:

* Restrict email addresses to a set of allowed domains.
* Automatically convert the name field to uppercase.
* Ensure that the age is a realistic number between 1 and 99.

**What I Learned:**

* How to write and use custom validators using `@field_validator()`.
* How Pydantic can coerce types (like converting a string to an integer).
* How validations improve data quality and reduce bugs.
* How models and validation logic are automatically applied when using `**kwargs` to instantiate a model.

This helped reinforce my understanding of how Pydantic can be used for both data validation and transformation in real applications.
