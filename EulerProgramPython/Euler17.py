from num2words import num2words
Words = ''
i = 1
while i <= 1000:
    Words = Words + num2words(i)
    i = i + 1
SpacelessWords = Words.replace(" ","")
SpacelessAndHyphenLessWords = SpacelessWords.replace("-","")


#print(SpacelessWords)
#print(SpacelessAndHyphenLessWords)
print(len(SpacelessAndHyphenLessWords)) 
    
