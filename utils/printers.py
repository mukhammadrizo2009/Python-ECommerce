from termcolor import colored


def print_status(text, status):
    status_map = {
        'error': 'red',
        'succes': 'green'
    }
    text = colored(text, status_map.get(status, 'red'))
    print(text)