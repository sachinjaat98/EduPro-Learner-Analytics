from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
FIGURES_DIR = ROOT / "reports" / "figures"

def ensure_directories():
    for path in (RAW_DIR, PROCESSED_DIR, FIGURES_DIR):
        path.mkdir(parents=True, exist_ok=True)

