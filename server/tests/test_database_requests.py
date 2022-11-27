import unittest
from server.database import requests as DBOperator


class MyTestCase(unittest.TestCase):
    def test_select_user_valid(self):
        print(DBOperator.DbOperator().select_user('ivan@mail.ru', "1124"))

    def test_select_user_invalid(self):
        print(DBOperator.DbOperator().select_user('sdfasdfasdfegor@mail.ru', "+sadfasdf1111"))

    def test_select_user_info_valid(self):
        print(DBOperator.DbOperator().select_user_info(1))

    def test_select_user_info_invalid(self):
        print(DBOperator.DbOperator().select_user_info(None))

    def test_update_task(self):
        print(DBOperator.DbOperator().update_task(4, 1, 2, "titel", "teыыыxt", True, "0", "100"))

    def test_select_all_user(self):
        print(DBOperator.DbOperator().select_all_user())

    def test_select_user_task(self):
        print(DBOperator.DbOperator().select_user_task(3))

    def test_delete_user_task(self):
        print(DBOperator.DbOperator())

    def test_select_all_tasks(self):
        print(DBOperator.DbOperator().select_all_task())




if __name__ == '__main__':
    unittest.main()
