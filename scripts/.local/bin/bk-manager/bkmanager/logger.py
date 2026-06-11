from datetime import datetime

from bkmanager.constants import LOGS_DIR


def _log(
    level: str,
    message: str
):

    now = datetime.now()

    logfile = get_today_logfile()

    line = (
        f"{now.strftime('%Y-%m-%d %H:%M:%S.%f')} "
        f"[{level}] "
        f"{message}\n"
    )

    with open(logfile, "a") as f:
        f.write(line)

def log_info(
    message: str
):

    _log(
        "INFO",
        message
    )

def log_error(
    message: str
):

    _log(
        "ERROR",
        message
    )

def get_today_logfile():

    now = datetime.now()

    return (
            LOGS_DIR
            / f"{now.strftime('%Y-%m-%d')}.log"
    )

def read_today_logs():

    logfile = get_today_logfile()

    if not logfile.exists():
        return []

    with open(logfile, "r") as f:

        return f.readlines()
