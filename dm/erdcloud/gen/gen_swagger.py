import json
import os.path
import time
import re

from jinja2 import Environment, FileSystemLoader

# 接口
apis = []


def generate(filepath=None, filter_tags=None):
    # swagger.json
    if filter_tags is None:
        filter_tags = []
    dir_path = os.path.abspath(os.path.dirname(__file__))
    file_loader = FileSystemLoader(os.path.join(dir_path, 'templates'))
    env = Environment(loader=file_loader)

    api_tmpl = env.get_template('APIS.txt')
    common_tmpl = env.get_template('swagger_template.txt')
    result_content = ""
    with open(filepath, encoding='utf-8') as f:
        d = json.loads(f.read())
        result_method = ""
        all_apis = []
        for api_url in d["paths"]:
            # print("=============")
            url = api_url
            # print(d["paths"][item])
            for method in d["paths"][api_url]:

                one_api = d["paths"][api_url][method]
                if not contains_tags(one_api.get("tags"), filter_tags):
                    continue

                print(url)
                one = {
                    "name": one_api.get("summary"),
                    "url": url.replace("/v1/", "/$VERSION$/"),
                    "method": method,
                    "apiKey": function_name(one_api.get("operationId")),
                    "desc": one_api.get("summary"),
                    "tags": one_api.get("tags"),
                    "payload": "",
                    "hasFormdata": "",
                    "strParam": "",
                    "hasParams": True,
                    "params": {

                    }
                }
                params = one_api.get("parameters")
                params_data = []
                params_json = []
                params_params = []
                params_path = []
                if params is not None and len(params) != 0:
                    for param in params:
                        the_param = get_param(param)
                        if param.get("in") == "query":
                            params_params.append(the_param)
                        if param.get("in") == "body":
                            params_json.append(the_param)
                        if param.get("in") == "path":
                            params_path.append(the_param)
                        if param.get("in") == "formData":
                            params_data.append(the_param)
                else:
                    one["hasParams"] = False

                one["params"] = {
                    "data": process_params_tail(params_data),
                    "json": process_params_tail(params_json),
                    "params": process_params_tail(params_params),
                    # "path": process_params_tail(params_path)
                }
                result_method += process_item_data(one, common_tmpl)
                all_apis.append(one)
            # print(all_apis)
        f.close()
        result_content = result_content + api_tmpl.render(apis=all_apis)
        result_content += result_method
        with open("Api_Swagger_" + time.strftime("%Y%m%d%H%M", time.localtime()) + ".py", "w",
                  encoding='utf-8') as writer:
            writer.write(result_content)
            writer.close()


def get_param(param):
    the_value = ""
    if hasattr(param, "default"):
        the_value = param.get("default")
    return {
        "key": param.get("name"),
        "value": the_value,
        "in": param.get("in"),
        "description": param.get("description"),
        "required": param.get("required"),
        "allowEmptyValue": param.get("allowEmptyValue")
    }


def contains_tags(tags, filter_tags):
    if len(filter_tags) == 0:
        return True
    for tag in tags:
        if filter_tags.count(tag) != 0:
            print(filter_tags.count(tag))
            return True
    return False


def process_params_tail(datas):
    size = len(datas)
    index = 0
    for data in datas:
        if index + 1 == size:
            data["tail"] = ""
        else:
            data["tail"] = ","
    return datas


def process_item_data(api_item, common_tmpl):
    return common_tmpl.render(item=api_item)


def function_name(name):
    api_name = re.split('([A-Z])', name)
    if len(api_name) > 3:
        api = ('%s_%s%s_%s%s' % (api_name[0], api_name[1], api_name[2], api_name[3], api_name[4])).lower()
        return api
    elif 3 >= len(api_name) >= 2:
        api = ('%s_%s%s' % (api_name[0], api_name[1], api_name[2])).lower()
        return api
    elif len(api_name) < 2:
        api = ('%s' % (api_name[0]).lower())
        return api


if __name__ == "__main__":
    print("根据swagger导出的脚本生成api接口")
    generate('F:/erdcloud_api/swagger.json', ["系统编码管理"])
