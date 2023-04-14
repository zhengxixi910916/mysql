import configparser
import requests
import time
import os
import random
def getHostAndHeaders():
    var_values = os.environ.get('erd.test.path.env.config')
    envPath = var_values.split('local:')
    conf = configparser.ConfigParser()
    conf.read(envPath[1])
    host = conf.get('envConf', 'host')
    password = conf.get('envConf', 'password')
    username = conf.get('envConf', 'user')
    oauth_Authorization = conf.get('envConf', 'Authorization')
    data = {
        "password": password,
        "username": username
    }
    oauth_headers = {
        "Authorization": oauth_Authorization
    }
    response = requests.request("POST", url=host + "/oauth/erdp-token", headers=oauth_headers, data=data)
    res = response.json()
    headers = {
        "Authorization": "Bearer " + res["res"]["data"]["access_token"]
    }
    return host, headers


def call(method=None, api=None, params=None, data=None, json=None):
    host, headers = getHostAndHeaders()
    url = host + api
    print(url)
    r = requests.request(method=method, url=url, headers=headers, params=params, data=data, json=json)
    return r.json()


def createUser():
    """
    接口名称：创建用户;
    接口地址：/org/v1/people；
    """
    host, headers = getHostAndHeaders()
    url = host + "/org/v1/people"
    str = int(time.time())
    data = {
        "code": f"zids{str}",
        "displayName": f"测试{str}",
        "lastName": "测试",
        "firstName": f"{str}",
        "name": f"zids{str}",
        "email": f"zids{str}@ceui.com",
        "mobile": f"{str}" + "1",
        "workPlace": "深圳",
        "orgName": "",
        "flexAttrs[orgName]": "",
        "orgId": "SYS_2d28fff04a3da56f410a241528b4",
        "joinDate": "2022-05-31",
        "type": "license",
        "expiryDate": "2023-12-30"
    }
    r = requests.request("POST", url=url, headers=headers, data=data)
    res = r.json()
    print(res)
    return res['res']['data']['id']


def add_category():
    """
    创建流程分类;
    /workflow/v1/category/add；
    """
    data = {"parentId": "-1", "title": "ZIDS分类01", "children": [], "categoryCode": 1657674559102, "sort": 0}
    host, headers = getHostAndHeaders()
    url = host + "/workflow/v1/category/add"
    r = requests.request("POST", url=url, headers=headers, json=data)


def saveOrUpdate_model():
    """
    创建流程模板;
    接口地址：/workflow/v1/procmodel/model/create/newsave；
    """
    data = {
        "jsonXml": '<?xml version="1.0" encoding="UTF-8"?><bpmn2:definitions xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:bpmn2="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" xmlns:di="http://www.omg.org/spec/DD/20100524/DI" xmlns:xsd="http://www.w3.org/2001/XMLSchema" id="diagram_Process_1677729961587" targetNamespace="http://activiti.org/test" xsi:schemaLocation="http://www.omg.org/spec/BPMN/20100524/MODEL BPMN20.xsd"><bpmn2:process id="' + str(
            random.randint(1000000000000,
                           99999999999999)) + '" name="业务流程_1677729961587" isExecutable="true"><bpmn2:startEvent id="Event_13wutva"><bpmn2:outgoing>Flow_00s13hp</bpmn2:outgoing></bpmn2:startEvent><bpmn2:exclusiveGateway id="Gateway_1x26y41" name="创建流程"><bpmn2:documentation>创建流程信息</bpmn2:documentation><bpmn2:incoming>Flow_00s13hp</bpmn2:incoming><bpmn2:outgoing>Flow_00xnl84</bpmn2:outgoing></bpmn2:exclusiveGateway><bpmn2:sequenceFlow id="Flow_00s13hp" sourceRef="Event_13wutva" targetRef="Gateway_1x26y41" /><bpmn2:endEvent id="Event_01vt2y8"><bpmn2:incoming>Flow_00xnl84</bpmn2:incoming></bpmn2:endEvent><bpmn2:sequenceFlow id="Flow_00xnl84" sourceRef="Gateway_1x26y41" targetRef="Event_01vt2y8" /></bpmn2:process><bpmndi:BPMNDiagram id="BPMNDiagram_1"><bpmndi:BPMNPlane id="BPMNPlane_1" bpmnElement="Process_1677729961587"><bpmndi:BPMNEdge id="Flow_00s13hp_di" bpmnElement="Flow_00s13hp"><di:waypoint x="-202" y="510" /><di:waypoint x="-145" y="510" /></bpmndi:BPMNEdge><bpmndi:BPMNEdge id="Flow_00xnl84_di" bpmnElement="Flow_00xnl84"><di:waypoint x="-95" y="510" /><di:waypoint x="-38" y="510" /></bpmndi:BPMNEdge><bpmndi:BPMNShape id="Event_13wutva_di" bpmnElement="Event_13wutva"><dc:Bounds x="-238" y="492" width="36" height="36" /></bpmndi:BPMNShape><bpmndi:BPMNShape id="Gateway_1x26y41_di" bpmnElement="Gateway_1x26y41" isMarkerVisible="true"><dc:Bounds x="-145" y="485" width="50" height="50" /><bpmndi:BPMNLabel><dc:Bounds x="-142" y="542" width="45" height="14" /></bpmndi:BPMNLabel></bpmndi:BPMNShape><bpmndi:BPMNShape id="Event_01vt2y8_di" bpmnElement="Event_01vt2y8"><dc:Bounds x="-38" y="492" width="36" height="36" /></bpmndi:BPMNShape></bpmndi:BPMNPlane></bpmndi:BPMNDiagram></bpmn2:definitions>',
        "name": "业务流程_1677729961587",
        "description": "",
        "category": "others",
        "tenantId": "erdp"}
    add_category()
    host, headers = getHostAndHeaders()
    url = host + "/workflow/v1/procmodel/model/create/newsave"
    r = requests.put(url=url, data=data, headers=headers)
    r = r.json()
    print(r)
    return r["res"]["data"]
