import os
from pathlib import Path
import logging

#logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'geminiai'

list_of_files = [
    ".github/workflows/.gitkeep", ## git cicd - main.yaml
    f"llm/{project_name}/__init__.py",
    f"llm/{project_name}/pipeline/__init__.py",   
    "params.yaml",
    "requirements.txt",
    "README.md",
    ".gitignore",
    "research/01_gemini.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")