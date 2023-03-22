from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
刷新生命周期
'''
apis = Api({
    "refreshLifecycleUsingPUT": "/proj/$VERSION$/refresh/lifecycle/%s",  # 刷新生命周期
})


def refreshLifecycleUsingPUT(self, list, type, checker=None):
    """
    接口名称：刷新生命周期
    接口地址：/proj/$VERSION$/refresh/lifecycle/{type}
    """
    r = RequestService.call_put(apis.get("refreshLifecycleUsingPUT", type), json=
        list
    , )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r
