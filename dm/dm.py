#!/usr/bin/python3
"""Usage:
  dm [--option] <command> [<args>...]
  dm --help | -h
  dm --version | -v

Common options:
  -h --help                         Show this screen.
  -v --version                      Show version.
  -l --log=<level>                  Log level
  -s --server=<server>              host of DM server
  -p --port=<port>                  port of DM server
  -u --user=<login>                 Username of DM
  -p --password=<password>          Password of DM

Commands:
  clusters                          List of clusters
  cluster                           Cluster info
  nodes                             List of nodes by cluster
  bind                              Node-cluster binding
  containers                        List of containers by cluster
  container                         Container's operations
  images                            Images
  applications                      Applications management
  configuration                     Store configuration to specified file
  compose                           Run specified compose file

Examples:
  dm cluster --help
  dm cluster --cluster=dev
  dm job_update --cluster=firstCluster --image=ni1.codeabovelab.com/cluster-manager:latest --to_version=1.171 --strategy=stopThenStartAll
  dm create --cluster=firstCluster --tag=latest --image=com.navinfo.platform.opentsp-stub-core


Help:
  You can put any configs to dm.conf file
  For help using this tool, please open an issue on the Github repository:
  https://codeabovelab.com
"""

from inspect import getmembers, isclass

import sys
import os
from .lib.docopt import docopt
from . import commands as COMMANDS
from . import __version__ as VERSION

def main():
    ini_config = load_ini_config()

    args = sys.argv[1:]

    init_args_key = []
    for i in args:
        if '=' in i:
            init_args_key.append(i.split('=')[0])

    for key, value in ini_config.items():
        if key not in init_args_key:
            args.append(key + '=' + value)

    options = docopt(__doc__, version=VERSION, options_first=True)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.

    c = options['<command>']
    if hasattr(COMMANDS, c):
        module = getattr(COMMANDS, c)
        commands = getmembers(module, isclass)
        command = [command[1] for command in commands if command[0] != 'Base'][0]
        options = docopt(module.__doc__, argv=args)
        command = command(options)
        command.run()
    else:
        print("command not found:" + c)
        print(__doc__)


def load_ini_config():
    import configparser

    # By using `allow_no_value=True` we are allowed to
    # write `--force` instead of `--force=true` below.

    config = configparser.ConfigParser(allow_no_value=True) # Pretend that we load the following INI file:

    config_files = ['dm.conf', '/etc/dm.conf']
    config.read(config_files)

    # ConfigParsers sets keys which have no value
    # (like `--force` above) to `None`. Thus we
    # need to substitute all `None` with `True`.
    try:
        return dict((key, True if value is None else value)
                    for key, value in config.items('default-arguments'))
    except Exception as e:
        print("dm.conf was not found ", e)
        return {}


if __name__ == '__main__':
    main()
