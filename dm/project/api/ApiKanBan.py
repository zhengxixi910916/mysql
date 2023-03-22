from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "sortCardUsingPUT": "/proj/$VERSION$/kanban/card/sort/%s/%s",  # 排序卡片
    "syncAllObjectUsingPUT": "/proj/$VERSION$/kanban/card/sync/all",  # 同步系统中所有业务对象到看板
    "updateCardUsingPUT": "/proj/$VERSION$/kanban/card/%s",  # 更新自定义卡片
    "deleteCardUsingDELETE": "/proj/$VERSION$/kanban/card/%s",  # 删除自定义卡片
    "updateCardCompleteUsingPUT": "/proj/$VERSION$/kanban/card/%s",  # 完成自定义卡片
    "createCardUsingPOST": "/proj/$VERSION$/kanban/card/%s",  # 新增自定义卡片
    "getMemberBoardStageUsingGET": "/proj/$VERSION$/kanban/member/board/stage/%s/%s/%s/%s/%s/%s",
    # 获取项目成员看板阶段数据
    "getMemberBoardUsingGET": "/proj/$VERSION$/kanban/member/board/%s/%s/%s",  # 获取项目成员看板
    "getProjectBoardUsingGET": "/proj/$VERSION$/kanban/project/board/%s/%s",  # 获取项目看板
    "getProjectBoardCardUsingGET": "/proj/$VERSION$/kanban/project/card/%s%s",  # 获取项目卡片数据
    "getProjectBoardStageUsingGET": "/proj/$VERSION$/kanban/project/stage/%s/%s/%s/%s/%s/%s",
    # 获取项目看板的阶段数据
    "sortStageUsingPUT": "/proj/$VERSION$/kanban/stage/sort/%s",  # 排序阶段
    "createStageUsingPOST": "/proj/$VERSION$/kanban/stage/%s",  # 创建新的阶段
    "updateStageUsingPUT": "/proj/$VERSION$/kanban/stage/%s",  # 编辑阶段
    "deleteStageUsingDELETE": "/proj/$VERSION$/kanban/stage/%s",  # 删除阶段
    "kanbanTargetTypeUsingGET": "/proj/$VERSION$/kanban/target/type",  # 看板类型字典
    "getUserBoardUsingGET": "/proj/$VERSION$/kanban/user/board",  # 获取当前用户个人看板
    "getUserBoardCardUsingGET": "/proj/$VERSION$/kanban/user/card/%s",  # 获取用户卡片数据
    "getUserBoardStageUsingGET": "/proj/$VERSION$/kanban/user/stage/%s/%s/%s/%s",
    # 获取用户看板的阶段数据
    "getUserBoardStageTypeUsingGET": "/proj/$VERSION$/kanban/user/stage/%s/%s/%s/%s/%s",
    # 获取用户看板的阶段数据-业务类型
    "taskStageBoardUsingGET": "/proj/$VERSION$/kanban/taskStage",  # 任务阶段看板
})


def sortCardUsingPUT(self, checker=None, stageId=None, cardId=None, data=None):
    """
    接口名称：排序卡片
    接口地址：/proj/$VERSION$/kanban/card/sort/{stageId}/{cardId}
    """
    r = RequestService.call_put(apis.get("sortCardUsingPUT", stageId, cardId), json=data
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def syncAllObjectUsingPUT(self, checker=None):
    """
    接口名称：同步系统中所有业务对象到看板
    接口地址：/proj/$VERSION$/kanban/card/sync/all
    """
    r = RequestService.call_put(apis.get("syncAllObjectUsingPUT", None), None)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def updateCardUsingPUT(self, checker=None, card_name=None, cardId=None):
    """
    接口名称：更新自定义卡片
    接口地址：/proj/$VERSION$/kanban/card/{cardId}
    """
    r = RequestService.call_put(apis.get("updateCardUsingPUT", cardId), json={
        "id": "09c4eedb212386166f9bf758b101eec9",
        "name": card_name,
        "complete": 0,
        "desc": "",
        "deadline": "",
        "priority": "低"
    }
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def deleteCardUsingDELETE(self, checker=None, card_id=None):
    """
    接口名称：删除自定义卡片
    接口地址：/proj/$VERSION$/kanban/card/{cardId}
    """
    r = RequestService.call_delete(apis.get("deleteCardUsingDELETE", card_id)
                                   )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def updateCardCompleteUsingPUT(self, checker=None, card_id=None, cardname=None):
    """
    接口名称：完成自定义卡片
    接口地址：/proj/$VERSION$/kanban/card/{cardId}/{complete}
    """
    r = RequestService.call_put(apis.get("updateCardCompleteUsingPUT", card_id), json={
        "id": card_id,
        "complete": 1,
        "name": cardname,
        "desc": "",
        "priority": "低",
        "orderNum": 100
    }
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def createCardUsingPOST(self, checker=None, card_name=None, stageId=None):
    """
    接口名称：新增自定义卡片
    接口地址：/proj/$VERSION$/kanban/card/{stageId}
    """
    r = RequestService.call_post(apis.get("createCardUsingPOST", stageId), json={
        "name": card_name,
        "desc": "",
        "deadline": "",
        "priority": "低",
        "targetType": "3",
        "stageId": stageId,
        "complete": 0,
        "orderNum": 100
    }
                                 )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getMemberBoardStageUsingGET(self, checker=None, data=None):
    """
    接口名称：获取项目成员看板阶段数据
    接口地址：/proj/$VERSION$/kanban/member/board/stage/{project_id}/{targetType}/{memberId}/{complete}/{pageNo}/{page_size}
    """
    r = RequestService.call_get(apis.get("getMemberBoardStageUsingGET",
                                         data['project_id'],
                                         data['targetType'],
                                         data['memberId'],
                                         data['complete'],
                                         data['pageNo'],
                                         data['page_size'],
                                         )
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getMemberBoardUsingGET(self, checker=None, data=None):
    """
    接口名称：获取项目成员看板
    接口地址：/proj/$VERSION$/kanban/member/board/{project_id}/{targetType}/{complete}
    """
    r = RequestService.call_get(apis.get("getMemberBoardUsingGET",
                                         data['project_id'],
                                         data['targetType'],
                                         data['complete'],
                                         )
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getProjectBoardUsingGET(self, checker=None, project_id=None, targetType=None):
    """
    接口名称：获取项目看板
    接口地址：/proj/$VERSION$/kanban/project/board/{project_id}/{targetType}
    """
    r = RequestService.call_get(apis.get("getProjectBoardUsingGET", project_id, targetType))
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getProjectBoardCardUsingGET(self, cardId, targetType, checker=None):
    """
    接口名称：获取项目卡片数据
    接口地址：/proj/$VERSION$/kanban/project/card/{cardId}/{targetType}
    """
    r = RequestService.call_get(apis.get("getProjectBoardCardUsingGET", cardId, targetType), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getProjectBoardStageUsingGET(self, checker=None, data=None):
    """
    接口名称：获取项目看板的阶段数据
    接口地址：/proj/$VERSION$/kanban/project/stage/{project_id}/{targetType}/{stageId}/{complete}/{pageNo}/{page_size}
    """
    r = RequestService.call_get(apis.get("getProjectBoardStageUsingGET",
                                         data['project_id'],
                                         data['targetType'],
                                         data['stageId'],
                                         data['complete'],
                                         data['pageNo'],
                                         data['page_size'],
                                         )
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def sortStageUsingPUT(self, checker=None, data=None, boardId=None):
    """
    接口名称：排序阶段
    接口地址：/proj/$VERSION$/kanban/stage/sort/{boardId}
    """
    r = RequestService.call_put(apis.get("sortStageUsingPUT", boardId), json=data)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def createStageUsingPOST(self, checker=None, boardId=None, board_name=None):
    """
    接口名称：创建新的阶段
    接口地址：/proj/$VERSION$/kanban/stage/{boardId}
    """
    r = RequestService.call_post(apis.get("createStageUsingPOST", boardId), json={
        "name": board_name,
        "orderNum": 600
    }
                                 )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def updateStageUsingPUT(self, checker=None, stageId=None, new_name=None):
    """
    接口名称：编辑阶段
    接口地址：/proj/$VERSION$/kanban/stage/{stageId}
    """
    r = RequestService.call_put(apis.get("updateStageUsingPUT", stageId), json={
        "name": new_name
    }
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def deleteStageUsingDELETE(self, checker=None, stageId=None):
    """
    接口名称：删除阶段
    接口地址：/proj/$VERSION$/kanban/stage/{stageId}
    """
    r = RequestService.call_delete(apis.get("deleteStageUsingDELETE", stageId))
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def kanbanTargetTypeUsingGET(self, checker=None):
    """
    接口名称：看板类型字典
    接口地址：/proj/$VERSION$/kanban/target/type
    """
    r = RequestService.call_get(apis.get("kanbanTargetTypeUsingGET", None), None)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getUserBoardUsingGET(self, checker=None):
    """
    接口名称：获取当前用户个人看板
    接口地址：/proj/$VERSION$/kanban/user/board
    """
    r = RequestService.call_get(apis.get("getUserBoardUsingGET", None), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getUserBoardCardUsingGET(self, checker=None, cardId=None):
    """
    接口名称：获取用户卡片数据
    接口地址：/proj/$VERSION$/kanban/user/card/{cardId}
    """
    r = RequestService.call_get(apis.get("getUserBoardCardUsingGET", cardId))
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getUserBoardStageUsingGET(self, checker=None, data=None):
    """
    接口名称：获取用户看板的阶段数据
    接口地址：/proj/$VERSION$/kanban/user/stage/{stageId}/{complete}/{pageNo}/{page_size}
    """
    r = RequestService.call_get(apis.get("getUserBoardStageUsingGET",
                                         data['stageId'],
                                         data['complete'],
                                         data['pageNo'],
                                         data['page_size']
                                         )
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getUserBoardStageTypeUsingGET(self, checker=None, data=None):
    """
    接口名称：获取用户看板的阶段数据-业务类型
    接口地址：/proj/$VERSION$/kanban/user/stage/{stageId}/{complete}/{pageNo}/{page_size}/{targetType}
    """
    r = RequestService.call_get(apis.get("getUserBoardStageTypeUsingGET",
                                         data['stageId'],
                                         data['complete'],
                                         data['pageNo'],
                                         data['page_size'],
                                         data['targetType']
                                         )
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def taskStageBoardUsingGET(self, project_id, checker=None):
    """
    接口名称：任务阶段看板
    接口地址：/proj/$VERSION$/kanban/taskStage
    """
    r = RequestService.call_get(apis.get("taskStageBoardUsingGET", None), params={
        "planStateComplete": -1,
        "stageFlag": 1,
        "projectId": project_id
    }
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r
