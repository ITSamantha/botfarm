"""empty message

Revision ID: ac04a67060ce
Revises: 
Create Date: 2024-04-30 22:29:11.868374

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from src.database.models import *
from src.database.choices import *


# revision identifiers, used by Alembic.
revision: str = 'ac04a67060ce'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('login', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('project_id', sa.UUID(), nullable=False),
    sa.Column('env', sqlalchemy_utils.types.choice.ChoiceType(ENV_CHOICES, impl=sa.String(32)), nullable=False),
    sa.Column('domain', sqlalchemy_utils.types.choice.ChoiceType(DOMAIN_CHOICES, impl=sa.String(32)), nullable=False),
    sa.Column('locktime', sa.TIMESTAMP(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('projects')
    # ### end Alembic commands ###
