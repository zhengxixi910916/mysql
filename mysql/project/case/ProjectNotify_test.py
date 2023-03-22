import unittest

from project.api import ApiProjectNotify, ApiProject
from project.case.file.runSql import db
import time

class ProjectNotify(unittest.TestCase):
    project_id = ''
    config_id = ''

    def setUp(self) -> None:

        project_name = "project_" + time.strftime('%Y%m%d', time.localtime())
        addProjectUsingPOST_1 = ApiProject.addProjectUsingPOST_1(self, name=project_name)
        print(addProjectUsingPOST_1)
        ProjectNotify.project_id = addProjectUsingPOST_1.get('id')
        pass

    def test_0100_filterListUsingGET(self):
        """
        接口名称：消息通知配置列表
        接口地址：/proj/$VERSION$/msg/v2/configure/list/{project_id}
        """
        ApiProjectNotify.filterListUsingGET(self,
                                            project_id=ProjectNotify.project_id
                                            )

    def test_0200_configureUsingPOST(self):
        """
        接口名称：消息通知配置
        接口地址：/proj/$VERSION$/msg/v2/configure/{project_id}
        """
        ApiProjectNotify.configureUsingPOST(self,
                                            project_id=ProjectNotify.project_id,
                                            remindActions="remindActions=%5B%7B%22key%22%3A%22email%2Csystem_msg%22%2C%22type%22%3A1%7D%2C%7B%22key%22%3A%22Daily_work_reminder%22%2C%22type%22%3A3%7D%2C%7B%22key%22%3A%22ELTask_count%22%2C%22type%22%3A2%7D%2C%7B%22key%22%3A%22report%22%2C%22type%22%3A2%7D%5D"
                                            )

    def test_0300_getWorkRemindUsingGET(self):
        """
        接口名称：获取每日工作条件
        接口地址：/proj/$VERSION$/msg/v2/getWorkRemind/{project_id}
        """
        ApiProjectNotify.getWorkRemindUsingGET(self,
                                               project_id=ProjectNotify.project_id
                                               )

    def test_0400_setWorkRemindUsingPUT(self):
        """
        接口名称：设置每日工作提醒
        接口地址：/proj/$VERSION$/msg/v2/setWorkRemind/{project_id}
        """
        ApiProjectNotify.setWorkRemindUsingPUT(self,
                                               project_id=ProjectNotify.project_id,
                                               messageWorkReminds=[{"id": 1, "day": ""}, {"id": 2, "day": ""},
                                                                   {"id": 3, "day": "10"}, {"id": 4, "day": "10"}]
                                               )

    def test_0500_add_notify_config(self):
        """
        接口名称：新增消息通知配置
        接口地址：/proj/$VERSION$/notify
        """
        r = ApiProjectNotify.addNotifyConfigUsingPOST(self, project_id=ProjectNotify.project_id)
        print(r)

    def test_0600_update_notify_config(self):
        """
        接口名称：修改消息通知配置/刷新本地配置的模板id
        接口地址：/proj/$VERSION$/notify/{configId}
        """
        ApiProjectNotify.updateNotifyConfigUsingPUT(self,
                                                    project_id=ProjectNotify.project_id,
                                                    configid=ProjectNotify.config_id
                                                    )

    def test_0700_get_notify_config(self):
        """
        接口名称：查询项目消息通知配置信息
        接口地址：/proj/$VERSION$/notify/{project_id}/list
        """

        r = ApiProjectNotify.getNotifyConfigUsingGET(self,
                                                     project_id=ProjectNotify.project_id)
        print(r)

    def test_0800_delete_notify_configs(self):
        """
        接口名称：批量删除项目消息通知配置信息
        接口地址：/proj/$VERSION$/notify
        """
        ApiProjectNotify.deleteNotifyConfigsUsingDELETE(self,
                                                        configid=ProjectNotify.config_id)

    def tearDown(self) -> None:
        # 删除项目
        deleteProjectUsingDELETE = ApiProject.deleteProjectUsingDELETE(self, project_id=ProjectNotify.project_id)
        print(deleteProjectUsingDELETE)
        # db.delete_sql()
        pass
if __name__ == '__main__':
    unittest.main()
