from fastapi import APIRouter, Depends, status

from app.dependencies import get_repository
from app.domain.credit_card.repositories.card import CreditCardRepository
from app.domain.credit_card.schemas import CardCreateResponseSchema, CardCreateSchema
from app.domain.credit_card.service import CardService

router = APIRouter()


@router.get("/list", summary="List Cards", status_code=status.HTTP_200_OK)
async def get_cards(
    repository: CreditCardRepository = Depends(
        get_repository(repo_type=CreditCardRepository)
    ),
):
    cards = await CardService(repository=repository).get_all()
    return cards


@router.post(
    "/add",
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
    return card


@router.get("/detail/{id}", summary="Card Detail", status_code=status.HTTP_200_OK)
async def get_card(
    id: int,
    repository: CreditCardRepository = Depends(
        get_repository(repo_type=CreditCardRepository)
    ),
):
    card = await CardService(repository=repository).get_card_by_id(id=id)
    return card
