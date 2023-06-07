"""
    Файл для работы с командами в сmd
"""

import subprocess


def run_command(command: str) -> dict:
    sub_popen = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        shell=True
    )    
    bytes_out, bytes_err = sub_popen.communicate()
    out = str(bytes_out).rstrip()
    err = str(bytes_err).rstrip()    
    return {'returncode': sub_popen.returncode, 'out': out, 'err': err}
