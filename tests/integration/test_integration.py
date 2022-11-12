from todo_list.todos.todos import todos 
import pandas as pd
import pytest
import shutil
from datetime import datetime

# @pytest.fixture()
# def three_cards(cards_db):
#     i = cards_db.add_card(Card("foo"))
#     j = cards_db.add_card(Card("bar"))
#     k = cards_db.add_card(Card("baz"))
#     return (i, j, k)  # ids for the cards
@pytest.fixture(scope="function")
def tmp_dir(tmpdir_factory):
    my_tmpdir = tmpdir_factory.mktemp("pytestdata")
    todos.PATH_TO_DATA = my_tmpdir
    yield my_tmpdir
    shutil.rmtree(str(my_tmpdir))


@pytest.fixture(scope="session")
def df_empty():
    return pd.DataFrame(columns=["created", "task", "summary", "status", "owner"])


@pytest.fixture(scope="session")
def df_full(new_row):
    return pd.DataFrame(
        [new_row], columns=["created", "task", "summary", "status", "owner"]
    )


@pytest.fixture(scope="function")
def df_full_stored(tmp_dir, df_full):
    df_full.to_csv(f"{tmp_dir}/todos.csv")
    return df_full


@pytest.fixture(scope="function")
def df_empty_stored(tmp_dir, df_empty):
    df_empty.to_csv(f"{tmp_dir}/todos.csv")
    return df_empty


@pytest.fixture(scope="session")
def new_row():
    return {
        "created": datetime.now().strftime("%Y-%m-%d %H-%M-%S"),
        "task": "cocinar",
        "summary": "Cocinar algo rico",
        "status": "todo",
        "owner": "Andre",
    }

def get_parameters():
    return [("test_list")]

@pytest.mark.parametrize("new_row, df_full", get_parameters())
def test_integracion(new_list_name: str):
    '''create a new list'''
    todos.create_list(new_list_name)
    ''' check if exists the list created'''
    assert todos.check_list_exists(new_list_name) == True