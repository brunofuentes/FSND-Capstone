"""empty message

Revision ID: 203efabea34c
Revises: 9f7a09c4c40b
Create Date: 2021-12-20 20:56:00.404026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '203efabea34c'
down_revision = '9f7a09c4c40b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movie', 'subtitle')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie', sa.Column('subtitle', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
