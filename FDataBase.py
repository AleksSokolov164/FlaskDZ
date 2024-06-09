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

    def addPost(self, username, email, message):
        '''записываем в таблицу fedback'''
        try:
            self.__cur.execute('INSERT INTO feedback VALUES(NULL, ?, ?, ?)', (username, email, message))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления отзыва в БД" + str(e))
            return False
        return True
