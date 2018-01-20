original = raw_input('Enter a word:').lower()

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word+word[0]+'ay'
  new_word = new_word[1:len(new_word)]
  print new_word
else:
  print "Not proper input"
