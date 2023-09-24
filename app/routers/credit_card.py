import uuid
from typing import List

from fastapi import APIRouter, Depends, status

from app.dependencies import get_repository
from app.domain.auth.auth_bearer import JWTBearer
from app.domain.credit_card.repositories.card import CreditCardRepository
from app.domain.credit_card.schemas import (CardCreateResponseSchema,
                                            CardCreateSchema,
                                            CardResponseSchema)
from app.domain.credit_card.service import CardService

router = APIRouter(
    prefix="/credit-card",
    tags=["credit-card"],
)

'''
JWTBearer is only considering authentication, in addition it could work with authorization as well
'''

@router.get(
    "/",
    dependencies=[Depends(JWTBearer())],
    summary="List Cards",
    status_code=status.HTTP_200_OK,
    response_model=List[CardResponseSchema],
)
async def get_cards(
    repository: CreditCardRepository = Depends(
        get_repository(repo_type=CreditCardRepository)
    ),
):
    cards = await CardService(repository=repository).get_all()
    return [CardResponseSchema(**card.__dict__).dict() for card in cards]


@router.post(
    "/",
    dependencies=[Depends(JWTBearer())],
    summary="Add Card",
    status_code=status.HTTP_201_CREATED,
    response_model=CardCreateResponseSchema,
)
async def add(
    data: CardCreateSchema,
    repository: CreditCardRepository = Depends(
        get_repository(repo_type=CreditCardRepository)
    ),
):
    card = await CardService(repository=repository).create_card(schema=data)

    return CardCreateResponseSchema(**card.__dict__).dict()


@router.get(
    "/{id}",
    dependencies=[Depends(JWTBearer())],
    summary="Card Detail",
    status_code=status.HTTP_200_OK,
    response_model=CardResponseSchema,
)
async def get_card(
    id: uuid.UUID,
    repository: CreditCardRepository = Depends(
        get_repository(repo_type=CreditCardRepository),
    ),
):
    card = await CardService(repository=repository).get_card_by_id(id=id)
    return CardResponseSchema(**card.__dict__)
