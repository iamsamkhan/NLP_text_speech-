import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "Speech_to_text"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"specch_text_nlp/{project_name}/__init__.py",
    f"specch_text_nlp/{project_name}/components/__init__.py",
    f"specch_text_nlp/{project_name}/utils/speech_text.py",
    f"specch_text_nlp/{project_name}/config/__init__.py",
    f"specch_text_nlp/{project_name}/utils/specch_text_main.py",
    f"specch_text_nlp/{project_name}/utils/__init__.py",
    f"specch_text_nlp/{project_name}/path/text/",
    f"specch_text_nlp/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "requirements.txt",
    "setup.py",
    "main.py",
    "app.py",
    "templates/index.html",
    "templates/index1.html"


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