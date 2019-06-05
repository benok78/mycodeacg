#!/usr/bin/python3
"""Author ACAGatela || Learning Paramiko SSH"""

import os
import paramiko

SRVRS = [{'ip':'10.10.2.3', 'un':'bender'},{'ip':'10.10.2.4', 'un':'fry'}]

# commands are saved in a file and will be read one line at the site.
with open("cmds2issue.txt", "r") as cmds:
    CMDLIST = cmds.readlines()

def cmdissue(sshsession, commandtoissue):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(commandtoissue)
    return ssh_stdout.read().decode('utf-8').rstrip('\n')

def main():
    # harvest RSA key (ssh priv key)
    myprivkey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    for server in SRVRS:
        # init connection to remote machine
        sshsession = paramiko.SSHClient()
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshsession.connect(hostname=server['ip'], username=server['un'], pkey=myprivkey)

        # touch two files
        # get uptime of server
        for commandtoissue in CMDLIST:
            result = cmdissue(sshsession, commandtoissue)
            if result != "":
                with open(server['un'] + ".log", "a") as svrlog:
                    print("COMMAND ISSUED - ", commandtoissue.rstrip('\n'), file=svrlog)
                    print(result, file=svrlog)
                    print("", file=svrlog)

        # close connection
        sshsession.close()

if __name__ == '__main__':
    main()

