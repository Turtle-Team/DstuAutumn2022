import typing

from server.database import handler, utils, obj
class DbOperator:
    def select_user(self, email: str, number: str) -> str:
        handlerDb = handler.Db()
        select_email = handlerDb._select_with_email(email)
        select_number = handlerDb._select_with_number(number)
        if isinstance(select_email, tuple) and isinstance(select_number, tuple):
            return utils.DataOperator.create_json_with_id(select_number[-1])
        return utils.DataOperator.create_json_with_id(None)
    def select_all_user(self):
        users = handler.Db()._select_all_user()
        return utils.DataOperator.create_json_all_users(users)

    def select_user_info(self, id: int) -> typing.Tuple[str] or None:
        user_info = handler.Db()._select_user_info(id)
        if isinstance(user_info, tuple):
            return utils.DataOperator.create_json_db(user_info)
        return None

    def new_user(self, email: str, secret_key: str, public_name: str, phone_number: str):
        handler.Db()._insert_user(email, secret_key, public_name, phone_number)
        return self.select_user(email, phone_number)

    def create_task(self, from_id: int, to_id: int, title: str, text: str, is_secret: bool, time_start, time_end):
        task_id = handler.Db()._insert_task(from_id, to_id, text, title, is_secret, 0, 100, time_start, time_end)
        return utils.DataOperator.create_json_task_info(task_id)

    def update_task(self, task_id: int, from_id: int, to_id: int, title: str, text: str, is_secret: bool, progress_start: int, progress_end: int, time_start: str, time_end: str):
        task_id = handler.Db()._update_task(task_id, from_id, to_id, text, title, is_secret, progress_start, progress_end, time_start, time_end)
        return utils.DataOperator.create_json_task_id(task_id)

    def select_task(self, task_id: int):
        task_id = handler.Db()._select_task(task_id)
        return utils.DataOperator.create_json_task_info(task_id)

    def select_all_task(self):
        tasks = handler.Db()._select_all_task()
        return utils.DataOperator.create_json_task_all_info(tasks)

    def select_user_task(self, user_id: int) -> typing.Tuple[int]:
        task_id = handler.Db()._select_user_task(user_id)
        return utils.DataOperator.create_json_task_info(task_id)

    def select_del_task(self, task_id: int):
        is_like = handler.Db()._delete_task(task_id)
        return utils.DataOperator.create_json_del_task(is_like)

    def create_note(self, from_id: int, title: str, text: str):
        note_id = handler.Db()._insert_notes(from_id, title, text)
        return utils.DataOperator.create_json_note_info(note_id)

    def select_note(self, from_id: int):
        note_id = handler.Db()._select_notes(from_id)
        return utils.DataOperator.create_json_note_info(note_id)




