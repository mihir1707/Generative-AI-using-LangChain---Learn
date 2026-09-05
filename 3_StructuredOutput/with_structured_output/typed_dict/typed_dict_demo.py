from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

newPerson: Person = {
    'name': 'Rohit',
    'age': 39 # also can be use string instead of int Like 'age': '39'
}
