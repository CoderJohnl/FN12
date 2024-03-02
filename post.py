import psycopg2

class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database='kun_uz',
            user='postgres',
            password='2004',
            host='localhost'
        )

    def manager(self, sql, *args,
                fetchone: bool = False,
                fetchall: bool = False,
                fetchmany: bool = False,
                commit: bool = False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    result = db.commit()
                elif fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
                elif fetchmany:
                    result = cursor.fetchmany()
            return result

    def create_table_posts(self):
        sql = '''CREATE TABLE IF NOT EXISTS posts(
               post_id SERIAL PRIMARY KEY,
               post_name varchar(20) UNIQUE
        )'''
        self.manager(sql, commit=True)

    def insert_posts(self, post):
        sql = '''INSERT INTO posts(post_name) VALUES (%s) ON CONFLICT DO NOTHING'''
        self.manager(sql, post, commit=True)

    def delete_posts(self, post_id):
        sql = '''DELETE FROM posts WHERE post_id = %s'''
        self.manager(sql, post_id, commit=True)
    def all_posts(self):
        sql = '''SELECT * FROM posts'''
        return self.manager(sql, fetchall=True)
    def create_table_posts(self):
        sql = '''CREATE TABLE IF NOT EXISTS posts(
               post_id SERIAL PRIMARY KEY,
               post_title VARCHAR(255),
               post_content TEXT,
               post_created TIMESTAMP DEFAULT NOW(),
               post_id INTEGER REFERENCES posts(post_id) ON DELETE CASCADE
         )'''
        self.manager(sql, commit=True)


db = DataBase()
