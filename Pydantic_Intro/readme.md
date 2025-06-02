# Pydantic Intro

## What is Pydantic?

[Pydantic](https://docs.pydantic.dev/) is a Python library used for data validation and settings management using Python type annotations. It enforces type checks and constraints at runtime, making data parsing and validation more reliable and developer-friendly. Pydantic is built on top of standard Python type hints, and it helps ensure that data entering your application is the correct type, shape, and within the expected constraints.

## Why Use Pydantic?

* Strong data validation using Python's type hints.
* Automatic data parsing (e.g., converting strings to integers if valid).
* Easy error handling and clear error messages.
* Great integration with modern frameworks like FastAPI.

## How Pydantic Helps in FastAPI

FastAPI, a modern web framework for building APIs with Python, heavily relies on Pydantic for:

* Request body validation: Pydantic models are used to define the structure of expected JSON inputs.
* Automatic documentation generation: FastAPI uses Pydantic's field definitions to generate OpenAPI documentation.
* Type safety and error handling: Pydantic ensures that API inputs conform to the declared schema.

By using Pydantic models, FastAPI becomes faster, more reliable, and easier to use, especially for building robust APIs quickly.

## Code Explanation: `Pydantic_intro`

```python
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# Define a Pydantic model representing patient data
class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Ebad', 'Syed'])]
    email: EmailStr  # Validates proper email format
    linkedin_url: AnyUrl  # Ensures the string is a valid URL
    age: int = Field(gt=0, lt=120)  # Must be between 1 and 119
    weight: Annotated[float, Field(gt=0, strict=True)]  # Strict float type, must be greater than 0
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]  # Optional list of strings, max 5 items
    contact_details: Dict[str, str]  # A dictionary containing contact info like phone or address

# Function to print selected patient details
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

# Sample dictionary representing patient data
patient_info = {
    'name': 'ebad',
    'email': 'mohammadebad1@hotmail.com',
    'linkedin_url': 'https://www.linkedin.com/in/syed-ebad-ml',
    'married': False,
    'allergies': ['milk'],
    'age': '28',  # Will be converted to int automatically by Pydantic
    'weight': 68.5,
    'contact_details': {'phone': '12345678'}
}

# Creating a Pydantic model instance using the dictionary
patient1 = Patient(**patient_info)

# Updating patient data using the defined function
update_patient_data(patient1)
```

## What I Did and What I Learned

In this `Pydantic_intro` script, I:

* Imported and used key classes and functions from the `pydantic` library.
* Defined a `Patient` model with strict data validation rules using `Field` and `Annotated`.
* Used various types including `EmailStr`, `AnyUrl`, `Optional`, `Dict`, and `List`.
* Created a sample patient dictionary and instantiated a model from it.
* Validated and parsed data automatically with Pydantic.
* Called a function to print selected patient attributes.

### What I Learned:

* How to use `Field` with metadata like `title`, `description`, `examples`, and value constraints.
* How to validate structured data using Pydantic models.
* How Pydantic simplifies parsing and ensures correct input types.
* How this validation can benefit frameworks like FastAPI.

This exercise was a great hands on introduction to Pydantic's capabilities and its role in modern Python development.
