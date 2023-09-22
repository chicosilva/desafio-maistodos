from typing import Any, List, Type

from sqlalchemy.orm import Session

from app.domain.common.entity_model_base import EntityModelBase


class RepositoryBase:
    __abstract__ = True

    def __init__(self, session: Session):
        self.session_db = session
        self.entity_model = EntityModelBase

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[tuple[Any]]:
        return self.session_db.query(self.entity_model).offset(skip).limit(limit).all()

    async def get_by_id(self, model_id: int) -> Type[EntityModelBase] | None:
        return self.session_db.query(self.entity_model).filter_by(id=model_id).one()

    async def find_by_id(self, model_id: int) -> tuple[Any] | None:
        return self.session_db.query(self.entity_model).filter_by(id=model_id).first()

    async def save(self, model) -> EntityModelBase:
        self.session_db.add(model)
        self.session_db.commit()
        self.session_db.refresh(model)

        return model

    def query(self):
        return self.session_db.query(self.entity_model)
