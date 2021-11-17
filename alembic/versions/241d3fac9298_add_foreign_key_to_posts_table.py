"""Add foreign-key to posts table

Revision ID: 241d3fac9298
Revises: 53bc597d7511
Create Date: 2021-11-17 17:16:30.088129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '241d3fac9298'
down_revision = '53bc597d7511'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_user_fk', source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('post_user_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
