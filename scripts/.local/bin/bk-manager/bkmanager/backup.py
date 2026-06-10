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
