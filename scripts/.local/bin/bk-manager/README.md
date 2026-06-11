# BK Manager

Simple rsync-based backup manager for Linux.

## Features

- Multiple backup groups
- YAML configuration
- Rsync-based backups
- Persistent state tracking
- Logging
- Systemd scheduler
- Execution locking

## Configuration

Groups are stored in:

```text
/etc/bk-manager/groups
```

Example:

```yaml
id: servizi

enabled: true

description: Backup servizi

schedule:
  type: daily
  time: "03:00"

jobs:
  - id: containers
    enabled: true
    source: /srv/containers
    destination: /backup/srv-containers
```

## Commands

List groups:

```bash
bk-manager list
```

Show group:

```bash
bk-manager show servizi
```

Show status:

```bash
bk-manager status
```

Show logs:

```bash
bk-manager logs
```

Run a group:

```bash
bk-manager run servizi
```

Run all groups:

```bash
bk-manager run --all
```

Run scheduled groups:

```bash
bk-manager run --scheduled
```

## State

Runtime state is stored in:

```text
/var/lib/bk-manager
```

## Scheduler

A systemd timer executes:

```bash
bk-manager run --scheduled
```

every 5 minutes.

The scheduler decides whether a group must be executed according to its configured schedule.
