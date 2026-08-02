"""Helper utilities for EduPro learner analytics.

This module can be used for shared path helpers, reusable formatting
functions, and small utility methods that support preprocessing,
analysis, and dashboard tasks.
"""

from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
REPORTS_DIR = ROOT_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"


def ensure_project_dirs() -> None:
    """Create the common project directories if they do not exist."""
    for directory in (RAW_DIR, PROCESSED_DIR, FIGURES_DIR):
        directory.mkdir(parents=True, exist_ok=True)
