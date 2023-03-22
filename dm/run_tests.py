# -*- coding: utf-8 -*-#
# Author: YANGJIONG
# Date:   2022/12/2
# @unittest.skip('xx')
# if checker is not None:
#     apis.check(self, r, checker["code"], checker["success"])
# else:
#     apis.check_success(self, r)
# return r

import json
from pathlib import Path
from unittest import defaultTestLoader

from erdcloud.HTMLTestRunner import HTMLTestRunner

# 指定测试用例为当前文件夹下的 interface 目录
test_dir = '.'


def parse_dir(root_dir):
    """
    读取package.json
    :return
    """
    path = Path(root_dir)
    all_json_file = list(path.glob('*/package.json'))
    parse_result = []
    for json_file in all_json_file:
        service_name = json_file.parent.stem
        with json_file.open(encoding="utf-8") as f:
            json_result = json.load(f)
            json_result['module_name'] = service_name
        parse_result.append(json_result)

    return parse_result


if __name__ == "__main__":
    filename = './report/test_interface_result.html'
    fp = open(filename, 'wb')

    # 读取服务json 文件
    package_json_list = parse_dir('./')

    runner = HTMLTestRunner(stream=fp,
                            title='eRDP企业研发管理平台',
                            description='unittest')
    runner.run(defaultTestLoader.discover(test_dir, pattern='*_test.py', top_level_dir=None))
    fp.close()
