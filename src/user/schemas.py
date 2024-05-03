import strawberry

### send
@strawberry.type
class UserOutput:
    name: str
    email: str
    
### input
@strawberry.input
class UserEmailInput:
    email: str


@strawberry.input
class UserCreateInput(UserEmailInput):
    name: str | None = None
    password: str


@strawberry.input
class UserPutInput(UserCreateInput):
    pass


@strawberry.input
class UserPatchInput:
    name: str | None = None
    email: str | None = None 
    password: str | None = None
