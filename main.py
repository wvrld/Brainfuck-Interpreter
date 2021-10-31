def find_parens(s):
	toret = {}
	pstack = []
	for i, c in enumerate(s):
		if c == '[':
			pstack.append(i)
		elif c == ']':
			if len(pstack) == 0:
				raise ValueError('errorrr')
			toret[pstack.pop()] = i
	if len(pstack) > 0:
		raise ValueError('unpaired brakets')
	return toret

def matchBracket(code, index): # the code index is 0 - based
	torit = find_parens(code) #torit is excactly the same as toret
	newTorit = {}
	for key, value in torit.items(): #make a new dictionary with key and value swapped
		newTorit[value] = key
	if code[index] == '[':
		return torit[index] #burrito / toret index is 0 - based
	elif code[index] == ']':
		return newTorit[index]



def Brainfrick(code, tapeLength):
	i = 0
	cells = [0 for i in range(tapeLength)]
	pointer = 0
	output = ''
	while i != len(code): #last character of code
		if code[i] == ',':
			print('One character of input needed')
			cells[pointer] = ord(input())
		if code[i] == '+':
			if cells[pointer] == 255:
				cells[pointer] = 0
			else:
				cells[pointer] += 1
		elif code[i] == '-':
			if cells[pointer] == 0:
				cells[pointer] = 255
			else:
				cells[pointer] -= 1
		elif code[i] == '>':
			if pointer == tapeLength - 1: pass
			else: pointer += 1
		elif code[i] == '<':
			if pointer == 0: pass
			else: pointer -= 1
		elif code[i] == '.':
			print('[' + 'C' + str(pointer) + ']' + ':' + str(chr(cells[pointer])))
			output += str(chr(cells[pointer]))
		elif code[i] == '[':
			if cells[pointer] == 0:
				i = matchBracket(code, i)  # jumps to the matching close braket
            # else/otherwise pointer is not 0, loops begins!
		elif code[i] == ']':
			if cells[pointer] != 0:
				i = matchBracket(code, i)
            #elif current cell is 0, keep going to the next slice of code
		i += 1
	
	print('\nOut\n' + str(output) + '\n\n')
	print('[', end = '')
	for x in range(tapeLength):
		if x == pointer:
			print('\033[4m' + str(cells[x]) + '\033[0m' + ',', end = '')
		else:
			print(str(cells[x]) + ',', end = '')
	print(']', end = ' ')

	
#Type code here:

code = '''

type brainfrick code here!
+++++++-+++<<<<><><<<<><><<>
'''



Brainfrick(code, 20)  # the 20 is the tapelength, you can change it if you want
