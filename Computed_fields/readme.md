# Pydantic Computed Field Example

## What is a Computed Field in Pydantic?

A **computed field** in Pydantic is a special property added to a model that is not directly passed during initialization, but instead is calculated from existing fields. It is useful when you want to derive some value (like `bmi`) from other fields (`weight` and `height`) and include it as part of the model.

Pydantic provides the `@computed_field` decorator to mark a property as computed, allowing it to be treated like any other model field (e.g., during serialization).

## Why Computed Fields are Useful

* Avoid redundant data storage.
* Automatically maintain consistency across derived values.
* Include calculated fields in API responses using FastAPI.

---

## Code Explanation

```python
from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float  # weight in kilograms
    height: float  # height in meters
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    # Computed field to calculate BMI
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('BMI', patient.bmi)
    print('updated')

# Sample patient data
patient_info = {
    'name': 'ebad',
    'email': 'mohammadebad1@hotmail.com',
    'age': '28',
    'weight': 68.7,
    'height': 1.74,
    'married': False,
    'allergies': ['milk', 'dust'],
    'contact_details': {'phone': '123456789', 'emergency': '656565'}
}

# Create Patient object with validation and type coercion
patient1 = Patient(**patient_info)

# Call update function
update_patient_data(patient1)
```

---

## What I did and what I learned:

In the `computed_fields.py` file:

* I learned how to use the `@computed_field` decorator provided by Pydantic.
* I created a `bmi` field that automatically calculates the patient's Body Mass Index using their weight and height.
* I understood how computed fields can be used for real-world applications like health-related APIs where such metrics are commonly needed.
* I practiced writing cleaner models by reducing the need to store derived values directly.

This helped reinforce the concept of model enrichment in Pydantic and its usefulness in FastAPI-based APIs or general data modeling workflows.

---

## Use Case

This approach is especially helpful in:

* Healthcare applications (e.g., BMI calculation).
* Financial systems (e.g., computing total price).
* Any domain where derived fields simplify client-side processing or response structures.