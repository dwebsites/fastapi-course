"""Add user table

Revision ID: 53bc597d7511
Revises: 98b8f542243d
Create Date: 2021-11-17 17:07:55.723653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53bc597d7511'
down_revision = '98b8f542243d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
                                server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
