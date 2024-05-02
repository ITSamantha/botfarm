"""empty message

Revision ID: c5066f662af2
Revises: bb856312326a
Create Date: 2024-05-02 19:19:24.618751

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision: str = 'c5066f662af2'
down_revision: Union[str, None] = 'bb856312326a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'login',
               existing_type=sa.VARCHAR(length=128),
               type_=sqlalchemy_utils.types.email.EmailType(length=255),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'login',
               existing_type=sqlalchemy_utils.types.email.EmailType(length=255),
               type_=sa.VARCHAR(length=128),
               existing_nullable=False)
    # ### end Alembic commands ###
