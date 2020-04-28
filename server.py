import subprocess
import threading
from os import system
from time import sleep


# Open new process opening bedrock_server.exe that pipes input and output here
process = subprocess.Popen('bedrock_server.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE)


# Allows for input from the console
def input_loop():
    while True:
        inp = input() + "\n"
        process.stdin.write(inp.encode())
        process.stdin.flush()


# Output from bedrock_server.exe
def output_loop():
    while True:
        for line in process.stdout:
            clean_line = line.decode("utf-8").rstrip("\n")
            print(clean_line)
            with open("log.txt", "a+") as log_file:
                log_file.write(clean_line)


# Backing up loop
def backup_loop():
    while True:
        to_type = "save hold\n"
        process.stdin.write(to_type.encode())
        process.stdin.flush()
        sleep(10)
        system("backup.bat")
        sleep(.75)
        to_type = "save resume\n"
        process.stdin.write(to_type.encode())
        process.stdin.flush()
        sleep(21600) # That's 6 hours


# Start the threads
_output = threading.Thread(target=input_loop)
_input = threading.Thread(target=output_loop)
_backup = threading.Thread(target=backup_loop)

_output.start()
_input.start()
sleep(15)
_backup.start()