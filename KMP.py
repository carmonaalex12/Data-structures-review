# Algorith, for KMP search in python
# from geeks for geeks


def kmpSearch(pat:str, txt:str) -> int:
	m = len(pat)
	n = len(txt)

	#create longest prefix table to hold the length of the 
	#longest suffix. Looking for longest prefix that
	#is also a suffix

	lps = [0] * m
	j = 0 #pointer of the pattern 
	computeLPSArray(pat, m, lps) #compute the longest prefix array
	i = 0 #pointer for the text
	while i < n:
		if pat[j] == txt[i]:
			i += 1
			j += 1

		if j == m:
			return i - j

		elif i < n and pat[j] != txt[i]:
			if j != 0:
				j = lps[j-1]

			else:
				i += 1

	return -1

def computeLPSArray(pat:str, m:int, lps:List[int]) -> None:
	length = 0 # this holds the length of the longest suffix

	lps[0] = 0

	i = 1

	while(i < m):
		#if the char at i is equal to the one at the length of the 
		#longest prefix increase the length of it and add
		#it to the lps table
		if pat[i] == pat[length]:
			length += 1
			lps[i] = length
			i += 1

		else:
			#if chars don't match and length is not 0 then the length is the previous length
			#there might be a chance of a new prefix starting from pat[lps[length - 1]]
			if length != 0:
				length = lps[length - 1]


			#if length of prefix is 0 then in a way you gotta start again from the next index i
			else:
				lps[i] = 0
				i += 1