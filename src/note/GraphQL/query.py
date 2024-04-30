import strawberry

from ..schemas import NoteOutput

@strawberry.type
class Query:
    
    @strawberry.field
    async def get_all_notes() -> list[NoteOutput | None]:
        return [NoteOutput(title="GraphQL", body=" не настроен")]