"""add mobile

Revision ID: 616e541d6bca
Revises: 5330f55c3d60
Create Date: 2021-11-06 09:00:39.284763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '616e541d6bca'
down_revision = '5330f55c3d60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tbl_authors', sa.Column('mobile', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tbl_authors', 'mobile')
    # ### end Alembic commands ###
