# Nested Models with Pydantic

## What is a Nested Model in Pydantic?

A **nested model** in Pydantic refers to a `BaseModel` that includes another `BaseModel` as a field. This is a powerful way to represent hierarchical or structured data. Nested models allow you to keep your data validation modular, reusable, and clean.

### Why Use Nested Models?

* To organize complex data structures more intuitively
* To validate each sub-structure independently
* To enable better type safety and code readability

## Code Explanation

```python
from pydantic import BaseModel

# Define an Address model with city, state, and pin code
class Address(BaseModel):
    city: str
    state: str
    pin: str

# Define a Patient model with a nested Address model
class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

# Create a dictionary that holds address information
address_dict = {'city': 'karachi', 'state': 'sindh', 'pin': '75290'}

# Create an Address object from the dictionary
address1 = Address(**address_dict)

# Create a dictionary for patient information, embedding the address object
patient_dict = {'name': 'ebad', 'gender': 'male', 'age': 28, 'address': address1}

# Create a Patient object from the dictionary
patient1 = Patient(**patient_dict)

# Dump the model data as a dictionary, including only specific fields
# In this case, only 'name' and 'address' are included
temp = patient1.model_dump(include={'name', 'address'})

# Check the type of the dumped result (should be a dict)
print(type(temp))
```

## What I Did in This File

* Defined two Pydantic models: `Address` and `Patient`.
* Used the `Address` model as a nested field inside the `Patient` model.
* Created instances of both models using dictionaries.
* Used `model_dump()` to selectively extract fields from the model.
* Verified the type of the result was a dictionary.

## What I Learned

* How to create and use nested models in Pydantic.
* How to instantiate nested models using dictionaries.
* How to selectively include fields using `model_dump()`.
* That nested models help keep code organized, readable, and easy to validate.

This structure is especially useful when working with APIs or structured JSON data, such as user profiles, configurations, or form submissions.
