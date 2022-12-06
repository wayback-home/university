import paramiko
import os

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect("210.119.145.6", 80, "uum06", "user1234")


filepath = os.path.dirname(os.path.realpath(__file__))
os.chdir(filepath)


sftp_client = client.open_sftp()
sftp_client.chdir("/users/uum06")
sftp_client.put("./test.bin", "test-remote.bin")

sftp_client.get("test-remote.bin", "test-from-server.bin")

sftp_client.close()
client.close()
