import requests

from erdcloud.CommonServerTest import CommonServer

commonServer = CommonServer()


class RequestService(object):

    @staticmethod
    def call(method="get", url=None, params=None, data=None, json=None, files=None, context=None, headers=None):
        """
        通用请求
        :param method: 请求方法
        :param url: url路径，可拼接请求参数或通过params传递
        :param params: url请求参数-可选
        :param data: 表单数据-可选
        :param json: application/json数据-可选
        :param files: 上传文件-可选
        :param context: 请求前缀-可选
        :param headers: 请求头-可选
        :return: 请求结果json字典数据
        """
        if context is None:
            context = commonServer.get_context()
        if headers is None:
            headers = commonServer.get_headers()

        api_path = method.upper() + ":" + context + url
        # ApiStats.add(api_path)
        print("接口：" + api_path)
        r = requests.request(method, commonServer.get_host() + context + url,
                             params=params,
                             data=data,
                             json=json,
                             files=files,
                             headers=headers)
        return r.json()

    @staticmethod
    def call_post(url, params=None, data=None, json=None, files=None, context=None, headers=None):
        """
        通用Post请求
        :param url: url路径，可拼接请求参数或通过params传递
        :param params: url请求参数-可选
        :param data: 表单数据-可选
        :param json: application/json数据-可选
        :param files: 上传文件-可选
        :param context: 请求前缀-可选
        :param headers: 请求头-可选
        :return: 请求结果json字典数据
        """
        return RequestService.call("post", url, params=params, data=data, json=json, files=files,
                                   context=context, headers=headers)

    @staticmethod
    def call_post_formdata(url, params=None, data=None, json=None, files=None, context=None, headers=None):
        """
        通用Post请求，用于文件上传
        :param url: url路径，可拼接请求参数或通过params传递
        :param params: url请求参数-可选
        :param data: 表单数据-可选
        :param json: application/json数据-可选
        :param files: 上传文件-可选
        :param context: 请求前缀-可选
        :param headers: 请求头-可选
        :return: 请求结果json字典数据
        """
        default_headers = commonServer.get_headers({
            "Content-Type": 'application/x-www-form-urlencoded;charset=UTF-8'
        })
        result = dict.copy(default_headers)
        if headers is not None:
            for k in headers:
                result[k] = headers[k]
        return RequestService.call("post", url, params=params, data=data, json=json, files=files,
                                   context=context, headers=result)

    @staticmethod
    def call_put(url, params=None, data=None, json=None, files=None, context=None, headers=None):
        """
        通用Put请求
        :param url: url路径，可拼接请求参数或通过params传递
        :param params: url请求参数-可选
        :param data: 表单数据-可选
        :param json: application/json数据-可选
        :param files: 上传文件-可选
        :param context: 请求前缀-可选
        :param headers: 请求头-可选
        :return: 请求结果json字典数据
        """
        return RequestService.call("put", url, params=params, data=data, json=json, files=files,
                                   headers=headers, context=context)

    @staticmethod
    def call_delete(url, params=None, data=None, json=None, files=None, context=None, headers=None):
        """
        通用delete请求
        :param url: url路径，可拼接请求参数或通过params传递
        :param params: url请求参数-可选
        :param data: 表单数据-可选
        :param json: application/json数据-可选
        :param files: 上传文件-可选
        :param context: 请求前缀-可选
        :param headers: 请求头-可选
        :return: 请求结果json字典数据
        """
        return RequestService.call("delete", url, params=params, data=data, json=json, files=files,
                                   headers=headers, context=context)

    @staticmethod
    def call_patch(url, params=None, data=None, json=None, files=None, context=None, headers=None):
        """
        通用patch请求
        :param url: url路径，可拼接请求参数或通过params传递
        :param params: url请求参数-可选
        :param data: 表单数据-可选
        :param json: application/json数据-可选
        :param files: 上传文件-可选
        :param context: 请求前缀-可选
        :param headers: 请求头-可选
        :return: 请求结果json字典数据
        """
        return RequestService.call("patch", url, params=params, data=data, json=json, files=files,
                                   headers=headers, context=context)

    @staticmethod
    def call_options(url, params=None, data=None, json=None, files=None, context=None, headers=None):
        """
        通用options请求
        :param url: url路径，可拼接请求参数或通过params传递
        :param params: url请求参数-可选
        :param data: 表单数据-可选
        :param json: application/json数据-可选
        :param files: 上传文件-可选
        :param context: 请求前缀-可选
        :param headers: 请求头-可选
        :return: 请求结果json字典数据
        """
        return RequestService.call("patch", url, params=params, data=data, json=json, files=files,
                                   headers=headers, context=context)

    @staticmethod
    def call_head(url, params=None, data=None, json=None, files=None, context=None, headers=None):
        """
        通用head请求
        :param url: url路径，可拼接请求参数或通过params传递
        :param params: url请求参数-可选
        :param data: 表单数据-可选
        :param json: application/json数据-可选
        :param files: 上传文件-可选
        :param context: 请求前缀-可选
        :param headers: 请求头-可选
        :return: 请求结果json字典数据
        """
        return RequestService.call("head", url, params=params, data=data, json=json, files=files,
                                   headers=headers, context=context)

    @staticmethod
    def call_get(url, params=None, context=None):
        return RequestService.call("get", url, params=params, context=context)

    @staticmethod
    def call_get_download(url, params=None, context=None):
        return RequestService.call_download("get", url, params=params, context=context)

    @staticmethod
    def call_post_json(url, body, context=None):
        return RequestService.call_post(url, json=body, context=context)

    @staticmethod
    def call_post_params(url, params, context=None):
        return RequestService.call_post(url, params=params, context=context)

    # form-date(text)
    @staticmethod
    def call_post_data(url, data, context=None):
        return RequestService.call_post(url, data=data, context=context)

    # form-date(file)
    @staticmethod
    def call_post_file(url, body, context=None):
        return RequestService.call_post(url, files=body, context=context)

    @staticmethod
    def call_post_file_gzip(url, params, files, data=None, json=None):
        zipHeader = commonServer.get_headers()
        if zipHeader.get("Content-Type") is not None:
            zipHeader.pop("Content-Type")
        zipHeader["Content-Encoding"] = "gzip"
        return RequestService.call_post(url, params=params, data=data, json=json, files=files, context=None,
                                        headers=zipHeader)

    @staticmethod
    def call_put_json(url, body, context=None):
        return RequestService.call_put(url, json=body, context=context)

    @staticmethod
    def call_put_params(url, params, context=None):
        return RequestService.call_put(url, params=params, context=context)

    @staticmethod
    def call_put_form_urlencoded(url, params=None, files=None, data=None, json=None):
        header = commonServer.get_headers(custom={'Content-Type': 'application/x-www-form-urlencoded'})
        return RequestService.call_put(url, params=params, data=data, json=json, files=files, context=None,
                                       headers=header)

    @staticmethod
    def call_del_params(url, params, context=None):
        return RequestService.call_delete(url, params=params, context=context)

    @staticmethod
    def call_del_json(url, body, context=None):
        return RequestService.call_delete(url, json=body, context=context)

    @staticmethod
    def call_patch_json(url, body, context=None):
        return RequestService.call_patch(url, json=body, context=context)

    @staticmethod
    def call_patch_params(url, body, context=None):
        return RequestService.call_patch(url, params=body, context=context)

    @staticmethod
    def call_options_json(url, body, context=None):
        return RequestService.call_options(url, json=body, context=context)

    @staticmethod
    def call_options_params(url, body, context=None):
        return RequestService.call_options(url, params=body, context=context)

    @staticmethod
    def call_head_json(url, body, context=None):
        return RequestService.call_head(url, json=body, context=context)

    @staticmethod
    def call_head_params(url, body, context=None):
        return RequestService.call_head(url, params=body, context=context)

    @staticmethod
    def call_download(method="get", url=None, params=None, data=None, json=None, files=None, context=None,
                      headers=None):
        """
        通用请求
        :param method: 请求方法
        :param url: url路径，可拼接请求参数或通过params传递
        :param params: url请求参数-可选
        :param data: 表单数据-可选
        :param json: application/json数据-可选
        :param files: 上传文件-可选
        :param context: 请求前缀-可选
        :param headers: 请求头-可选
        :return: 请求结果json字典数据
        """

        if headers is None:
            headers = commonServer.get_headers()
        if context is None:
            context = commonServer.get_context()

        api_path = method.upper() + ":" + context + url
        # ApiStats.add(api_path)
        r = requests.request(method, commonServer.get_host() + context + url,
                             params=params,
                             data=data,
                             json=json,
                             files=files,
                             headers=headers)
        return r
