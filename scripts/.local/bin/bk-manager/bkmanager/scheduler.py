from datetime import datetime

def should_run_daily(
    scheduled_time: str,
    last_run: str | None
):

    now = datetime.now()

    hour, minute = map(
        int,
        scheduled_time.split(":")
    )

    scheduled_today = now.replace(
        hour=hour,
        minute=minute,
        second=0,
        microsecond=0
    )

    if now < scheduled_today:
        return False

    if last_run is None:
        return True

    last_run_dt = datetime.fromisoformat(
        last_run
    )

    if last_run_dt.date() == now.date():
        return False

    return True

def should_run(
    group,
    state
):

    if not group.enabled:
        return False

    if group.schedule.type == "daily":

        last_run = None

        if state:
            last_run = state.get(
                "last_run"
            )

        return should_run_daily(
            group.schedule.time,
            last_run
        )

    raise ValueError(
        f"Unsupported schedule type: "
        f"{group.schedule.type}"
    )
