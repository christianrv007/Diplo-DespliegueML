import typer
from datetime import datetime
from .todos import todos as todos

app = typer.Typer(add_completion=False)

### CLI METHODS ###

"""
Method create 

PARAMETERS:
    name
"""

@app.command("create")
def create(name: str = typer.Option("Unnamed", "-ln", "--listname")):

    """Create a new todo list"""

    if todos.check_list_exists(name):
        print("There is already a todo list with this name.")
        return

    todos.create_list(name)
    print(f"Todo list {name} successfully created!")

"""
Method list 

PARAMETERS:
    
Print all existing list
"""

@app.command("list")
def list_lists():

    """Lists all existing todo lists"""

    existing_lists = todos.get_existing_lists()
    for ls in existing_lists:
        print(ls)

"""
Method show

PARAMETERS:
    list_name 

show specific list
"""
@app.command("show")
def show_list(list_name: str = typer.Option(..., "-ln", "--listname")):
    """Shows Task in one list"""
    if not todos.check_list_exists(list_name):
        print("The list does not exist. Use create list first.")
        return
    df = todos.load_list(list_name)
    print(df.to_markdown())

"""
Method create 

PARAMETERS:
    list_name 
    task_name
    summary
    owner

Add new list
"""

@app.command("add")
def add_task(
    list_name: str = typer.Option(..., "-ln", "--listname"),
    task_name: str = typer.Option(..., "-tn", "--taskame"),
    summary: str = typer.Option(None, "-d", "--description"),
    owner: str = typer.Option(..., "-o", "--owner"),
):
    """Add a task to a given todo list"""

    if not todos.check_list_exists(list_name):
        print("The list does not exist. Use create list first.")
        return

    new_row = {
        "created": datetime.now().strftime("%Y-%m-%d %H-%M-%S"),
        "task": task_name,
        "summary": summary if summary else None,
        "status": "todo",
        "owner": owner,
    }

    todos.add_to_list(list_name, new_row)
    print("Task successfully added")

"""
Method update

PARAMETERS:
    list_name
    task_id
    field
    change

update task in list
"""
@app.command("update")
def update_task(
    list_name: str = typer.Option(..., "-ln", "--listname"),
    task_id: int = typer.Option(..., "-i", "--taskid"),
    field: str = typer.Option(..., "-f", "--field"),
    change: str = typer.Option(..., "-c", "--change"),
):

    """Update a task in a given todo list"""
    if not todos.check_list_exists(list_name):
        print("The list does not exist. Use create list first.")
        return
    todos.update_task_in_list(list_name, task_id, field, change)
    print("Task successfully updated")

if __name__ == "__main__":
    app()
