import json
from datetime import datetime

from bkmanager.constants import (
        STATE_DIR,
        STATE_GROUPS_DIR
)

def ensure_state_dirs():

    (STATE_DIR / "groups").mkdir(
            parents=True,
            exist_ok=True
    )

    (STATE_DIR / "logs").mkdir(
            parents=True,
            exist_ok=True
    )

def load_group_state(
    group_id: str
):
    path = (
        STATE_GROUPS_DIR
        / f"{group_id}.json"
    )

    if not path.exists():
        return None

    with open(path, "r") as f:
        return json.load(f)

def save_group_state(
    group_id: str,
    result: str
):

    path = (
        STATE_GROUPS_DIR
        / f"{group_id}.json"
    )

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    data = {
        "last_run": (
            datetime.now()
            .isoformat()
        ),
        "last_result": result
    }

    with open(path, "w") as f:

        json.dump(
            data,
            f,
            indent=2
        )
