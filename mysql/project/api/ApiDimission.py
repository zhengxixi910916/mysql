from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "oneButtonProcessingByUserIdUsingPUT_1": "/proj/$VERSION$/dimission/replace",  # 一键替换遗留事项
    "replaceSimpleByUserIdUsingPUT": "/proj/$VERSION$/dimission/replace/%s/info/%s",  # 单个替换遗留事项
    "oneButtonProcessingByUserIdUsingPUT": "/proj/$VERSION$/dimission/replace/%s/%s",  # 一键替换遗留事项
    "getDimissionInfoByUserIdUsingGET": "/proj/$VERSION$/dimission/%s",  # 根据ID查询离职人员遗留事项
    "getDetailsInfoUsingGET": "/proj/$VERSION$/dimission/%s/info",  # 遗留事项详情列表
})


def oneButtonProcessingByUserIdUsingPUT_1(self, checker):
    """
    接口名称：一键替换遗留事项
    接口地址：/proj/$VERSION$/dimission/replace
    """
    r = RequestService.call_put(apis.get("oneButtonProcessingByUserIdUsingPUT_1", None), json={
        "params": ""  # params - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r


def replaceSimpleByUserIdUsingPUT(self, checker, type, userId, replaceDtoList):
    """
    接口名称：单个替换遗留事项
    接口地址：/proj/$VERSION$/dimission/replace/{userId}/info/{type}
    """
    r = RequestService.call_put(apis.get("replaceSimpleByUserIdUsingPUT", userId, type), json={
        "replaceDtoList": replaceDtoList  # 离职替换对象 - required: False
    }
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r


def oneButtonProcessingByUserIdUsingPUT(self, userId, replaceId, checker=None):
    """
    接口名称：一键替换遗留事项
    接口地址：/proj/$VERSION$/dimission/replace/{userId}/{replaceId}
    """
    r = RequestService.call_put(apis.get("oneButtonProcessingByUserIdUsingPUT", userId, replaceId), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getDimissionInfoByUserIdUsingGET(self, checker, userId):
    """
    接口名称：根据ID查询离职人员遗留事项
    接口地址：/proj/$VERSION$/dimission/{userId}
    """
    r = RequestService.call_get(apis.get("getDimissionInfoByUserIdUsingGET", userId)
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r


def getDetailsInfoUsingGET(self, checker, userId):
    """
    接口名称：遗留事项详情列表
    接口地址：/proj/$VERSION$/dimission/{userId}/info
    """
    r = RequestService.call_get(apis.get("getDetailsInfoUsingGET", userId), params={
        "type": 5,
        "pageindex": 1,
        "pagesize": 5
    },
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
