import time

def special_passwords(wordlist):
	numofspecials = input("Enter the NUMBER of words of importance to the target (words like sport name, food etc): ")
	
	for i in range(int(numofspecials)):
		baseword = input("Enter the %d word: " % (i + 1))
		count = 0
		wordlist = [baseword, baseword.title(), baseword.lower(), baseword.upper()]
		common_numbs = ["123", "456", "789", "111", "222", "333", "444", "555", "666", "777", "888", "999"]
		
		while count < 2500:
			wordlist.append(baseword.upper() + str(count))
			wordlist.append(baseword.lower() + str(count))
			wordlist.append(baseword.title() + str(count))
			wordlist.append(str(count) + baseword.upper())
			wordlist.append(str(count) + baseword.lower())
			wordlist.append(str(count) + baseword.title())
		
			if count < 12:
				wordlist.append(baseword.upper() + str(common_numbs[count]))
				wordlist.append(baseword.lower() + str(common_numbs[count]))
				wordlist.append(baseword.title() + str(common_numbs[count]))
				wordlist.append(str(common_numbs[count]) + baseword.upper())
				wordlist.append(str(common_numbs[count]) + baseword.lower())
				wordlist.append(str(common_numbs[count]) + baseword.title())
			
			count += 1
	return wordlist

def common_passwords(commonpw):
	name = input("Enter the name of the target: ")
	
	for i in range(2500):
		commonpw.append(name.upper() + str(i))
		commonpw.append(name.lower() + str(i))
		commonpw.append(name.title() + str(i))
		commonpw.append(str(i) + name.upper())
		commonpw.append(str(i) + name.lower())
		commonpw.append(str(i) + name.title())

	
	lastname = input("Enter target's last name: ")
	
	for j in range(2500):
		commonpw.append(name.upper() + lastname.upper() + str(j))
		commonpw.append(name.lower() + lastname.lower() + str(j))
		commonpw.append(name.title() + lastname.title() + str(j))
		commonpw.append(str(j) + name.upper() + lastname.upper())
		commonpw.append(str(j) + name.lower() + lastname.lower())
		commonpw.append(str(j) + name.title() + lastname.title())

	return commonpw


def personalized_passwords(personalizedpw):
	imp = input("Enter name of someone important to the target: ")
	
	for i in range(2500):
		personalizedpw.append(imp.upper() + str(i))
		personalizedpw.append(imp.lower() + str(i))
		personalizedpw.append(imp.title() + str(i))
		personalizedpw.append(str(i) + imp.upper())
		personalizedpw.append(str(i) + imp.lower())
		personalizedpw.append(str(i) + imp.title())


	choice = input("Do you want to add another important person? (yes/no): ")
	
	if choice == "yes":
		imp2 = input("Enter the name: ")
		for j in range(2500):
			personalizedpw.append(imp2.upper() + str(j))
			personalizedpw.append(imp2.lower() + str(j))
			personalizedpw.append(imp2.title() + str(j))
			personalizedpw.append(str(j) + imp2.upper())
			personalizedpw.append(str(j) + imp2.lower())
			personalizedpw.append(str(j) + imp2.title())


	else:
		print("okay")

	return personalizedpw

def favourite_passwords(fav):
	celeb = input("Enter target's favourite celebrity: ")
	cell = input("Enter target's cellphone number: ")
	fav.append(cell)

	for i in range(2500):
		fav.append(celeb.upper() + str(i))
		fav.append(celeb.lower() + str(i))
		fav.append(celeb.title() + str(i))
		fav.append(str(i) + celeb.upper())
		fav.append(str(i) + celeb.lower())
		fav.append(str(i) + celeb.title())

	return fav

def special_blend(resultlist):
	speciallist = []
	special_chars = ["-", "+", "@", "?", "!", "%", "&", "#", "$", "*", "^", "=", "."]
	count = 0

	while count < 13:
		for item in resultlist:
			speciallist.append(item)
			speciallist.append(item + special_chars[count])
			speciallist.append(special_chars[count] + item)
		count += 1

	return speciallist


if __name__ == "__main__":
	f = open("passwords.txt", "w+")
	wordlist = []
	commonpw = ["123456", "123456789", "qwerty", "password", "111111", "12345678", "abc123", "1234567", "password1", "12345"]
	personalizedpw = []
	fav = []
	resultlist = []
	a = special_passwords(wordlist)
	b = common_passwords(commonpw)
	c = personalized_passwords(personalizedpw)
	d = favourite_passwords(fav)

	for i in range(0, len(a)): 
		resultlist.append(a[i]) 

	for j in range(0, len(b)): 
		resultlist.append(b[j]) 

	for k in range(0, len(c)): 
		resultlist.append(c[k]) 

	for l in range(0, len(d)): 
		resultlist.append(d[l]) 

	e = special_blend(resultlist)

	start_time = time.time()

	for m in range(len(resultlist)):
	     f.write("%s\n" % (resultlist[m]))

	for n in range(len(e)):
	     f.write("%s\n" % (e[n]))

	f.close()
	print("File has been saved under the name 'passwords.txt' ")
	elapsed_time = time.time() - start_time
	print("%d passwords created! " %(len(resultlist) + len(e)))
	print("Time elapsed: " + str(elapsed_time))
	