"""users testing table

Revision ID: 55cd987340a6
Revises: 08a5c42be6af
Create Date: 2023-03-30 17:23:24.803172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55cd987340a6'
down_revision = '08a5c42be6af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Registergroup',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('groupid', sa.String(length=200), nullable=False),
    sa.Column('groupname', sa.String(length=200), nullable=False),
    sa.Column('adminname', sa.String(length=200), nullable=False),
    sa.Column('mobile', sa.Integer(), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('confirmpass', sa.String(length=200), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('groupid'),
    sa.UniqueConstraint('mobile')
    )
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userid', sa.String(length=200), nullable=False),
    sa.Column('firstname', sa.String(length=200), nullable=False),
    sa.Column('lastname', sa.String(length=200), nullable=False),
    sa.Column('phoneNo', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('confirmpass', sa.String(length=200), nullable=False),
    sa.Column('place', sa.String(length=200), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phoneNo'),
    sa.UniqueConstraint('userid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Users')
    op.drop_table('Registergroup')
    # ### end Alembic commands ###
