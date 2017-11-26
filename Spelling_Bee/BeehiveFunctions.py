#determine if the first is contained within the second
def subset(sub,super):
	for i in sub:
		if i not in super:
			return False
	return True

#center = input("Please enter central letter: ")

#checks input variable's length and type
#should probably make this generic typewise, but whatever
def valid_input(inputVar, length):
	if len(inputVar) == length:
		for i in inputVar:
			if len(i) == 1 and 97 <= ord(i) <= 122:
				pass
			else:
				return False	
	return True
#print(check_input(1,center))
#adds central letter to list of other letters
list1 = ['a']
list2 = ['b','c']
def concatenate_lists(addend1,addend2):
	addend2 += addend1
	return sorted(addend2)
	#return addend2

#print(concatenate_lists(list1,list2))
#concatenate_lists(list1,list2)
#print(list2)

#check full list against letter database, return list of 3-point words
def threes(DBdict,inputList):
	threesList = []
	for (key, value) in DBdict.items():
		if inputList == value:
			threesList.append(key)
	#print(threesList)
	return threesList

#use central letter and associated ones of that three to find ones
def ones(associated, central):
	onesList = []
	for i in associated:
		if central[0] in i:
			onesList.append(i)
	#print(onesList)
	return onesList

#in the event that there are no threes, this is used to serach the database for ones thr long way
def ones_no_threes(DBdict, inputList):
	onesList = []
	for (key, value) in DBdict.items():
		#if inputList == value:
		if subset(value, inputList):
			onesList.append(key)
	#print(threesList)
	return onesList