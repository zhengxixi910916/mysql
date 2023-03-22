from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
项目日历
'''
apis = Api({
    "getCalendarByIdUsingGET": "/proj/$VERSION$/calendar/%s",  # 查询项目日历
    "updateCalendarUsingPUT": "/proj/$VERSION$/calendar/%s",  # 修改日历
    "addHolidayUsingPOST": "/proj/$VERSION$/holiday",  # 新增日历节假日
    "deleteHolidayUsingDELETE": "/proj/$VERSION$/holiday",  # 删除节假日
    "getHolidayByIdUsingGET": "/proj/$VERSION$/holiday/%s",  # 查询节假日详情
    "updateHolidayUsingPUT": "/proj/$VERSION$/holiday/%s",  # 修改节假日
})



def getCalendarByIdUsingGET(self, project_id, year, checker=None):
    """
    接口名称：查询项目日历
    接口地址：/proj/$VERSION$/calendar/{project_id}
    """
    r = RequestService.call_get(apis.get("getCalendarByIdUsingGET", project_id), params={
        "year": year  # 年份 - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def updateCalendarUsingPUT(self, project_id, calendar, checker=None):
    """
    接口名称：修改日历
    接口地址：/proj/$VERSION$/calendar/{project_id}
    """
    r = RequestService.call_put(apis.get("updateCalendarUsingPUT", project_id), json={
        "calendar": calendar  # 项目日历 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def addHolidayUsingPOST(self, calendarId, name, startTime, finishTime, year, dayType,
                        project_id, checker=None):
    """
    接口名称：新增日历节假日
    接口地址：/proj/$VERSION$/holiday
    """
    r = RequestService.call_post(apis.get("addHolidayUsingPOST", None), params={
        "calendarId": calendarId,
        "dayType": dayType,  # 日期类型（0：放假；1调休） - required: False
        "finishTime": finishTime,  # 结束时间 - required: False
        "name": name,  # 名称 - required: False
        "projectId": project_id,  # 项目id - required: False
        "startTime": startTime,  # 开始时间 - required: False
        "year": year,  # 年份 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def deleteHolidayUsingDELETE(self, arrayIds, checker=None):
    """
    接口名称：删除节假日
    接口地址：/proj/$VERSION$/holiday
    """
    r = RequestService.call_delete(apis.get("deleteHolidayUsingDELETE", None), json=arrayIds)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def getHolidayByIdUsingGET(self, projCalendar_id, year, checker=None):
    """
    接口名称：查询节假日详情
    接口地址：/proj/$VERSION$/holiday/{id}
    """
    r = RequestService.call_get(apis.get("getHolidayByIdUsingGET", projCalendar_id), params={
        "year": year
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def updateHolidayUsingPUT(self, id, cHoliday, checker=None):
    """
    接口名称：修改节假日
    接口地址：/proj/$VERSION$/holiday/{id}
    """
    r = RequestService.call_put(apis.get("updateHolidayUsingPUT", id), json=cHoliday)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r
