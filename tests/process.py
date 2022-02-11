

import pytest

from pymono.process import Process


@pytest.fixture(scope="function")
def process():
    return Process.spawn(r'C:\WINDOWS\system32\notepad.exe')


def test_process_spawn(process):
    print(process.pid)
    assert process.pid is not None



