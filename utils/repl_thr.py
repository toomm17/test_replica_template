"""
    Файл со всей логикой работы с репликационным потоком.
"""

import threading

from cmd import run_command

CURL_COMMAND = 'curl {flags} {url}'


class RunThr(threading.Thread):
    """
        Реализация многопоточного запуска репликационного потока.
        На вход класс получает имя потока, который мы должны запустить с помощью curl
    """

    def __init__(self, thr_name: str):
        self.thr_name = thr_name
        super().__init__()

    def run(self):
        pass
