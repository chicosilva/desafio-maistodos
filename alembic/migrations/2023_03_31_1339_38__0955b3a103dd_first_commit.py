"""First commit

Revision ID: 0955b3a103dd
Revises: 
Create Date: 2023-03-31 13:39:38.855978

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "0955b3a103dd"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "cards",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("canceled_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("exp_date", sa.Date(), nullable=False),
        sa.Column("holder", sa.String(length=150), nullable=False),
        sa.Column("number", sa.String(length=255), nullable=False),
        sa.Column("brand", sa.String(length=10), nullable=False),
        sa.Column("cvv", sa.Numeric(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    pass
