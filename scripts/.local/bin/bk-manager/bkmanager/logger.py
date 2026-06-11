from datetime import datetime

from bkmanager.constants import LOGS_DIR


def _log(
    level: str,
    message: str
):

    now = datetime.now()

    logfile = (
        LOGS_DIR
        / f"{now.strftime('%Y-%m-%d')}.log"
    )

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
