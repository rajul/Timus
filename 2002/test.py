n = int(raw_input())

users = {}

def handle_register(register_command):
	username = register_command[1]
	password = register_command[2]

	if username in users:
		return "fail: user already exists"
	else:
		users[username] = {'password': password, 'logged_in': False}
		return "success: new user added"

def handle_login(login_command):
	username = login_command[1]
	password = login_command[2]

	if username not in users:
		return "fail: no such user"
	else:
		user = users[username]

		if user['password'] != password:
			return "fail: incorrect password"

		if user['logged_in'] == True:
			return "fail: already logged in"
		else:
			users[username]['logged_in'] = True
			return "success: user logged in"

def handle_logout(logout_command):
	username = logout_command[1]

	if username not in users:
		return "fail: no such user"
	else:
		user = users[username]

		if user['logged_in'] == False:
			return "fail: already logged out"
		else:
			users[username]['logged_in'] = False
			return "success: user logged out"

for i in range(n):
	line = raw_input().strip().split()

	if line[0] == 'register':
		msg = handle_register(line)
	elif line[0] == 'login':
		msg = handle_login(line)
	elif line[0] == 'logout':
		msg = handle_logout(line)

	print msg