import paramiko
import argparse

parser = argparse.ArgumentParser(prog="scp2.py")
parser.add_argument("-i", "--ip", required=True)
parser.add_argument("-t", "--type", choices=["l2r", "r2l"], required=True)

args = parser.parse_args()

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect(args.ip, args.port, args.user, args.password)

sftp_client = client.open_sftp()
sftp_client.chdir()


if args.type == "l2r":
    pass
else:
    pass


sftp_client.close()
client.close()
