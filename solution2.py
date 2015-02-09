import socket, time
alpha = list("abcdefghijklmnopqrstuvwxyz")
host = "54.209.5.48"
port = 12345
def skip(text):
	for skip in range(len(text)):
		lists = []
		for i in range(skip):
			lists.append([])
			lists[i] = []
		for i in range(len(text)):
			for j in range(skip):
				if i % skip == j:
					lists[j].append(text[i])
		output = ""
		for i in lists:
			output += ''.join(i)
		if "challenge" in output:
			return output
def shift(string_in, by):
	string_out = ""
	for l in string_in:
		if l in alpha:
			x = (alpha.index(l) + by)%len(alpha)
			string_out += alpha[x]
		else:
			string_out += l
	return string_out
def select1(initial):
	for i in range(127):
		out = shift(initial, i)
		if "the" in out or "THE" in out:
			return out
def select2(initial):
	initial = str(initial)
	if "bogus" in initial or "tired" in initial or "making" in initial or " up " in initial:
		return "tired of making up bogus answers"
	if "this is" in initial or "is where" in initial or "where the" in initial or "answer goes" in initial:
		return "this is where the answer goes"
	if "easiest" in initial or "ist answ" in initial:
		return "easiest answer"
	if "more" in initial or "re answ" in initial or "ers here" in initial:
		return "more answers here"
	if "win" in initial or "for the" in initial:
		return "winning for the win"
	if "not" in initial or "wrong" in initial:
		return "not not wrong"
	else:
		return "x"
def get_sifer():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	time.sleep(.25)
	data = s.recv(1024)
	psifer = data[198:-1]
	results = str(select1(psifer))
	key = results[28:]
	key += "\n"
	s.send(key)
	time.sleep(.25)
	data = s.recv(1024)
	psifer = data[186:-1]
	results = skip(psifer)
	key = select2(results)
	key += "\n"
	s.send(key)
	time.sleep(.25)
	data = s.recv(1024)
	key = "magicwand"	#space?
	key += "\n"
	s.send(key)
	time.sleep(.25)
	data = s.recv(1024)
	s.close()
	return data
while 1:
	feedback = get_sifer()
	if "study more" not in feedback:
		print feedback
		break

#RESULT:
#OQ ICLQL WBRWL WQBZW HZJHW HWKWD APZWE KFVOA PHCHT EHDRJ AHYHJ A
#Congratulations, you have solved stage 3. The flag is: flag{IGraduatedPsiferSchoolAndAllIGotWasThisLousyFlag}.
