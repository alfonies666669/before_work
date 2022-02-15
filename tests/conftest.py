import pytest


@pytest.fixture(autouse=True)
def clean_text_file():
    with open('ttestread.txt', "w") as file:
        pass
