# ====using os.system====
import subprocess
import os
os.system('ls')

# ====using subprocess.run====
subprocess.run(['ls'])
subprocess.run(["ls", "-l"])
subprocess.run(["ls", "-l", "readme.md"])


# ====retrieving system information====
command = 'uname'
commandArgument = '-a'
print(
    f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])


# ====retrieving information about disk space====
command = 'ps'
commandArgument = '-x'
print(
    f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])
