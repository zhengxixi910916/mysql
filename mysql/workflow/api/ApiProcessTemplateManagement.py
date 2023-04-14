import requests
from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api
from workflow.api import ApiTools as ApiTools

apis = Api({
    "delete_process_definition": "/workflow/$VERSION$/procmodel",  # 级联删除流程定义(把流程定义流程实例等相关联的所有信息删除)
    "copy_model_using": "/workflow/$VERSION$/procmodel/copymodel",  # 复制流程模型
    "process_model_start": "/workflow/$VERSION$/procmodel/deploy",  # 部署流程模型
    "get_stencilset_using": "/workflow/$VERSION$/procmodel/editor/stencilset",  # 流程模型设计器调用
    "export_bpmn_and": "/workflow/$VERSION$/procmodel/export/config/%s/%s",  # 导出BPNM及节点配置
    "export_bpmn_using": "/workflow/$VERSION$/procmodel/export/%s/%s",  # 导出BPNM
    "import_bpmn_using": "/workflow/$VERSION$/procmodel/import",  # 导入BPNM
    "import_bpmn_and": "/workflow/$VERSION$/procmodel/import/config",  # 导入BPNM及节点配置
    "list_process_using": "/workflow/$VERSION$/procmodel/list/available",  # 根据多个key查询已发布的流程模型
    "delete_model_using": "/workflow/$VERSION$/procmodel/model",  # 删除流程模板
    "get_editor_xml": "/workflow/$VERSION$/procmodel/model/%s/xml",  # 新流程模型设计器调用，返回xml数据
    "query_model_list": "/workflow/$VERSION$/procmodel/modellist",  # 查询流程模型列表
    "new_validate_process": "/workflow/$VERSION$/procmodel/newvalidate",  # 验证流程模板格式是否正确
    "query_deployed_process": "/workflow/$VERSION$/procmodel/procdef/list",  # 查询所有已经发布的流程定义
    "query_process_using": "/workflow/$VERSION$/procmodel/query/available",  # 分页查询已发布的流程模型
    "query_other_using": "/workflow/$VERSION$/procmodel/queryOther",  # 未绑定生命周期流程模型
    "query_page_using_get_5": "/workflow/$VERSION$/procmodel/queryPage",  # 分页查询流程模型
    "get_resource_path": "/workflow/$VERSION$/procmodel/resource/path/%s/%s",  # 查询流程节点资源包
    "query_process_resource": "/workflow/$VERSION$/procmodel/resource/%s",
    # 流程资源文件（resourceType为xml或png）
    "delete_deployment_using": "/workflow/$VERSION$/procmodel/undeploy",  # 级联删除流程定义(把流程定义流程实例等相关联的所有信息删除)
    "validate_process_model": "/workflow/$VERSION$/procmodel/validate",  # 验证流程模板格式是否正确
})


def delete_process_definition(self, deploy_ment_id, checker=None):
    """
    接口名称：级联删除流程定义(把流程定义流程实例等相关联的所有信息删除);    接口地址：/workflow/$VERSION$/procmodel；
    """
    r = RequestService.call_delete(apis.get("delete_process_definition", None), params={
        "deploymentId": deploy_ment_id  # 流程部署ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def copy_model_using(self, model_key, newname, model_id, checker=None):
    """
    接口名称：复制流程模型;    接口地址：/workflow/$VERSION$/procmodel/copymodel；
    """
    r = RequestService.call_post(apis.get("copy_model_using", None), params={
        "newModelKey": model_key,  # 模板KEY - required: True
        "newModelName": newname,  # 模板名称 - required: True
        "sourceModelId": model_id,  # 模板ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def process_model_start(model_id):
    """
    接口名称：部署流程模型;    接口地址：/workflow/$VERSION$/procmodel/deploy；
    """
    r = RequestService.call_get(apis.get("process_model_start", ), params={
        "modelId": model_id
    }
                                )
    return r


def get_stencilset_using(self):
    """
    接口名称：流程模型设计器调用;    接口地址：/workflow/$VERSION$/procmodel/editor/stencilset；
    """
    r = RequestService.call_get(apis.get("get_stencilset_using", None), None)
    if r is not None:
        self.assertNotEqual(r["stencils"], None)
    else:
        apis.check_success(self, r)
    return r


def export_bpmn_and(self, checker=None):
    """
    接口名称：导出BPNM及节点配置;    接口地址：/workflow/$VERSION$/procmodel/export/config/{processDefinitionKey}/{modelId}；
    """
    r = RequestService.call_get(apis.get("export_bpmn_and", None), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def export_bpmn_using(self, checker=None):
    """
    接口名称：导出BPNM;    接口地址：/workflow/$VERSION$/procmodel/export/{processDefinitionKey}/{modelId}；
    """
    r = RequestService.call_get(apis.get("export_bpmn_using", None), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def import_bpmn_using(self, checker=None):
    """
    接口名称：导入BPNM;    接口地址：/workflow/$VERSION$/procmodel/import；
    """
    r = RequestService.call_post(apis.get("import_bpmn_using", None), data={
        "file": ""  # file - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def import_bpmn_and(self, checker=None):
    """
    接口名称：导入BPNM及节点配置;    接口地址：/workflow/$VERSION$/procmodel/import/config；
    """
    r = RequestService.call_post(apis.get("import_bpmn_and", None), data={
        "file": ""  # file - required: True
    }, params={
        "appId": "",  # None - required: False
        "isConfig": "",  # 是否导入节点配置 1导入 2不导入 - required: False
        "isReleased": "",  # 是否发布标识 1发布 2不发布 - required: False
        "userId": "",  # None - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def list_process_using(self, def_key, checker=None):
    """
    接口名称：根据多个key查询已发布的流程模型;    接口地址：/workflow/$VERSION$/procmodel/list/available；
    """
    r = RequestService.call_get(apis.get("list_process_using", None), params={
        "processDefinitionKeys": def_key  # 流程模型KEYs,多个逗号隔开 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delete_model_using(model_id):
    """
    接口名称：删除流程模板;    接口地址：/workflow/$VERSION$/procmodel/model；
    """
    r = RequestService.call_delete(apis.delete("delete_model_using", None), params={
        "modelId": model_id  # 流程模型ID - required: True
    }, )
    return r


def get_editor_xml(self, model_id, checker=None):
    """
    接口名称：新流程模型设计器调用，返回xml数据;    接口地址：/workflow/$VERSION$/procmodel/model/{modelId}/xml；
    """
    r = RequestService.call_get(apis.get("get_editor_xml", model_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_model_list(self, checker=None):
    """
    接口名称：查询流程模型列表;    接口地址：/workflow/$VERSION$/procmodel/modellist；
    """
    r = RequestService.call_get(apis.get("query_model_list", None), params={

    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def new_validate_process(self, json_xml, checker=None):
    """
    接口名称：验证流程模板格式是否正确;    接口地址：/workflow/$VERSION$/procmodel/newvalidate；
    """
    r = RequestService.call_post(apis.post("new_validate_process", None), params={
        "json_xml": json_xml  # json_xml - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_deployed_process(self, checker=None):
    """
    接口名称：查询所有已经发布的流程定义;    接口地址：/workflow/$VERSION$/procmodel/procdef/list；
    """
    r = RequestService.call_get(apis.get("query_deployed_process", None), None)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_process_using(self, def_key="", checker=None):
    """
    接口名称：分页查询已发布的流程模型;    接口地址：/workflow/$VERSION$/procmodel/query/available；
    """
    r = RequestService.call_get(apis.get("query_process_using", None), params={
        "pageIndex": 1,  # 页码 - required: False
        "pageSize": 20,  # 每页条数 - required: False
        "processDefinitionKey": def_key,  # 流程模型KEY或者流程名称 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_other_using(self, tenant_id="", checker=None):
    """
    接口名称：未绑定生命周期流程模型;    接口地址：/workflow/$VERSION$/procmodel/queryOther；
    """
    r = RequestService.call_get(apis.get("query_other_using", None), params={
        "tenantId": tenant_id  # tenantId - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_page_using_get_5(self, dto, checker=None):
    """
    接口名称：分页查询流程模型
    接口地址：/workflow/$VERSION$/procmodel/queryPage
    """
    r = RequestService.call_get(apis.get("query_page_using_get_5", None), params={
        "tenantId": dto.get("tenantId", "erdp"),
        "name": dto.get("name", ""),
        "modelKey": dto.get("modelKey", ""),
        "processDefinitionName": dto.get("processDefinitionName", ""),
        "sortBy": dto.get("sortBy", ""),
        "orderBy": dto.get("orderBy", ""),
        "pageSize": dto.get("pageSize", "100000"),
        "pageIndex": dto.get("pageIndex", "1"),
        "contextType": dto.get("contextType", "0"),
        "category": dto.get("category", ""),
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def get_resource_path(self, def_id, act_def_id, checker=None):
    """
    接口名称：查询流程节点资源包;    接口地址：/workflow/$VERSION$/procmodel/resource/path/{processDefinitionId}/{taskDefKey}；
    """
    r = RequestService.call_get(apis.get("get_resource_path", def_id, act_def_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_process_resource(self, def_key, resource_type, checker=None):
    """
    接口名称：流程资源文件（resourceType为xml或png）;    接口地址：/workflow/$VERSION$/procmodel/resource/{processDefinitionKey}；
    """
    r = RequestService.call_get(apis.get("query_process_resource", def_key), params={
        "resourceType": resource_type  # 资源类型(xml或image) - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def procmodel_undeploy(name):
    """
    接口名称：禁用流程模板;    接口地址：/workflow/v1/procmodel/undeploy；
    """
    api = "/workflow/v1/dynamic/api/common/pageQuery/model/20/1"
    r = ApiTools.call(method='POST', api=api,
                      json={"pageSize": 20, "currentPage": 1, "dynamicCondition": [], "orders": [], "keyword": name})
    tmp_list = r['res']['data']['record'][0]['attribute']
    id = ''
    for tmp_dict in tmp_list:
        if tmp_dict['attrName'] == 'deploymentId':
            id = tmp_dict['value']
    res = RequestService.call_delete(url=apis.delete('delete_deployment_using', None), params={"deploymentId": id})
    return res


def delete_deployment_using(self, deploy_ment_id, checker=None):
    """
    接口名称：级联删除流程定义(把流程定义流程实例等相关联的所有信息删除);    接口地址：/workflow/$VERSION$/procmodel/undeploy；
    """
    r = RequestService.call_delete(apis.delete("delete_deployment_using", None), params={
        "deploymentId": deploy_ment_id  # 流程部署ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def validate_process_model(self, json_xml, checker=None):
    """
    接口名称：验证流程模板格式是否正确;    接口地址：/workflow/$VERSION$/procmodel/validate；
    """
    r = RequestService.call_post(apis.post("validate_process_model", None), params={
        "json_xml": json_xml  # json_xml - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r
