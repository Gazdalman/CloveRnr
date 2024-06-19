"""empty message

Revision ID: 086c3f3e27ba
Revises: 528ddb279a88
Create Date: 2024-06-19 09:15:10.272023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '086c3f3e27ba'
down_revision = '528ddb279a88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('spots', schema=None) as batch_op:
        batch_op.add_column(sa.Column('city', sa.String(length=150), nullable=False))
        batch_op.add_column(sa.Column('state', sa.String(length=150), nullable=False))
        batch_op.drop_column('location')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('spots', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location', sa.VARCHAR(length=150), nullable=True))
        batch_op.drop_column('state')
        batch_op.drop_column('city')

    # ### end Alembic commands ###
