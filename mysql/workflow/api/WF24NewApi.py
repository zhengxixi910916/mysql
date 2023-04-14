import json
import time
from workflow.api import ApiTools
import requests
from erdcloud.erdApi import Api

apis = Api({
    "saveOrUpdate_model": "/workflow/$VERSION$/dynamic/api/model/saveOrUpdate",  # 创建流程模板接口
    "model_view": "/workflow/$VERSION$/dynamic/api/model/view/{templateId}",  # 模板详情接口
    "task_completetasks": "/workflow/$VERSION$/dynamic/api/task/completetasks",
    "submitActivityTask": "/workflow/$VERSION$/dynamic/api/submit/process/submitActivityTask",  # pbo审批接口
    "start_processbypbo": "/workflow/v1/start/processbypbo"
})


def tasks_grouped(taskids):
    """
    接口名称：批量审批任务查询接口;
    接口地址：/workflow/v1/dynamic/api/task/tasks/grouped；
    """
    host, headers = ApiTools.getHostAndHeaders()
    url = host + "/workflow/v1/dynamic/api/task/tasks/grouped"
    data = {"taskIds": taskids}
    r = requests.request("POST", url=url, headers=headers, json=data)
    return r.json()


def task_completetasks(taskIds):
    """
    接口名称：批量审批接口;
    接口地址：/workflow/v1/dynamic/api/task/completetasks；
    """
    apis.get('task_completetasks', None)
    data = {
        "completeTasks": [
            {
                "taskIds": taskIds,
                "routeFlag": "0",
                "comment": "已阅，同意"
            }
        ]
    }
    host, headers = ApiTools.getHostAndHeaders()
    url = host + "/workflow/v1/dynamic/api/task/completetasks"
    r = requests.request("POST", url=url, headers=headers, json=data)
    print(r.json())
    return r.json()


def add_category():
    """
    接口名称：创建流程分类接口;
    接口地址：/workflow/v1/category/add；
    """
    data = {"parentId": "-1", "title": "ZIDS分类01", "children": [], "categoryCode": 1657674559102, "sort": 0}
    host, headers = ApiTools.getHostAndHeaders()
    url = host + "/workflow/v1/category/add"
    r = requests.request("POST", url=url, headers=headers, json=data)
    # print(r.text)
    # js = r.json()
    # print(js["res"]["data"]["id"])


def saveOrUpdate_model():
    """
    接口名称：创建流程模板接口;
    接口地址：/workflow/v1/dynamic/api/model/saveOrUpdate；
    """
    apis.post('saveOrUpdate_model', None)
    data = {"id": None, "category": "1657674559102", "tenantId": "erdp", "globalVariables": [], "globalConfig": [],
            "actData": [{"actDefId": "Event_0hal8ek", "currentAppId": "erdp", "localConfig": []},
                        {"actDefId": "Activity_1rfvv5a", "currentAppId": "erdp", "localConfig": []},
                        {"actDefId": "Event_1xso1lb", "currentAppId": "erdp", "localConfig": []},
                        {"actDefId": "Event_ZIDS001", "currentAppId": "erdp", "localConfig": []},
                        {"actDefId": "Event_Zids001", "currentAppId": "erdp", "localConfig": []},
                        {"actDefId": "Activity_Zids002", "currentAppId": "erdp", "localConfig": []},
                        {"actDefId": "Event_Zids003", "currentAppId": "erdp", "localConfig": []},
                        {"actDefId": "Activity_Zids001", "currentAppId": "erdp", "localConfig": []}],
            "xmlData": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<bpmn2:definitions xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:bpmn2=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:dc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:di=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:activiti=\"http://activiti.org/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" id=\"diagram_Process_1657675109776\" targetNamespace=\"http://activiti.org/test\" xsi:schemaLocation=\"http://www.omg.org/spec/BPMN/20100524/MODEL BPMN20.xsd\">\n  <bpmn2:process id=\"ProcessZids001\" name=\"业务流程(ZIDS)001\" isExecutable=\"true\">\n    <bpmn2:documentation>流程描述</bpmn2:documentation>\n    <bpmn2:startEvent id=\"Event_Zids001\" name=\"开始\">\n      <bpmn2:documentation>节点描述</bpmn2:documentation>\n      <bpmn2:extensionElements>\n        <activiti:flowstate>业务状态1,业务状态2</activiti:flowstate>\n      </bpmn2:extensionElements>\n      <bpmn2:outgoing>Flow_Zids001</bpmn2:outgoing>\n    </bpmn2:startEvent>\n    <bpmn2:userTask id=\"Activity_Zids001\" name=\"处理节点001\" activiti:assignee=\"SYS_E39B20EA11E7A81AC85B767C89C1\" activiti:dueDate=\"${dueDate}\" activiti:priority=\"${priority}\">\n      <bpmn2:documentation>节点描述</bpmn2:documentation>\n      <bpmn2:extensionElements>\n        <activiti:serialnumber>1</activiti:serialnumber>\n        <activiti:flowstate>业务状态3,业务状态4</activiti:flowstate>\n        <activiti:rolekey>ADMIN</activiti:rolekey>\n      </bpmn2:extensionElements>\n      <bpmn2:incoming>Flow_Zids001</bpmn2:incoming>\n      <bpmn2:outgoing>Flow_Zids002</bpmn2:outgoing>\n    </bpmn2:userTask>\n    <bpmn2:endEvent id=\"Event_Zids003\" name=\"结束\">\n      <bpmn2:documentation></bpmn2:documentation>\n      <bpmn2:extensionElements>\n        <activiti:flowstate>业务状态5,业务状态6</activiti:flowstate>\n      </bpmn2:extensionElements>\n      <bpmn2:incoming>Flow_Zids002</bpmn2:incoming>\n      <bpmn2:terminateEventDefinition id=\"TerminateEventDefinition_0q3r15l\" activiti:terminateAll=\"true\" />\n    </bpmn2:endEvent>\n    <bpmn2:sequenceFlow id=\"Flow_Zids001\" sourceRef=\"Event_Zids001\" targetRef=\"Activity_Zids001\" />\n    <bpmn2:sequenceFlow id=\"Flow_Zids002\" sourceRef=\"Activity_Zids001\" targetRef=\"Event_Zids003\" />\n  </bpmn2:process>\n  <bpmndi:BPMNDiagram id=\"BPMNDiagram_1\">\n    <bpmndi:BPMNPlane id=\"ProcessZids001_di\" bpmnElement=\"ProcessZids001\">\n      <bpmndi:BPMNEdge id=\"Flow_Zids001_di\" bpmnElement=\"Flow_Zids001\">\n        <di:waypoint x=\"-402\" y=\"-210\" />\n        <di:waypoint x=\"-290\" y=\"-210\" />\n      </bpmndi:BPMNEdge>\n      <bpmndi:BPMNEdge id=\"Flow_Zids002_di\" bpmnElement=\"Flow_Zids002\">\n        <di:waypoint x=\"-190\" y=\"-210\" />\n        <di:waypoint x=\"-58\" y=\"-210\" />\n      </bpmndi:BPMNEdge>\n      <bpmndi:BPMNShape id=\"Event_Zids001_di\" bpmnElement=\"Event_Zids001\">\n        <dc:Bounds x=\"-438\" y=\"-228\" width=\"36\" height=\"36\" />\n        <bpmndi:BPMNLabel>\n          <dc:Bounds x=\"-431\" y=\"-185\" width=\"22\" height=\"14\" />\n        </bpmndi:BPMNLabel>\n      </bpmndi:BPMNShape>\n      <bpmndi:BPMNShape id=\"Activity_Zids001_di\" bpmnElement=\"Activity_Zids001\">\n        <dc:Bounds x=\"-290\" y=\"-230\" width=\"100\" height=\"40\" />\n      </bpmndi:BPMNShape>\n      <bpmndi:BPMNShape id=\"Event_Zids003_di\" bpmnElement=\"Event_Zids003\">\n        <dc:Bounds x=\"-58\" y=\"-228\" width=\"36\" height=\"36\" />\n        <bpmndi:BPMNLabel>\n          <dc:Bounds x=\"-51\" y=\"-185\" width=\"22\" height=\"14\" />\n        </bpmndi:BPMNLabel>\n      </bpmndi:BPMNShape>\n    </bpmndi:BPMNPlane>\n  </bpmndi:BPMNDiagram>\n</bpmn2:definitions>\n",
            "processModelName": "业务流程(ZIDS)001", "processModelKey": "ProcessZids001", "description": "流程描述",
            "isCheckIn": "Y", "procCodeRule": "procInstCodeRule"}
    host, headers = ApiTools.getHostAndHeaders()
    url = host + "/workflow/v1/dynamic/api/model/saveOrUpdate"
    r = requests.request("POST", url=url, headers=headers, json=data)
    res = dict(r.json())
    # print(res)
    if 'res' in res:
        id = res["res"]["data"]["id"]
        requests.request("GET", url=host + f"/workflow/v1/dynamic/api/model/view/{id}", headers=headers)
        return res
    else:
        # print("模板已存在")
        return {'code': '200'}


def start_processbypbo():
    """
    接口名称：发起流程;
    接口地址：/workflow/v1/start/processbypbo；
    """
    data = {
        "baseForm": {
            "processBasicInfo": {
                "applicationKey": '',
                "resourceKey": '',
                "name": "123",
                "description": "项目预算审批流程",
                "procInstVariables": {}
            },
            "businessForm": {
                "reviewItemList": []
            },
            "businessFormJsonStr": "{\"reviewItemList\":[]}"
        },
        "processDefKey": "BUDGET_APPROVE",
        "isDraft": False,
        "baseStartProcessDto": {
            "title": "123",
            "dueDate": "2023-03-06",
            "description": "项目预算审批流程",
            "priority": "50",
            "uploadFileIds": [],
            "deleteFileIds": [],
            "userMap": {
                "approve_candidateUsers": "SYS_E39B20EA11E7A81AC85B767C89C1",
                "sid-E9E1828A-6C1D-403B-B875-0B2AF06D56B1_candidateUsers": "SYS_E39B20EA11E7A81AC85B767C89C1"
            },
            "roleMap": {
                "approve_candidateRoles": "",
                "sid-E9E1828A-6C1D-403B-B875-0B2AF06D56B1_candidateRoles": ""
            },
            "groupMap": {
                "approve_candidateGroups": "",
                "sid-E9E1828A-6C1D-403B-B875-0B2AF06D56B1_candidateGroups": ""
            },
            "category": "ppm_model",
            "roleUserMap": {},
            "groupUserMap": {},
            "showUserJson": "[{\"memberType\":\"OPERATOR\",\"memberId\":\"SYS_E39B20EA11E7A81AC85B767C89C1\",\"parentId\":\"-1\",\"actDefId\":\"approve\"},{\"memberType\":\"OPERATOR\",\"memberId\":\"SYS_E39B20EA11E7A81AC85B767C89C1\",\"parentId\":\"-1\",\"actDefId\":\"sid-E9E1828A-6C1D-403B-B875-0B2AF06D56B1\"}]"
        }
    }
    host, headers = ApiTools.getHostAndHeaders()
    url = host + "/workflow/v1/start/processbypbo"
    apis.post('start_processbypbo', None)
    r = requests.request("POST", url=url, headers=headers, json=data)
    res = r.json()
    pboId = res["data"]["erd.cloud.pbo.domain.vo.ParameterVO"]["pboId"]
    id = res["data"]["erd.cloud.pbo.domain.vo.ParameterVO"]["baseForm"]["processBasicInfo"]["id"]
    processInstanceId = res["data"]["erd.cloud.dto.EtProcessInstance"]["processInstanceId"]
    number = res["data"]["erd.cloud.pbo.domain.vo.ParameterVO"]["baseForm"]["processBasicInfo"]["number"]
    processDefinitionId = res["data"]["erd.cloud.dto.EtProcessInstance"]["processDefinitionId"]
    return pboId, id, processInstanceId, number, processDefinitionId


def runningusertask(processInstanceId):
    """
    接口名称：查询流程任务id;
    接口地址：/workflow/v1/task/runningusertask/{processInstanceId}；
    """
    host, headers = ApiTools.getHostAndHeaders()
    url = host + f"/workflow/v1/task/runningusertask/{processInstanceId}"
    r = requests.request("GET", url=url, headers=headers, params={"_": int(time.time())})
    res = r.json()
    taskid = res['res']['data'][0]['id']
    processDefinitionId = res['res']['data'][0]['processDefinitionId']
    print(taskid)
    print(processDefinitionId)
    return taskid, processDefinitionId


def pageQuery_todoList():
    """
    接口名称：查询taskid列表接口;
    接口地址：/workflow/v1/dynamic/api/common/pageQuery/todoList/20/1；
    """
    host, headers = ApiTools.getHostAndHeaders()
    url = host + "/workflow/v1/dynamic/api/common/pageQuery/todoList/20/1"
    data = {"pageSize": 20, "currentPage": 1, "dynamicCondition": [], "orders": [], "keyword": ""}
    r = requests.request("POST", url=url, headers=headers, json=data)
    res = r.json()
    taskids = []
    records = res['res']['data']['record']
    # print(res['res']['data']['record'][5]['id'])
    for record in records:
        taskids.append(record['id'])
    return taskids


def queryNumber(pbId):
    """
    接口地址：/workflow/v1/findformdata/bypobandnodekey；
    """
    host, headers = ApiTools.getHostAndHeaders()
    url = host + "/workflow/v1/findformdata/bypobandnodekey"
    data = {
        "pboId": pbId,
        "sessionId": "Activity_Zids001",
        "processDefinitionId": "ProcessZids001:1:bab0dff6024b11eda24d0a580a010339",
        "taskId": "8b756b65025411eda24d0a580a010339",
        "executionId": "8b5efd1e025411eda24d0a580a010339"
    }
    r = requests.request("POST", url=url, headers=headers, data=data)
    res = r.json()
    print(res)
    return res['data']['processBasicInfo']['number']


def submitActivityTask(pboId, id, processInstanceId, number, taskid):
    """
    接口名称：pbo审批接口;
    接口地址：/workflow/v1/dynamic/api/submit/process/submitActivityTask；
    """

    data = {"parameterVO": {"pboId": pboId, "baseForm": {
        "processBasicInfo": {"id": id, "createBy": "SYS_E39B20EA11E7A81AC85B767C89C1",
                             "createTime": "2022-07-13 10:36:06", "updateBy": "SYS_E39B20EA11E7A81AC85B767C89C1",
                             "updateTime": "2022-07-13 10:36:06", "delFlag": "0", "name": "流程实例(ZIDS)001",
                             "number": number, "description": "原因", "status": "业务状态3,业务状态4",
                             "processId": processInstanceId,
                             "proposer": {"id": "SYS_E39B20EA11E7A81AC85B767C89C1", "code": "1", "name": "admin",
                                          "displayName": "管理员", "mobile": "", "email": "admin@admin.cn",
                                          "avatar": "./static/images/avatar/Avatar-3.png", "type": "license",
                                          "status": "1", "active": "1"}, "roles": [
                {"id": "SYS_101", "updateTime": "2022-06-16 10:02:15", "delFlag": "0", "code": "ADMIN", "name": "系统管理",
                 "flexAttrs": {}, "parentId": "-1", "type": "SYSTEM", "displayCn": "ADMIN", "displayEn": "ADMIN",
                 "sort": -10, "isDefault": "1"},
                {"id": "SYS_dbb4995640faaf0966c4a89dd362", "createTime": "2017-06-02 12:03:18",
                 "updateTime": "2022-06-16 10:01:48", "delFlag": "0", "code": "GENERALUSER", "name": "普通用户",
                 "flexAttrs": {}, "parentId": "-1", "type": "SYSTEM", "displayCn": "GENERALUSER",
                 "displayEn": "GENERALUSER", "sort": -20, "isDefault": "1"}], "procInstVariables": {
                "startCurrentUser": {"leader": "0", "flexAttrs": {}, "orgName": "组织部门", "code": "1",
                                     "displayName": "管理员", "securityLabel": "CONFIDENTIAL", "mobile": "", "active": "1",
                                     "displayEn": "guanliyuan", "updateTime": "1501461835000",
                                     "avatar": "./static/images/avatar/Avatar-3.png", "type": "license", "delFlag": "0",
                                     "orgId": "SYS_2d28fff04a3da56f410a241528b4", "createBy": "", "updateBy": "",
                                     "name": "admin", "id": "SYS_E39B20EA11E7A81AC85B767C89C1",
                                     "email": "admin@admin.cn", "status": "1"}},
                             "startUserId": "SYS_E39B20EA11E7A81AC85B767C89C1",
                             "oid": pboId},
        "businessForm": {"reviewItemList": []}, "businessFormJsonStr": "{\"reviewItemList\":[]}"},
                            "processInstanceId": processInstanceId,
                            "baseSubmitTaskDto": {"routeFlag": 0, "priority": "50", "dueDate": "2022-09-13",
                                                  "sessionId": "Activity_Zids001", "attachmentId": "",
                                                  "taskId": taskid, "comment": "已阅，同意",
                                                  "taskVariables": {}, "userMap": {}, "roleMap": {},
                                                  "customformJson": "{}", "uploadFileIds": [],
                                                  "deleteAttachmentIds": []}}, "informedUserId": ""}
    host, headers = ApiTools.getHostAndHeaders()
    apis.post('submitActivityTask', None)
    url = host + "/workflow/v1/dynamic/api/submit/process/submitActivityTask"
    r = requests.request("POST", url=url, headers=headers, json=data)
    res = r.json()
    print(res)
    return res


def enums(enumName):
    """
    接口名称：pbo审批接口;
    接口地址：/workflow/v1/dynamic/api/status/enums/{enumName}；
    """
    host, headers = ApiTools.getHostAndHeaders()
    url = host + f"/workflow/v1/dynamic/api/status/enums/{enumName}"
    data = {'_': int(time.time())}
    r = requests.request("GET", url=url, headers=headers, params=data)
    res = r.json()
    print(res)
    return res


def model_view(templateId):
    """
    接口名称：模板详情接口;
    接口地址：/workflow/v1/dynamic/api/model/view/{templateId}；
    """
    host, headers = ApiTools.getHostAndHeaders()
    url = host + f"/workflow/v1/dynamic/api/model/view/{templateId}"
    apis.get('model_view', None)
    r = requests.request("GET", url=url, headers=headers)
    res = r.json()
    print(res)
    return res


def queryLayout():
    """
    查询表单
    """
    host, headers = ApiTools.getHostAndHeaders()
    url = host + '/workflow/v1/formlayout/page'
    data = {
        "tenantId": "type1",
        "formName": "表单布局",
        "layoutType": "",
        "pager_name": 20,
        "sortBy": "",
        "orderBy": "",
        "pageSize": 20,
        "pageIndex": 1,
        "contextType": 0,
        "category": 1657674559102,
        "_": int(time.time()),
    }
    r = requests.request("GET", url=url, headers=headers, params=data)
    res = r.json()
    print(res)
    return res['res']['data']['records'][0]['id']


def createLayout():
    """
    创建表单布局
    """
    # 创建分类
    add_category()
    tplJson_data = {
        '1657788956767-0': {'formType': 'text-input', 'title': '单行输入框', 'langKey': 'single__input', 'active': True,
                            'cateType': 'input', 'regex': '/.*/', 'regexTips': '', 'cateName': '输入框',
                            'name': '1657788956767-0', 'disabled': False, 'displayCn': '输入框', 'displayEn': 'input_box',
                            'value': '', 'type': 'text', 'placeholder': '', 'max': 500, 'column': 12, 'required': False,
                            'iconClazz': 'icon-pencil', 'items': [
                {'formType': 'text-input', 'title': '单行输入框', 'langKey': 'single__input', 'active': True},
                {'formType': 'text-icon', 'title': '单行输入框（带图标）', 'icon': 'eliconfont icon-file',
                 'langKey': 'single_input(icon)'},
                {'formType': 'text-addon', 'title': '单行输入框（带单位）', 'langKey': 'single_input(unit)', 'prefix': '$',
                 'suffix': ''}]}}

    tplJson = json.dumps(tplJson_data, ensure_ascii=False)
    data = {"entityTable": "CTM_流程表单", "category": "1657674559102", "entityId": "66be97b9bc7aa25afbce2a80a0fb0749",
            "formName": f"表单布局(ZIDS){int(time.time())}",
            "tplJson": tplJson}
    host, headers = ApiTools.getHostAndHeaders()
    url = host + "/workflow/v1/formlayout"
    r = requests.request("POST", url=url, headers=headers, json=data)
    print(r.text)
    res = r.json()

    return res


def deleteLayout(Layout_id):
    """
      删除表单布局
    """
    host, headers = ApiTools.getHostAndHeaders()
    url = host + f"/workflow/v1/formlayout/{Layout_id}"
    print(url)
    data = [Layout_id]
    r = requests.request("DELETE", url=url, headers=headers, json=data)
    res = r.json()
    return res
