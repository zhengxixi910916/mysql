# coding=utf8
import configparser as parser
import logging
import threading

import pymysql.cursors


from erdcloud import Utils

logging.basicConfig()
logger = logging.getLogger(__name__)
DEFAULT_SECTION = "default"


# ======== MySql base operating ===================
class DB:
    _instance_lock = threading.Lock()

    def __init__(self):
        self.configs = None
        self.connection_map = dict()

    @classmethod
    def instance(cls, *args, **kwargs):
        with cls._instance_lock:
            if not hasattr(DB, "_instance"):
                DB._instance = DB()
                return DB._instance
            return DB._instance

    def get_connection(self, section=DEFAULT_SECTION):
        if self.connection_map.get(section) is None:
            data = dict()
            if self.configs is None:
                db_config_str = Utils.Config.db_config()
                if db_config_str == '':
                    print("数据库配置信息为空！！！")
                    return

                cf = parser.ConfigParser()
                cf.read_string(db_config_str)
                self.configs = cf

            if not self.configs.has_section(section):
                section = DEFAULT_SECTION
            opts = self.configs.options(section)
            print(opts)
            for opt in opts:
                data[opt] = self.configs.get(section, opt)

            print(data)
            try:
                # Connect to the database
                connection = pymysql.connect(host=data.get("host"),
                                             port=int(data.get('port')),
                                             user=data.get('user'),
                                             password=data.get('password'),
                                             db=data.get('db_name'),
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
                self.connection_map[section] = connection
            except pymysql.err.OperationalError as e:
                print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
        result = self.connection_map.get(section)
        result.ping(True)
        return result

    def insert(self, section=DEFAULT_SECTION, table_name=None, table_data=None):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        print(key)
        value = ','.join(table_data.values())
        print(value)
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        print(real_sql)
        connection = self.get_connection(section)
        connection.cursor().execute(real_sql, table_data)
        connection.commit()

    def query(self, section=DEFAULT_SECTION, query_sql=None):
        if query_sql is None:
            return {}
        connection = self.get_connection(section)
        cur = connection.cursor()  # 获取游标
        cur.execute(query_sql)  # 执行SQL
        data = cur.fetchall()  # 获取查询结果
        # cur.close()  # 关闭游标
        # connection.close()  # 关闭连接
        return data  # 返回执行SQL的数据信息

    # clear table data
    def clear(self, section=DEFAULT_SECTION, table=None, eid=None):
        if table is None:
            return
        delete_sql = "delete from " + table + " where id ='" + eid + "';"
        print(delete_sql)
        connection = self.get_connection(section)
        connection.cursor().execute(delete_sql)
        connection.commit()

    # clear table data
    def clear_condition(self, section=DEFAULT_SECTION, table=None, condition=None):
        if table is None or condition is None:
            return
        delete_sql = "delete from " + table + " where "
        has_condition = False
        and_flag = "AND "
        for k in condition:
            has_condition = True
            delete_sql += k + "=%(" + k + ")s " + and_flag
        if not has_condition:
            return
        delete_sql = delete_sql[0:-len(and_flag)]

        print("SQL: " + delete_sql)
        print(condition)
        connection = self.get_connection(section)
        connection.cursor().execute(delete_sql, condition)
        connection.commit()

    # close database
    def close(self, section=DEFAULT_SECTION):
        self.get_connection(section).close()


if __name__ == '__main__':
    db = DB.instance()
    data = db.query("select count(1) from sys_basic_config", "system")
    print(data)
    db = DB.instance()
    data = db.query("select count(1) from sys_basic_config", "system")
    print(data)
    db = DB.instance()
    data = db.query("select count(1) from wiki_label", "wiki")
    print(data)
    db = DB.instance()
    data = db.query("select count(1) from wiki_label", "system")
    print(data)
    db = DB.instance()
    data = db.query("select count(1) from wiki_label", "project")
    print(data)
