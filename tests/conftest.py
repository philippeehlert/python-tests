# All fixtures must be declared in the `conftest.py` file

import pytest
from src.database import Database

# pytest fixtures can be "injected" into your test methods
# to inject a fixture, simple add a parameter with the same name of the method that produces it (example on test_important.py line 5)
@pytest.fixture
def database():
    # do whatever you need to do to initialize your fixture
    database = Database()
    database.open()

    # produces the fixture
    yield database

    # do whatever you need to do to teardown the fixture
    database.close()
