def curl_asserter(output, error):
    """
        Проверяем на ошибки результат работы запуска курла
    """
    assert error is None, 'Have start error'
    assert not 'curl --help' in str(output), 'Curl error'


def full_run_thread(thread_name):
    """
        Запускаем один поток по имени
        И проверяем его пока он не отработает полностью (не зависит по времени)
        TODO:
        Разбораться с while True
    """
    result = run_thread(thread_name)
    output, error = result.communicate()

    curl_asserter(output, error)

    loading_id = get_loading_id(output)
    print(loading_id, 'LOADING_ID')

    # Примерно такая логика должна быть, нужно будет порефачить иф и подумать над while True (Bad Practice)
    while True:
        stats = get_all_threads(thread_name)
        output, error = stats.communicate()
        to_json = json.loads(output.decode('utf-8'))
        thread_dict = get_dict_with_id(int(loading_id), to_json)

        if thread_dict and thread_dict['ctlState'] == ThreadCtlStates.ACTIVE \
            and thread_dict['orcherstratorState'] == ThreadOrcherstratorStates.RUNNING:
            time.sleep(25)
            continue
        else:
            # TODO Logging
            break


def thread_dict_asserter(thread_dict, id, thread_name):
    """
        Проверяем состояния потока
    """
    assert thread_dict['ctlState'] == ThreadCtlStates.COMPLETED
    assert thread_dict['orcherstratorState'] == ThreadOrcherstratorStates.SUCCESS
    assert thread_dict['id'] == id
    assert thread_dict['workflowName'] == thread_name
    # TODO Возможно нужно проверить дату и время запуска
