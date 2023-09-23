from sqlalchemy import Column, Date, Numeric, String

from app.domain.common.entity_model_base import EntityModelBase
import uuid


def generate_uuid():
    return str(uuid.uuid4())


class CreditCard(EntityModelBase):
    __tablename__ = "cards"

    id = Column(String, name="id", primary_key=True, default=generate_uuid)
    exp_date = Column(Date(), nullable=False)
    holder = Column(String(150), nullable=False)
    number = Column(String(255), nullable=False)
    cvv = Column(Numeric(4), nullable=True)
    brand = Column(String(10), nullable=False)
