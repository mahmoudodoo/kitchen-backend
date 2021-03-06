"""empty message

Revision ID: 92a72e3adb62
Revises: 
Create Date: 2021-04-02 12:13:26.629213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92a72e3adb62'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('public_id', sa.String(length=50), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_index(op.f('ix_admin_name'), 'admin', ['name'], unique=True)
    op.create_table('kitchen',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('public_id', sa.String(length=50), nullable=True),
    sa.Column('kitchen_name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('cook',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('public_id', sa.String(length=50), nullable=True),
    sa.Column('cook_name', sa.String(length=80), nullable=True),
    sa.Column('video_link', sa.String(length=300), nullable=True),
    sa.Column('steps', sa.String(length=300), nullable=True),
    sa.Column('kitchen_id', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['kitchen_id'], ['kitchen.public_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cook')
    op.drop_table('kitchen')
    op.drop_index(op.f('ix_admin_name'), table_name='admin')
    op.drop_table('admin')
    # ### end Alembic commands ###
