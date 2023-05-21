"""
    Файл для работы с командами в сmd
"""

import subprocess


def run_command(command: str) -> bytes:
    sub_popen = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        shell=True
    )
    output, error = sub_popen.communicate()
    if error is None:
        return output
