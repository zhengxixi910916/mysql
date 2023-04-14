# -*- coding: utf-8 -*-
# @Time    :  2021/4/29 15:46
# @Author  : xiaoli
from erdcloud.mysql_db import DB
import uuid
import time
import os


def joinPath(path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)


class init:
    # 组织准备数据
    orgid = uuid.uuid1().hex
    orgcode = "ORG" + time.strftime('%H%M%S', time.localtime())
    orgname = "p" + time.strftime('%H%M%S', time.localtime())

    # 用户准备数据
    userid = uuid.uuid1().hex
    usercode = "U" + time.strftime('%H%M%S', time.localtime())
    username = usercode
    display_name = usercode
    email = usercode + "@qq.com"
    display_en = usercode

    # 流程定义
    ACT_RE_PROCDEF_id = "autotestworkflow:1:e548a84cb6d711ebbca20a580a01028e"

    # 流程
    ACT_RE_DEPLOYMENT_id = "e535e399b6d711ebbca20a580a01028e"

    # 流程模型
    ACT_RE_MODEL_id = "df3b2096b6d711ebbca20a580a01028e"

    # 模板
    ACT_GE_BYTEARRAY_id1 = "df3be3e7b6d711ebbca20a580a01028e"
    ACT_GE_BYTEARRAY_id2 = "df3ca738b6d711ebbca20a580a01028e"
    ACT_GE_BYTEARRAY_id3 = "e535e39ab6d711ebbca20a580a01028e"
    ACT_GE_BYTEARRAY_id4 = "e5485a2bb6d711ebbca20a580a01028e"

    # def setDirBase(self, dirbase):
    #     self._dirbase = dirbase

    def sql_insert_file_org(self):
        # 添加组织
        params1 = [init.orgid, init.orgcode, init.orgname]
        print("params1=", params1)
        DB.instance().readSql(filePath=joinPath("insert_org.sql"), params=params1, section="system")

    def sql_insert_file_user(self):
        # 添加用户
        params2 = [init.userid, init.usercode, init.username,
                   init.display_name, init.orgid,
                   init.email, init.display_en]
        print("params2=", params2)
        DB.instance().readSql(filePath=joinPath("insert_user.sql"), params=params2, section="system")

    def sql_insert_file_workflow(self):
        # 创建流程模板
        DB.instance().readSql(filePath=joinPath("创建流程模板.sql"), params=None, section="workflow")

    def del_db_user(self):
        # 删除用户
        if init.userid != "":
            DB.instance().clear_condition(section="system",
                                          table="sys_eluser",
                                          condition={"id": init.userid}
                                          )

    def del_db_org(self):
        # 删除组织
        if init.orgid != "":
            DB.instance().clear_condition(section="system",
                                          table="sys_elorganization",
                                          condition={"id": init.orgid}
                                          )

    def del_db_workflow(self):
        # 删除流程定义
        if init.ACT_RE_PROCDEF_id != "":
            DB.instance().clear_condition(section="workflow",
                                          table="ACT_RE_PROCDEF",
                                          condition={"ID_": init.ACT_RE_PROCDEF_id}
                                          )
        # 删除流程
        if init.ACT_RE_DEPLOYMENT_id != "":
            DB.instance().clear_condition(section="workflow",
                                          table="ACT_RE_DEPLOYMENT",
                                          condition={"ID_": init.ACT_RE_DEPLOYMENT_id}
                                          )

        # 删除流程模型
        if init.ACT_RE_MODEL_id != "":
            DB.instance().clear_condition(section="workflow",
                                          table="ACT_RE_MODEL",
                                          condition={"ID_": init.ACT_RE_MODEL_id}
                                          )

        # 删除模板1
        if init.ACT_GE_BYTEARRAY_id1 != "":
            DB.instance().clear_condition(section="workflow",
                                          table="ACT_GE_BYTEARRAY",
                                          condition={"ID_": init.ACT_GE_BYTEARRAY_id1}
                                          )

        # 删除模板2
        if init.ACT_GE_BYTEARRAY_id2 != "":
            DB.instance().clear_condition(section="workflow",
                                          table="ACT_GE_BYTEARRAY",
                                          condition={"ID_": init.ACT_GE_BYTEARRAY_id2}
                                          )
        if init.ACT_GE_BYTEARRAY_id3 != "":
            DB.instance().clear_condition(section="workflow",
                                          table="ACT_GE_BYTEARRAY",
                                          condition={"ID_": init.ACT_GE_BYTEARRAY_id3}
                                          )
        if init.ACT_GE_BYTEARRAY_id4 != "":
            DB.instance().clear_condition(section="workflow",
                                          table="ACT_GE_BYTEARRAY",
                                          condition={"ID_": init.ACT_GE_BYTEARRAY_id4}
                                          )


db = init()
# db.sql_insert_file_workflow()
db.sql_insert_file_org()
db.sql_insert_file_user()
