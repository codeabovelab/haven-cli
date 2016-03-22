#!/usr/bin/python3
"""dm

Usage:
  dm containers --server=<server> --port=<port> --login=<login> --password=<password> [--verbose=<level>]
  dm --help | -h
  dm --version | -v

Options:
  -h --help                         Show this screen.
  -v --version                      Show version.
  -u --server=<server>              host of DM server
  -p --port=<port>                  port of DM server
  -l --login=<login>                Username of DM
  -p --password=<password>          Password of DM
  -r --verbose=<level>              Log level

Examples:
  dm hello

Help:
  You can put any configs to dm.conf file
  For help using this tool, please open an issue on the Github repository:
  https://codeabovelab.com
"""

from inspect import getmembers, isclass

import sys
from lib.docopt import docopt


def main():
    import commands
    ini_config = load_ini_config()
    conf_list = dictAsList(ini_config)
    options = docopt(__doc__, argv=list(sys.argv[1:] + conf_list), version='1.0')

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.

    for k, v in options.items():
        if hasattr(commands, k) and v:
            module = getattr(commands, k)
            commands = getmembers(module, isclass)
            command = [command[1] for command in commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()


def load_ini_config():
    import configparser

    # By using `allow_no_value=True` we are allowed to
    # write `--force` instead of `--force=true` below.

    config = configparser.ConfigParser(allow_no_value=True) # Pretend that we load the following INI file:
    config.read('dm.conf')

    # ConfigParsers sets keys which have no value
    # (like `--force` above) to `None`. Thus we
    # need to substitute all `None` with `True`.
    return dict((key, True if value is None else value)
                for key, value in config.items('default-arguments'))


def dictAsList(dict):
    dict_list = []
    for key, value in dict.items():
        dict_list.append(key)
        dict_list.append(value)
    return dict_list


if __name__ == '__main__':
    main()
