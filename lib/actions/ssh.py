import datetime
import os
import os.path
import re
import subprocess
import sys

class ActionClass:
    def __init__(self, evolve):
        extra_vars = evolve.get_extra_vars()

        command = [
            'ssh',
            '-i',
            os.path.join(evolve.ansible_path[0], 'files/ssh/id_rsa'),
            'deploy@%s.%s' % (extra_vars['stage'], evolve.group_vars['domain']),
        ]

        if evolve.arguments.command:
            command.append(evolve.arguments.command)
            try:
                evolve.call(command)
            except subprocess.CalledProcessError as err:
                evolve.announce(err)
        else:
            evolve.exec_process(command)