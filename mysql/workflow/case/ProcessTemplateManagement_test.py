import time
import unittest
from workflow.api.ApiProcessTemplateManagement import *
from workflow.api import ApiTools

id = ''
name = ''


class PTM(unittest.TestCase):
    """流程模板管理"""
    mode_id = ''
    def setUp(self) -> None:
        PTM.mode_id = ApiTools.saveOrUpdate_model()
        # # 创建流程模板
        # tim = int(time.time())
        # actDefId = f"Event_{tim}"
        # data = {
        #     "id": None,
        #     "category": "1658800511091",
        #     "tenantId": "erdp",
        #     "globalVariables": [
        #
        #     ],
        #     "globalConfig": [
        #
        #     ],
        #     "actData": [
        #         {
        #             "actDefId": actDefId,
        #             "currentAppId": "erdp",
        #             "localConfig": [
        #
        #             ]
        #         }
        #     ],
        #     "xmlData": f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<bpmn2:definitions xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:bpmn2=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:dc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:activiti=\"http://activiti.org/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" id=\"diagram_Process_1658997221061\" targetNamespace=\"http://activiti.org/test\" xsi:schemaLocation=\"http://www.omg.org/spec/BPMN/20100524/MODEL BPMN20.xsd\">\n  <bpmn2:process id=\"Process_{tim}\" name=\"业务流程_{tim}\" isExecutable=\"true\">\n    <bpmn2:startEvent id=\"" + actDefId + "\" name=\"单节点\">\n      <bpmn2:extensionElements>\n        <activiti:flowstate>1</activiti:flowstate>\n      </bpmn2:extensionElements>\n    </bpmn2:startEvent>\n  </bpmn2:process>\n  <bpmndi:BPMNDiagram id=\"BPMNDiagram_1\">\n    <bpmndi:BPMNPlane id=\"BPMNPlane_1\" bpmnElement=\"Process_1658997221061\">\n      <bpmndi:BPMNShape id=\"" + actDefId + "_di\" bpmnElement=\"" + actDefId + "\">\n        <dc:Bounds x=\"-38\" y=\"-228\" width=\"36\" height=\"36\" />\n        <bpmndi:BPMNLabel>\n          <dc:Bounds x=\"-36\" y=\"-185\" width=\"32\" height=\"14\" />\n        </bpmndi:BPMNLabel>\n      </bpmndi:BPMNShape>\n    </bpmndi:BPMNPlane>\n  </bpmndi:BPMNDiagram>\n</bpmn2:definitions>\n",
        #     "processModelName": f"业务流程_{tim}",
        #     "processModelKey": f"Process_{tim}",
        #     "description": "",
        #     "isCheckIn": "Y",
        #     "procCodeRule": "procInstCodeRule"
        # }
        # r = ApiTools.saveOrUpdate_model(data)
        # print(r)
        # global id, name
        # id = r['res']['data']['id']
        # name = r['res']['data']['processModelName']

    # def test_0001_ptm(self):
    #     # """
        # 部署流程模型:/workflow/v1/procmodel/deploy
        # """
        # # 调用位置:模板维护列表点击启用调用
        #
        # r = process_model_start(model_id=PTM.mode_id)
        # print(r)
        # self.assertEqual('200', r['code'])

    # def test_0002_ptm(self):
    #     """
    #     删除流程模板:/workflow/v1/procmodel/model
    #     """
    #
    #     # # 禁用流程模板
    #     # procmodel_undeploy(name)
    #     # 删除流程模板
    #     r = delete_model_using(model_id=PTM.mode_id)
    #
    #     self.assertEqual('200', r['code'])


if __name__ == '__main__':
    unittest.main()