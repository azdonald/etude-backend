"""Change user profile table to TutorProfile

Revision ID: e8fa13dd9d0a
Revises: 0e74f8b7d218
Create Date: 2018-12-05 21:34:00.968160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8fa13dd9d0a'
down_revision = '0e74f8b7d218'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tutor_profile',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('bio', sa.String(length=255), nullable=True),
    sa.Column('rate', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user_profile')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profile',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('bio', sa.VARCHAR(length=255), nullable=True),
    sa.Column('rate', sa.NUMERIC(precision=10, scale=2), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('created_on', sa.DATETIME(), nullable=True),
    sa.Column('updated_on', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('tutor_profile')
    # ### end Alembic commands ###
