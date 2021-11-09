import datetime

if __name__ == '__main__':
    user = input()
    try:
        datetime.datetime.strptime(user, "%Y-%m-%d")
    except ValueError:
        print("error")
