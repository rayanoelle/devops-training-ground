import paramiko
import time
import getpass
#CONNECTING TO SSH 

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
password = getpass.getpass('Enter Password: ')
router = {'hostname':'192.168.40.37', 'port': '22', 'username':'admin', 'password': password}
ssh_client.connect(**router, look_for_keys= False, allow_agent=False)

#SENDING COMMANDS

shell = ssh_client.invoke_shell()
shell.send('show ip int br\n')
time.sleep(1)
output = shell.recv(10000)
output = output.decode('utf-8')
print(output)

#CLOSING CONNECTION

if ssh_client.get_transport().is_active() == True:
    print('closing connection')
    ssh_client.close() 