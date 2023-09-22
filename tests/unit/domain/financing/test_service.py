import pytest

from app.domain.person.repositories.person import PersonRepository
from app.domain.person.schemas import PersonCreate
from app.domain.person.service import PersonService


@pytest.fixture
@pytest.mark.usefixtures("session_db")
@pytest.mark.usefixtures("metadata_create_all")
def repository(metadata_create_all, session_db):
    return PersonRepository(session=session_db)


@pytest.fixture
def service(repository):
    return PersonService(repository=repository)


@pytest.fixture
def person_schema():
    data = {
        "name": "Name 1",
        "email": "teste@teste.com",
    }
    return PersonCreate(**data)


@pytest.fixture()
@pytest.mark.asyncio
async def create_person(service, person_schema):
    return await service.create_person(person_schema)
