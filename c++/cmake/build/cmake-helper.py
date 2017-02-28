
#!/usr/bin/python

import subprocess
import sys

commands = {
    'default' : ['cmake', '../project'],
    
    'debug': ['cmake', '-DCMAKE_BUILD_TYPE=Debug', '../project'],
    
    'release': ['cmake', '-DCMAKE_BUILD_TYPE=Release', '../project'],
    
    'eclipse': ['cmake', '-G',
                         'Eclipse CDT4 - Unix Makefiles',
                         '-DCMAKE_BUILD_TYPE=Debug',
                         '../project'],
    
    'eclipse-src': ['cmake', '-G',
                         'Eclipse CDT4 - Unix Makefiles',
                         '-DCMAKE_BUILD_TYPE=Debug',
                         '-DCMAKE_ECLIPSE_GENERATE_SOURCE_PROJECT=TRUE',
                         '../project']
}

if len(sys.argv) <= 1:
    subprocess.call(commands['default'])
    exit()

command = sys.argv[1];
if not command in commands:
    print('Bad argument(s)')
    exit()

# We have a valid command
subprocess.call(commands[command])
