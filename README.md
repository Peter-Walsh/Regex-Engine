# Regex-Engine
I made my own regular expression engine. It's not super fancy but I think it's kind of cool.

Note to self for now; The input has to be taken in the form "regex|string" or something like that with the "|" seperating the regular expression and the string. It only works with a few meta characters. There's no grouping or defining sets of characters or anything like that.

Meta characters:
  
  "$" Matches the end of the string\n
  "^" Matches the start of the string\n
  "?" Matches 0 or 1 of the preceding character\n
  "\*" Matches 0 or more of the preceding character\n
  "+" Matches 1 or more of the preceding character\n
  "." The wildcard operator works in here. Matches any character\n
  
  "\\" The escape sequence also works here to escape any of the other meta characters\n
