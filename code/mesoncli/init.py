#!/usr/bin/env python3

#
# Troglobyte stdlib:
# author: Michael Gene Brockus
# Gmail: <mail: michaelbrockus@gmail.com>
#
from pathlib import Path
import subprocess


class MesonInit:
    '''Meson init command wrapper class'''

    def __init__(self, srcdir) -> None:
        '''Constructors are used to initialize the
        object’s state. The task of constructors is to
        initialize(assign values) to the data members
        of the class when an object of class is created.

        In this case anything for the meson init
        command.
        '''
        super().__init__()
        self._srcdir: Path = srcdir
    # end of method

    def run(self, args: list = []):
        '''Should run the process of the current command
        which in this case is to generate a new project
        using Meson build systems tenplate generator.
        '''
        run_cmd = ['meson', 'init', '-C', str(self._srcdir)]
        run_cmd.extend(args)
        process = subprocess.Popen(run_cmd, encoding='utf8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process.communicate()[0]
    # end of method

# end class
