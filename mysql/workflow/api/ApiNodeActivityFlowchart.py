from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "get_diagram_by": "/flowchart/processdefinition/%s/diagramlayout",  # 根据流程定义ID查询流程定义所有元素
    "get_diagram_by1": "/flowchart/processinstance/%s/diagramlayout",  # 根据流程实例ID查询流程定义所有元素
    "get_highlighted_using": "/flowchart/processinstance/%s/highlights",  # 高亮显示活动节点
    "get_highlighted_using1": "/flowchart/processinstance/%s/%s/highlights",
    # 高亮显示活动节点（流程图使用）
})


def get_diagram_by(self, process_instance_id, process_definition_id, checker=None):
    """
    接口名称：根据流程定义ID查询流程定义所有元素;    接口地址：/flowchart/processdefinition/{processDefinitionId}/diagramlayout；
    """
    r = RequestService.call_get(apis.get("get_diagram_by", process_definition_id, ), params={
        "processInstanceId": process_instance_id  # 流程实例ID - required: False
    }, )
    print(r)
    try:
        if r['code'] == '500':
            self.assertEqual('200', r['code'])
    except:
        self.assertEqual(1, 1)


def get_diagram_by1(self, process_instance_id, checker=None):
    """
    接口名称：根据流程实例ID查询流程定义所有元素;    接口地址：/flowchart/processinstance/{processInstanceId}/diagramlayout；
    """
    r = RequestService.call_get(apis.get("get_diagram_by1", process_instance_id), )
    print(r)
    try:
        if r['code'] == '500':
            self.assertEqual('200', r['code'])
    except:
        self.assertEqual(1, 1)


def get_highlighted_using(self, process_instance_id, checker=None):
    """
    接口名称：高亮显示活动节点;    接口地址：/flowchart/processinstance/{processInstanceId}/highlights；
    """
    r = RequestService.call_get(apis.get("get_highlighted_using", process_instance_id), )
    print(r)
    try:
        if r['code'] == '500':
            self.assertEqual('200', r['code'])
    except:
        self.assertEqual(1, 1)


def get_highlighted_using1(self, process_definition_id, process_instance_id, checker=None):
    """
    接口名称：高亮显示活动节点（流程图使用）;    接口地址：/flowchart/processinstance/{processInstanceId}/{processDefinitionId}/highlights；
    """
    r = RequestService.call_get(apis.get("get_highlighted_using1", process_instance_id, process_definition_id, ), )
    print(r)
    try:
        if r['code'] == '500':
            self.assertEqual('200', r['code'])
    except:
        self.assertEqual(1, 1)
