from pathlib import Path

import yaml

from bkmanager.constants import GROUPS_DIR
from bkmanager.models import (
        Group,
        Job,
        Schedule,
)


def load_group(path: Path) -> Group:

    with open(path, "r") as f:
        data = yaml.safe_load(f)

    schedule = Schedule(
        type=data["schedule"]["type"],
        time=data["schedule"]["time"],
        day=data["schedule"].get("day")
    )

    jobs = []

    for job in data["jobs"]:

        jobs.append(
            Job(
                id=job["id"],
                enabled=job["enabled"],
                source=job["source"],
                destination=job["destination"]
            )
        )

    return Group(
        id=data["id"],
        enabled=data["enabled"],
        description=data["description"],
        schedule=schedule,
        jobs=jobs
    )

def load_group_by_id(group_id: str) -> Group:

    path = GROUPS_DIR / f"{group_id}.yaml"

    if not path.exists():
        raise FileNotFoundError(
            f"Group '{group_id}' not found"
        )

    return load_group(path)

def load_groups() -> list[Group]:

    groups = []

    for file in GROUPS_DIR.glob("*.yaml"):

        groups.append(
            load_group(file)
        )

    return groups
