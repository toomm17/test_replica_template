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
