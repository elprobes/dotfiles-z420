from dataclasses import dataclass, field


@dataclass
class Job:
    id: str
    enabled: bool
    source: str
    destination: str


@dataclass
class Schedule:
    type: str
    time: str
    day: str | None = None


@dataclass
class Group:
    id: str
    enabled: bool
    description: str
    schedule: Schedule
    jobs: list[Job] = field(default_factory=list)
