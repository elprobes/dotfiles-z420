from pathlib import Path

HOME = Path.home()

SYSTEM_CONFIG_DIR = Path(
    "/etc/bk-manager"
)

USER_CONFIG_DIR = (
    Path.home()
    / ".config"
    / "bk-manager"
)

CONFIG_DIR = (
    SYSTEM_CONFIG_DIR
    if SYSTEM_CONFIG_DIR.exists()
    else USER_CONFIG_DIR
)

GROUPS_DIR = (
    CONFIG_DIR
    / "groups"
)

SYSTEM_STATE_DIR = Path(
    "/var/lib/bk-manager"
)

USER_STATE_DIR = (
    Path.home()
    / ".local"
    / "state"
    / "bk-manager"
)

STATE_DIR = (
    SYSTEM_STATE_DIR
    if SYSTEM_CONFIG_DIR.exists()
    else USER_STATE_DIR
)

STATE_GROUPS_DIR = (
    STATE_DIR
    / "groups"
)

LOG_DIR = (
    STATE_DIR
    / "logs"
)

RSYNC_ARGS = [
    "-aHAX",
    "--delete",
]
