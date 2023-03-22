from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
日程参与者
'''
apis = Api({
    "updateAgendaResponsibleRelationUsingPUT": "/agenda/$VERSION$/focus/%s",  # updateAgendaResponsibleRelation
})


def updateAgendaResponsibleRelationUsingPUT(self, agenda, checker=None):
    """
    接口名称：updateAgendaResponsibleRelation
    接口地址：/agenda/$VERSION$/focus/{agendaId}
    """
    r = RequestService.call_put(apis.get("updateAgendaResponsibleRelationUsingPUT", None), json={
        "agenda": agenda  # 日程对象 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]
