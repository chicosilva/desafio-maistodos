import calendar
from datetime import date, datetime
from typing import Optional

from creditcard import CreditCard
from pydantic import BaseModel, Field, field_validator


class CardCreateSchema(BaseModel):
    exp_date: str
    holder: str = Field(min_length=2)
    number: str
    cvv: Optional[str] = Field(min_length=3, max_length=4, default=None)
    brand: str = None

    @field_validator("exp_date")
    @classmethod
    def exp_date_format(cls, value: str) -> str:
        _due_date = datetime.strptime(value, "%m/%Y").date()

        if _due_date < date.today():
            raise ValueError("Due date must be greater than today")

        last_day = cls.last_day_of_month(year=_due_date.year, month=_due_date.month)
        _due_date = f"{last_day}/{value}"

        return datetime.strptime(_due_date, "%d/%m/%Y").date()

    @classmethod
    def last_day_of_month(cls, year: int, month: int) -> int:
        _, last_day = calendar.monthrange(year, month)
        return last_day

    @field_validator("cvv")
    @classmethod
    def cvv_validate(cls, value: str) -> str:
        if value and not value.isnumeric():
            raise ValueError("CVV must be numeric")

        return int(value)

    @field_validator("number")
    @classmethod
    def number_validate(cls, value: str) -> str:
        # Todo: implement hash to write card
        card_number = value
        cc = CreditCard(card_number)

        if not cc.is_valid():
            raise ValueError("Invalid card number")

        return value


class CardCreateResponseSchema(BaseModel):
    exp_date: date
    holder: str
    number: str
    cvv: int
    brand: str
