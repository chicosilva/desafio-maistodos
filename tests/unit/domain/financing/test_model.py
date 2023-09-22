import pytest

from app.domain.person.model import Person


@pytest.mark.asyncio
@pytest.mark.usefixtures("cap_logger")
def test_model_with_error(cap_logger):

    person = Person(name="unknowfund")

    with pytest.raises(Exception, match="Key not found"):
        person.name
