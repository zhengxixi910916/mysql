from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "check_cache_using_get": "/$VERSION$/cache/check",  # 判断某个key存在于哪级的缓存中
    "clear_using_get": "/$VERSION$/cache/clear",  # 清空缓存空间
    "clear_using_post": "/$VERSION$/cache/clear",  # 清空多个缓存空间
    "clear_all_using_get": "/$VERSION$/cache/clearAll",  # 清空所有空间缓存
    "evict_using_post": "/$VERSION$/cache/evict",  # 清空缓存
    "get_cache_using_get": "/$VERSION$/cache/get",  # 获取缓存
    "get_cache_keys_using_get": "/$VERSION$/cache/keys",  # 获取空间keys
    "get_cache_regions_using_get": "/$VERSION$/cache/regions",  # 获取空间
    "check_cache_using_get_1": "/wf/$VERSION$/cache/check",  # 判断某个key存在于哪级的缓存中
    "clear_using_get_1": "/wf/$VERSION$/cache/clear",  # 清空缓存空间
    "clear_using_post_1": "/wf/$VERSION$/cache/clear",  # 清空多个缓存空间
    "clear_all_using_get_1": "/wf/$VERSION$/cache/clearAll",  # 清空所有空间缓存
    "evict_using_post_1": "/wf/$VERSION$/cache/evict",  # 清空缓存
    "get_cache_using_get_1": "/wf/$VERSION$/cache/get",  # 获取缓存
    "get_cache_keys_using_get_1": "/wf/$VERSION$/cache/keys",  # 获取空间keys
    "get_cache_regions_using_get_1": "/wf/$VERSION$/cache/regions",  # 获取空间
})


def check_cache_using_get(self, key, region, checker=None):
    """
    接口名称：判断某个key存在于哪级的缓存中
    接口地址：/$VERSION$/cache/check
    """
    r = RequestService.call_get(apis.get("check_cache_using_get", None), params={
        "key": key,  # key - required: True
        "region": region,  # region - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def clear_using_get(self, region, checker=None):
    """
    接口名称：清空缓存空间
    接口地址：/$VERSION$/cache/clear
    """
    r = RequestService.call_get(apis.get("clear_using_get", None), params={
        "region": region  # region - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def clear_using_post(self, regions, checker=None):
    """
    接口名称：清空多个缓存空间
    接口地址：/$VERSION$/cache/clear
    """
    r = RequestService.call_post(apis.get("clear_using_post", None), json=regions, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def clear_all_using_get(self, checker=None):
    """
    接口名称：清空所有空间缓存
    接口地址：/$VERSION$/cache/clearAll
    """
    r = RequestService.call_get(apis.get("clear_all_using_get", None), None)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def evict_using_post(self, ids, region, checker=None):
    """
    接口名称：清空缓存
    接口地址：/$VERSION$/cache/evict
    """
    r = RequestService.call_post(apis.get("evict_using_post", None), json=ids, params={
        "region": region  # region - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def get_cache_using_get(self, key, region, checker=None):
    """
    接口名称：获取缓存
    接口地址：/$VERSION$/cache/get
    """
    r = RequestService.call_get(apis.get("get_cache_using_get", None), params={
        "key": key,  # key - required: True
        "region": region,  # region - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def get_cache_keys_using_get(self, region, page_index=1, page_size=20, checker=None):
    """
    接口名称：获取空间keys
    接口地址：/$VERSION$/cache/keys
    """
    r = RequestService.call_get(apis.get("get_cache_keys_using_get", None), params={
        "region": region,  # region - required: True
        "pageIndex": page_index,  # None - required: True
        "pageSize": page_size,  # None - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def get_cache_regions_using_get(self, service, page_index=1, page_size=20, checker=None):
    """
    接口名称：获取空间
    接口地址：/$VERSION$/cache/regions
    """
    r = RequestService.call_get(apis.get("get_cache_regions_using_get", None), params={
        "service": service,
        "pageIndex": page_index,  # None - required: True
        "pageSize": page_size,  # None - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def check_cache_using_get_1(self, key, region, checker=None):
    """
    接口名称：判断某个key存在于哪级的缓存中
    接口地址：/wf/$VERSION$/cache/check
    """
    r = RequestService.call_get(apis.get("check_cache_using_get_1", None), params={
        "key": key,  # key - required: True
        "region": region,  # region - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def clear_using_get_1(self, region, checker=None):
    """
    接口名称：清空缓存空间
    接口地址：/wf/$VERSION$/cache/clear
    """
    r = RequestService.call_get(apis.get("clear_using_get_1", None), params={
        "region": region  # region - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def clear_using_post_1(self, regions, checker=None):
    """
    接口名称：清空多个缓存空间
    接口地址：/wf/$VERSION$/cache/clear
    """
    r = RequestService.call_post(apis.get("clear_using_post_1", None), json=regions, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def clear_all_using_get_1(self, checker=None):
    """
    接口名称：清空所有空间缓存
    接口地址：/wf/$VERSION$/cache/clearAll
    """
    r = RequestService.call_get(apis.get("clear_all_using_get_1", None), None)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def evict_using_post_1(self, ids, region, checker=None):
    """
    接口名称：清空缓存
    接口地址：/wf/$VERSION$/cache/evict
    """
    r = RequestService.call_post(apis.get("evict_using_post_1", None), json=ids, params={
        "region": region  # region - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def get_cache_using_get_1(self, key, region, checker=None):
    """
    接口名称：获取缓存
    接口地址：/wf/$VERSION$/cache/get
    """
    r = RequestService.call_get(apis.get("get_cache_using_get_1", None), params={
        "key": key,  # key - required: True
        "region": region,  # region - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def get_cache_keys_using_get_1(self, region, page_index=1, page_size=20, checker=None):
    """
    接口名称：获取空间keys
    接口地址：/wf/$VERSION$/cache/keys
    """
    r = RequestService.call_get(apis.get("get_cache_keys_using_get_1", None), params={
        "region": region,  # region - required: True
        "pageIndex": page_index,  # None - required: True
        "pageSize": page_size,  # None - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def get_cache_regions_using_get_1(self, service, page_index=1, page_size=20, checker=None):
    """
    接口名称：获取空间
    接口地址：/wf/$VERSION$/cache/regions
    """
    r = RequestService.call_get(apis.get("get_cache_regions_using_get_1", None), params={
        "service": service,
        "pageIndex": page_index,  # None - required: True
        "pageSize": page_size,  # None - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r
