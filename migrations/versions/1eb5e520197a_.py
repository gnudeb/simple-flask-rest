"""empty message

Revision ID: 1eb5e520197a
Revises: a5be82245fdd
Create Date: 2017-10-29 13:40:11.606677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1eb5e520197a'
down_revision = 'a5be82245fdd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('first_name', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('hashed_password', sa.String(length=128), nullable=True))
    op.add_column('user', sa.Column('last_name', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('plain_password', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('user_name', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'user_name')
    op.drop_column('user', 'plain_password')
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'hashed_password')
    op.drop_column('user', 'first_name')
    # ### end Alembic commands ###
