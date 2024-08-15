"""novas colunas

Revision ID: 090b786368f4
Revises: 5692068a6cfa
Create Date: 2024-08-15 19:49:16.950272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '090b786368f4'
down_revision = '5692068a6cfa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('escola', schema=None) as batch_op:
        batch_op.add_column(sa.Column('dono_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'user', ['dono_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('escola', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('dono_id')

    # ### end Alembic commands ###
