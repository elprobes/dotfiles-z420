from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(PROJECT_ROOT))

from bkmanager.config import load_groups

groups = load_groups()

for group in groups:
    print(group.id)
