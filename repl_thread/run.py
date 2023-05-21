import json
import time
import threading

from repl_thread.consts import (
    CURL_COMMAND,
    CurlFlags,
    CurlUrls,
    ThreadCtlStates,
    ThreadOrcherstratorStates
)
from utils.cmd import run_command


class SingleStartThrByName:
    """
        Класс для последовательного запуска потока
    """

    def __init__(self, thr_name: str) -> None:
        self.thr_name = thr_name

        self.start_thr_command = CURL_COMMAND.format(
            url=CurlUrls.START.format(self.thr_name),
            flags=CurlFlags.START
        )
        self.get_thrs_history = CURL_COMMAND.format(
            url=CurlUrls.GET_ALL_THREADS.format(self.thr_name),
            flags=CurlFlags.GET_ALL_THREADS
        )
        
    @staticmethod
    def get_thr_loading_id(output: str):
        """
            Получаем loading_id после успешного запуска потока
            Получаем output в формате: TODO добавить формат
        """
        loading_id = output.split('\\n')[-1]
        loading_id_string = loading_id.split(',')[-1].replace("]'", '')
        return loading_id_string[1:-1]
    
    @staticmethod
    def get_thr_info_by_loading_id(all_thrs: dict, loading_id: int) -> dict:
        """
            Получаем информацию о текущем запуске потока из истории запуска всех потоков.
        """
        for item in all_thrs['items']:
            if item['id'] == loading_id:
                return item

        return {}
    
    def thr_dict_asserter(self, thr_info: dict, loading_id: int):
        """
            Проверяем, что поток завершился успешно
        """
        assert thr_info['ctlState'] == ThreadCtlStates.COMPLETED
        assert thr_info['orcherstratorState'] == ThreadOrcherstratorStates.SUCCESS
        assert thr_info['id'] == loading_id
        assert thr_info['workflowName'] == self.thr_name

    def get_thr_info(self, loading_id: int) -> dict:
        """
            Запускаем команду, которая получают всю историю запуска потоков
        """
        all_thrs_output = run_command(self.get_thrs_history)
        all_thrs_dict = json.loads(all_thrs_output.decode('utf-8'))
        return self.get_thr_info_by_loading_id(all_thrs_dict, int(loading_id))

    def thr_still_running(self, thr_info: dict) -> bool:
        """
            Проверяем состояния потока
        """
        if thr_info and thr_info['ctlState'] == ThreadCtlStates.ACTIVE \
            and thr_info['orcherstratorState'] == ThreadOrcherstratorStates.RUNNING:
            return True
        
        return False

    def start_thr_by_name(self) -> None:
        output = run_command(self.start_thr_command)
        loading_id = self.get_thr_loading_id(str(output))

        thr_info = self.get_thr_info(loading_id)

        while self.thr_still_running(thr_info):
            time.sleep(25)
            thr_info = self.get_thr_info(loading_id)

        self.thr_dict_asserter(thr_info)
        

class MultiStartThrByName(threading.Thread):
    def __init__(self, thr_name: str):
        self.thr_name = thr_name
        super().__init__()

    def run(self):
        th = SingleStartThrByName(self.thr_name)
        th.start_thr_by_name()
    