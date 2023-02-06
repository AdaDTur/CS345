"""
#### Problem 1.1
Input: 
```
ababababab
abb
bbabaa
bba
abbabb
```

Output:
```
abb
abbabb
```

Note: Do not use the regular expression which resembles `(word1|word2)` to handle each case individually. This defeats the purpose of the regular expression.
"""

import re

words = ["ababababab", "abb", "bbabaa", "bba", "abbabb"]
pattern = re.compile("abb")
for word in words:
  if pattern.match(word):
    print(word)

"""#### Problem 1.2
Input: 
```
abc
bc
ab
aabbcc
abbbbbbbb
ccbbaa
```

Output:
```
abc
ab
abbbbbbbb
```
"""

words = ["abc", "bc", "ab", "aabbcc", "abbbbbbbb", "ccbbaa"]
# write code
pattern = re.compile("abc*")
for word in words:
  if pattern.match(word):
    print(word)

"""#### Problem 1.3

Input: 
```
abc
abbbbbbbb
acc
abcbcbcbc
ac
xzzyyyyzyzzzz
accvvvvcvcccc
 ```

Output:
```
abc
abbbbbbbb
abcbcbcbc
```

Note: Use positive strings to define the regular expression.
"""

words = ['abc', 'abbbbbbbb', 'acc', 'abcbcbcbc', 'ac', 'xzzyyyyzyzzzz', 'accvvvvcvcccc']

# write code
pattern = re.compile("a*bc*")
for word in words:
  if pattern.match(word):
    print(word)

"""#### Problem 1.4

Input:
```
x. y
x?  Y
x! y
x y
x.  Y
x Y
xY
```

Ouput:
```
x. y
x?  Y
x! y
x.  Y
```

"""

words = ['x. y', 'x?  Y', 'x! y', 'x y', 'x.  Y', 'x Y', 'xY']

# write code
pattern = re.compile("x[.?!]")
for word in words:
  if pattern.match(word):
    print(word)

"""
#### Problem 1.5
Input:

```
<html class="client-nojs" lang="en" dir="ltr">
<table class="infobox biota" style="text-align: left; width: 200px; font-size: 100%">
<body class="ltr sitedir-ltr">
<div id="page-base" class="noprint">
<a id="top"></a>
```

Output:
```
tags:
html
table
body
div
a

keys:
class
lang
dir
style
id

values:
client-nojs; infobox biota; ltr sitedir-ltr; noprint
en
ltr
text-align: left; width: 200px; font-size: 100%
page-base; top
```

Note: For this question, your code must either use either the function [re.group()](https://docs.python.org/3/library/re.html#re.Match.group) or [re.findall()](https://docs.python.org/3/library/re.html#re.findall) to find tags, keys and values. Do not write a separate regular expression for each input line (i.e., your code has to make use of the same regular expression for each line). The output should be exactly as above. 
"""

import re
input_lines = ['<html class="client-nojs" lang="en" dir="ltr">', '<table class="infobox biota" style="text-align: left; width: 200px; font-size: 100%">', '<body class="ltr sitedir-ltr">', '<div id="page-base" class="noprint">', '<a id="top"></a>']

tags={}
keys={}
values={}

for line in input_lines:
  m = re.findall('(<([^\s]+) )|([^\s]+)=\"([^\"]+)\"', line)
  for group in m:
    tags[group[1]]=1
    if group[2] in keys and group[2] != '':
      keys[group[2]]+='; '+group[3]
    elif group[2] != '':
      keys[group[2]]=group[3]

print('tags:')
for key in tags.keys():
  if(key != ''):
    print(key)

print('\nkeys:')
for key in keys.keys():
  if(key != ''):
    print(key)

print('\nvalues:')
for key in keys.keys():
  print(keys[key])
