def get_filedata(filepath_arg=""):
    """get file data function help"""
    try:
        with open(filepath_arg, "r") as file:
            filedata = file.readlines()
            return filedata
    except FileNotFoundError as FNF:
        raise FNF


def write_filedata(filepath_arg="", todo_arg=None):
    if todo_arg is None:
        todo_arg = []
    try:
        with open(filepath_arg, "w") as file:
            file.writelines(todo_arg)
    except FileNotFoundError as FNF:
        raise FNF


def create_file(filepath_arg=""):
    try:
        with open(filepath_arg, "w") as file:
            pass
    except FileNotFoundError as FNF:
        raise FNF


if __name__ == "__main__":
    print("Executed from main !")