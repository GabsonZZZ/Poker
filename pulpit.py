def print_red(x)
def print_green(x)
def clear_line()

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')
