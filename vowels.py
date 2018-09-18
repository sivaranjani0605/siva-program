h=raw_input()
if((h>'a'or h<'z')and(h>'A' or h<'Z')):
	if(h in ['a','e','i','o','u']):
		print("Vowels")
	else:
		print("consonant")
else:
	print("invalid")
