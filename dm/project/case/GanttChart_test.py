import unittest
from project.api import ApiGanttChart
from project.case.file.runSql import db


class GanttChart(unittest.TestCase):
    """甘特图"""

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass


    def test_0100_updateTasksUsingPOST(self):
        """
        接口名称：更新甘特图数据
        接口地址：/plan/$VERSION$/gantt/tasks
        """
        ApiGanttChart.updateTasksUsingPOST(self,
                                           taskJson="taskJson=%7B%22StartDate%22%3A%222022-02-22%22%2C%22UID%22%3A%225bdcc29893b011ecac3f484d7ec83ee6%22%2C%22Tasks%22%3A%5B%7B%22UID%22%3A%222A89A38E-B90F-4649-88AA-4737E486690D%22%2C%22Name%22%3A%22%E6%B5%8B%E8%AF%95%22%2C%22PercentComplete%22%3A0%2C%22Work%22%3A0%2C%22Weight%22%3A0%2C%22ConstraintType%22%3A0%2C%22Start%22%3A%222022-02-22%22%2C%22Finish%22%3A%222022-02-22%22%2C%22Duration%22%3A1%2C%22ProjectUID%22%3A%225bdcc29893b011ecac3f484d7ec83ee6%22%2C%22_pid%22%3A-1%2C%22_id%22%3A1%2C%22_uid%22%3A1%2C%22ParentTaskUID%22%3A-1%2C%22_level%22%3A0%2C%22ID%22%3A1%2C%22OutlineLevel%22%3A1%2C%22OutlineNumber%22%3A%221%22%2C%22Summary%22%3A0%2C%22PredecessorLink%22%3A%5B%5D%2C%22Critical%22%3A0%2C%22ActualStart%22%3Anull%2C%22ActualFinish%22%3Anull%2C%22FixedDate%22%3A0%2C%22Conflict%22%3A0%2C%22isBaseline%22%3Afalse%2C%22_state%22%3A%22modified%22%2C%22Principal%22%3A%22SYS_E39B20EA11E7A81AC85B767C89C1%22%2C%22Assignments%22%3A%22PM%22%2C%22ConstraintDate%22%3Anull%7D%5D%2C%22Principals%22%3A%5B%7B%22UID%22%3A%22SYS_E39B20EA11E7A81AC85B767C89C1%22%2C%22Name%22%3A%22%E7%AE%A1%E7%90%86%E5%91%98%22%7D%5D%2C%22TaskCount%22%3A0%2C%22Resources%22%3A%22%22%2C%22FinishDate%22%3A%222023-02-22%22%2C%22Name%22%3A%22project_2022-02-22+15-23-40%22%2C%22roles%22%3A%5B%7B%22flexAttrs%22%3A%7B%7D%2C%22code%22%3A%22PM%22%2C%22displayEn%22%3A%22%E9%A1%B9%E7%9B%AE%E7%BB%8F%E7%90%86%22%2C%22updateTime%22%3A%222018-01-31+15%3A51%3A10%22%2C%22sort%22%3A1%2C%22delFlag%22%3A%220%22%2C%22displayCn%22%3A%22%E9%A1%B9%E7%9B%AE%E7%BB%8F%E7%90%86%22%2C%22type%22%3A%22PROJECT%22%2C%22parentId%22%3A%22-1%22%2C%22isDefault%22%3A%220%22%2C%22children%22%3A%5B%5D%2C%22createTime%22%3A%222017-09-26+18%3A57%3A00%22%2C%22projectRole%22%3A%7B%22id%22%3A%222bbc5d00df8db3a977b954d370279ac2%22%2C%22objectClassName%22%3A%22erd.cloud.project.dto.EtProject%22%2C%22objectId%22%3A%225bdcc29893b011ecac3f484d7ec83ee6%22%2C%22roleKey%22%3A%22PM%22%2C%22userId%22%3A%22SYS_E39B20EA11E7A81AC85B767C89C1%22%2C%22active%22%3A%220%22%2C%22joinTime%22%3A%222022-02-22+15%3A24%3A27%22%2C%22isKeyMember%22%3A%220%22%7D%2C%22name%22%3A%22%E9%A1%B9%E7%9B%AE%E7%BB%8F%E7%90%86%22%2C%22id%22%3A%2262b85f8a2a004dd1bdf37aa5d204be25%22%7D%5D%2C%22elCalendar%22%3A%7B%22computeType%22%3A%220%22%2C%22isIncludeException%22%3A%220%22%2C%22weeks%22%3A6%2C%22repeatMode%22%3A%221%22%2C%22sysCalendarId%22%3A%226c85d725126419d13f9543bbfb4043d7%22%2C%22lastMonth%22%3A1%2C%22updateTime%22%3A%222022-02-22+16%3A27%3A04%22%2C%22delFlag%22%3A%220%22%2C%22listProjectHoliday%22%3A%5B%7B%22dayType%22%3A%220%22%2C%22finishTime%22%3A%222022-02-02+00%3A00%3A00%22%2C%22year%22%3A2022%2C%22name%22%3A%22%E6%B5%8B%E8%AF%951231231%22%2C%22startTime%22%3A%222022-02-01+00%3A00%3A00%22%2C%22id%22%3A%22a682378b856dd8d2c1a22c38d1d67e66%22%2C%22project_id%22%3A%225bdcc29893b011ecac3f484d7ec83ee6%22%7D%2C%7B%22dayType%22%3A%220%22%2C%22finishTime%22%3A%222022-03-02+00%3A00%3A00%22%2C%22year%22%3A2022%2C%22name%22%3A%22%E6%B5%8B%E8%AF%95112312312312312312312%22%2C%22startTime%22%3A%222022-03-01+00%3A00%3A00%22%2C%22id%22%3A%22a8327a120ae2427ef7fc082d85fcf12f%22%2C%22project_id%22%3A%225bdcc29893b011ecac3f484d7ec83ee6%22%7D%2C%7B%22dayType%22%3A%221%22%2C%22finishTime%22%3A%222022-04-06+00%3A00%3A00%22%2C%22year%22%3A2022%2C%22name%22%3A%22%E6%B5%8B%E8%AF%9513123111%22%2C%22startTime%22%3A%222022-04-05+00%3A00%3A00%22%2C%22id%22%3A%226ec7bd1cacaf42226789466d0a6ccadc%22%2C%22project_id%22%3A%225bdcc29893b011ecac3f484d7ec83ee6%22%7D%2C%7B%22dayType%22%3A%220%22%2C%22finishTime%22%3A%222022-04-13+00%3A00%3A00%22%2C%22year%22%3A2022%2C%22name%22%3A%22%E6%B5%8B%E8%AF%952%22%2C%22startTime%22%3A%222022-04-12+00%3A00%3A00%22%2C%22id%22%3A%2297d26894f1d7aab85d66828d59e654e7%22%2C%22project_id%22%3A%225bdcc29893b011ecac3f484d7ec83ee6%22%7D%5D%2C%22cycle%22%3A%221%2C2%2C3%2C4%22%2C%22repetitions%22%3A1%2C%22fewWeeks%22%3A-1%2C%22listHoliday%22%3A%5B%5D%2C%22createTime%22%3A%222022-02-22+15%3A24%3A45%22%2C%22updateBy%22%3A%22SYS_E39B20EA11E7A81AC85B767C89C1%22%2C%22startTime%22%3A%222022-02-22%22%2C%22id%22%3A%22c2ccaa5b6303257e00fe873e2aa9f2f2%22%2C%22project_id%22%3A%225bdcc29893b011ecac3f484d7ec83ee6%22%2C%22stDate%22%3A%222022-02-22T08%3A00%3A00%22%2C%22fsDate%22%3A%222022-03-03T00%3A00%3A00%22%2C%22finishTime%22%3A%222022-03-03%22%7D%2C%22CalendarUID%22%3A%221%22%2C%22Calendars%22%3A%5B%7B%22UID%22%3A1%2C%22IsBaseCalendar%22%3A1%2C%22BaseCalendarUID%22%3A-1%2C%22Name%22%3A%22%22%2C%22WeekDays%22%3A%5B%7B%22DayType%22%3A1%2C%22DayWorking%22%3A0%7D%2C%7B%22DayType%22%3A2%2C%22DayWorking%22%3A1%7D%2C%7B%22DayType%22%3A3%2C%22DayWorking%22%3A1%7D%2C%7B%22DayType%22%3A4%2C%22DayWorking%22%3A1%7D%2C%7B%22DayType%22%3A5%2C%22DayWorking%22%3A1%7D%2C%7B%22DayType%22%3A6%2C%22DayWorking%22%3A1%7D%2C%7B%22DayType%22%3A7%2C%22DayWorking%22%3A0%7D%5D%2C%22Exceptions%22%3A%5B%5D%7D%5D%2C%22RemovedTasks%22%3A%5B%5D%7D",
                                           )

    def test_0200_getTaskListUsingGET_1(self):
        """
        接口名称：根据项目获取任务，用户甘特图显示
        接口地址：/plan/$VERSION$/gantt/tasks/tree
        """
        r = ApiGanttChart.getTaskListUsingGET_1(self,
                                                project_id=db.project_id
                                                )
        print(r)


if __name__ == '__main__':
    unittest.main()
