from database import db

def add_post():
    post_title = input("Enter post title: ")
    db.insert_post(post_title)
    yes_no = input("Do you want to add another post? (yes/no): ").lower()
    if yes_no == 'yes':
        add_post()

def view_posts():
    posts = db.all_posts()
    if posts:
        print("All Posts:")
        for post in posts:
            print('|', post[0], '|', post[1], '|', post[3], '|')  # Print post_id, post_title, and post_created
    else:
        print("No posts found.")


def del_post():
    view_posts()
    try:
        post_id = int(input("Enter the ID of the post you want to delete: "))
        db.delete_post(post_id)
        yes_no = input("Do you want to delete another post? (yes/no): ").lower()
        if yes_no == 'yes':
            del_post()
    except ValueError:
        print("Please enter a valid post ID.")

def help_command():
    print("Available commands:")
    print("add post - Add a new post")
    print("del post - Delete a post")
    print("view posts - View all posts")
    print("stop - Stop the program")

def run():
    help_command()  # Display available commands initially
    while True:
        command = input("Enter a command: ").lower()

        if command == "stop":
            break
        elif command == "help":
            help_command()
        elif command == "add post":
            add_post()
        elif command == "del post":
            del_post()
        elif command == "view posts":
            view_posts()
        else:
            print("Invalid command. Type 'help' to see available commands.")

if __name__ == "__main__":
    db.create_table_posts()
    run()
