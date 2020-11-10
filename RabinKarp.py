# Rabin Karp algorithm created in Python
# By Alejandro Carmona
# 11/9/2020

PRIME = 101


def createHash(s:str, end:int) -> int:
	hash = 0

	for i in range(end + 1):
		hash += (ord(s[i]) - ord('a') + 1) * pow(PRIME, i)

	return hash



def checkEqual(s:str, start1: int, end1: int, t: str, start2: int, end2:int):
	if end1 - start1 != end2 - start2:
		return False

	while(start1 <= end1 and start2 <= end2):
		if s[start1] != t[start2]:
			return False

		start1 += 1
		start2 += 1

	return True


def recalculateHash(s:str, oldIndex: int, newIndex: int, oldHash: int, patternLen: int) -> int:
	newHash = oldHash - (ord(s[oldIndex]) - ord('a') + 1)

	newHash = int(newHash/PRIME)
	newHash += (ord(s[newIndex]) - ord('a') + 1) * pow(PRIME, patternLen -1)

	return newHash

def rabinKarpSearch(text:str, pattern:str) -> int:
	if len(text) < len(pattern):
		return -1
	m = len(pattern)
	n = len(text)

	patterHash = createHash(pattern, m - 1)
	textHash = createHash(text, m -1)

	for i in range(1 ,n - m + 2):
		if patterHash == textHash and checkEqual(text, i - 1, i + m - 2, pattern, 0, m -1):
			return i - 1

		if i < n - m + 1:
			textHash = recalculateHash(text, i - 1, i + m - 1, textHash, m)


	return -1




s = 'abcabazy'
t = 'az'


print(rabinKarpSearch(s, t))

