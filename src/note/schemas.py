import strawberry


### send
@strawberry.type
class NoteOutput:
    id: int
    title: str
    body: str


### input
@strawberry.input
class NoteCreateInput:
    title: str
    body: str


@strawberry.input
class NotePutInput(NoteCreateInput):
    id: int


@strawberry.input
class NotePatchInput(NotePutInput):
    title: str | None = None
    body: str | None = None
