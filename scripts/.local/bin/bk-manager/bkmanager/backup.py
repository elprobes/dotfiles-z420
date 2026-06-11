import subprocess

from bkmanager.constants import RSYNC_ARGS
from bkmanager.models import Group
from bkmanager.state import save_group_state
from bkmanager.config import load_groups
from bkmanager.logger import (
        log_info,
        log_error
)
from bkmanager.scheduler import (
        should_run
)
from bkmanager.state import (
        load_group_state
)


def dry_run_group(group: Group):

    print()
    print(f"Group: {group.id}")
    print()

    print("Would run:")
    print()

    for job in group.jobs:

        if not job.enabled:
            continue

        print(job.id)
        print()

        print("  source:")
        print(f"    {job.source}")
        print()

        print("  destination:")
        print(f"    {job.destination}")
        print()

def run_job(job):

    print()
    print(f"Running job: {job.id}")
    print()

    print(f"Source:      {job.source}")
    print(f"Destination: {job.destination}")
    print()

    cmd = [
        "rsync",
        *RSYNC_ARGS,
        f"{job.source}/",
        f"{job.destination}/",
    ]

    log_info(
        f"Job {job.id} started"
    )

    subprocess.run(
        cmd,
        check=True
    )

    log_info(
        f"Job {job.id} completed"
    )

def run_group(group):

    log_info(
        f"Group {group.id} started"
    )

    print()
    print(f"Running group: {group.id}")
    print()

    try:

        for job in group.jobs:

            if not job.enabled:
                continue

            run_job(job)

        save_group_state(
            group.id,
            "success"
        )

        log_info(
           f"Group {group.id} completed"
        )

    except Exception as e:

        log_error(
            f"Group {group.id} failed: {e}"
        )

        save_group_state(
            group.id,
            "failed"
        )

        raise

def run_all_groups():

    groups = load_groups()

    for group in groups:

        if not group.enabled:
            continue

        run_group(group)

def run_scheduled_groups():

    groups = load_groups()

    for group in groups:

        state = load_group_state(
            group.id
        )

        if not should_run(
            group,
            state
        ):

            log_info(
                    f"Skipping {group.id}: already executed today"
            )

            continue

        run_group(group)
