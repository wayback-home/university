import paramiko

# ssh host : 210.119.145.6, port : 80, username : uum06, pw : user1234
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect("210.119.145.6", 80, "uum06", "user1234")
# sin, sout, serr = client.exec_command("cal")
# sin, sout, serr = client.exec_command("cat /proc/cpuinfo")
sin, sout, serr = client.exec_command("cat /proc/meminfo")
print(sout.readline())
# for line in sout.readline():
#     print(line)


client.close()
