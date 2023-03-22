from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
产品分类信息
'''
apis = Api({
    "addProductCategoryUsingPOST": "/product/$VERSION$/category",  # 创建分类信息
    "updateProductCategoryUsingPUT": "/product/$VERSION$/category",  # 修改分类信息
    "getAllProductCategoryListUsingGET": "/product/$VERSION$/category/all",  # 查询所有产品分类信息
    "getAllMajorMinorsUsingGET": "/product/$VERSION$/category/all/majorminors",  # 查询所有大类小类
    "getProductCategoryListUsingGET": "/product/$VERSION$/category/list",  # 查询多个分类信息
    "getNextLevelProductCategoryListUsingGET": "/product/$VERSION$/category/list/%s",  # 查询下一级分类信息
    "getProductCategoryUsingGET": "/product/$VERSION$/category/%s",  # 查询单个分类信息
    "deleteProductCategoryUsingDELETE": "/product/$VERSION$/category/%s",  # 删除分类信息
})


def addProductCategoryUsingPOST(self, name, categoryCode, majorType, minorType,
                                description, parentId, checker=None):
    """
    接口名称：创建分类信息
    接口地址：/product/$VERSION$/category
    """
    r = RequestService.call_post(apis.get("addProductCategoryUsingPOST", None), params={
        "name": name,
        "categoryCode": categoryCode,
        "majorType": majorType,
        "minorType": minorType,
        "description": description,
        "parentId": parentId
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def updateProductCategoryUsingPUT(self, category, checker=None):
    """
    接口名称：修改分类信息
    接口地址：/product/$VERSION$/category
    """
    r = RequestService.call_put(apis.get("updateProductCategoryUsingPUT", None), json={
        "category": category  # 产品分类信息 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getAllProductCategoryListUsingGET(self, checker=None):
    """
    接口名称：查询所有产品分类信息
    接口地址：/product/$VERSION$/category/all
    """
    r = RequestService.call_get(apis.get("getAllProductCategoryListUsingGET", None), None)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getAllMajorMinorsUsingGET(self, checker=None):
    """
    接口名称：查询所有大类小类
    接口地址：/product/$VERSION$/category/all/majorminors
    """
    r = RequestService.call_get(apis.get("getAllMajorMinorsUsingGET", None), None)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getProductCategoryListUsingGET(self, code, name, checker=None):
    """
    接口名称：查询多个分类信息
    接口地址：/product/$VERSION$/category/list
    """
    r = RequestService.call_get(apis.get("getProductCategoryListUsingGET", None), params={
        "code": code,  # 分类编码 - required: False
        "name": name,  # 分类名称 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getNextLevelProductCategoryListUsingGET(self, CategoryId, checker=None):
    """
    接口名称：查询下一级分类信息
    接口地址：/product/$VERSION$/category/list/{id}
    """
    r = RequestService.call_get(apis.get("getNextLevelProductCategoryListUsingGET", CategoryId), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getProductCategoryUsingGET(self, CategoryId, checker=None):
    """
    接口名称：查询单个分类信息
    接口地址：/product/$VERSION$/category/{id}
    """
    r = RequestService.call_get(apis.get("getProductCategoryUsingGET", CategoryId), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def deleteProductCategoryUsingDELETE(self, CategoryId, checker=None):
    """
    接口名称：删除分类信息
    接口地址：/product/$VERSION$/category/{id}
    """
    r = RequestService.call_delete(apis.get("deleteProductCategoryUsingDELETE", CategoryId), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]
