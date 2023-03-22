from erdcloud.CommonServerTest import CommonServer
import requests


class Ppm(CommonServer):
    """
    主要用来删除PPM里面多余的数据
    """

    def __init__(self):
        super().__init__()
        self.header = self.get_headers()

    def get_project_id_list(self):
        url = self.host + '/proj/v1/projects'
        print(url, '\n', self.header)
        r = requests.get(url=url,
                         headers=self.header,
                         params={
                             "page_size": 10000,
                             "pageindex": 1,
                             "contextType": 0
                         }).json()
        project_id_list = []
        project_data = r['res']['data']['records']
        for i in range(len(project_data)):
            # if 'TR' in project_data[i]['name'] or 'DCP' in project_data[i]['name']:
            if 'project' in project_data[i]['name']:
                project_id_list.append(project_data[i]['id'])

        return project_id_list

    def delete_project(self, project_id):
        url = self.host + f'/proj/v1/{project_id}'
        print(url, '\n', self.header)
        r = requests.delete(url=url,
                            headers=self.header,
                            )
        print(r.text)


if __name__ == '__main__':
    p = Ppm()
    # var = Ppm.__doc__
    # print(var)
    id_list = p.get_project_id_list()
    for id_ in id_list:
        p.delete_project(id_)
