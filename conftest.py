import os
import shutil
import pytest
from zipfile import ZipFile

@pytest.fixture
def test_create_archive():
    with ZipFile('zapakovkaslyoz.zip', 'w') as zf:
        for file in ['file.csv', 'file.pdf', 'file.xlsx']:
            filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp/" + file)
            zf.write(filepath, file)

    os.makedirs('resources', exist_ok=True)
    shutil.move('zapakovkaslyoz.zip.', 'resources/zapakovkaslyoz.zip')
    yield
    shutil.rmtree('resources')
