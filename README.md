# FastAPI example app

Stack: FastAPI, SQLAlchemy + Asyncpg, Alembic, strawberry-graphql

# StartApp
```python
mv var/.env.dev.sample var/.env.dev
docker compose -f docker-compose-local.yml up -d
poetry shell
alembic upgrade head
python3 main.py
```

# URLs
- localhost:8888/ - Hello World
- localhost:8888/docs - Interactive documentation
- localhost:8888/redoc - Documentation
- localhost:8888/rest/... - REST urls
- localhost:8888/graphql - GraphQL url
