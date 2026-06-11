import fcntl

from bkmanager.constants import (
    STATE_DIR
)

LOCKFILE = (
        STATE_DIR
        / "bk-manager.lock"
)

def acquire_lock():

    lock_file = open(
        LOCKFILE,
        "w"
    )

    try:

        fcntl.flock(
            lock_file,
            fcntl.LOCK_EX
            | fcntl.LOCK_NB
        )

    except BlockingIOError:

        return None

    return lock_file
