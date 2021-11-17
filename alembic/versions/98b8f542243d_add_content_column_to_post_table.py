"""add content column to post table

Revision ID: 98b8f542243d
Revises: b0ebc545c1e6
Create Date: 2021-11-17 17:03:29.489802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98b8f542243d'
down_revision = 'b0ebc545c1e6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
