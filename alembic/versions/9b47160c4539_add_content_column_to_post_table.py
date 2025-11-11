"""add content column to post table

Revision ID: 9b47160c4539
Revises: f85b9f4cbff2
Create Date: 2025-11-11 15:05:30.597083

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b47160c4539'
down_revision: Union[str, Sequence[str], None] = 'f85b9f4cbff2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
