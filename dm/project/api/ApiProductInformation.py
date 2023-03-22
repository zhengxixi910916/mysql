from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "addProductUsingPOST": "/productteam/$VERSION$/product",  # 产品新增接口
    "getProductMemberUsingGET": "/productteam/$VERSION$/product/list",  # 产品信息查询接口(支持根据人员信息模糊分页查询)
    "removeProductMemberUsingDELETE": "/productteam/$VERSION$/product/%s/members",  # 删除团队
    "getProductByUsingGET": "/productteam/$VERSION$/product/tree",  # 产品查询
    "updateProductUsingPUT": "/productteam/$VERSION$/product/%s",  # 产品信息修改接口
    "deleteProductUsingDELETE": "/productteam/$VERSION$/product/%s",  # 产品软删除接口
    "getProductMemberUsingGET_1": "/productteam/$VERSION$/product/%s/members",  # 查询团队角色或成员
    "saveProductMemberUsingPOST": "/productteam/$VERSION$/product/%s/members",  # 角色新增/修改
    "getUsedCountUsingGET": "/productteam/$VERSION$/product/%s/count",  # 用户在产品团队中应用的数量
    "getUsedInfoUsingGET": "/productteam/$VERSION$/product/%s/info",  # 用户在产品团队中应用的详情信息
})


def add_product(self, parent_id, product_name, checker):
    """
    接口名称：产品新增接口
    接口地址：/productteam/$VERSION$/product
    """
    r = RequestService.call_post(apis.get("addProductUsingPOST", None), json={
        "name": product_name,
        "parentId": parent_id,
        "isSyncProject": 1,
        "type": "businessLine",
        "description": ""
    })
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_product_member(self, page_index, page_Size, checker):
    """
    接口名称：产品信息查询接口(支持根据人员信息模糊分页查询)
    接口地址：/productteam/$VERSION$/product/list
    """
    r = RequestService.call_get(apis.get("getProductMemberUsingGET", None), params={
        "pageIndex": page_index,
        "pagesize": page_Size,
        "likeField": ''
    })
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def remove_product_member(self, product_id, checker):
    """
    接口名称：删除团队
    接口地址：/productteam/$VERSION$/product/members
    """
    r = RequestService.call_get(apis.get("removeProductMemberUsingDELETE", product_id), params={
        "roleKey": "PQA"
    }
                                   )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_product_by(self, parent_id, checker):
    """
    接口名称：产品查询
    接口地址：/productteam/$VERSION$/product/tree
    """
    r = RequestService.call_get(apis.get("getProductByUsingGET", None), params={
        "parentId": parent_id,  # 父产品id - required: False
        "productId": "",  # 产品id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def update_product(self, update_name, update_type, product_id, checker):
    """
    接口名称：产品信息修改接口
    接口地址：/productteam/$VERSION$/product/{productId}
    """
    r = RequestService.call_put(apis.get("updateProductUsingPUT", product_id), json={
        "productId": product_id,
        "name": update_name,
        "parentId": "-1",
        "isSyncProject": 1,
        "type": update_type,
        "description": ""
    }
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delete_product(self, product_id, checker):
    """
    接口名称：产品软删除接口
    接口地址：/productteam/$VERSION$/product/{productId}
    """
    r = RequestService.call_delete(apis.get("deleteProductUsingDELETE", product_id)
                                   )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_product_member_1(self, product_id, checker):
    """
    接口名称：查询团队角色或成员
    接口地址：/productteam/$VERSION$/product/{productId}/members
    """
    r = RequestService.call_get(apis.get("getProductMemberUsingGET_1", product_id))
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def save_product_member(self, user_id, product_id, checker):
    """
    接口名称：角色新增/修改
    接口地址：/productteam/$VERSION$/product/{productId}/members
    """
    r = RequestService.call_post(apis.get("saveProductMemberUsingPOST", product_id), params={
        "roleKey": "PQA",
        "productId": product_id,
        "userIds": user_id
    })
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_used_count(self, user_id, checker):
    """
    接口名称：用户在产品团队中应用的数量
    接口地址：/productteam/$VERSION$/product/{userId}/count
    """
    r = RequestService.call_get(apis.get("getUsedCountUsingGET", user_id))
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_used_info(self, user_id, page_index, page_Size, checker):
    """
    接口名称：用户在产品团队中应用的详情信息
    接口地址：/productteam/$VERSION$/product/{userId}/info
    """
    r = RequestService.call_get(apis.get("getUsedInfoUsingGET", user_id), params={
        "pageIndex": page_index,
        "pagesize": page_Size,  # 页大小 - required: False
    }
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r
