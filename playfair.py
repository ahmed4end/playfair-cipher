string = "BALLOON" 

key = "MONARCHY"

alphabet = iter( [chr(i) for i in range(65, 91) if chr(i) not in key and chr(i) != "J"])

#### i used dictionary to put the matrix each letter as a value holds coordinates as a key in dictionary  ex: {(0,0): 'M', ect...} ####
mat = {(i, j):((lambda x: list(key)[x] if x<len(key) else next(alphabet))(j+i*5)) for i in range(5) for j in range(5)}

#### splitting string into pairs ####
chunks, skip = [], False
for i,j in enumerate(string[:-1]):
	if skip:
		skip = False
		continue
	if string[i] != string[i+1]:chunks.append(string[i:i+2])
	else:     
		chunks.append(string[i]+"X")
		continue
	skip = True

#### (ds = dictionary search) special search engine for dicts by values only ####
ds = lambda value, dict=mat: list(dict.keys())[list(dict.values()).index(value)] 

#### encoding engine ####
result = []
for i in chunks:
	x, y = i[0], i[1]
	p1, p2 = ds(x), ds(y) #coordinates of the two letter in the mat.
	if ds(x)[1] == ds(y)[1]:   #same column case.
		x, y= mat[(p1[0]+1, p1[1])], mat[(p2[0]+1, p2[1])]
		result += [x, y]
	elif ds(x)[0] == ds(y)[0]: #same row case.
		x, y= mat[(p1[0], p1[1]+1)], mat[(p2[0], p2[1]+1)]
		result += [x, y]
	else:                      #different column and row case.
		x, y= mat[(p1[0], p2[1])], mat[(p2[0], p1[1])]
		result += [x, y]
print("".join(result))
