import os 

import requests

from utils.cmd import run_command
from utils.json_loader import get_json_data


class ReplicationThread:

    HOST = 'http://ctl-dev.dev.df.sbrf.ru:8080/'
    RUN = HOST + 'v1/api/wf/sched/name/{}'
    STATS = HOST + 'v1/api/loading/filtered-compact?wfNamesLike=%5B%22{}%22%5D'
    PARAMFILE_PATH = HOST + 'v1/api/wf/name/{}'

    def __init__(self, name: str):
        self.name = name

    def _parse_paramfile_dict(self, params):
        # TODO Filter
        for param in params:
            paramfile_path = param['prior_value']
            if paramfile_path.endswith('.json'):
                return paramfile_path
        
    def _get_paramfile_path(self):
        response = requests.get(self.PARAMFILE_PATH.format(self.name))
        thread_params_json = response.json()
        params = thread_params_json[0].get('param')
        return self._parse_paramfile_dict(params)
            
    def get_tables_name(self, paramfile_path: str):
        hdfs_copy_to_local = run_command('hdfs dfs -copyToLocal ' + paramfile_path)

        tmp_dict = {}
        if hdfs_copy_to_local['returncode'] == 0:
            tmp_dict = get_json_data(os.path.basename(paramfile_path))

        tables = [item['bd_table_name'] for item in tmp_dict['table_list']]
        return tables

    def get_stats(self):
        response = requests.get(self.STATS.format(self.name))
        return response.json()

    def run(self) -> dict:
        response = requests.post(
            self.RUN.format(self.name),
            headers={'Content-Type': 'application/json'},
            data='{}'
        )
        loading_id = response.text.split(',')[-1].replace("]'", '')
        return {
            'status_code': response.status_code,
            'loading_id': loading_id[1:-1]
        }


