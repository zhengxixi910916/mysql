from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
计划、需求、问题、风险跟催
'''
apis = Api({
    "task_urge_mail_using_post": "/plan/$VERSION$/urge/mail",  # 计划跟催邮件发送
    "req_urge_mail_using_post": "/req/$VERSION$/urge/mail",  # 需求跟催邮件发送
    "issue_urge_mail_using_post": "/issue/$VERSION$/urge/mail",  # 问题跟催邮件发送
    "risk_urge_mail_using_post": "/risk/$VERSION$/urge/mail",  # 风险跟催邮件发送
})


def task_urge_mail_using_post(self, task_id, title, to_mails, copy_mails, description, checker=None):
    """
    接口名称：计划跟催邮件发送
    接口地址：/plan/$VERSION$/urge/mail
    """
    r = RequestService.call_post(apis.get("task_urge_mail_using_post", ), params={
        "copy_mails": copy_mails,
        "description": description,
        "id": task_id,
        "title": title,
        "to_mails": to_mails,
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def req_urge_mail_using_post(self, req_id, title, to_mails, copy_mails, description, checker=None):
    """
    接口名称：需求跟催邮件发送
    接口地址：/req/$VERSION$/urge/mail
    """
    r = RequestService.call_post(apis.get("req_urge_mail_using_post", ), params={
        "copy_mails": copy_mails,
        "description": description,
        "id": req_id,
        "title": title,
        "to_mails": to_mails,
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def issue_urge_mail_using_post(self, issue_id, title, to_mails, copy_mails, description, checker=None):
    """
    接口名称：问题跟催邮件发送
    接口地址：/issue/$VERSION$/urge/mail
    """
    r = RequestService.call_post(apis.get("issue_urge_mail_using_post", ), params={
        "copy_mails": copy_mails,
        "description": description,
        "id": issue_id,
        "title": title,
        "to_mails": to_mails,
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def risk_urge_mail_using_post(self, risk_id, title, to_mails, copy_mails, description, checker=None):
    """
    接口名称：风险跟催邮件发送
    接口地址：/risk/$VERSION$/urge/mail
    """
    r = RequestService.call_post(apis.get("risk_urge_mail_using_post", ), params={
        "copy_mails": copy_mails,
        "description": description,
        "id": risk_id,
        "title": title,
        "to_mails": to_mails,
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r
