# Pydantic Serialization Example

## What is Serialization in Pydantic?

Serialization in Pydantic refers to the process of converting a Pydantic model (Python object) into a serializable data format such as a dictionary. This is useful when you want to export data, send it through an API, or store it in a database or a file format like JSON.

Pydantic provides the `model_dump()` method to convert models into dictionaries. This method also allows you to control what gets included or excluded in the output using options like `exclude_unset`, `include`, and `exclude`.

* `exclude_unset=True`: Only includes fields explicitly set during model creation (ignores default values).
* `include={}` or `exclude={}`: Controls specific fields to include or exclude in the output.

## Code Explanation

```python
from pydantic import BaseModel

# Define a nested Address model
class Address(BaseModel):
    city: str
    state: str
    pin: str

# Define the Patient model, which includes an Address model as a nested field
class Patient(BaseModel):
    name: str
    gender: str = 'Male'  # Default value provided
    age: int
    address: Address

# Create a dictionary representing address information
address_dict = {'city': 'karachi', 'state': 'sindh', 'pin': '75290'}

# Initialize Address model from dictionary
address1 = Address(**address_dict)

# Create a dictionary with partial Patient data (gender is omitted, so default will be used)
patient_dict = {'name': 'ebad', 'age': 28, 'address': address1}

# Initialize Patient model with data
patient1 = Patient(**patient_dict)

# Serialize the model into a dictionary, excluding fields that were not explicitly set
# Since gender was not set in patient_dict, it will not appear in the output
temp = patient1.model_dump(exclude_unset=True)

# Print the serialized data and its type
print(temp)            # Output: {'name': 'ebad', 'age': 28, 'address': {'city': 'karachi', 'state': 'sindh', 'pin': '75290'}}
print(type(temp))      # Output: <class 'dict'>
```

## What I Did and Learned in `serialization.py`

* You created a nested Pydantic model structure using `Address` and `Patient`.
* You practiced initializing a model from dictionaries using unpacking (`**` operator).
* You learned how to use `model_dump(exclude_unset=True)` to exclude default values from the serialized output.
* You verified that the serialization returned a `dict` type.

### Takeaway:

I now understand how Pydantic handles serialization, which is critical when working with APIs and storing structured data. Knowing when and how to exclude unset or default values gives you more control over data cleanliness and communication in applications.
