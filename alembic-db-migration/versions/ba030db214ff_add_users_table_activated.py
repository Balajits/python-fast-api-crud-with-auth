"""add users table activated

Revision ID: ba030db214ff
Revises: 
Create Date: 2022-01-13 19:42:39.864256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba030db214ff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('is_activated', sa.Boolean()))
    # pass


def downgrade():
    pass
