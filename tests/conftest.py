import pytest
from app import domain
from loguru import logger


from app.database import engine
from app.dependencies import get_session_db
from app.internal.config import DATABASE_URL


@pytest.fixture(scope='session')
def metadata_create_all():
    meta_data = [
        domain.credit_card.model.EntityModelBase,
    ]
    if '_test' in DATABASE_URL:
        [m.metadata.create_all(bind=engine, checkfirst=True) for m in meta_data]


@pytest.fixture
def session_db():
    return next(get_session_db())


@pytest.fixture
def cap_logger(caplog):
    handler_id = logger.add(caplog.handler, format="{message}")

    yield caplog

    logger.remove(handler_id)


@pytest.fixture
@pytest.mark.usefixtures('cap_logger')
def token(client):
    response = client.post(
        '/users/login',
        json={'email': 'test@teste.com', 'password': '123123'},
    )

    return response.json()['access_token']