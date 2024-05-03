from fastapi import APIRouter
from strawberry.tools import merge_types
from strawberry import Schema
from strawberry.fastapi import GraphQLRouter

from ..user import REST as userREST
from ..user import GraphQL as userGraphQL

from ..note import REST as noteREST
from ..note import GraphQL as noteGraphQL



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
Query = merge_types("Query", (userGraphQL.Query, noteGraphQL.Query))
Mutation = merge_types("Mutation", (userGraphQL.Mutation, noteGraphQL.Mutation))
schema = Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema=schema, path="/")
main_router.graphql.include_router(router=graphql_app)


# REST include
app_routers = (userREST.router, noteREST.router)

for router in app_routers:
    main_router.rest.include_router(router=router)
