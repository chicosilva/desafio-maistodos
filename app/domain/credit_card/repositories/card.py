from typing import List

from sqlalchemy.exc import DatabaseError

from app.domain.common.repository_base import RepositoryBase
from app.domain.credit_card.model import CreditCard


class CreditCardRepository(RepositoryBase):
    def __init__(self, session):
        super().__init__(session)
        self.entity_model = CreditCard

    async def get_all_contacts(self) -> List[CreditCard]:
        return self.query().all()

    async def get_card_by_id(self, id: int) -> CreditCard:
        return self.query().filter_by(id=id).one()

    async def save_card(self, person: CreditCard) -> CreditCard:
        try:
            return await self.save(person)
        except Exception as e:
            raise DatabaseError(e)
