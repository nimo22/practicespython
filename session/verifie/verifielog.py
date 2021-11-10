from db.data import Data


class Ver:
    def __init__(self):
        self.connector = Data()

    def get_username_pass(self):
        self.connector.disconnect()
        self.p = self.connector.cursor().execute("SELECT * FROM users ").fetchall()
        return self.p

    def ver_username_pass(self, cur, user, pas):
        a = False
        for y in cur:

            if user in y[0] and pas in y[1]:
                a = True
        return a

