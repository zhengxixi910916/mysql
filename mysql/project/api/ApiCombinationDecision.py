from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "updateUsingPUT_2": "/decision/$VERSION$/portindelemlinks",  # 添加/修改组合决策指标要素关系
    "queryOneUsingGET_1": "/decision/$VERSION$/portindelemlinks/%s",  # 查询组合决策指标要素关系
    "saveWeightUsingPUT": "/decision/$VERSION$/portindelemlinks/%s/weight",  # 分配组合下的指标权重
    "updatestateUsingPUT": "/decision/$VERSION$/portindelemlinkstate/%s",  # 修改组合决策指标要素关系状态
})
def updateUsingPUT_2(self,portfolioId,role_bid1,parent_id,role_bid2, checker=None):
    """
    接口名称：添加/修改组合决策指标要素关系
    接口地址：/decision/$VERSION$/portindelemlinks
    """
    r = RequestService.call_put(apis.get("updateUsingPUT_2", None),json=[{
        "roleAId":portfolioId,
        "roleBId":role_bid1,
        "type":"2",
        "parentId":parent_id
    },{
        "roleAId":portfolioId,
        "roleBId":role_bid2,
        "type":"1",
        "parentId":"-1"}], )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r

def queryOneUsingGET_1(self, portfolioId,checker=None):
    """
    接口名称：查询组合决策指标要素关系
    接口地址：/decision/$VERSION$/portindelemlinks/{portfolioId}
    """
    r = RequestService.call_get(apis.get("queryOneUsingGET_1", portfolioId), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r["res"]["data"]

def saveWeightUsingPUT(self, portfolioId,id1,role_bid1,id2,parent_id,role_bid2,checker=None):
    """
    接口名称：分配组合下的指标权重
    接口地址：/decision/$VERSION$/portindelemlinks/{portfolioId}/weight
    """
    r = RequestService.call_put(apis.get("saveWeightUsingPUT", portfolioId),json=[{
        "id":id1,
        "parentId":"-1",
        "roleAClassName":"erd.cloud.portfolio.portfolio.dto.EtPortfolio",
        "roleAId":portfolioId,
        "roleBClassName":"erd.cloud.portfolio.desicion.dto.EtIndicatorElementDef",
        "roleBId":role_bid1,
        "type":"1",
        "weight":100
    },{
        "id":id2,
        "parentId":parent_id,
        "roleAClassName":"erd.cloud.portfolio.portfolio.dto.EtPortfolio",
        "roleAId":portfolioId,
        "roleBClassName":"erd.cloud.portfolio.desicion.dto.EtIndicatorElementDef",
        "roleBId":role_bid2,
        "type":"2",
        "weight":100
    }],  )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r

def updatestateUsingPUT(self, portfolioId,checker=None):
    """
    接口名称：修改组合决策指标要素关系状态
    接口地址：/decision/$VERSION$/portindelemlinkstate/{portfolioId}
    """
    r = RequestService.call_put(apis.get("updatestateUsingPUT", portfolioId), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r