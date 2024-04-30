from fastapi import APIRouter
from strawberry.tools import merge_types
from strawberry import Schema
from strawberry.fastapi import GraphQLRouter

from ..user.REST import user_rest_router
from ..note.REST import note_rest_router

from ..user.GraphQL import Query as UserQuery
from ..note.GraphQL import Query as NoteQuery


class MainRouter:
    def __init__(
        self,
        rest: APIRouter = APIRouter(),
        graphql: APIRouter = APIRouter(),
    ) -> None:
        self.rest = rest
        self.graphql = graphql


# init router
rest = APIRouter(prefix="/rest", tags=["REST"])
graphql = APIRouter(prefix="/graphql", tags=["GraphQL"])
main_router = MainRouter(rest=rest, graphql=graphql)


# GraphQL include
Query = merge_types("Query", (UserQuery, NoteQuery))
schema = Schema(query=Query)
graphql_app = GraphQLRouter(schema=schema, path="/")
main_router.graphql.include_router(router=graphql_app)


# REST include
app_routers = (user_rest_router, note_rest_router)

for router in app_routers:
    main_router.rest.include_router(router=router)
