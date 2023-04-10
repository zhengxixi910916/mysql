import math
import time
import unittest
from erdcloud.mysql_db import DB
from project.case.file.runSql import db
from project.api import ApiDimission,ApiIssueManage,ApiProject

class Dimision(unittest.TestCase):
    businessId = None
    user_id = 'SYS_E39B20EA11E7A81AC85B767C89C1'
    replace_id = ''
    project_id = ''
    issue_id = ''


    def test_0100_getDimissionInfoByUserIdUsingGET(self):
        """
        接口名称：根据ID查询离职人员遗留事项
        接口地址：/proj/$VERSION$/dimission/{userId}
        """
        ApiDimission.getDimissionInfoByUserIdUsingGET(self,
                                                      checker=None,
                                                      userId=Dimision.user_id
                                                      )

    def test_0200_getDetailsInfoUsingGET(self):
        """
        接口名称：遗留事项详情列表
        接口地址：/proj/$VERSION$/dimission/{userId}/info
        """
        # 创建项目
        project_name = "project_" + time.strftime('%Y%m%d', time.localtime())
        addProjectUsingPOST_1 = ApiProject.addProjectUsingPOST_1(self, name=project_name)
        print(addProjectUsingPOST_1)
        Dimision.project_id = addProjectUsingPOST_1.get('id')
        # 新增问题单
        issue_name = "issue_" + time.strftime('%H%M%S', time.localtime())
        add_issue_result = ApiIssueManage.add_issue(self,
                                                    name=issue_name,
                                                    project_id=Dimision.project_id,
                                                    submitid=Dimision.user_id,
                                                    priority="1",
                                                    state="DRAFT",
                                                    type="1"
                                                    )
        Dimision.issue_id = add_issue_result.get("id")

        # 遗留事项详情列表
        r = ApiDimission.getDetailsInfoUsingGET(self,
                                                checker=None,
                                                userId=Dimision.user_id
                                                )
    @unittest.skip('xx')
    def test_0300_replaceSimpleByUserIdUsingPUT(self):
        """
        接口名称：单个替换遗留事项
        接口地址：/proj/$VERSION$/dimission/replace/{userId}/info/{type}
        """
        ApiDimission.replaceSimpleByUserIdUsingPUT(self,
                                                   checker=None,
                                                   type='0',
                                                   userId=db.user_id,
                                                   replaceDtoList=[
                                                       {
                                                           "businessId": Dimision.issue_id,
                                                           "replaceId": "SYS_E39B20EA11E7A81AC85B767C89C1"
                                                       }
                                                   ]
                                                   )

        delete_issue_result = ApiIssueManage.delete_issue(self, Dimision.issue_id)
        print(delete_issue_result)

        # 删除项目
        deleteProjectUsingDELETE = ApiProject.deleteProjectUsingDELETE(self, project_id=Dimision.project_id)
        print(deleteProjectUsingDELETE)
        # db.delete_sql()


if __name__ == '__main__':
    unittest.main()
