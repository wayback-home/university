import paramiko
import argparse

parser = argparse.ArgumentParser(prog="scp.py")
parser.add_argument("-a", "--ip", required=True, help="IP address of remote system")
parser.add_argument("-p", "--port", required=True, help="Port of remote system")
parser.add_argument("-u", "--user", required=True, help="User of remote system")
parser.add_argument("-w", "--pw", required=True, help="Password of remote system")
parser.add_argument("sourcefile", help="source file")
parser.add_argument("targetfile", help="target file")
parser.add_argument("-t", "--type", required=True, choices=["r2l", "l2r"])
args = parser.parse_args()

print(args.ip, args.port, args.user, args.pw)


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect(args.ip, args.port, args.user, args.pw)


sftp_client = client.open_sftp()
sftp_client.chdir(f"/users/{args.user}")
if args.type == "r2l":
    sftp_client.get(args.sourcefile, args.targetfile)
else:
    sftp_client.put(args.sourcefile, args.targetfile)


sftp_client.close()
client.close()
