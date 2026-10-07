import os


def move_file(command: str) -> None:
    command_elements = command.split()

    if len(command_elements) != 3 or command_elements[0] != "mv":
        return

    if "/" not in command_elements[2]:
        os.rename(command_elements[1], command_elements[2])
        return

    else:
        directories = command_elements[2].split("/")
        new_file_name = command_elements[1]
        if directories[-1]:
            new_file_name = directories.pop(-1)
        else:
            del directories[-1]

        checked_path = ""
        for dir_name in directories:
            checked_path += dir_name + "/"
            if not os.path.exists(checked_path):
                os.mkdir(checked_path)
        checked_path += new_file_name

        with (open(command_elements[1], "r") as file_in,
              open(checked_path, "w") as file_out):
            file_out.write(file_in.read())

        os.remove(command_elements[1])
