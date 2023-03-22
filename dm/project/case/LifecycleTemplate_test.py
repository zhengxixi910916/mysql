# -*- coding: utf-8 -*-#
# Author: YANGJIONG
# Date:   2022/7/5
import unittest
from project.api import ApiLifecycleTemplate, ApiObjectLifeCycleStatus


class LifecycleTemplate(unittest.TestCase):
    life_template_id = ''
    to_be_released_id = ''
    life_state_id = ''

    def test_0100_find_el_lifecycle_template_using_get(self):
        """
        接口名称：生命周期模板列表
        接口地址：/proj/$VERSION$/lifecycle/template
        """
        r = ApiLifecycleTemplate.find_el_lifecycle_template_using_get(self)
        for i in range(len(r)):
            if r[i]['templateName'] == '风险生命周期':
                LifecycleTemplate.life_template_id = r[i]['id']
                break

    def test_0200_select_et_life_cycle_state_using_get(self):
        """
        接口名称：生命周期状态查询条件信息
        接口地址：/proj/$VERSION$/lifecycle/state
        """
        r = ApiObjectLifeCycleStatus.select_et_life_cycle_state_using_get(self,
                                                                          life_template_id=LifecycleTemplate.life_template_id)
        LifecycleTemplate.life_state_id = r[0]['id']

    def test_0300_inset_et_life_cycle_state_using_put(self):
        """
        接口名称：新增或修改生命周期状态
        接口地址：/proj/$VERSION$/lifecycle/state
        """
        ApiObjectLifeCycleStatus.inset_et_life_cycle_state_using_put(self,
                                                                     life_template_id=LifecycleTemplate.life_template_id,
                                                                     life_state_id=LifecycleTemplate.life_state_id
                                                                     )

    def test_0400_get_temp_versions_by_id_using_get(self):
        """
        接口名称：根据模板ID获取对应所有已发布版本
        接口地址：/proj/$VERSION$/lifecycle/template/{id}/release/versions
        """
        version_for_id = ApiLifecycleTemplate.get_temp_all_versions_by_id_using_get(self,
                                                                                    LifecycleTemplate.life_template_id)
        # 获取待发布的id
        for i in range(len(version_for_id)):
            if version_for_id[i]['active'] == 0:
                LifecycleTemplate.to_be_released_id = version_for_id[i]['id']
                break

    def test_0500_release_el_lifecycle_template_using_post(self):
        """
        接口名称：发布生命周期模板
        接口地址：/proj/$VERSION$/lifecycle/template/release
        """
        ApiLifecycleTemplate.release_el_lifecycle_template_using_post(self,
                                                                      to_be_released_id=LifecycleTemplate.to_be_released_id
                                                                      )

    def test_0600_get_temp_all_state_by_id_using_get(self):
        """
        接口名称：根据模板ID获取对应所有版本的状态并去重
        接口地址：/proj/$VERSION$/lifecycle/template/{id}/state
        """
        ApiLifecycleTemplate.get_temp_all_state_by_id_using_get(self,
                                                                life_template_id=LifecycleTemplate.life_template_id)


if __name__ == '__main__':
    unittest.main()
