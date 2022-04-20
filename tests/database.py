import pytest
from fastapi.testclient import TestClient
from app.main import app

from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.database import get_db
from app.database import Base

sqlalchemy_db_url = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'
#sqlalchemy_db_url = 'postgresql://postgres:19021991@localhost:5433/fastapi_test'

engine = create_engine(sqlalchemy_db_url)
testing_session_local = sessionmaker(autocommit=False,autoflush=False,bind=engine)


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = testing_session_local()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    #run our code before we return our test
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    #run our code after our test finishes
    
