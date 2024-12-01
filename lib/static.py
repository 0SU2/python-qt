from pathlib import Path

# * DIRECTORIES
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
LIB_DIR = Path(BASE_DIR, "lib")

UI_FOLDER = Path(BASE_DIR, "ui")
UI_COMPILED_FOLDER = Path(BASE_DIR, "ui", "compiled")

LOGO_FILE = Path(BASE_DIR, "ui", "assets", "logo.png")
LOGO_XS_FILE = Path(BASE_DIR, "ui", "assets", "logo-xs.png")