
def computePatternList(pattern):
	index = 0
	lookupArray = [0] * len(pattern)
	i = 1
	while i < len(pattern):
		if pattern[i] == pattern[index]:
			lookupArray[i] = index + 1
			index += 1
			i+=1
		else:
			if index != 0:
				index = lookupArray[index-1]
			else:
				lookupArray[i] = 0
				i+=1
	return lookupArray

def checkStringMatch(text, pattern):
	la = computePatternList(pattern)
	i,j = 0,0
	checkList = []
	while i<len(text) and j<len(pattern):
		if text[i]==pattern[j]:
			i+=1
			j+=1
		else:
			if j!= 0:
				j = la[j-1]
			else:
				i+=1
		if j == len(pattern):
			checkList.append(i-j)
			j=0
	print (checkList)
	if len(checkList) > 0:
		return True
#	if j == len(pattern):
#		return True
	return False

#print (computePatternList("aabaabaaa"))
#print (computePatternList("abcaby"))
#print (computePatternList("abcdabcy"))

print (checkStringMatch("abcxabcdabcdabcyabcxabcdabcdabcyabcxabcdabcdabcyabcxabcdabcdabcyabcxabcdabcdabcy","abcdabcy"))