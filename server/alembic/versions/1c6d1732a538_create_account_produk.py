"""create account produk

Revision ID: 1c6d1732a538
Revises: 
Create Date: 2023-10-30 01:16:51.161021

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1c6d1732a538"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "produk",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("nama", sa.String(255), nullable=False),
        sa.Column("harga", sa.Integer, nullable=False),
        sa.Column("deskripsi", sa.Text, nullable=True),
        sa.Column("stok", sa.Integer, nullable=False),
        sa.Column("gambar", sa.String(255), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("product")
