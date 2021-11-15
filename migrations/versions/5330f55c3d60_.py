"""empty message

Revision ID: 5330f55c3d60
Revises: 
Create Date: 2021-11-06 08:51:57.541941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5330f55c3d60'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tbl_authors', sa.Column('email', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tbl_authors', 'email')
    # ### end Alembic commands ###
