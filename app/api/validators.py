from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Dish, Menu, SubMenu


class BaseValidation:
    def __init__(self, model):
        self.model = model
        self.model_name = model.__tablename__

    async def check_exists(
        self,
        obj_id: str,
        session: AsyncSession,
    ):
        obj = await session.execute(
            select(self.model).where(
                self.model.id == obj_id,
            ),
        )
        obj = obj.scalars().first()
        if obj is None:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail=f'{self.model_name} not found',
            )
        return obj

    async def check_title(
        self,
        obj_title: str,
        session: AsyncSession,
    ):
        obj_id = await session.execute(
            select(self.model.id).where(
                self.model.title == obj_title,
            ),
        )
        obj_id = obj_id.scalars().first()
        if obj_id is not None:
            raise HTTPException(
                status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                detail=f'{self.model_name} с таким именем уже существует!',
            )
        return obj_id


menu_validator = BaseValidation(Menu)
submenu_validator = BaseValidation(SubMenu)
dish_validator = BaseValidation(Dish)
