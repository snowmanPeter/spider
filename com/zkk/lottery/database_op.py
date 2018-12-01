# encoding: utf-8

from com.zkk.Util import Properties
import MySQLdb

class mysql():

    def __init__(self, config):
        prop = Properties(config)
        host = prop['host']
        user = prop['user']
        passwd = prop['passwd']
        db_name = prop['db']
        charset = prop['charset']
        __connect = MySQLdb.connect(host = host, user= user, passwd = passwd, db = db_name, charset = charset)
        __cursor = __connect.cursor()

    def createTable(self, sql):
        self.__cursor.execute(sql)


    def Insert(self, sql):
        try:
            self.__cursor.execute(sql)
            self.__connect.commit()
        except:
            self.__connect.rollback()

    def Select(self, sql):
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        return result

    def Close(self):
        self.__cursor.close()
        self.__connect.close()