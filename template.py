# import Libraries
import os   # interacting with the operation system file
from pathlib import Path   # import the class path from the pathlib medule for working file paths


# Building Structure
structure = [
    "main.py",
    "requirements.txt",
    "config.yaml",
    "Dockerfile",
    "application/streamlit_app.py",
    "application/__init__.py",
    "models/summarizer_model.py",
    "models/summarizer_experiment.ipynb",
    "models/__init__.py",
    "models/preprocessing.py",
    "utils/config_loader.py",
    "utils/__init__.py",
    "logging/custom_logging.py",
    "logging/__init__.py",
]


for filepath in map(Path, structure):
    if filepath.parent:
        filepath.parent.mkdir(parents = True, exist_ok = True)
        print(f"Ensured directory exists: {filepath.parent}")
    if not filepath.exists():
        filepath.touch()
        print(f"Created file: {filepath}")
    else:
        print(f"File already exists: {filepath}")