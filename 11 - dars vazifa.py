from database import Database

db = Database()

def add_article():
    article_title = input("Maqola nomini kiriting: ")
    article_content = input("Maqola tarkibini kiriting: ")
    db.insert_article(article_title, article_content)
    yes_no = input("Yana maqola qo'shasizmi? (yes/no): ").lower()
    if yes_no == 'yes':
        add_article()

def view_articles():
    articles = db.all_articles()
    if articles:
        print("Barcha maqolalar:")
        for article in articles:
            print('|', article[0], '|', article[1], '|', article[2], '|')
    else:
        print("Hech qanday maqola topilmadi.")

def del_article():
    view_articles()
    try:
        article_id = int(input("Enter the ID of the article you want to delete: "))
        db.delete_article(article_id)
        yes_no = input("Yana maqola o'chirmoqchisiz? (yes/no): ").lower()
        if yes_no == 'yes':
            del_article()
    except ValueError:
        print("Bunday maqola ID si mavjud emas.")

def help_command():
    print("Barcha komandalar:")
    print("add article - Yangi maqola yaratish")
    print("del article - Maqolani o'chirish")
    print("view articles - Hamma maqolani ko'rish")
    print("stop - To'xtatish")

def run():
    help_command()
    while True:
        command = input("Komandani kiriting: ").lower()

        if command == "stop":
            db.close()
            break
        elif command == "help":
            help_command()
        elif command == "add article":
            add_article()
        elif command == "del article":
            del_article()
        elif command == "view articles":
            view_articles()
        else:
            print("Kiritilgan kommanda mavjud emas")

if __name__ == "__main__":
    run()
