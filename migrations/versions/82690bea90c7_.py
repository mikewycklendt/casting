"""empty message

Revision ID: 82690bea90c7
Revises: 
Create Date: 2020-08-17 18:24:09.278995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82690bea90c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('presiden_blackhat')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('presiden_blackhat',
    sa.Column('filename', sa.TEXT(), autoincrement=False, nullable=True)
    )
    # ### end Alembic commands ###
