import pytest
from datetime import date
from app.domain.credit_card.model import CreditCard


@pytest.mark.asyncio
@pytest.mark.usefixtures("cap_logger")
@pytest.mark.usefixtures("session_db")
def test_model_with_success(cap_logger, session_db):

    card = CreditCard(
        exp_date=date(2025, 12, 31),
        holder="John Doe",
        number="1234567890123456",
        cvv=123,
        brand="Visa"
    )

    session_db.add(card)
    session_db.commit()

    queried_card = session_db.query(CreditCard).filter_by(id=card.id).first()

    assert queried_card is not None
    assert queried_card.exp_date == date(2025, 12, 31)
    assert queried_card.holder == "John Doe"
    assert queried_card.number == "1234567890123456"
    assert queried_card.cvv == 123
    assert queried_card.brand == "Visa"


@pytest.mark.asyncio
@pytest.mark.usefixtures("cap_logger")
@pytest.mark.usefixtures("session_db")
def test_invalid_credit_card(session_db):
    invalid_card = CreditCard()

    session_db.add(invalid_card)
    with pytest.raises(Exception):
        session_db.commit()