"""create posts table

Revision ID: b0ebc545c1e6
Revises: 
Create Date: 2021-11-17 16:53:32.598157

"""
from typing import Text
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0ebc545c1e6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True)
    , sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
