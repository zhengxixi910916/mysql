import json
import requests

from erdcloud import ApiStats, Utils, commonServer

# 获取mapping文件json数据
json_mapping = json.loads(Utils.Config.api_mapping())


def load_prefix():
    """
    加载最新的prefix前缀
    :return: 前缀字典
    """
    # 发送请求，获取数据
    host = commonServer.get_host()
    resp = requests.get(url=host + "/route/prefix")
    data = resp.json().get("res").get("data")

    if data:
        prefix_dict = {}
        for item in data:
            key = item.get("contextPath")
            value = item.get("path")
            # if key != "" and value != "":
            # 判断host/route/prefix接口获取contextPath和path字段属性值为“”或null
            if key != "" and value != "":
                if key is not None and value is not None:
                    prefix_dict[key.split("/")[1]] = value
        return prefix_dict


def parse_version(url):
    """
    解析接口使用的版本
    :param url: url地址
    :return: 版本号
    """
    parts = url.split("$VERSION$")
    if len(parts) > 1:
        version = json_mapping.get("version")
        if version is not None:
            return version
        else:
            return "v1"
    else:
        return ""


def read_prefix(url, prefix_dict):
    """
    获取对应服务的前缀
    :param prefix_dict: 前缀字典
    :param url: url地址
    :return: 服务前缀
    """
    res_prefix = ""
    url_type = url.split("/")[1]
    if prefix_dict is None:
        return res_prefix
    for prefix in prefix_dict:
        if url_type in prefix_dict[prefix]:
            res_prefix = prefix
            break
    return res_prefix


def get_api(apis, key, method="GET", *args):
    """
    获取api版本和前缀
    :param apis: apis属性
    :param key: 需要的apis对应key值
    :param method: 方法
    :param args: 参数
    :return: api地址
    """
    url = apis.get(key)
    version = parse_version(url)
    prefix = read_prefix(url, load_prefix())
    if "$VERSION$" in url:
        api_path = url.replace("$VERSION$", version)
        module = api_path[0: api_path.index("/v")]
        if module.index("/") == 0:
            module = module[1:]
        ApiStats.add(method + ":" + api_path, {
            "prefix": prefix,
            "module": module,
            "version": version,
            "method": method,
            "api": api_path
        })
    else:
        api_path = url

    if args is None or len(args) == 0 or args[0] is None:
        pass
    else:
        api_path = api_path % args

    if prefix != "":
        return "/" + prefix + api_path
    return api_path


class Api:
    def __init__(self, apis):
        self.apis = apis

    def get(self, key, *args):
        """获取解析后的URL"""
        return get_api(self.apis, key, "GET", *args)

    def post(self, key, *args):
        """获取解析后的URL"""
        return get_api(self.apis, key, "POST", *args)

    def put(self, key, *args):
        """获取解析后的URL"""
        return get_api(self.apis, key, "PUT", *args)

    def delete(self, key, *args):
        """获取解析后的URL"""
        return get_api(self.apis, key, "DELETE", *args)

    def check_success(self, context, resp):
        """检查相应结果为成功"""
        self.check(context, resp, "200", True)

    def check_fail(self, context, resp):
        """检查相应结果为失败"""
        context.assertNotEqual("200", resp.get("code"), resp.get("message"))
        context.assertEqual(False, resp.get("success"), resp.get("message"))

    def check(self, context, resp, code, success):
        """自定义检查相应结果"""
        context.assertEqual(code, resp.get("code"), resp.get("message"))
        context.assertEqual(success, resp.get("success"), resp.get("message"))


# ENDING_TMPL = r"""
# <div id='ending'>&nbsp;</div>
# <h3>测试接口数量：%(count)d</h3>
# <div>%(apis)s</div>
# """
# stats = {'count': 149,
#          'apis': ['/sys/v1/acl', '/sys/v1/role/users', '/sys/v1/role/%s/users', '/sys/v1/role/%s/userspage']}
# print(ENDING_TMPL % stats)
