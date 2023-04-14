# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/5/9

import unittest
from workflow.api import ApiQueryProcessInstancesByBusinessId


class QueryProcessInstancesByBusinessId(unittest.TestCase):
    """业务对象查询流程历史"""

    def test_0100_query_process_instances(self):
        """
            根据流程业务关联表查询流程实例相关信息：/workflow/v1/business/process/history/{businessId}
        """
        query1 = ApiQueryProcessInstancesByBusinessId.query_process_instances(self,
                                                                              business_id="task")
        print(query1)

    def test_0200_query_query_by_business(self):
        """
            根据业务ID获取流程定义ID、流程实例ID、当前活动任务ID：/workflow/v1/business/process/ids/{businessIds}
        """
        query2 = ApiQueryProcessInstancesByBusinessId.query_by_business(self,
                                                                        business_ids="task")
        print(query2)


if __name__ == '__main__':
    unittest.main()
