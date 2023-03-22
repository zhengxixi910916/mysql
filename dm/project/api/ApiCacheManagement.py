from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
缓存管理
'''
apis = Api({
    "checkCacheUsingGET": "/proj/$VERSION$/cache/check",  # 判断某个key存在于哪级的缓存中
    "clearUsingGET": "/proj/$VERSION$/cache/clear",  # 清空缓存空间
    "clearUsingPOST": "/proj/$VERSION$/cache/clear",  # 清空多个缓存空间
    "clearAllUsingGET": "/proj/$VERSION$/cache/clearAll",  # 清空所有空间缓存
    "evictUsingPOST": "/proj/$VERSION$/cache/evict",  # 清空缓存
    "getCacheUsingGET": "/proj/$VERSION$/cache/get",  # 获取缓存
    "getCacheKeysUsingGET": "/proj/$VERSION$/cache/keys",  # 获取空间keys
    "getCacheRegionsUsingGET": "/proj/$VERSION$/cache/regions",  # 获取空间
    "checkCacheUsingGET_1": "/$VERSION$/cache/check",  # 判断某个key存在于哪级的缓存中
    "clearUsingGET_1": "/$VERSION$/cache/clear",  # 清空缓存空间
    "clearUsingPOST_1": "/$VERSION$/cache/clear",  # 清空多个缓存空间
    "clearAllUsingGET_1": "/$VERSION$/cache/clearAll",  # 清空所有空间缓存
    "evictUsingPOST_1": "/$VERSION$/cache/evict",  # 清空缓存
    "getCacheUsingGET_1": "/$VERSION$/cache/get",  # 获取缓存
    "getCacheKeysUsingGET_1": "/$VERSION$/cache/keys",  # 获取空间keys
    "getCacheRegionsUsingGET_1": "/$VERSION$/cache/regions",  # 获取空间
})


def checkCacheUsingGET(self, checker):
    """
    接口名称：判断某个key存在于哪级的缓存中
    接口地址：/proj/$VERSION$/cache/check
    """
    r = RequestService.call_get(apis.get("checkCacheUsingGET", None), params={
        "key": "",  # key - required: True
        "region": "",  # region - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def clearUsingGET(self, region, checker=None):
    """
    接口名称：清空缓存空间
    接口地址：/proj/$VERSION$/cache/clear
    """
    r = RequestService.call_get(apis.get("clearUsingGET", None), params={
        "region": region  # region - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def clearUsingPOST(self, regions, checker=None):
    """
    接口名称：清空多个缓存空间
    接口地址：/proj/$VERSION$/cache/clear
    """
    r = RequestService.call_post(apis.get("clearUsingPOST", None), json=regions
                                 )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def clearAllUsingGET(self, checker=None):
    """
    接口名称：清空所有空间缓存
    接口地址：/proj/$VERSION$/cache/clearAll
    """
    r = RequestService.call_get(apis.get("clearAllUsingGET", None), None)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def evictUsingPOST(self, ids, region, checker=None):
    """
    接口名称：清空缓存
    接口地址：/proj/$VERSION$/cache/evict
    """
    r = RequestService.call_post(apis.get("evictUsingPOST", None), json=ids, params={
        "region": region  # region - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def getCacheUsingGET(self, key, region, checker=None):
    """
    接口名称：获取缓存
    接口地址：/proj/$VERSION$/cache/get
    """
    r = RequestService.call_get(apis.get("getCacheUsingGET", None), params={
        "key": key,  # key - required: True
        "region": region,  # region - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getCacheKeysUsingGET(self, page_index, page_size, region, checker=None):
    """
    接口名称：获取空间keys
    接口地址：/proj/$VERSION$/cache/keys
    """
    r = RequestService.call_get(apis.get("getCacheKeysUsingGET", None), params={
        "region": region,  # region - required: True
        "pageindex": page_index,  # None - required: True
        "pagesize": page_size,  # None - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getCacheRegionsUsingGET(self, page_index, page_size, service,pager_name,
                            sortBy=None, orderBy=None, checker=None):
    """
    接口名称：获取空间
    接口地址：/proj/$VERSION$/cache/regions
    """
    r = RequestService.call_get(apis.get("getCacheRegionsUsingGET", None), params={
        "pager_name":pager_name,
        "service": service,
        "sortBy": sortBy,
        "orderBy": orderBy,
        "pageindex": page_index,  # None - required: True
        "pagesize": page_size,  # None - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def checkCacheUsingGET_1(self, checker):
    """
    接口名称：判断某个key存在于哪级的缓存中
    接口地址：/$VERSION$/cache/check
    """
    r = RequestService.call_get(apis.get("checkCacheUsingGET_1", None), params={
        "key": "",  # key - required: True
        "region": "",  # region - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def clearUsingGET_1(self, region, checker=None):
    """
    接口名称：清空缓存空间
    接口地址：/$VERSION$/cache/clear
    """
    r = RequestService.call_get(apis.get("clearUsingGET_1", None), params={
        "region": region  # region - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def clearUsingPOST_1(self, checker):
    """
    接口名称：清空多个缓存空间
    接口地址：/$VERSION$/cache/clear
    """
    r = RequestService.call_post(apis.get("clearUsingPOST_1", None), json={
        "regions": ""  # regions - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def clearAllUsingGET_1(self, checker):
    """
    接口名称：清空所有空间缓存
    接口地址：/$VERSION$/cache/clearAll
    """
    r = RequestService.call_get(apis.get("clearAllUsingGET_1", None), None)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def evictUsingPOST_1(self, checker):
    """
    接口名称：清空缓存
    接口地址：/$VERSION$/cache/evict
    """
    r = RequestService.call_post(apis.get("evictUsingPOST_1", None), json={
        "ids": ""  # ids - required: True
    }, params={
        "region": ""  # region - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getCacheUsingGET_1(self, checker):
    """
    接口名称：获取缓存
    接口地址：/$VERSION$/cache/get
    """
    r = RequestService.call_get(apis.get("getCacheUsingGET_1", None), params={
        "key": "",  # key - required: True
        "region": "",  # region - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getCacheKeysUsingGET_1(self, checker):
    """
    接口名称：获取空间keys
    接口地址：/$VERSION$/cache/keys
    """
    r = RequestService.call_get(apis.get("getCacheKeysUsingGET_1", None), params={
        "region": ""  # region - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getCacheRegionsUsingGET_1(self, page_index, page_size, service, sortBy=None, orderBy=None, checker=None):
    """
    接口名称：获取空间
    接口地址：/$VERSION$/cache/regions
    """
    r = RequestService.call_get(apis.get("getCacheRegionsUsingGET_1", None), params={
        "service": service,
        "sortBy": sortBy,
        "orderBy": orderBy,
        "pageindex": page_index,  # None - required: True
        "pagesize": page_size,  # None - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]
