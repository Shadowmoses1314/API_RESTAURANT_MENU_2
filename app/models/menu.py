from sqlalchemy import Column, String, and_, func, select
from sqlalchemy.orm import column_property, relationship

from app.models.base import BaseModel
from app.models.dish import Dish
from app.models.submenu import SubMenu
from app.models.utils import generate_uuid


class Menu(BaseModel):
    id = Column(String, primary_key=True, default=generate_uuid)

    # Declare the relationships as usual
    submenus = relationship(
        'SubMenu', cascade='delete', backref='menu', lazy='selectin'
    )

    # Declare the column properties using SQLAlchemy annotations
    submenus_count = column_property(
        select(func.count(
            SubMenu.id)).where(SubMenu.parent_id == id).scalar_subquery(),
    )

    dishes_count = column_property(
        select(func.count(Dish.id))
        .join(SubMenu)
        .where(and_(SubMenu.parent_id == id, SubMenu.id == Dish.parent_id))
        .correlate_except(Dish)
        .scalar_subquery()
    )
