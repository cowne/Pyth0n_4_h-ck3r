from pwn import *
import sys 

def exploit(hash_wanted, list):
	attempts = 0
	with log.progress("Attempts to hack: '{}' !\n".format(hash_wanted)) as p:
		with open(list, 'r', encoding='latin-1') as password_list:
			for password in password_list:
				password = password.strip('\n').encode('latin-1')
				password_hash = sha256sumhex(password)
				p.status("[{}] : {} = {}".format(attempts, password.decode('latin-1'), password_hash))
				if(password_hash == hash_wanted):
					p.success("The password found after {} attempts: {}".format(attempts,password.decode('latin-1')))
					exit()
				attempts += 1
			p.failure("Password not found!")

	
if __name__ == '__main__':
	try:
		hash_wanted = sys.argv[1].strip()
		word_list = sys.argv[2].strip()
	except IndexError:
		print("[x] Syntax error!")
		print("[>] Usage: %s <sha256> <wordlist>" %sys.argv[0])
		exit(0)

	exploit(hash_wanted, word_list)