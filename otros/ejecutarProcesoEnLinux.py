import shlex, subprocess

command_line = 'sudo apt-get update'
args = shlex.split(command_line)
subprocess.call(args)