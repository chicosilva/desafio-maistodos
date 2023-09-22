from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_session_db
from app.domain.credit_card.model import CreditCard

router = APIRouter()


@router.get("/healthcheck", summary="API is active?")
async def live(session_db: Session = Depends(get_session_db)) -> dict:

    count = session_db.query(CreditCard).count()

    return {"status": "alive", "count": count}
