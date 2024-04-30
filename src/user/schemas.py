import strawberry


### send
@strawberry.type
class UserOutput:
    email: str


### input
@strawberry.input
class UserBaseInput:
    email: str


@strawberry.input
class UserInput(UserBaseInput):
    password: str
