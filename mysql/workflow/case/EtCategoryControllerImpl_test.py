# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/4/8

import unittest
import time
import random
from workflow.api import ApiEtCategoryControllerImpl, ApiProcessTemplateManagement, ApiOutOfProcessPersonnel, ApiTools


class EtCategoryControllerImpl(unittest.TestCase):
    """et-category-controller-impl/流程模板管理/流程外人员"""
    time1 = time.strftime("%H%M%S")
    category_code = ""
    model_key = ""
    category_id = ""
    def_key = ""
    def_id = ""
    act_def_id = ""
    deploy_ment_id = ""
    model_id = ""
    model_id1 = ""  # 用来闭环测试数据
    model_id2 = ""  # 用来闭环测试数据

    def test_0100_select_all_with_relation_using_get(self):
        """
        接口名称：查询出的类型按照子父关系排好    ;    接口地址：/workflow/$VERSION$/category/relation    ;    调用位置：流程管理-模板维护
        """

        r = ApiEtCategoryControllerImpl.select_all_with_relation_using_get(self)
        print(r)
        EtCategoryControllerImpl.category_code = r["res"]["data"][0]["categoryCode"]
        print("EtCategoryControllerImpl.category_code:", EtCategoryControllerImpl.category_code)

    def test_0101_query_all_using_get(self):
        """
        接口名称：查询所有的类型    ;    接口地址：/workflow/$VERSION$/category/getAll    ;    调用位置：流程管理
        """
        r = ApiEtCategoryControllerImpl.query_all_using_get(self)
        print(r)

    def test_0102_insert_one_using_post(self):
        """
        接口名称：新增一条记录    ;    接口地址：/workflow/$VERSION$/category/add    ;    调用位置：流程管理-模板维护-分类-创建分类
        """

        T = time.time()
        t = str(int(T))
        r = ApiEtCategoryControllerImpl.insert_one_using_post(self,
                                                              category_dto={"title": "分类_" + t,
                                                                            "categoryCode": "test_" + t,
                                                                            "parentId": "-1", "sort": t, "remark": t}
                                                              )
        print(r)
        EtCategoryControllerImpl.category_id = r["res"]["data"]["id"]
        print("EtCategoryControllerImpl.category_id:", EtCategoryControllerImpl.category_id)

    def test_0103_get_one_using_get(self):
        """
        接口名称：getOne    ;    接口地址：/workflow/$VERSION$/category/get/{id}   ;    调用位置：流程管理-模板维护-分类-编辑-点击修改图标
        """

        r = ApiEtCategoryControllerImpl.get_one_using_get(self,
                                                          category_id=EtCategoryControllerImpl.category_id
                                                          )
        print(r)

    def test_0104_update_data_using_put(self):
        """
        接口名称：更新一条记录   ;     接口地址：/workflow/$VERSION$/category/change/{id}    ;    调用位置：流程管理-模板维护-分类-编辑分类
        """

        T = time.time()
        t = str(int(T))
        r = ApiEtCategoryControllerImpl.update_data_using_put(self,
                                                              category_id=EtCategoryControllerImpl.category_id,
                                                              category_dto={"title": "分类_" + t,
                                                                            "categoryCode": "test_" + t,
                                                                            "parentId": "-1", "sort": t, "remark": t,
                                                                            "flexAttrs": {}}
                                                              )
        print(r)

    def test_0105_delete_one_using_delete(self):
        """
        接口名称：deleteOne    ;    接口地址：/workflow/$VERSION$/category/delete/{id}   ;  调用位置：流程管理-模板维护-分类-删除分类
        """

        r = ApiEtCategoryControllerImpl.delete_one_using_delete(self,
                                                                category_id=EtCategoryControllerImpl.category_id
                                                                )
        print(r)
    @unittest.skip
    def test_0300_bind_user_using_post(self):
        """
        该接口在BPM2.4.0已废弃
        接口名称：绑定用户   ;    接口地址：/workflow/$VERSION$/view/bind    ;  调用位置：不知道
        """

        r = ApiOutOfProcessPersonnel.bind_user_using_post(self,
                                                          category=EtCategoryControllerImpl.category_code,
                                                          model_key=EtCategoryControllerImpl.model_key,
                                                          user_ids=""
                                                          )
        print(r)

    def test_0301_get_bind_user_using_get(self):
        """
        接口名称：查看绑定得用户    ;    接口地址：/workflow/$VERSION$/view/{modelKey}    ;    调用位置：不知道
        """

        r = ApiOutOfProcessPersonnel.get_bind_user_using_get(self,
                                                             model_key=EtCategoryControllerImpl.model_key,
                                                             category=EtCategoryControllerImpl.category_code,
                                                             )
        print(r)

    def test_0201_query_deployed_process(self):
        """
          接口名称：查询所有已经发布的流程定义;    接口地址：/workflow/$VERSION$/procmodel/procdef/list；
        """
        r = ApiProcessTemplateManagement.query_deployed_process(self, )
        print(r)

    def test_0202_query_query_process_using(self):
        """
        接口名称：分页查询已发布的流程模型;    接口地址：/workflow/$VERSION$/procmodel/query/available；
        """
        r = ApiProcessTemplateManagement.query_process_using(self, )
        print(r)

    def test_0203_query_other_using(self):
        """
        接口名称：未绑定生命周期流程模型;    接口地址：/workflow/$VERSION$/procmodel/queryOther；
        """
        r = ApiProcessTemplateManagement.query_other_using(self, )
        print(r)
    @unittest.skip
    def test_0204_get_resource_path(self):
        """
        该接口在BPM2.4.0版本 弃用
        接口名称：查询流程节点资源包;    接口地址：/workflow/$VERSION$/procmodel/resource/path/{processDefinitionId}/{taskDefKey}；
        """
        r = ApiProcessTemplateManagement.get_resource_path(self,
                                                           def_id=EtCategoryControllerImpl.def_id,
                                                           act_def_id=EtCategoryControllerImpl.act_def_id
                                                           )
        print(r)

    # todo 未完成,这个应该是一个导出的接口。
    # def test_0205_query_process_resource(self):
    #     """
    #     接口名称：流程资源文件（resourceType为xml或png）;    接口地址：/workflow/$VERSION$/procmodel/resource/{processDefinitionKey}；
    #     """
    #     ApiProcessTemplateManagement.query_process_resource(self,
    #                                                         def_key=EtCategoryControllerImpl.def_key,
    #                                                         resource_type="image"  # 有两个类型：image和xml
    #                                                         )

    def test_0206_validate_process_model(self):
        """
        接口名称：流程资源文件（resourceType为xml或png）;    接口地址：/workflow/$VERSION$/procmodel/resource/{processDefinitionKey}；
        """
        r = ApiProcessTemplateManagement.validate_process_model(self,
                                                                json_xml='{"resourceId":"create","properties":{"process_id":"elead_1652407631068","name":"","businessinterface":"","documentation":"","process_author":"","signaldefinitions":""},"stencil":{"id":"BPMNDiagram"},"childShapes":[{"resourceId":"sid-0307436E-C03D-4AC3-AA49-B607DCA77C1B","properties":{"overrideid":"keyl33sudun","name":"","documentation":"","flowstate":"","businessinterface":"","duedatedefinition":"${dueDate}","prioritydefinition":"${priority}"},"stencil":{"id":"StartNoneEvent"},"childShapes":[],"outgoing":[],"bounds":{"lowerRight":{"x":223,"y":134},"upperLeft":{"x":193,"y":104}},"dockers":[]}],"bounds":{"lowerRight":{"x":3200,"y":5050},"upperLeft":{"x":0,"y":0}},"stencilset":{"url":"stencilsets/bpmn2.0/bpmn2.0.json","namespace":"http://b3mn.org/stencilset/bpmn2.0#"},"ssextensions":[]}'
                                                                )
        print(r)

    def test_0207_new_validate_process(self):
        """
        接口名称：流程资源文件（resourceType为xml或png）;    接口地址：/workflow/$VERSION$/procmodel/resource/{processDefinitionKey}；
        """
        r = ApiProcessTemplateManagement.new_validate_process(self,
                                                              json_xml='<?xml version="1.0" encoding="UTF-8"?> <bpmn2:definitions xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:bpmn2="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" xmlns:xsd="http://www.w3.org/2001/XMLSchema" id="diagram_Process_1652406677462" targetNamespace="http://activiti.org/test" xsi:schemaLocation="http://www.omg.org/spec/BPMN/20100524/MODEL BPMN20.xsd">   <bpmn2:process id="Process_1652406677462" name="业务流程_1652406677462" isExecutable="true">     <bpmn2:startEvent id="Event_1wggv85" />   </bpmn2:process>   <bpmndi:BPMNDiagram id="BPMNDiagram_1">     <bpmndi:BPMNPlane id="BPMNPlane_1" bpmnElement="Process_1652406677462">       <bpmndi:BPMNShape id="Event_1wggv85_di" bpmnElement="Event_1wggv85">         <dc:Bounds x="-88" y="-38" width="36" height="36" />       </bpmndi:BPMNShape>     </bpmndi:BPMNPlane>   </bpmndi:BPMNDiagram> </bpmn2:definitions>'
                                                              )
        print(r)

    def test_0208_query_model_list(self):
        """
        接口名称：查询流程模型列表;    接口地址：/workflow/$VERSION$/procmodel/modellist；
        """
        r = ApiProcessTemplateManagement.query_model_list(self,
                                                          )
        print(r)

    def test_0209_get_editor_xml(self):
        """
        接口名称：新流程模型设计器调用，返回xml数据;    接口地址：/workflow/$VERSION$/procmodel/model/{modelId}/xml；
        """
        r = ApiProcessTemplateManagement.get_editor_xml(self,
                                                        model_id=EtCategoryControllerImpl.model_id
                                                        )
        print(r)
    @unittest.skip
    # def test_0210_get_editor_json(self):
    #     """
    #     该接口在BPM2.4.0版本 弃用
    #     接口名称：流程模型设计器调用;    接口地址：/workflow/$VERSION$/procmodel/model/{modelId}/json；
    #     """
    #     r = ApiProcessTemplateManagement.get_editor_json(self,
    #                                                      model_id=EtCategoryControllerImpl.model_id
    #                                                      )
    #     print(r)

    def test_0212_list_process_using(self):
        """
        接口名称：根据多个key查询已发布的流程模型;    接口地址：/workflow/$VERSION$/procmodel/list/available；
        """
        r = ApiProcessTemplateManagement.list_process_using(self,
                                                            def_key=EtCategoryControllerImpl.def_key
                                                            )
        print(r)

    def test_0213_get_stencilset_using(self):
        """
        接口名称：流程模型设计器调用;    接口地址：/workflow/$VERSION$/procmodel/editor/stencilset；
        """
        r = ApiProcessTemplateManagement.get_stencilset_using(self,
                                                              )
        print(r)

    # def test_0291_delete_deployment_using(self):
    #     """
    #     接口名称：级联删除流程定义(把流程定义流程实例等相关联的所有信息删除);    接口地址：/workflow/$VERSION$/procmodel/undeploy；
    #     """
    #     # # 创建流程模板
    #     # tim = int(time.time())
    #     # actDefId = f"Event_{tim}"
    #     # data = {
    #     #     "id": None,
    #     #     "category": "1658800511091",
    #     #     "tenantId": "erdp",
    #     #     "globalVariables": [
    #     #
    #     #     ],
    #     #     "globalConfig": [
    #     #
    #     #     ],
    #     #     "actData": [
    #     #         {
    #     #             "actDefId": actDefId,
    #     #             "currentAppId": "erdp",
    #     #             "localConfig": [
    #     #
    #     #             ]
    #     #         }
    #     #     ],
    #     #     "xmlData": f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<bpmn2:definitions xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:bpmn2=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:dc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:activiti=\"http://activiti.org/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" id=\"diagram_Process_1658997221061\" targetNamespace=\"http://activiti.org/test\" xsi:schemaLocation=\"http://www.omg.org/spec/BPMN/20100524/MODEL BPMN20.xsd\">\n  <bpmn2:process id=\"Process_{tim}\" name=\"业务流程_{tim}\" isExecutable=\"true\">\n    <bpmn2:startEvent id=\"" + actDefId + "\" name=\"单节点\">\n      <bpmn2:extensionElements>\n        <activiti:flowstate>1</activiti:flowstate>\n      </bpmn2:extensionElements>\n    </bpmn2:startEvent>\n  </bpmn2:process>\n  <bpmndi:BPMNDiagram id=\"BPMNDiagram_1\">\n    <bpmndi:BPMNPlane id=\"BPMNPlane_1\" bpmnElement=\"Process_1658997221061\">\n      <bpmndi:BPMNShape id=\"" + actDefId + "_di\" bpmnElement=\"" + actDefId + "\">\n        <dc:Bounds x=\"-38\" y=\"-228\" width=\"36\" height=\"36\" />\n        <bpmndi:BPMNLabel>\n          <dc:Bounds x=\"-36\" y=\"-185\" width=\"32\" height=\"14\" />\n        </bpmndi:BPMNLabel>\n      </bpmndi:BPMNShape>\n    </bpmndi:BPMNPlane>\n  </bpmndi:BPMNDiagram>\n</bpmn2:definitions>\n",
    #     #     "processModelName": f"业务流程_{tim}",
    #     #     "processModelKey": f"Process_{tim}",
    #     #     "description": "",
    #     #     "isCheckIn": "Y",
    #     #     "procCodeRule": "procInstCodeRule"
    #     # }
    #
    #     res = ApiTools.saveOrUpdate_model()
    #     # api = "/workflow/v1/dynamic/api/common/pageQuery/model/20/1"
    #     # r = ApiTools.call(method='POST', api=api,
    #     #                   json={"pageSize": 20, "currentPage": 1, "dynamicCondition": [], "orders": [],
    #     #                         "keyword": name})
    #     # tmp_list = r['res']['data']['record'][0]['attribute']
    #     # id = ''
    #     # for tmp_dict in tmp_list:
    #     #     if tmp_dict['attrName'] == 'deploymentId':
    #     #         id = tmp_dict['value']
    #     r = ApiProcessTemplateManagement.delete_deployment_using(self,
    #                                                              deploy_ment_id=res
    #                                                              )
    #     print(r)
    @unittest.skip
    def test_0293_delete_process_definition(self):
        """
        该接口在BPM2.4.0版本已废弃
        接口名称：级联删除流程定义(把流程定义流程实例等相关联的所有信息删除);    接口地址：/workflow/$VERSION$/procmodel；
        """
        r = ApiProcessTemplateManagement.delete_process_definition(self,
                                                                   deploy_ment_id=EtCategoryControllerImpl.deploy_ment_id
                                                                   )
        print(r)
        r = ApiProcessTemplateManagement.process_model_start(self,
                                                             model_id=EtCategoryControllerImpl.model_id
                                                             )
        print(r)

    @unittest.skip
    def test_0292_process_model_start(self):
        """
        该接口在BPM2.4.0版本 弃用
        接口名称：部署流程模型;    接口地址：/workflow/$VERSION$/procmodel/deploy；
        """
        r = ApiProcessTemplateManagement.process_model_start(self,
                                                             model_id=EtCategoryControllerImpl.model_id
                                                             )
        print(r)

    @unittest.skip
    def test_0294_copy_model_using(self):
        """
        该接口在BPM2.4.0版本 弃用
        接口名称：复制流程模型;    接口地址：/workflow/$VERSION$/procmodel/copymodel；
        """
        r = ApiProcessTemplateManagement.copy_model_using(self,
                                                          model_key="key" + EtCategoryControllerImpl.time1,
                                                          newname="name" + EtCategoryControllerImpl.time1,
                                                          model_id=EtCategoryControllerImpl.model_id
                                                          )
        print(r)
        # 重新获取一下参数。
        r = ApiProcessTemplateManagement.query_page_using_get_5(self,
                                                                dto={
                                                                    "category": EtCategoryControllerImpl.category_code,
                                                                    "pageSize": 20
                                                                }
                                                                )
        EtCategoryControllerImpl.model_id = r["res"]["data"]["records"][0]["id"]
        print("EtCategoryControllerImpl.model_id:", EtCategoryControllerImpl.model_id)

if __name__ == '__main__':
    # unittest.TestCase()
    unittest.main()