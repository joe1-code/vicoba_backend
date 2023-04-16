"""created Newwindow column

Revision ID: 297b61198e07
Revises: 6a3debe48d38
Create Date: 2023-04-16 11:42:03.873041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '297b61198e07'
down_revision = '6a3debe48d38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Newwindow',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('windowid', sa.String(length=200), nullable=False),
    sa.Column('startdate', sa.DateTime(), nullable=True),
    sa.Column('payamount', sa.String(length=200), nullable=False),
    sa.Column('durationOne', sa.String(length=200), nullable=True),
    sa.Column('receivingpeople', sa.String(length=200), nullable=False),
    sa.Column('total', sa.String(length=200), nullable=True),
    sa.Column('durationTwo', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('Users', sa.Column('groupid', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Users', 'groupid')
    op.drop_table('Newwindow')
    # ### end Alembic commands ###