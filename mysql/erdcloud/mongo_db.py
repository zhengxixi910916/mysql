# coding:utf-8
import configparser as cparser
from os.path import abspath, dirname

from pymongo import MongoClient

# ======== Reading db_config.ini setting ===========
base_dir = dirname(dirname(abspath(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config.ini"

cf = cparser.ConfigParser()

cf.read(file_path)
host = cf.get("mongodbconf", "host")
port = cf.get("mongodbconf", "port")
db1 = cf.get("mongodbconf", "db_name")
user = cf.get("mongodbconf", "user")
password = cf.get("mongodbconf", "password")


# ======== MySql base operating ===================

class DB:
    def __init__(self):
        try:
            # Connect to the database
            client = MongoClient(host=host, port=int(port))
            # 连接mongodb数据库,账号密码认证
            self.mgdb = client.get_database(db1)  # mydb数据库，同上解释
            self.mgdb.authenticate(name=user, password=password, mechanism='SCRAM-SHA-1')
            # self.collection=mgdb
        except self.mgdb.errors.ConfigurationError as e:
            print("mongodb Error %d: %s" % (e.args[0], e.args[1]))

    def clear(self, table_name):
        collection = self.mgdb.get_collection(table_name)
        # collection.remove()
        collection.delete_many(self.getFilterByTable(table_name))
        # t=collection.remove({"username": re.compile('suo00')})

    # insert sql statement
    def insert(self, table_name, table_data):
        collection = self.mgdb.get_collection(table_name)
        collection.insert(table_data)

    # init data
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        # self.close()

    def getFilterByTable(self, table_name):
        filters = {
            "sys_user": {"email": {"$regex": "^suo00"}},
            "sys_organization": {"code": {"$regex": "^suotest1"}}
        }
        return filters[table_name]


if __name__ == '__main__':
    db = DB()
