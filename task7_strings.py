# String Processing & Traversal
sentence=input("Enter the sentence:")
vowel=0
consonant=0
digits=0
spaces=0
for i in sentence:
  if(i.lower() in 'aeiou'):
    vowel+=1
  elif(i.isdigit()):
    digits+=1
  elif(i.isspace()): # i==" "
    spaces+=1
  elif i.isalpha():
    consonant+=1
print("vowel:",vowel)
print("consonant:",consonant)
print("digit:",digits)
print("spaces:",spaces)

print(sentence.lower())
print(sentence.upper())
print(sentence.strip())


# 1. Why is string processing critical in cybersecurity and NLP?
# Cybersecurity often deals with textual data: passwords, logs, emails, network packets, scripts.
# String processing allows threats ,spam detection and filtering in text data.

# In NLP, it enables machines to understand, clean, and extract meaningful information from human language.
# converting into lowercases ,removing stop words ,spaces.
# Example: Chatbots, spam filters, search engines all rely on string processing.


# 2. How can improper string handling introduce vulnerabilities?

# Strings longer than expected overflow memory buffers.
# - Sql injection,command injection
