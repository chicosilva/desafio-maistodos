import pytest
from app.domain.credit_card.model import CreditCard
from datetime import date
from app.domain.credit_card.repositories.card import CreditCardRepository
from app.domain.credit_card.schemas import CardCreateSchema
from app.domain.credit_card.service import CardService

@pytest.fixture
@pytest.mark.usefixtures('session_db')
@pytest.mark.usefixtures('metadata_create_all')
def repository(metadata_create_all, session_db):
    return CreditCardRepository(session=session_db)

@pytest.fixture
def service(repository):
    return CardService(repository=repository)

@pytest.fixture
def card_schema():
    data = {
        'exp_date': '02/2026',
        'holder': 'Francisco A silva',
        'number': '4539578763621486',
        'cvv': '123'
    }
    return CardCreateSchema(**data)

@pytest.mark.usefixtures('cap_logger')
@pytest.mark.usefixtures('session_db')
@pytest.mark.asyncio
async def test_create_card(service, card_schema):
    card = await service.create_card(card_schema)
    assert isinstance(card, CreditCard)
    
    assert card.exp_date == date(2026, 2, 28)
    assert card.holder == 'Francisco A silva'
    assert card.number == '4539578763621486'
    assert card.cvv == 123

@pytest.mark.usefixtures('cap_logger')
@pytest.mark.usefixtures('session_db')
@pytest.mark.asyncio
async def test_get_cards(service, card_schema):
    cards = await service.get_all()
    assert isinstance(cards, list)
    assert len(cards) >= 0
