def get_todos(filepath = "todos.txt"):
    """Read a rext file and return list of to-do items"""
    with open(filepath, "r") as file:
        todos = file.readlines()
        return todos


def write_todos(todos_arg, filepath = "todos.txt"):
    """Write the todo items list in the file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
