from services import service_one, service_three, service_two


def main():
    """
    Main function to run services.
    """
    posts = service_one.get_posts()
    users = service_two.get_users()
    todos = service_three.get_todos()

    print(f"Number of posts fetched: {len(posts)}")
    print(f"Number of users fetched: {len(users)}")
    print(f"Number of todos fetched: {len(todos)}")


if __name__ == "__main__":
    main()
