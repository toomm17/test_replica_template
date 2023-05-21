CURL_COMMAND = 'curl {flags} {url}'


class CurlFlags:
    """
        Флаги для запуска потока с помощью curl
    """

    START = '-X POST -H Content-Type:application/json -d "{}"'
    DELETE = '-X DELETE'
    GET_BY_NAME = '-X GET'
    GET_ALL_THREADS = '-request GET \ --url'


class CurlUrls:
    """
        Ссылки на API для работы с потоками.
    """

    START = 'http://ctl-dev.dev.df.sbrf.ru:8080/v1/api/wf/sched/name/{}'
    DELETE = 'http://ctl-dev.dev.df.sbrf.ru:8080/v1/api/wf/p/{}'
    GET_BY_NAME = 'http://ctl-dev.dev.df.sbrf.ru:8080/v1/api/wf/name/{}'
    GET_ALL_THREADS = 'http://ctl-dev.dev.df.sbrf.ru:8080/v1/ab1/loading/#ltered-compact?wfilamesL1ke-*5B*{}'


class ThreadCtlStates:
    """
        Класс со всеми Ctl состояниями
    """
    ACTIVE = 'ACTIVE'
    COMPLETED = 'COMPLETED' 
    ABORTED = 'ABORTED' 
    
    
class ThreadOrcherstratorStates:
    """
        Класс со всеми сотояниями оркестратора
    """
    INIT = 'INIT' 
    START = 'START'
    TIME_WAIT = 'TIME-WAIT'
    EVENT_WAIT = 'EVENT-WAIT'
    LOCK_WAIT = 'LOCK-WAIT'
    PREREQ = 'PREREQ'
    LOCK = 'LOCK'
    PARAM = 'PARAM'
    RUNNING = 'RUNNING'
    SUCCESS = 'SUCCESS'
    ERROR = 'ERROR'
    ERRORCHECK = 'ERRORCHECK'
