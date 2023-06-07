import os
import threading
from multiprocessing.dummy import Pool

from repl_thread.run import ReplicationThread
from utils.db import postgres_cursor


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
