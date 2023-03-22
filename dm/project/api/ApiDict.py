# -*- coding: utf-8 -*-
# @Time    : 2021/2/23 11:16
# @Author  : guogaojian

import random

from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "add_dict": "/sys/$VERSION$/dictionary",
    "dict_by_id": "/sys/$VERSION$/dictionary/%s",
    "dict_list": "/sys/$VERSION$/dictionary/types",
    "dict_page": "/sys/$VERSION$/dictionarys",
    "dict_import": "/sys/$VERSION$/dictionary/import",
    "dict_context": "/sys/$VERSION$/dictionarys/context"

})


def add_dict(self, name, typename, attribute, value, sort, display_cn, display_en, parent_id="-1",
             context_id=str(random.randint(100, 999)), context_type="System"):
    """
    新增字典

    Args:
        self:testcase
        name:字典名称
        typename:类型
        attribute:属性
        parent_id:父id
        value:数据值
        sort:排序
        display_cn:中文显示名
        display_en:英文显示名
        context_id:上下文id
        context_type:上下文类型（System/Organization/Project）
    """
    r = RequestService.call_post_params(apis.get("add_dict"), params={
        "typeName": typename,
        "attribute": attribute,
        "parentId": parent_id,
        "value": value,
        "sort": sort,
        "displayCn": display_cn,
        "displayEn": display_en,
        "contextId": context_id,
        "contextType": context_type,
        "name": name
    })
    apis.check_success(self, r)
    return r["res"]["data"]


def dict_import(self, name, typename, attribute, value, sort, display_cn, display_en, parent_id="-1",
                context_id=str(random.randint(100, 999)), context_type="System"):
    """
    导入字典

    Args:
        self:testcase
        name:字典名称
        typename:类型
        attribute:属性
        parent_id:父id
        value:数据值
        sort:排序
        display_cn:中文显示名
        display_en:英文显示名
        context_id:上下文id
        context_type:上下文类型（System/Organization/Project）
    """
    r = RequestService.call_post_params(apis.get("dict_import"), params={
        "typeName": typename,
        "attribute": attribute,
        "parentId": parent_id,
        "value": value,
        "sort": sort,
        "displayCn": display_cn,
        "displayEn": display_en,
        "contextId": context_id,
        "contextType": context_type,
        "name": name
    })
    apis.check_success(self, r)
    return r["res"]["data"]


def query_dict_id(self, eid, name):
    """
    获取字典详情
    """
    r = RequestService.call_get(apis.get("dict_by_id", eid), None)
    apis.check_success(self, r)
    if name is not None:
        self.assertEqual(r['res']["data"]["name"], name)
    return r['res']["data"]


def query_dict_list(self, context_id):
    """
    获取字典类型列表数据
    """
    params = {
        "contextId": context_id
    }
    r = RequestService.call_get(apis.get("dict_list"), params)
    apis.check_success(self, r)


def query_dict_page(self, typename, active):
    """
    获取字典类型列表数据
    """
    params = {
        "typeName": typename,
        "active": active
    }
    r = RequestService.call_get(apis.get("dict_page"), params)
    apis.check_success(self, r)
    if active is not None:
        self.assertEqual(r['res']["data"]["records"][0]["active"], active)


def query_dict_context(self, context_id):
    """
    获取字典类型列表数据
    """
    params = {
        "contextId": context_id
    }
    r = RequestService.call_get(apis.get("dict_context"), params)
    apis.check_success(self, r)


def update_dict(self, eid, name, typename, attribute, value, sort, display_cn, display_en,
                active=1, parent_id="-1", context_type="System"):
    """
    修改字典信息

    Args:
        self:testcase
        eid: 字典id
        name:字典名称
        typename:类型
        attribute:属性
        parent_id:父id
        value:数据值
        sort:排序
        display_cn:中文显示名
        display_en:英文显示名
        active:状态（有效、失效）
        context_type:上下文类型（System/Organization/Project）
    """
    body = {
        "typeName": typename,
        "attribute": attribute,
        "parentId": parent_id,
        "value": value,
        "sort": sort,
        "displayCn": display_cn,
        "displayEn": display_en,
        "active": active,
        "contextType": context_type,
        "name": name,
        "id": eid
    }
    r = RequestService.call_put_json(apis.get("dict_by_id", eid), body)
    apis.check_success(self, r)
    return r['res']["data"]


def delete_dict(self, eid):
    """
    单个删除字典
    """
    r = RequestService.call_del_params(apis.get("dict_by_id", eid), None)
    apis.check_success(self, r)
    return True


def delete_batch_dict(self, payload):
    """
    批量删除字典
    """
    r = RequestService.call_del_json(apis.get("add_dict"), payload)
    apis.check_success(self, r)
    return True
