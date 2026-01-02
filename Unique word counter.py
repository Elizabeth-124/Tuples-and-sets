sentence=input("Enter a sentence: ")
sentence=sentence.lower()
words=sentence.split()
unique_words=set(sentence)
print (f"Original wordcount: {sentence}")
print (f"unique wordcount:{words}")

