"""empty message

Revision ID: 585f5d5c9fbf
Revises: 1c41f00ff38a
Create Date: 2014-08-08 19:59:57.786139

"""

# revision identifiers, used by Alembic.
revision = '585f5d5c9fbf'
down_revision = '1c41f00ff38a'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('article_id', sa.Integer(), nullable=True),
    sa.Column('author', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['article_id'], ['article.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column(u'article', 'author',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True,
               existing_server_default='')
    op.alter_column(u'article', 'category',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True,
               existing_server_default='')
    op.alter_column(u'article', 'content',
               existing_type=mysql.TEXT(),
               nullable=True)
    op.alter_column(u'article', 'date_created',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column(u'article', 'title',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True,
               existing_server_default='')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(u'article', 'title',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False,
               existing_server_default='')
    op.alter_column(u'article', 'date_created',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column(u'article', 'content',
               existing_type=mysql.TEXT(),
               nullable=False)
    op.alter_column(u'article', 'category',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False,
               existing_server_default='')
    op.alter_column(u'article', 'author',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False,
               existing_server_default='')
    op.drop_table('comment')
    ### end Alembic commands ###
