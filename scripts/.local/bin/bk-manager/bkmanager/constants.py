from pathlib import Path

HOME = Path.home()

CONFIG_DIR = (
    HOME
    / ".config"
    / "bk-manager"
)

GROUPS_DIR = (
    CONFIG_DIR
    / "groups"
)

STATE_DIR = (
    HOME
    / ".local"
    / "state"
    / "bk-manager"
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
