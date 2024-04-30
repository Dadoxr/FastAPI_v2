import strawberry


@strawberry.type
class NoteOutput:
    title: str
    body: str