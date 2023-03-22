# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 18:23
# @Author  : Liao
import random
import time
import unittest

# from db_fixture.mysql_db import DB
from project.api import ApiProgramManage
from project.case.file.runSql import db


class ProgramManage(unittest.TestCase):
    """项目群管理"""

    user_id = db.user_id
    department_id = db.org_id
    project_id = db.project_id
    # 新增项目群
    program_name = "program_" + time.strftime('%Y-%m-%d %H %M %S', time.localtime())
    start_time = time.strftime('%Y-%m-%d %H %M %S', time.localtime())
    finish_time = time.strftime('%Y-%m-%d %H %M %S', time.localtime())
    workload = str(random.randint(10, 99))
    budget = str(random.randint(1000, 9999))
    description = program_name
    program_id = ""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # if ProgramManage.program_id != "":
        #     DB.instance().clear_condition(section="project",
        #                                   table="ppm_elprogram",
        #                                   condition={"id": ProgramManage.program_id}
        #                                   )
        # if __name__ == '__main__':
        #     print("delete sql")
        #     db.delete_sql()
        pass

    def test_0100_create_program(self):
        """
        新增项目群
        """
        # /portfolio/v1/program
        create_result = ApiProgramManage.create_program(self,
                                                        ProgramManage.program_name,
                                                        ProgramManage.department_id,
                                                        ProgramManage.user_id,
                                                        ProgramManage.start_time,
                                                        ProgramManage.finish_time,
                                                        ProgramManage.workload,
                                                        ProgramManage.budget,
                                                        ProgramManage.description,
                                                        "0")
        ProgramManage.program_id = create_result.get("id")
        print("program_id:", ProgramManage.program_id)

    def test_0200_get_all_page_program(self):
        """
        查询所有项目群列表分页
        """
        # /portfolio/v1/program/all/page
        get_all_page = ApiProgramManage.get_all_page_program(self)
        print(get_all_page)

    def test_0300_archive_program(self):
        """
        项目群归档
        """
        # /portfolio/v1/program/archive/{id}
        archive_result = ApiProgramManage.archive_program(self, ProgramManage.program_id)
        print(archive_result)

    def test_0400_get_archives_program(self):
        """
        查询用户归档项目群
        """
        # /portfolio/v1/program/archives/{userId}
        archive_list = ApiProgramManage.get_archives_program(self, ProgramManage.user_id)
        print(archive_list)

    def test_0500_add_attention(self):
        """
        添加关注/收藏/打开对象
        """
        # /portfolio/v1/program/attention
        # 类型，0:最近打开的;1:我关注的; 2:我收藏的
        type = "0"
        add_attention_result = ApiProgramManage.add_attention(self, ProgramManage.program_id, type)
        print(add_attention_result)

    def test_0600_cancel_attention(self):
        """
        取消关注/收藏/打开对象
        """
        # /portfolio/v1/program/attention
        # 类型，0:最近打开的;1:我关注的; 2:我收藏的
        type = "0"
        cancel_attention_result = ApiProgramManage.cancel_attention(self, ProgramManage.program_id, type)
        print(cancel_attention_result)

    def test_0700_get_attentions(self):
        """
        查询用户关注/收藏/打开对象
        """
        # /portfolio/v1/program/attentions
        # 类型，0:最近打开的;1:我关注的; 2:我收藏的
        type = "0"
        get_attention_result = ApiProgramManage.get_attentions(self, type)
        print(get_attention_result)

    def test_0800_get_candidates(self):
        """
        获取候选项目群、项目
        """
        # /portfolio/v1/program/candidates/{programId}
        type = "0"
        get_candidates_result = ApiProgramManage.get_candidates(self, ProgramManage.program_id, type)
        print(get_candidates_result)

    def test_0900_get_dept_program_tree(self):
        """
        获取用户部门项目群树
        """
        # /portfolio/v1/program/depttree/{userId}
        get_dept_program_tree = ApiProgramManage.get_dept_program_tree(self, ProgramManage.user_id)
        print(get_dept_program_tree)

    def test_1000_get_milestones_by_progid(self):
        """
        根据项目群ID获取子项目里程碑列表
        """
        # /portfolio/v1/program/milestones/{id}
        # type：id类型，program 或 project
        milestone_type = "project"
        get_milestones = ApiProgramManage.get_milestones_by_progid(self, ProgramManage.program_id, milestone_type)
        print(get_milestones)

    def test_1100_get_overview_by_progid(self):
        """
        根据项目群ID获取子项目群、子项目信息概览列表
        """
        # /portfolio/v1/program/overview/{id}
        # type：id类型，program 或 project
        overview_type = "project"
        get_overview_result = ApiProgramManage.get_overview_by_progid(self, ProgramManage.program_id, overview_type)
        print(get_overview_result)

    def test_1200_search_program(self):
        """
        搜索项目群
        """
        # /portfolio/v1/program/search/{userId}
        search_program_result = ApiProgramManage.search_program(self, ProgramManage.user_id, ProgramManage.program_name)
        print(search_program_result)

    def test_1300_add_sub_prog_proj(self):
        """
        添加/移除子项目群、子项目
        """
        # /portfolio/v1/program/subs/{id}
        operation = "add"
        add_type = "project"
        add_sub_result = ApiProgramManage.add_sub_prog_proj(self, ProgramManage.program_id, ProgramManage.project_id,
                                                            add_type, operation)
        print(add_sub_result)

    def test_1400_get_sub_tree_by_progid(self):
        """
        根据项目群ID查询子项目群、项目树
        """
        # /portfolio/v1/program/subtree/{programId}
        get_sub_tree_result = ApiProgramManage.get_sub_tree_by_progid(self, ProgramManage.program_id)
        print(get_sub_tree_result)

    def test_1500_get_program_by_id(self):
        """
        查询单个项目群
        """
        # /portfolio/v1/program/{id}
        get_program_result = ApiProgramManage.get_program_by_id(self, ProgramManage.program_id)
        print(get_program_result)

    def test_1600_update_program_by_id(self):
        """
        修改项目群
        """
        # /portfolio/v1/program/{id}
        update_program_name = "update_" + ProgramManage.program_name
        update_program_result = ApiProgramManage.update_program_by_id(self, ProgramManage.program_id,
                                                                      update_program_name)
        print(update_program_result)

    def test_1700_get_program_member_by_id(self):
        """
        项目群成员查询
        """
        # /portfolio/v1/program/{id}/members
        get_program_member_result = ApiProgramManage.get_program_member_by_id(self, ProgramManage.program_id)
        print(get_program_member_result)

    def test_1800_get_proj_of_program(self):
        """
        查询项目群下所有项目
        """
        # /portfolio/v1/program/{id}/projects
        get_proj_result = ApiProgramManage.get_proj_of_program(self, ProgramManage.program_id)
        print(get_proj_result)

    def test_1900_get_prog_milestone_baseline(self):
        """
        查询项目群项目基线里程碑
        """
        # /portfolio/v1/programMilestoneBl
        get_prog_milestone_result = ApiProgramManage.get_prog_milestone_baseline(self)
        print(get_prog_milestone_result)

    def test_2000_get_prog_milestone_finished(self):
        """
        查询项目群里程碑完成情况
        """
        # /portfolio/v1/programMilestoneCena
        get_milestone_finished_result = ApiProgramManage.get_prog_milestone_finished(self)
        print(get_milestone_finished_result)

    def test_2100_get_programs_by_userid(self):
        """
        获取项目群经理所有项目群、子项目群
        """
        # /portfolio/v1/user/programs/{userId}
        get_programs_result = ApiProgramManage.get_programs_by_userid(self, ProgramManage.user_id)
        print(get_programs_result)

    def test_2200_delete_program_by_id(self):
        """
        删除项目群
        """
        # /portfolio/v1/program/{id}
        delete_result = ApiProgramManage.delete_program_by_id(self, ProgramManage.program_id)
        print(delete_result)


if __name__ == '__main__':
    unittest.main()
