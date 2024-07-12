import os
import shutil
import pytest
from zipfile import ZipFile

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE)
TMP_DIR = os.path.join(CURRENT_DIRECTORY, "tmp")
RESOURCES_DIR = os.path.join(CURRENT_DIRECTORY, "resources")


@pytest.fixture(scope='function', autouse=True)
def create_archive():
    if not os.path.exists("resources"):
        os.mkdir("resources")

    with ZipFile(os.path.join(RESOURCES_DIR, 'zapakovkaslyoz.zip'), "w") as zf:
        for file in ['file.csv', 'file.pdf', 'file.xlsx']:
            add_file = os.path.join(TMP_DIR, file)
            zf.write(add_file, os.path.basename(add_file))

    yield
    shutil.rmtree(RESOURCES_DIR)