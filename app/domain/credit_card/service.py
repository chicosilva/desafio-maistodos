import uuid
from dataclasses import dataclass
from typing import List

from creditcard import CreditCard as CreditCardValidator

from app.domain.common.service_base import ServiceBase
from app.domain.credit_card.model import CreditCard
from app.domain.credit_card.repositories.card import CreditCardRepository
from app.domain.credit_card.schemas import CardCreateSchema


@dataclass
class CardService(ServiceBase):
    repository: CreditCardRepository

    async def get_all(self) -> List[CreditCard]:
        return await self.repository.get_all()

    async def get_card_by_id(self, id: uuid.UUID) -> CreditCard:
        return await self.repository.get_card_by_id(id=id)

    async def create_card(self, schema: CardCreateSchema) -> CreditCard:
        
        '''
        The best way to store the number (schema.numbe) field is to tokenize it or create a hash, 
        for example, but for testing purposes I left it as full text, 
        remembering that full text is not a good security practice
        '''
        
        card = CreditCard(
            exp_date=schema.exp_date,
            holder=schema.holder,
            number=schema.number,
            cvv=schema.cvv,
            brand=CreditCardValidator(schema.number).get_brand(),
        )

        return await self.repository.save_card(card)
