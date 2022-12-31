user = {"username": "gholi", "access_level": "guest"}




def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin Permission for {user['username']}"

    return secure_function

@make_secure
def get_admin_password():
    return "1234"

get_admin_password = make_secure(get_admin_password)


print(get_admin_password())