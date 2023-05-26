"""
    Тесты для запуска потока
    TODO:
        В файле желательно оставить только тесты 
"""
from repl_thread.run import SingleStartThrByName, MultiStartThrByName


def test_run_thread_new(repl_thr_list):
    for thr in repl_thr_list:
        if thr['insert_row_in_table']:
            # TODO INSERT ROW IN TABLE
            pass

        if thr['is_single_run'] is False:
            thr = MultiStartThrByName(thr['name'])
            thr.start()

        if thr['is_single_run'] is True:
            thr = SingleStartThrByName(thr['name'])
            thr.start()



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
