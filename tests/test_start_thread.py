import time
import random
from multiprocessing.dummy import Pool

from repl_thread.run import ReplicationThread
from utils.db import postgres_cursor


class ThreadRunManager:

    ORCHESTRATOR_RUNNING_STATES = ('RUNNING', 'START')

    def __init__(self, thread: dict):
        self.thread = ReplicationThread(thread['name'])
        self.run_with_insert = self.thread['insert_row_in_table']

    def ctl_state(self, loading_id: int):
        return self.thread.get_thread_state('ctlState', loading_id)
    
    def orchestrator_state(self, loading_id: int):
        return self.thread.get_thread_state('orchestratorState', loading_id)
        
    def run_thread(self):
        thread_loading_id = self.thread.run()

        while self.ctl_state(thread_loading_id) == 'ACTIVE':
            if self.orchestrator_state(thread_loading_id) in self.ORCHESTRATOR_RUNNING_STATES:
                print(self.thread.name, ' активен')
                time.sleep(random.randint(10, 20))
        
        thread_state = self.ctl_state(thread_loading_id)
        log_string = '{name} закончил работу с состоянием {state}'.format(
            name=self.thread.name, state=thread_state
        )
        print(log_string)


    def run_thread_with_insert(self):
        pass

    def run_thread_without_insert(self):
        pass


def run_thread(thread: dict):
    thr = ReplicationThread(thread['name'])
    postgres_cursor = postgres_cursor()
    
    if thread['insert_row_in_table']:
        paramfile_path = thr._get_paramfile_path()
        tables_name = thr.get_tables_name(paramfile_path)
        # postgres_cursor.execute(....format(table_name=tables_name[0]))

    result = thr.run()
    return result


def test_run_thread_new(config, postgres_cursor):
    workers = config['workers']
    thread_list = config['list']
    if workers == 1:
        for thread_name in thread_list:
            run_thread(thread_name)
    else:
        pool = Pool(workers)
        result = pool.map(run_thread, thread_list)
        
        print(result)






# def test_run_thread(multistart_repl_thr, singlestart_repl_thr):
#     """
#         Получаем из фикстуры список с именами потоков 
#         Запускаем многопточно все потоки в цикле
#     """

#     if multistart_repl_thr:
#         print('Запускается многопоточно', multistart_repl_thr)
#         for thread_name in multistart_repl_thr:
#             th = MultiStartThrByName(thread_name)
#             th.start()

#     for thr_name in singlestart_repl_thr:
#         print(thread_name, 'Запустился последовательно')
#         thr = SingleStartThrByName(thr_name)
#         thr.start_thr_by_name()
