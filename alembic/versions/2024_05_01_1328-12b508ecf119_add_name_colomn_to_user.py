"""add name colomn to User

Revision ID: 12b508ecf119
Revises: 971ed5556e1f
Create Date: 2024-05-01 13:28:13.090099

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '12b508ecf119'
down_revision: Union[str, None] = '971ed5556e1f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.String(length=40), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'name')
    # ### end Alembic commands ###
