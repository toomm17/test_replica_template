import time
import random
from multiprocessing.dummy import Pool

from repl_thread.run import ReplicationThread
from repl_thread.consts import ThreadCtlStates
from utils.db import postgres_cursor


ORCHESTRATOR_RUNNING_STATES = ('RUNNING', 'START')

    
def run_thread(thread: dict):
    thread = ReplicationThread(thread['name'])
    thread_loading_id = thread.run()

    if thread['insert_row_in_table']:
        pass

    while thread.get_state('ctlState', thread_loading_id) == ThreadCtlStates.ACTIVE:
        if thread.get_state('orchestratorState', thread_loading_id) in ORCHESTRATOR_RUNNING_STATES:
            print(thread.name, ' активен')
            time.sleep(random.randint(10, 20))
    
    thread_state = thread_state.get_state('ctlState', thread_loading_id)
    log_string = '{name} закончил работу с состоянием {state}'.format(
        name=thread.name, state=thread_state
    )
    return log_string


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
