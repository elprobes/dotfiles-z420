from pathlib import Path

CONFIG_DIR = Path.home() / ".config" / "bk-manager"

GROUPS_DIR = CONFIG_DIR / "groups"

STATE_DIR = (
    Path.home()
    / ".local"
    / "state"
    / "bk-manager"
)

STATE_DIR.mkdir(
    parents=True,
    exist_ok=True
)

STATE_GROUPS_DIR = STATE_DIR / "groups"

LOG_DIR = STATE_DIR / "logs"
