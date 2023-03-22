from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
周报管理Api
'''
apis = Api({
    "addWeeklyUsingPOST": "/rpt/$VERSION$/api/weekly",  # 添加周报数据
    "editWeeklyTaskUsingPUT": "/rpt/$VERSION$/api/weekly/task/edit",  # 天马-根据周报ID修改周报数据，修改周报任务记录
})


def addWeeklyUsingPOST(self, year, weekOfYear, startTime, finishTime, title, remark, reporterId, submitId, takeoverIds,
                       copyToIds, stateKey,

                       workDate0="1643587200000", startTime0="1643589000000", endTime0="1643623200000", type0="0",
                       freeWorkTime0="1.5", workTime0="8", project_id0="b7111200906511ec898e484d7ec83ee6",
                       projectName0="project_2022-02-18 10-51-47", isTravel0="0", remarks0=None, sort0="0",

                       workDate1="1643587200000", startTime1="1643589000000", endTime1="1643623200000", type1="0",
                       freeWorkTime1="1.5", workTime1="8", project_id1="b7111200906511ec898e484d7ec83ee6",
                       projectName1="project_2022-02-18 10-51-47", isTravel1="0", remarks1=None, sort1="0",

                       workDate2="1643587200000", startTime2="1643589000000", endTime2="1643623200000", type2="0",
                       freeWorkTime2="1.5", workTime2="8", project_id2="b7111200906511ec898e484d7ec83ee6",
                       projectName2="project_2022-02-18 10-51-47", isTravel2="0", remarks2=None, sort2="0",

                       workDate3="1643587200000", startTime3="1643589000000", endTime3="1643623200000", type3="0",
                       freeWorkTime3="1.5", workTime3="8", project_id3="b7111200906511ec898e484d7ec83ee6",
                       projectName3="project_2022-02-18 10-51-47", isTravel3="0", remarks3=None, sort3="0",

                       workDate4="1643587200000", startTime4="1643589000000", endTime4="1643623200000", type4="0",
                       freeWorkTime4="1.5", workTime4="8", project_id4="b7111200906511ec898e484d7ec83ee6",
                       projectName4="project_2022-02-18 10-51-47", isTravel4="0", remarks4=None, sort4="0",
                       checker=None):
    """
    接口名称：添加周报数据
    接口地址：/rpt/$VERSION$/api/weekly
    """
    r = RequestService.call_post(apis.get("addWeeklyUsingPOST", ), json={
        "year": year,
        "weekOfYear": weekOfYear,
        "startTime": startTime,
        "finishTime": finishTime,
        "title": title,
        "remark": remark,
        "reporterId": reporterId,
        "submitId": submitId,
        "takeoverIds": takeoverIds,
        "copyToIds": copyToIds,
        "stateKey": stateKey,
        "weeklyTimesheet[0].workDate": workDate0,
        "weeklyTimesheet[0].startTime": startTime0,
        "weeklyTimesheet[0].endTime": endTime0,
        "weeklyTimesheet[0].type": type0,
        "weeklyTimesheet[0].freeWorkTime": freeWorkTime0,
        "weeklyTimesheet[0].workTime": workTime0,
        "weeklyTimesheet[0].project_id": project_id0,
        "weeklyTimesheet[0].projectName": projectName0,
        "weeklyTimesheet[0].isTravel": isTravel0,
        "weeklyTimesheet[0].remarks": remarks0,
        "weeklyTimesheet[0].sort": sort0,
        "weeklyTimesheet[1].workDate": workDate1,
        "weeklyTimesheet[1].startTime": startTime1,
        "weeklyTimesheet[1].endTime": endTime1,
        "weeklyTimesheet[1].type": type1,
        "weeklyTimesheet[1].freeWorkTime": freeWorkTime1,
        "weeklyTimesheet[1].workTime": workTime1,
        "weeklyTimesheet[1].project_id": project_id1,
        "weeklyTimesheet[1].projectName": projectName1,
        "weeklyTimesheet[1].isTravel": isTravel1,
        "weeklyTimesheet[1].remarks": remarks1,
        "weeklyTimesheet[1].sort": sort1,
        "weeklyTimesheet[2].workDate": workDate2,
        "weeklyTimesheet[2].startTime": startTime2,
        "weeklyTimesheet[2].endTime": endTime2,
        "weeklyTimesheet[2].type": type2,
        "weeklyTimesheet[2].freeWorkTime": freeWorkTime2,
        "weeklyTimesheet[2].workTime": workTime2,
        "weeklyTimesheet[2].project_id": project_id2,
        "weeklyTimesheet[2].projectName": projectName2,
        "weeklyTimesheet[2].isTravel": isTravel2,
        "weeklyTimesheet[2].remarks": remarks2,
        "weeklyTimesheet[2].sort": sort2,
        "weeklyTimesheet[3].workDate": workDate3,
        "weeklyTimesheet[3].startTime": startTime3,
        "weeklyTimesheet[3].endTime": endTime3,
        "weeklyTimesheet[3].type": type3,
        "weeklyTimesheet[3].freeWorkTime": freeWorkTime3,
        "weeklyTimesheet[3].workTime": workTime3,
        "weeklyTimesheet[3].project_id": project_id3,
        "weeklyTimesheet[3].projectName": projectName3,
        "weeklyTimesheet[3].isTravel": isTravel3,
        "weeklyTimesheet[3].remarks": remarks3,
        "weeklyTimesheet[3].sort": sort3,
        "weeklyTimesheet[4].workDate": workDate4,
        "weeklyTimesheet[4].startTime": startTime4,
        "weeklyTimesheet[4].endTime": endTime4,
        "weeklyTimesheet[4].type": type4,
        "weeklyTimesheet[4].freeWorkTime": freeWorkTime4,
        "weeklyTimesheet[4].workTime": workTime4,
        "weeklyTimesheet[4].project_id": project_id4,
        "weeklyTimesheet[4].projectName": projectName4,
        "weeklyTimesheet[4].isTravel": isTravel4,
        "weeklyTimesheet[4].remarks": remarks4,
        "weeklyTimesheet[4].sort": sort4,
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def editWeeklyTaskUsingPUT(self, checker):
    """
    接口名称：天马-根据周报ID修改周报数据，修改周报任务记录
    接口地址：/rpt/$VERSION$/api/weekly/task/edit
    """
    r = RequestService.call_put(apis.get("editWeeklyTaskUsingPUT", None), json={
        "dto": ""  # dto - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]
