import argparse
from datetime import datetime

from bkmanager.config import (
        load_groups,
        load_group_by_id
)
from bkmanager.backup import (
        dry_run_group,
        run_group,
        run_all_groups,
        run_scheduled_groups
)
from bkmanager.state import (
        ensure_state_dirs,
        load_group_state
)
from bkmanager.logger import (
        read_today_logs
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

def cmd_status():

    groups = load_groups()

    print()

    print(
        f"{'GROUP':<15}"
        f"{'RESULT':<12}"
        f"{'LAST RUN'}"
    )

    print()

    for group in groups:

        state = load_group_state(
            group.id
        )

        if state is None:

            result = "never"
            last_run = "-"

        else:

            result = state.get(
                "last_result",
                "-"
            )

            last_run = state.get(
                "last_run"
            )

            if last_run:

                last_run = (
                    datetime
                    .fromisoformat(last_run)
                    .strftime("%Y-%m-%d %H:%M")
                )

            else:

                last_run = "-"

        print(
            f"{group.id:<15}"
            f"{result:<12}"
            f"{last_run}"
        )

def cmd_logs():

    for line in read_today_logs():

        print(
            line,
            end=""
        )

def main():

    ensure_state_dirs()

    parser = argparse.ArgumentParser(
        prog="bk-manager"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    subparsers.add_parser("list")
    subparsers.add_parser("status")
    subparsers.add_parser("logs")

    show_parser = subparsers.add_parser(
        "show"
    )

    show_parser.add_argument(
        "group"
    )

    run_parser = subparsers.add_parser(
    "run"
)

    run_parser.add_argument(
        "group",
        nargs="?"
    )

    run_parser.add_argument(
        "--all",
        action="store_true"
    )

    run_parser.add_argument(
        "--scheduled",
        action="store_true"
    )

    run_parser.add_argument(
        "--dry-run",
        action="store_true"
    )

    args = parser.parse_args()


    if args.command == "list":
        cmd_list()
        return

    if args.command == "show":
        cmd_show(args.group)
        return

    if args.command == "status":
        cmd_status()
        return

    if args.command == "logs":
        cmd_logs()
        return

    if args.command == "run":

        if args.all:

            run_all_groups()
            return

        if args.scheduled:
            run_scheduled_groups()
            return

        if not args.group:

            print(
                "Specify a group "
                "or use --all"
            )
            return

        group = load_group_by_id(
            args.group
        )

        if args.dry_run:

            dry_run_group(group)
            return

        run_group(group)
        return

    parser.print_help()
