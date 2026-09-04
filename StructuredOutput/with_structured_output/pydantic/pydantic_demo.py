from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    # name: str = "Default Name"  # Optional default value
    age: Optional[int] = None  # Optional field with default value None
    email: EmailStr  # Email field with validation
    cgpa: float = Field(gt=0, lt=10, default=9, description='A decimal value representing the cgpa of the student')  # CGPA field with validation
    
new_student = {'name': 'John Doe', 'email': 'john.doe@example.com', 'cgpa': 8.5}
# new_student = {'age': 20}
# new_student = {'age': '20'} # in this case, pydantic will try to convert the string '20' to an integer. this is called type coercion. if the conversion is successful, it will create a Student instance with age=20. if the conversion fails (e.g., if you provide a non-numeric string), pydantic will raise a validation error. 

student = Student(**new_student)

print(student)
print(type(student))

student_dict = dict(student)
print(student_dict)

student_json = student.model_dump_json()
print(student_json)