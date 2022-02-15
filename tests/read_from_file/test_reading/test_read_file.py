from tests.read_from_file.read import reading


def test_read():
    test_data = ["one\n", "two\n", "three"]
    with open("ttestread.txt", "a") as fil:
        fil.writelines(test_data)
    assert test_data == reading("ttestread.txt")


def test_read2():
    test_data = ["one\n", "two\n", "three"]
    with open("ttestread.txt", "a") as fil:
        fil.writelines(test_data)
    assert test_data == reading("ttestread.txt")
