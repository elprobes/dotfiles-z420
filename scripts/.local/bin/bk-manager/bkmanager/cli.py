import argparse

from bkmanager.config import (
        load_groups,
        load_group_by_id
)

def cmd_list():

    groups = load_groups()

    for group in groups:
        print(group.id)


def cmd_show(group_id: str):

    group = load_group_by_id(group_id)

    print(f"Group: {group.id}")
    print()

    print(f"Enabled: {group.enabled}")
    print()

    print("Description:")
    print(group.description)
    print()

    print("Schedule:")
    print(
        f"  {group.schedule.type} "
        f"{group.schedule.time}"
    )

    if group.schedule.day:
        print(
            f"  day: {group.schedule.day}"
        )

    print()

    print("Jobs:")
    print()

    for job in group.jobs:

        print(f"  {job.id}")

        print(
            f"    enabled: {job.enabled}"
        )

        print(
            f"    source: {job.source}"
        )

        print(
            f"    destination: {job.destination}"
        )

        print()


def main():

    parser = argparse.ArgumentParser(
        prog="bk-manager"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    subparsers.add_parser("list")

    show_parser = subparsers.add_parser(
        "show"
    )

    show_parser.add_argument(
        "group"
    )

    args = parser.parse_args()

    if args.command == "list":
        cmd_list()
        return

    if args.command == "show":
        cmd_show(args.group)
        return

    parser.print_help()
