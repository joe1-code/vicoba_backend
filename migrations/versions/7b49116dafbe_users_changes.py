"""users changes

Revision ID: 7b49116dafbe
Revises: 55cd987340a6
Create Date: 2023-03-30 17:25:24.092313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b49116dafbe'
down_revision = '55cd987340a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('Users_userid_key', 'Users', type_='unique')
    op.drop_column('Users', 'userid')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Users', sa.Column('userid', sa.VARCHAR(length=200), autoincrement=False, nullable=False))
    op.create_unique_constraint('Users_userid_key', 'Users', ['userid'])
    # ### end Alembic commands ###