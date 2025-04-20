

if __name__ == "__main__":

    USER_ROLE = "admin"
    ACCOUNT_IS_DISSABLED = True

    print((USER_ROLE == "admin") ^ (not ACCOUNT_IS_DISSABLED))