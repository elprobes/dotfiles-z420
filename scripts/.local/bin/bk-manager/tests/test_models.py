from bkmanager.models import *

g = Group(
    id="servizi",
    enabled=True,
    description="Backup servizi",
    schedule=Schedule(
        type="daily",
        time="03:00"
    ),
    jobs=[
        Job(
            id="containers",
            enabled=True,
            source="/srv/containers",
            destination="/backup/srv-containers"
        )
    ]
)

print(g)
