from sqlalchemy import Column, Date, Numeric, String

from app.domain.common.entity_model_base import EntityModelBase


class CreditCard(EntityModelBase):
    __tablename__ = "cards"

    exp_date = Column(Date(), nullable=False)
    holder = Column(String(150), nullable=False)
    number = Column(String(255), nullable=False)
    cvv = Column(Numeric(4), nullable=True)
    brand = Column(String(10), nullable=False)
