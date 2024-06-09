import sqlite3


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getMenu(self):
        '''читаем из базы из ьаблицы feedback'''
        sql = '''SELECT * FROM feedback'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print('Ошибка чтения из базы')
        return []

    def addFeedback(self, username, email, message):
        '''записываем в таблицу fedback'''
        try:
            self.__cur.execute('INSERT INTO feedback VALUES(NULL, ?, ?, ?)', (username, email, message))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления отзыва в БД" + str(e))
            return False
        return True

    def addUser(self, name, email, hpsw):
        try:
            self.__cur.execute(f"SELECT COUNT() as 'count' FROM users WHERE email LIKE '{email}'")
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print('Пользователь с таким email  уже существует')
                return False

            self.__cur.execute("INSERT INTO users VALUES(NULL, ?, ?, ?)", (name, email, hpsw))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления отзыва в БД" + str(e))
            return False
        return True

    def getUser(self, user_id):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE id = {user_id} LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print('Пользователь не найден')
                return False

            return res
        except sqlite3.Error as e:
            print("Ошибка добавления отзыва в БД" + str(e))
        return False


    def getUserByEmail(self, email):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE email = '{email}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print('Пользователь не найден')
                return False

            return res
        except sqlite3.Error as e:
            print("Ошибка добавления отзыва в БД" + str(e))
        return False