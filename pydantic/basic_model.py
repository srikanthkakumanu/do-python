from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "John Doe"
    age: int


user = User(id=1, age=30)  # valid
print(user.id)
user = User(id="1", age=30)  # valid, id will be converted to int
print(user.id)
# user = User(id='abc', age=30) # invalid, raises ValidationError
print(f"model_computed_fields: {user.model_computed_fields}")
print(f"model_json_schema: {user.model_json_schema}")
print(f"model_json_schema(by_alias=True): {user.model_json_schema(by_alias=True)}")
print(f"model_fields: {user.model_fields}")
print(f"model_fields_set: {user.model_fields_set}")
print(f"model_dump: {user.model_dump()}")
print(f"model_dump_json: {user.model_dump_json()}")
print(f"model_dump_json(indent=2): {user.model_dump_json(indent=2)}")
print(
    f"model_dump_json(exclude={'id'}): {user.model_dump_json(exclude={'id'})}",
    user.model_computed_fields,
)
print(f"model_json_schema: {user.model_json_schema}")
print(f"model_json_schema(by_alias=True): {user.model_json_schema(by_alias=True)}")
print(f"model_fields: {user.model_fields}")
print(f"model_fields_set: {user.model_fields_set}")
print(f"model_dump: {user.model_dump()}")
print(f"model_dump_json: {user.model_dump_json()}")
print(f"model_dump_json(indent=2): {user.model_dump_json(indent=2)}")
print(f'model_dump_json(exclude={{"id"}}): {user.model_dump_json(exclude={"id"})}')
print(
    f'model_dump_json(exclude={{"id"}}, indent=2): {user.model_dump_json(exclude={"id"}, indent=2)}'
)
print(
    f'model_dump_json(exclude={{"id"}}, indent=2, by_alias=True): {user.model_dump_json(exclude={"id"}, indent=2, by_alias=True)}'
)
