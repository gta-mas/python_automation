import pytest

from pytest_demo.base_class import base_class


@pytest.mark.usefixtures("load_data")
class TestExample2(base_class):
    def test_edit_profile(self, load_data):
        log = self.get_logger()
        log.info(load_data[0])
        log.info(load_data[2])

        print(load_data[2])