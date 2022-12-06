import paramiko
import time

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect("210.119.145.6", 80, "uum06", "user1234")


sftp_client = client.open_sftp()
sftp_client.chdir(f"/users/uum06")

attrs = sftp_client.listdir_attr()
for attr in attrs:
    print("=" * 125)
    print(attr.longname)
    print(time.localtime(attr.st_atime))


sftp_client.close()
client.close()
