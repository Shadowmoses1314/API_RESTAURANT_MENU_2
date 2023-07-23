"""Add models

Revision ID: 3d98ad3a4faf
Revises:
Create Date: 2023-01-28 18:42:59.680742

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "3d98ad3a4faf"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "menu",
        sa.Column("title", sa.String(length=100), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("id", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("title"),
    )
    op.create_table(
        "submenu",
        sa.Column("title", sa.String(length=100), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("parent_id", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(["parent_id"], ["menu.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("title"),
    )
    op.create_table(
        "dish",
        sa.Column("title", sa.String(length=100), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("price", sa.String(), nullable=False),
        sa.Column("parent_id", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(["parent_id"], ["submenu.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("title"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("dish")
    op.drop_table("submenu")
    op.drop_table("menu")
    # ### end Alembic commands ###