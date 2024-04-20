"""Initial migration

Revision ID: 2e67e0a34975
Revises: 
Create Date: 2024-04-16 01:13:10.740480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e67e0a34975'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('photo_rating',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('photo_id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('photo_ratings')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('photo_ratings',
    sa.Column('id', sa.INTEGER(), nullable=True),
    sa.Column('photo_id', sa.INTEGER(), nullable=False),
    sa.Column('rating', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('photo_rating')
    # ### end Alembic commands ###
