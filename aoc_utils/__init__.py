import colorama

def read_input(name):
    # Use a breakpoint in the code line below to debug your script.
    with open(
        f"input_{name}.txt", "r"
    ) as input_file:  # Press Ctrl+F8 to toggle the breakpoint.
        input_lines = input_file.readlines()

    return input_lines
def print_colored_text(text, color):
    colorama.init()
    print(color + text + colorama.Style.RESET_ALL)