import os
import sys

import psycopg2 as dbapi2

INIT_STATEMENTS = [
     """
    create table if not exists movie(
        id serial primary key,
        name varchar not null,
        likes integer default 0 not null,
        dislikes integer default 0 not null,
        image varchar not null
    )
    """,
    """
    create table if not exists actor(
        id serial primary key,
        name varchar not null,
        likes integer default 0 not null,
        dislikes integer default 0 not null,
        image varchar not null
    )
    """,
    """
    create table if not exists index(
        movie_id integer references movie(id) on delete set null on update cascade,
        actor_id integer references actor(id) on delete set null on update cascade,
        primary key(movie_id,actor_id)
    )"""
]
#serial id her eleman eklendiğinde id yi +1 yapar
# varchar: string alması demek

def initialize(url):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor() #aradaki git gel yapan eleman
            for statement in INIT_STATEMENTS:
                cursor.execute(statement)
            cursor.close()

if __name__ == '__main__':
    url = os.getenv('DATABASE_URL')
    if url is None:
        print('Usage: DATABASE_URL=url pyhton dbinit.py ')
        sys.exit(1)
    initialize(url)