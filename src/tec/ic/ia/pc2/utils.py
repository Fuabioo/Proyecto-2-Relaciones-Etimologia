"""
Modulo utils
"""
import os
import platform
from datetime import datetime
from tec.ic.ia.pc2.data_structures import Graph


def hms_string(sec_elapsed):
    """
    Returns a time lapse
    """
    hours = int(sec_elapsed / (60 * 60))
    minutes = int((sec_elapsed % (60 * 60)) / 60)
    seconds = sec_elapsed % 60.
    return "{} h:{:>02} m:{:>05.2f} s".format(hours, minutes, seconds)


def format_path(path):
    """
    Formats a path to the following standart:
     - Divides directorys with / instead of \
     - Last character is /
     - If empty the its the current working directory
    """
    result = path
    if result == "":
        result = os.getcwd()
    result = result.replace('\\', '/')
    if result[-1] != '/':
        result = result + '/'
    return result


def check_folder(directory):
    """
    Checks if a folder exists, if not creates it
    """
    result = not os.path.exists(directory)
    if result:
        os.makedirs(directory)
    return result


def create_directory(directory):
    """
    Creates a directory with current time as name
    """
    folder = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    folder = folder.replace('-', '_')
    folder = folder.replace(':', '_')
    folder = folder.replace(' ', '-')
    folder = directory + folder
    check_folder(folder)
    return folder + '/'


def check_root(root_path, folders):
    """
    Checks if a root path has all the specified folders
    If a folder does not exist, it is created.
    Returns the amount of folders created (for debugging)
    """
    created_folders = 0
    for folder in folders:
        if check_folder(root_path + folder + '/'):
            created_folders += 1
    return created_folders


def load_input(filename: str):
    """
    Obtains a list of strings from the text file
    """
    result = []
    with open(filename, 'r') as file:
        result = file.readlines()
    return result


def get_adjacents(row, col, max_row, max_col):
    """
    Obtains the directions of the adjacent spaces
    """
    result = []
    up_row = row - 1
    left_col = col - 1
    down_row = row + 1
    right_col = col + 1
    if up_row >= 0:
        result.append((up_row, col))
    if left_col >= 0:
        result.append((row, left_col))
    if down_row < max_row:
        result.append((down_row, col))
    if right_col < max_col:
        result.append((row, right_col))
    return result


def get_end_line():
    """
    Obtains the endline based on the operative system
    """
    current_os = platform.system()
    result = ''
    if current_os == "Linux":
        result = '\n'
    elif current_os == "Windows":
        result = '\n'
    else:
        result = '\n'
    return result


def get_characters():
    """
    Obtains the valida character set
    """
    characters = {
        "bunny": 'C',
        "carrot": 'Z',
        "space": ' ',
        "end_line": get_end_line()}

    return characters


def parse_input_a_estrella(strings):
    """
    Obtains:
     (1) The positions of the carrots and the bunny
     (2) The graph corresponding to the board
    """
    characters = get_characters()

    result = {"bunny": (-1, -1), "carrot": []}
    graph = Graph()
    max_row = len(strings)
    max_col = len(strings[0]) - 1  # Discard EOL char

    for row in range(max_row):
        for col in range(max_col):
            if strings[row][col] != characters["end_line"]:
                adjacents = get_adjacents(row, col, max_row, max_col)
                node_key = (row, col)
                graph.add_node(node_key)
                for node in adjacents:
                    graph.add_edge(node_key, node)
                if strings[row][col] == characters["bunny"]:
                    result["bunny"] = node_key
                elif strings[row][col] == characters["carrot"]:
                    graph.nodes[node_key].carrot = True
                    result["carrot"].append(node_key)
            else:
                pass

    result["size"] = (max_col, max_row)
    return result, graph


def fill_string(max_col, max_row, c_position, z_positions):
    """
    Fills the board string
     - max_row: int rows size
     - max_col: int columns size
     - c_position: tuple position of the bunny
     - z_position: tuple positions of the carrots
    """
    characters = get_characters()
    result = ""
    for row in range(max_row):
        line = ""
        for col in range(max_col):
            if (row, col) == c_position:
                line += characters["bunny"]
            elif (row, col) in z_positions:
                line += characters["carrot"]
            else:
                line += characters["space"]
        line += characters["end_line"]
        result += line
    return result


def write_output_file(step, output_dir, enviroment, debug=False):
    """
    Writes the enviroment to a text file
    If debug is True it prints it on the console
    """
    filename = output_dir + str(step) + '.txt'
    string = fill_string(
        enviroment["size"][0],
        enviroment["size"][1],
        enviroment["bunny"],
        enviroment["carrot"])
    if debug:
        print(string)
    with open(filename, 'w') as file:
        file.write(string)


def print_console(step, scores):
    """
    Prints the step result in console
    """
    outs = ["IZQUIERDA", "DERECHA", "ARRIBA", "ABAJO", "MOVIMIENTO"]
    line = ""
    for key in outs:
        if key not in scores.keys():
            line += key + ": N/A "
        else:
            line += key + ': ' + str(scores[key]) + ' '

    print("PASO:", step, line)


def get_direction(src, dest):
    """
    Obtains the direction of a movement
    """
    direction = ""
    x_diference = dest[1] - src[1]
    y_diference = dest[0] - src[0]
    if x_diference == -1:
        direction = "IZQUIERDA"
    if x_diference == 1:
        direction = "DERECHA"
    if y_diference == -1:
        direction = "ARRIBA"
    if y_diference == 1:
        direction = "ABAJO"
    return direction


def get_node(src, direction):
    """
    Obtains the direction of a movement
    """
    dest = (-1, -1)
    down = (src[0] + 1, src[1])
    up = (src[0] - 1, src[1])
    right = (src[0], src[1] + 1)
    left = (src[0], src[1] - 1)
    if get_direction(src, down) == direction:
        dest = down
    if get_direction(src, up) == direction:
        dest = up
    if get_direction(src, right) == direction:
        dest = right
    if get_direction(src, left) == direction:
        dest = left
    return dest
