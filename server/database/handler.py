import typing
from typing import List, Tuple, Any

import psycopg2
from server.settings import database as setting


class Db:
    def __init__(self):
        self.connection = psycopg2.connect(user=setting.USER,
                                      password=setting.PASSWORD,
                                      host=setting.HOST,
                                      port=setting.PORT)
        self.cur = self.connection.cursor()

    def _select_with_email(self, email: str) -> typing.Tuple[str] or None:
        self.cur.execute("SELECT user_id FROM users WHERE email=%s", (email,))
        return self.cur.fetchone()

    def _select_with_number(self, number: str) -> typing.Tuple[str] or None:
        self.cur.execute("SELECT user_id FROM users WHERE phone_number=%s", (number,))
        return self.cur.fetchone()

    def _select_user_info(self, id: int) -> typing.Tuple[str] or None:
        self.cur.execute("SELECT * FROM users WHERE user_id=%s", (id,))
        return self.cur.fetchone()

    def _insert_user(self, email: str, secret_key: str, public_name: str, phone_number: str):
        self.cur.execute("INSERT INTO public.users(email, secret_key, public_name, phone_number) "
                         "VALUES (%s, %s, %s, %s)", (email, secret_key, public_name, phone_number,))
        return self.connection.commit()

    def _select_all_user(self):
        sql = """SELECT * FROM users"""
        self.cur.execute(sql)
        return self.cur.fetchall()

    def _insert_task(self, from_id, to_id, text, title, is_secret, progress_start, progress_end, time_start, time_end):
        sql = """INSERT INTO public.task(
        from_id, to_id, text, is_secret, progress_start, progress_end, title, time_start, time_end)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING task_id"""
        self.cur.execute(sql, (from_id, to_id, text, is_secret, progress_start, progress_end, title, time_start, time_end))
        self.connection.commit()
        return self.cur.fetchone()

    def _update_task(self, task_id, from_id, to_id, text, title, is_secret, progress_start, progress_end, time_start, time_end):
        sql = """UPDATE public.task
        SET from_id=%s, to_id=%s, text=%s, is_secret=%s, progress_start=%s, progress_end=%s, title=%s, time_start=%s, time_end=%s
        WHERE task_id=%s"""
        self.cur.execute(sql, (from_id, to_id, text, is_secret, progress_start, progress_end, title, task_id, time_start, time_end))
        self.connection.commit()
        return (task_id)

    def _select_task(self, task_id: int) -> typing.Tuple[str or int]:
        sql = """SELECT * FROM public.task WHERE task_id = %s"""
        self.cur.execute(sql, (task_id,))
        return self.cur.fetchone()

    def _select_all_task(self) -> list[tuple[Any, ...]]:
        sql = """SELECT * FROM public.task"""
        self.cur.execute(sql)
        return self.cur.fetchall()

    def _select_user_task(self, user_id: int) -> typing.Tuple[str or int]:
        sql = """SELECT task_id FROM public.task WHERE from_id=%s OR to_id=%s"""
        self.cur.execute(sql, (user_id, user_id,))
        return self.cur.fetchall()

    def _select_like_task(self, title: str) -> typing.List[tuple]:
        sql = """SELECT task_id FROM public.task WHERE title LIKE %s;"""
        self.cur.execute(sql, ("%"+title+"%",))
        return self.cur.fetchall()

    def _insert_notes(self, user_id, title, text):
        sql = """INSERT INTO public.notes(
                uesr_id, title, text)
                VALUES (%s, %s, %s) RETURNING note_id"""
        self.cur.execute(sql, (user_id, title, text))
        self.connection.commit()
        return self.cur.fetchone()

    def _update_notes(self, title: str, text: str, note_id: str):
        sql = """UPDATE public.notes title=%s, text=%s WHERE note_id=%s"""
        self.cur.execute(sql, (title, text, note_id))
        return note_id

    def _select_notes(self, from_id):
        sql = """SELECT uesr_id, title, text, note_id FROM public.notes WHERE uesr_id=%s"""
        self.cur.execute(sql, (from_id,))
        self.connection.commit()
        return self.cur.fetchone()
# Фиг знает как работает, но работает плохова-то
    def _delete_task(self, task_id):
        sql = """DELETE FROM public.task WHERE task_id=%s;"""
        self.cur.execute(sql, (task_id,))
        self.connection.commit()
        return True



