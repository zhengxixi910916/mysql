# -*- coding: utf-8 -*-
# @Time    : 2021/4/27 15:04
# @Author  : yangjoing
import os.path
import time
import uuid

from project.case.file.mysql_db import DB


class DataBaseOperation:

    def __init__(self):
        self.org_id = ""  # 组织ID
        self.user_id = ""  # 用户ID
        self.project_id = ""  # 项目ID
        self.project_report_id = ""  # 项目报告ID
        self.project_name = ""  # 项目名称
        self.viewid_id = "de2d00fcd8712c712dd749364f05aa4b"  # 视图ID
        self.sysCalendar_id = uuid.uuid1().hex  # 系统日历ID
        self.projCalendar_id = uuid.uuid1().hex  # 项目日历ID
        self.document_id = uuid.uuid1().hex  # 文档ID
        self.baseline_id = "cdfaef81e6326685af761d5c7313252f"  # 基线ID
        self.object_id = uuid.uuid1().hex  # 对象ID
        self.agenda_id = uuid.uuid1().hex  # 日程ID
        self.task_view_id = "de2d00fcd8712c712dd749364f05aa4b"  # 计划ID
        self.require_view_id = "513345ee2219415a94dab80991614fe6"  # 需求ID
        self.issue_view_id = "cb73735437c14de381294291bc1ee32d"  # 问题ID
        self.risk_view_id = "fa2fb0892fb74ef9acc584c4a7ae9dd9"  # 风险ID

    def insert_sql(self):
        # 插入组织
        self.org_id = uuid.uuid1().hex
        org_code = "ORG" + time.strftime('%Y-%m-%d %H %M %S', time.localtime())
        org_name = "org_" + time.strftime('%Y-%m-%d %H %M %S', time.localtime())
        org_params = [self.org_id, org_code, org_name]

        file = fr'{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}/file/insert_org.sql'
        DB.instance().readSql(filePath=file, params=org_params, section="system")

        # 插入用户
        self.user_id = uuid.uuid1().hex
        user_code = "USER" + time.strftime('%Y-%m-%d %H %M %S', time.localtime())
        user_name = "name_" + time.strftime('%Y-%m-%d %H %M %S', time.localtime())
        display_name = "Cn_" + time.strftime('%Y-%m-%d %H %M %S', time.localtime())
        email = time.strftime('%H%M%S', time.localtime()) + "@qq.com"
        display_en = "En_" + time.strftime('%Y-%m-%d %H %M %S', time.localtime())
        user_params = [self.user_id, user_code, user_name, display_name, self.org_id, email, display_en]

        file = fr'{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}/file/insert_user.sql'
        DB.instance().readSql(filePath=file, params=user_params, section="system")

        # 插入项目
        self.project_id = uuid.uuid1().hex
        project_code = "PRO" + time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime())
        project_name = "project_" + time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime())
        self.project_name = project_name
        project_description = project_name

        project_params = [self.project_id, project_code, project_name, project_description, self.user_id,
                          self.org_id,
                          self.user_id]

        file = fr'{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}/file/insert_project.sql'
        DB.instance().readSql(filePath=file, params=project_params, section="project")

        # 插入项目报告
        self.project_report_id = uuid.uuid1().hex
        project_report_name = "project_report_" + time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime())

        project_report_params = [self.project_report_id, project_report_name, self.project_id]

        file = fr'{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}/file/insert_project_report.sql'
        DB.instance().readSql(filePath=file, params=project_report_params, section="project")
        DB().close(section="system")

        # 插入项目视图

        file = fr'{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}/file/insert_view.sql'
        DB.instance().readSql(filePath=file, params=None, section="system")
        DB().close(section="system")



    def delete_sql(self):
        # 删除数据
        if self.user_id != "":
            DB.instance().clear_condition(section="system",
                                          table="sys_eluser",
                                          condition={"id": self.user_id}
                                          )
        if self.org_id != "":
            DB.instance().clear_condition(section="system",
                                          table="sys_elorganization",
                                          condition={"id": self.org_id}
                                          )
        if self.project_id != "":
            print('delete project')
            DB.instance().clear_condition(section="project",
                                          table="proj_elproject",
                                          condition={"id": self.project_id}
                                          )
        if self.project_report_id != "":
            print('delete project report')
            DB.instance().clear_condition(section="project",
                                          table="rpt_elproject_report",
                                          condition={"id": self.project_report_id}
                                          )

        # 关闭数据库
        DB().close(section="system")
        DB().close(section="project")


db = DataBaseOperation()
db.insert_sql()

if __name__ == '__main__':
    # db.delete_sql()
    dir_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    print(dir_path)
