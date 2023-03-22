## erdcloud自动化测试基础工具包使用方法

### 功能
* mysql数据库
* Nacos
* http请求客户端
* Api统计
* Api封装


### 环境变量

| 名称 | 键 | 值 |
| --- | --- | --- |
| nacos地址 | env.nacos.server.ip | 127.0.0.1 |
| nacos端口 | env.nacos.server.port | 8848 |
| namespace | env.nacos.server.config.namespace | ceb2fa99-0989-47f9-80c8-ec6375d806c4 |
| api版本映射文件路径 | erd.test.path.apimapping | 空 | 
| 环境配置信息文件路径 | erd.test.path.env.config | 空 | 
| 数据库配置文件存贮方式 | erd.test.path.db.config | 空 | 

#### 使用本地配置信息：
```
erd.test.path.apimapping=local:D:\config\api_mapping.json
erd.test.path.db.config=local:D:\config\db.ini
erd.test.path.env.config=local:D:\config\env.ini
```

#### 使用nacos配置信息
```
env.nacos.server.ip=192.168.0.243
env.nacos.server.port=8848
env.nacos.server.config.namespace=da3f1f30-c146-41ec-af29-fe9249af6943
env.nacos.server.config.group=eCloud

erd.test.path.apimapping=nacos:erdcloud-test-apimapping.json
erd.test.path.db.config=nacos:erdcloud-test-db.ini
erd.test.path.env.config=nacos:erdcloud-test-env.ini
```
!> 只要有一个节点使用nacos配置信息，就需要配置nacos链接信息。

使用时，将相应配置信息粘贴到pyCharm运行的环境变量中。

### erd.test.path.apimapping
对应文件配置内容：
```json
{
  "/sys/": "v1"
}
```

### erd.test.path.env.config
对应文件配置内容：

```ini
[envConf]
host = http://127.0.0.1
env = develop
context =
user = admin
password = {erdp}MTIzNDU2
Authorization = Basic ZXJkcDpOaVhpbkU3WVRyZDluaDUvUkgxOFBMN3FYMkd6bndvalhmK0preWpNQ0ZUaWVVWFhHZXhtUnplQmdmbHYwdFcrSFpIQjFoZ2dkenpBaFlTK0VUdFFIUjlOSzRnWlBDaGwzUUFmWlZIRm9NVkpzTXdiNWh4c0FlZFJISnN0WGhSSFM3SlIwNXEvZFpMalpWcHFpcXJLWDk0Y2JzbFpDckt5WUx2NHRoY0hxd0k9
```

### erd.test.path.db.config

数据库配置在部分库的情况下，只有default节点就可以。

如果分库的情况下，根据数据库配置要和数据库操作的`section`保持一致。

对应文件配置内容：
```ini
[default]
host = 127.0.0.1
port = 3306
user = erdcloud
password = Pw!123456
db_name = erddb_dev

[system]
host = db地址
port = db端口
user = 用户名
password = 密码
db_name = system服务库名

[message]
host = db地址
port = db端口
user = 用户名
password = 密码
db_name = message服务库名
 .
 .
 .
;各个服务规范定义：[system]/[message]/[mq]/[doc]/[wiki]...
```

### 使用方法

#### 私库账号信息

开发账号：erdp-python-developer/elead@2018

#### 项目
项目中使用：
```shell
# 安装依赖
pip install ErdPkg -U -i http://erdp-python-admin:nexus2018@nexus.ddns.e-lead.cn/repository/elead-pypi/simple/ --trusted-host nexus.ddns.e-lead.cn

# 安装所有其他必须的依赖：
pip install -r requirements.txt

```

项目中如果安装了其他依赖，需要更新依赖清单：
```shell
pip freeze > requirements.txt
```

## 测试接口生成

### 根据postman导出的脚本生成api接口

#### 使用方法

* 在postman中选择要导出的测试脚本，导出到文件`postman.json`。
* 创建python文件`gen.py`，内容如下示例。
    * 第一个参数为导出的源文件`postman.json`的位置。
* 执行`gen.py`。
* 执行完成后会生成`Api_{data}.py`，内部为所有的接口定义。

> 生成的接口需要格式化，修改处理，将接口中写死的变量用正确的传参等形式进行重构。
> 使用处理后的api编写测试场景进行测试。

```python
from erdcloud.gen import gen_postman

if __name__ == '__main__':
    # 针对postman使用
    gen_postman('D:\generator\postman.json')
```
> 可以要求开发人员提供postman的测试脚本
> 测试脚本，生成对应api接口

### 根据swagger文档导出的脚本生成api接口

#### 使用方法

* 从swagger中导出接口定义。通常文档接口地址如：`/sys/v2/api-docs`
* 将接口的文档内容保存到`swagger.json`文件中。
* 创建python文件`gen.py`，内容如下示例。
    * 第一个参数为导出的源文件`postman.json`的位置。
    * 第二个参数：要生成的tag，如果是不填，默认全部接口。如果填某些tag就只生成某些tag的接口。
* 执行`gen.py`。
* 执行完成后会生成`Api_{data}.py`，内部为所有的接口定义。
* 生成的接口需要格式化，修改处理，将接口中写死的变量用正确的传参等形式进行重构。
* 使用处理后的api编写测试场景进行测试。

```python
from erdcloud.gen import gen_swagger

if __name__ == '__main__':
    # 针对swagger使用
    gen_swagger('D:\generator\swagger.json', ['tag1', 'tag2'])
```
