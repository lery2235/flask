"""empty message

Revision ID: 912140edcb09
Revises: 0732676d553e
Create Date: 2024-01-02 09:42:21.200305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '912140edcb09'
down_revision = '0732676d553e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_question')
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(batch_op.f('fk_question_user_id_user'), 'user', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_question_user_id_user'), type_='foreignkey')
        batch_op.drop_column('user_id')

    op.create_table('_alembic_tmp_question',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('subject', sa.VARCHAR(length=200), nullable=False),
    sa.Column('content', sa.TEXT(), nullable=False),
    sa.Column('create_date', sa.DATETIME(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_question_user_id_user', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###