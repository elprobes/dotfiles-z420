import subprocess

from bkmanager.constants import RSYNC_ARGS
from bkmanager.models import Group


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

    subprocess.run(
        cmd,
        check=True
    )

def run_group(group):

    print()
    print(f"Running group: {group.id}")
    print()

    for job in group.jobs:

        if not job.enabled:
            continue

        run_job(job)
