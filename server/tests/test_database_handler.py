import unittest
from server.database import handler


class MyTestCase(unittest.TestCase):
    def test_connect(self):
        handler.Db()

    def test_check_user_valid(self):
        print(handler.Db()._select_with_email("egor@mail.ru"))

    def test_check_user_invalid(self):
        handler.Db()._select_with_email("sdfasdfasdfasdf")

    def test_new_user(self):
        handler.Db()._insert_user('egor@mail.ru', 'rand', 'egor lyad', "+1111")

    def test_new_task(self):
        handler.Db()._insert_task(1, 2, "titel", "text", "0", "0", "100", '', '')

    def test_select_like(self):
        print(handler.Db()._select_like_task("ti"))

    def test_delete_task(self):
        print(handler.Db()._delete_task(23))

    def test_get_all_task(self):
        print(handler.Db()._select_all_task())


if __name__ == '__main__':
    unittest.main()
