import psycopg2

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="maqolalar",
            user="postgres",
            password="parol",
            host="localhost"
        )
        self.cur = self.conn.cursor()
        self.create_table_articles()

    def create_table_articles(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS articles (
                article_id SERIAL PRIMARY KEY,
                article_title TEXT,
                article_content TEXT
            )
        """)
        self.conn.commit()

    def insert_article(self, title, content):
        self.cur.execute("INSERT INTO articles (article_title, article_content) VALUES (%s, %s)", (title, content))
        self.conn.commit()

    def all_articles(self):
        self.cur.execute("SELECT * FROM articles")
        return self.cur.fetchall()

    def delete_article(self, article_id):
        self.cur.execute("DELETE FROM articles WHERE id = %s", (article_id,))
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()
