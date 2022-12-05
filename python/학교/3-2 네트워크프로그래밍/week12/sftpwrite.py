import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect("210.119.145.6", 80, "uum06", "user1234")

sin, sout, serr = client.exec_command("pwd")
home_dir = sout.readline().strip()

sftp_client = client.open_sftp()
sftp_client.chdir(home_dir)

fd = sftp_client.open("welcome.txt", "w")
fd.writelines("welcome")


fd.close()
sftp_client.close()
client.close()
