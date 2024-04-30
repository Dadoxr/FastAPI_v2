import strawberry


### send
@strawberry.type
class NoteOutput:
    title: str
    body: str

