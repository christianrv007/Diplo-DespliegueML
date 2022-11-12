import os
import pandas as pd
from pathlib import Path

PATH = str(Path(__file__).parent)
PATH_TO_DATA = f"{PATH}/data/"

def update_task_in_list(list_name: str, task_id: str, field: str, change: str):
    """ update task in list with the received parameters"""
    df = load_list(list_name)
    df.loc[task_id, field] = change
    store_list(df, list_name)


def create_list(name: str):
    """ create new list with recived name parameter"""
    df = pd.DataFrame(columns=["created", "task", "summary", "status", "owner"])
    store_list(df, name)


def get_existing_lists() -> list[str]:
    """ get all existings lists"""
    return os.listdir(PATH_TO_DATA)


def check_list_exists(name) -> 'list':
    """ check if exists list with the specific name """
    return get_list_filename(name) in get_existing_lists()


def get_list_filename(name: str) -> str:
    return f"{name}.csv"


def load_list(name: str):
    return pd.read_csv(get_list_path(name))


def store_list(df, name: str):
    df.to_csv(get_list_path(name), index=False)


def get_list_path(name: str):
    return f"{PATH_TO_DATA}{get_list_filename(name)}"


def add_to_list(list_name: str, new_row: str):
    """ add new row to list"""
    df = load_list(list_name)
    df.loc[len(df.index)] = new_row
    store_list(df, list_name)