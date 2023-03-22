import json
import os.path
import time

from jinja2 import Environment, FileSystemLoader

# 接口
apis = []


def get_item_data(item):
    result = {
        "name": item["name"],
        "url": "/".join(item["request"]["url"]["path"]),
        "apiKey": "_".join(item["request"]["url"]["path"]),
        "payload": "params",
        "method": item["request"]["method"].lower()
    }

    if dict(item["request"]).get("body") is not None:
        mode = item["request"]["body"]["mode"]
        result["mode"] = mode
        if mode == "formdata":
            formdata = item["request"]["body"]["formdata"]
            result["payload"] = "data"
            result["hasFormdata"] = True
            result["params"] = parse_formdata_params(formdata)
        if mode == "urlencoded":
            result["payload"] = "params"
            formdata = item["request"]["body"]["urlencoded"]
            result["hasFormdata"] = True
            result["params"] = parse_urlencoded_params(formdata)
        if mode == "raw":
            result["payload"] = "json"
            raw = json.loads(item["request"]["body"]["raw"])
            result["hasFormdata"] = True
            result["strParam"] = False
            if type(raw) == list:
                # 集合
                result_row = []
                for ele in raw:
                    if type(ele) == str:
                        # 字符串
                        result_row.append(ele)
                        result["strParam"] = True
                    else:
                        # 对象
                        result_row.append(parse_raw_params(ele))
                result["params"] = result_row
            else:
                # 对象
                result["params"] = parse_raw_params(raw)
        else:
            result["hasFormdata"] = False
    print(result)
    append_api(result)
    return result


def parse_raw_params(raw):
    n = 0
    data_len = len(raw)
    params = []
    for prop in raw:
        n = n + 1
        params.append(add_param_prop(data_len, n, prop, raw.get(prop)))
    return params


def parse_formdata_params(formdata):
    n = 0
    data_len = len(formdata)
    params = []
    for dataItem in formdata:
        n = n + 1
        params.append(add_param_prop(data_len, n, dataItem["key"], dataItem["value"]))
    return params


def parse_urlencoded_params(formdata):
    n = 0
    data_len = len(formdata)
    params = []
    for dataItem in formdata:
        n = n + 1
        params.append(add_param_prop(data_len, n, dataItem["key"], dataItem["value"]))
    return params


def add_param_prop(data_len, n, key, value):
    if data_len != n:
        return {
            "key": key,
            "value": value,
            "tail": ","
        }
    else:
        return {
            "key": key,
            "value": value,
            "tail": ""
        }


def append_api(result):
    apis.append({
        "apiKey": result.get("apiKey"),
        "url": result.get("url").replace("/v1/", "/$VERSION$/"),
        "desc": result.get("name")
    })


def generate(filepath=None):
    # 'postman.json'
    dir_path = os.path.abspath(os.path.dirname(__file__))
    file_loader = FileSystemLoader(os.path.join(dir_path, 'templates'))
    env = Environment(loader=file_loader)

    api_tmpl = env.get_template('APIS.txt')
    common_tmpl = env.get_template('postman_template.txt')
    result_content = ""
    with open(filepath, encoding='utf-8') as f:
        d = json.loads(f.read())
        result_method = ""
        print(d["item"])
        hasChild = hasattr(d["item"], "item")
        if hasChild:
            for item in d["item"]:
                children = item["item"]
                for child in children:
                    result_method = process_item_data(child, common_tmpl, result_method)
        else:
            for child in d["item"]:
                result_method = process_item_data(child, common_tmpl, result_method)

        result_content = result_content + api_tmpl.render(apis=apis)
        result_content += result_method
        f.close()
        with open("Api_Postman_" + time.strftime("%Y%m%d%H%M", time.localtime()) + ".py", "w", encoding='utf-8') as writer:
            writer.write(result_content)
            writer.close()


def process_item_data(child, common_tmpl, result_method):
    if child["request"]["method"] == "GET":
        result_method += common_tmpl.render(item=get_item_data(child))
    if child["request"]["method"] == "POST":
        result_method += common_tmpl.render(item=get_item_data(child))
    if child["request"]["method"] == "PUT":
        result_method += common_tmpl.render(item=get_item_data(child))
    if child["request"]["method"] == "DELETE":
        result_method += common_tmpl.render(item=get_item_data(child))
    return result_method


if __name__ == "__main__":
    print("根据postman导出的脚本生成api接口")
    generate('D:\git\erdcloud-test\erdcloud-test-py\generator\postman.json')
