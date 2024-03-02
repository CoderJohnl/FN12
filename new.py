from database import db

def add_posts():
    post = input("Postni kiriting: ")
    db.insert_post(post)
    yes_no = input("Yana post qo'shasizmi? yes/no: ").lower()
    if yes_no == 'yes':
        add_posts()

def view_posts():
    posts = db.all_posts()
    for post in posts:
        post_id, post_name = post
        print('|', post_id, '|', post_name, '|')


def del_posts():
    view_posts()
    post_id = int(input("O'chirmoqchi bo'lgan postni idsini kiriting:  "))
    db.delete_posts(post_id)
    yes_no = input("Yana postni o'chirasizmi? yes/no: ").lower()
    if yes_no == 'yes':
        del_posts()

def run ():
    while True:
        command = input("Buyruqni kiriting: ").lower()

        if command == "stop":
            break
        elif command == "help":
            pass
        elif command == "add post":
            add_posts()
        elif command == "del post":
            del_posts()
        elif command == "view posts":
            view_posts()
if __name__ == "__main__":
    db.create_table_posts()
    db.create_table_posts()
    run()
