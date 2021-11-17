"""Add last few column to post table

Revision ID: 726480f10a80
Revises: 241d3fac9298
Create Date: 2021-11-17 17:23:32.877269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '726480f10a80'
down_revision = '241d3fac9298'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False,
                                     server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                     nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
