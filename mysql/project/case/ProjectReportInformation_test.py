import unittest
from project.api import ApiProjectReportInformation
from project.case.file.runSql import db

class ProjectReportInformation(unittest.TestCase):
    """项目统计信息"""
    project_id = db.project_id

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass


    def test_0100_showReportUsingGET(self):
        """查看项目自定义报表"""
        ApiProjectReportInformation.showReportUsingGET(self,
                                                       project_id=ProjectReportInformation.project_id
                                                       )

    # def test_0200
    # """保存项目报表基本信息"""
    # 接口未找到

    # def test_0300_getProjectReportsUsingGET(self):
    #     """查询所有项目报表"""
        # 接口未找到
    # def test_0400
    #     接口未找到


if __name__ == "__main__":
    unittest.main()