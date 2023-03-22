# -*- coding: utf-8 -*-
# @Time    : 2022/2/23
# @Author  : yangjiong
import time
import unittest

from project.api import ApiKanBan, ApiRequireManage, ApiTaskManage
from project.case.file.runSql import db


class KanBan(unittest.TestCase):
    project_id = db.project_id
    project_stage_id = ''
    member_id = ''
    stages_id = ''
    card_id = ''
    card_id2 = ''
    card_name = ''
    board_name = ''
    boardId = 'SYS_E39B20EA11E7A81AC85B767C89C1'
    new_card_list = []
    sort_card_dict = {}
    new_stages_id = []
    stage_name_list = []
    sort_stage_dict = {}
    task_id = ""

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     db.delete_sql()

    def test_0060_kanbanTargetTypeUsingGET(self):
        """
        接口名称：看板类型字典
        接口地址：/proj/$VERSION$/kanban/target/type
        """
        ApiKanBan.kanbanTargetTypeUsingGET(self)

    def test_0070_createStageUsingPOST(self):
        """
        接口名称：创建新的阶段
        接口地址：/proj/$VERSION$/kanban/stage/{boardId}
        """
        # # 创建阶段任务
        # r = ApiTaskManage.add_task(self, project_id=KanBan.project_id)
        # KanBan.task_id = r["id"]
        #

        for i in range(1, 3):
            KanBan.board_name = f"自动化创建阶段{i}" + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
            ApiKanBan.createStageUsingPOST(self,
                                           board_name=KanBan.board_name,
                                           boardId=KanBan.boardId
                                           )

    def test_0080_getUserBoardUsingGET(self):
        """
        接口名称：获取当前用户个人看板
        接口地址：/proj/$VERSION$/kanban/user/board
        """
        r = ApiKanBan.getUserBoardUsingGET(self)
        KanBan.stages_id = r['res']['data']['stages'][1]['id']
        stage_list = r['res']['data']['stages']
        for i in range(len(stage_list)):
            if "自动化" in stage_list[i]['name']:
                KanBan.new_stages_id.append(stage_list[i]['id'])
            KanBan.sort_stage_dict[stage_list[i]['id']] = stage_list[i]['orderNum']

    def test_0090_updateStageUsingPUT(self):
        """
        接口名称：编辑阶段
        接口地址：/proj/$VERSION$/kanban/stage/{stageId}
        """
        ApiKanBan.updateStageUsingPUT(self,
                                      stageId=KanBan.new_stages_id[0],
                                      new_name='编辑阶段'
                                      )

    def test_0100_sortStageUsingPUT(self):
        """
        接口名称：排序阶段
        接口地址：/proj/$VERSION$/kanban/stage/sort/{boardId}
        """
        ApiKanBan.sortStageUsingPUT(self,
                                    boardId=KanBan.boardId,
                                    data=KanBan.sort_stage_dict,
                                    )

    def test_0200_createCardUsingPOST(self):
        """
        接口名称：新增自定义卡片
        接口地址：/proj/$VERSION$/kanban/card/{stageId}
        """
        for i in range(1, 3):
            card_name = f'自动化创建卡片{i}' + time.strftime('%Y%m%d %H%M%S', time.localtime(time.time()))
            ApiKanBan.createCardUsingPOST(self,
                                          card_name=card_name,
                                          stageId=KanBan.stages_id
                                          )

    def test_0300_getUserBoardStageTypeUsingGET(self):
        """
        接口名称：获取用户看板的阶段数据-业务类型
        接口地址：/proj/$VERSION$/kanban/user/stage/{stageId}/{complete}/{pageNo}/{page_size}/{targetType}
        """
        data_ = {
            'stageId': KanBan.stages_id,
            'complete': 0,
            'pageNo': 1,
            'page_size': 20,
            'targetType': 5
        }
        r = ApiKanBan.getUserBoardStageTypeUsingGET(self,
                                                    data=data_
                                                    )
        KanBan.card_id = r['res']['data']['cardsPage']['records'][0]['id']
        card_list = r['res']['data']['cardsPage']['records']
        # 获取卡片id和数字用于排序
        KanBan.sort_card_dict[card_list[1]['id']] = card_list[1]['orderNum'] / 2
        for i in range(len(card_list)):
            if "自动化" in card_list[i]['data']['name']:
                KanBan.new_card_list.append(card_list[i]['id'])

    def test_0310_getUserBoardCardUsingGET(self):
        """
        接口名称：获取用户卡片数据
        接口地址：/proj/$VERSION$/kanban/user/card/{cardId}
        """
        ApiKanBan.getUserBoardCardUsingGET(self,
                                           cardId=KanBan.new_card_list[1]
                                           )

    def test_0400_updateCardUsingPUT(self):
        """
        接口名称：更新自定义卡片
        接口地址：/proj/$VERSION$/kanban/card/{cardId}
        """
        card_name = "自动化测试更新卡片" + time.strftime('%Y%m%d %H%M%S', time.localtime(time.time()))
        KanBan.card_name = card_name
        ApiKanBan.updateCardUsingPUT(self,
                                     card_name=card_name,
                                     cardId=KanBan.card_id
                                     )

    def test_0410_sortCardUsingPUT(self):
        """
        接口名称：排序卡片
        接口地址：/proj/$VERSION$/kanban/card/sort/{stageId}/{cardId}
        """
        card_id = list(KanBan.sort_card_dict.keys())
        ApiKanBan.sortCardUsingPUT(self,
                                   stageId=KanBan.stages_id,
                                   cardId=card_id[0],
                                   data=KanBan.sort_card_dict
                                   )

    def test_0500_updateCardCompleteUsingPUT(self):
        """
        接口名称：完成自定义卡片
        接口地址：/proj/$VERSION$/kanban/card/{cardId}/{complete}
        """
        ApiKanBan.updateCardCompleteUsingPUT(self,
                                             card_id=KanBan.card_id,
                                             cardname=KanBan.card_name
                                             )

    def test_0600_deleteCardUsingDELETE(self):
        """
        接口名称：删除自定义卡片
        接口地址：/proj/$VERSION$/kanban/card/{cardId}
        """
        for card_id in KanBan.new_card_list:
            ApiKanBan.deleteCardUsingDELETE(self,
                                            card_id=card_id
                                            )

    def test_0700_deleteStageUsingDELETE(self):
        """
        接口名称：删除阶段
        接口地址：/proj/$VERSION$/kanban/stage/{stageId}
        """
        for new_stages_id in KanBan.new_stages_id:
            ApiKanBan.deleteStageUsingDELETE(self,
                                             stageId=new_stages_id
                                             )

    def test_0800_getProjectBoardUsingGET(self):
        """
        接口名称：获取项目看板
        接口地址：/proj/$VERSION$/kanban/project/board/{project_id}/{targetType}
        """
        r = ApiKanBan.getProjectBoardUsingGET(self,
                                              project_id=KanBan.project_id,
                                              targetType=1
                                              )
        KanBan.project_stage_id = r['res']['data'][6]['id']
        print(r['res']['data'][6]['id'])

    def test_0900_getProjectBoardStageUsingGET(self):
        """
        接口名称：获取项目看板的阶段数据
        接口地址：/proj/$VERSION$/kanban/project/stage/{project_id}/{targetType}/{stageId}/{complete}/{pageNo}/{page_size}
        """
        ApiRequireManage.add_require(self,
                                     name="require_" + time.strftime('%H%M%S', time.localtime()),
                                     project_id=KanBan.project_id
                                     )

        data_ = {
            'project_id': KanBan.project_id,
            'targetType': 1,
            'stageId': KanBan.project_stage_id,
            'complete': 0,
            'pageNo': 1,
            'page_size': 20
        }
        r = ApiKanBan.getProjectBoardStageUsingGET(self,
                                                   data=data_
                                                   )
        print(r)
        KanBan.card_id2 = r["res"]["data"]["id"]


    @unittest.skip('该接口未被调用')
    def test_0901_getProjectBoardCardUsingGET(self):
        """
        接口名称：获取项目卡片数据
        接口地址：/proj/$VERSION$/kanban/project/card/{cardId}/{targetType}
        """
        ApiKanBan.getProjectBoardCardUsingGET(self,
                                              cardId=KanBan.card_id2,
                                              targetType=1
                                              )

    def test_1000_getMemberBoardUsingGET(self):
        """
        接口名称：获取项目成员看板
        接口地址：/proj/$VERSION$/kanban/member/board/{project_id}/{targetType}/{complete}
        """
        data_ = {
            'project_id': KanBan.project_id,
            'targetType': 1,
            'complete': -1
        }
        r = ApiKanBan.getMemberBoardUsingGET(self,
                                             data=data_
                                             )
        KanBan.member_id = r['res']['data']['stages'][0]['id']

    def test_1100_getMemberBoardStageUsingGET(self):
        """
        接口名称：获取项目成员看板阶段数据
        接口地址：/proj/$VERSION$/kanban/member/board/stage/{project_id}/{targetType}/{memberId}/{complete}/{pageNo}/{page_size}
        """
        data_ = {
            'project_id': KanBan.project_id,
            'targetType': 1,
            'memberId': KanBan.member_id,
            'complete': -1,
            'pageNo': 1,
            'page_size': 20
        }
        ApiKanBan.getMemberBoardStageUsingGET(self,
                                              data=data_
                                              )

    def test_1200_taskStageBoardUsingGET(self):
        """
        接口名称：任务阶段看板
        接口地址：/proj/$VERSION$/kanban/taskStage
        """
        ApiKanBan.taskStageBoardUsingGET(self,
                                         project_id=KanBan.project_id)


if __name__ == '__main__':
    unittest.main()
