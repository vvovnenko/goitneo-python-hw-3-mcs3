import functools
import types

COMMANDS = dict[str, types.FunctionType]()

class InvalidCommandError(Exception):
    pass


def get_handler(command: str):
    handler = COMMANDS.get(command)
    if handler is None:
        raise InvalidCommandError('Invalid command.')
    return handler

def command(name):
    """Register a function as a plug-in"""
    def register_command(func):
        COMMANDS[name] = func
        return func
    return register_command


def input_error(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f'Input error: {e}'
        except IndexError:
            return 'Incorrect index'
        except KeyError as e:
            return f'Incorrect key: {e}'

    return inner

@command(name='hello')
def hello(args) -> str:
    '''Just greet youself'''
    return 'How can I help you?'


class ExitProgram(Exception):
    pass


@command(name='exit')
@command(name='close')
def exit(*args, **kwargs):
    '''Exit from assistant'''
    raise ExitProgram('Good bye!')

@command(name='help')
def help(args):
    '''Show info about all commands'''
    lines = []
    for command, func in COMMANDS.items():
        lines.append('{:<20}:\t{}'.format(command, func.__doc__))
    return '\n'.join(lines)

@input_error
def execute_command(command: str, args: list[str]):
    return get_handler(command)(args)