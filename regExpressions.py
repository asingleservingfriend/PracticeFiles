import re

l = "Beautiful is better than ugly"

matches = re.findall("beautiful", l, re.IGNORECASE)

#print(matches)


#MATCH MULTIPLE CHARACTERS
string = "Two too"

m = re.findall("t[wo]o", string, re.IGNORECASE)
#print(m)

#MATCH DIGITS
line = "123?34 hello?"

d = re.findall("\d", line, re.IGNORECASE)
#print(d)

#NON GREEDY REPITITION MATCHING
# the quesiton mark makes the expression non-greedy. 

t= "__one__ __two__ __three__"
found = re.findall("__.*?__", t)
#print (found)

#ESCAPING
line2 = "I love $"
l = re.findall("\\$", line2, re.IGNORECASE)
#print(l)


#PRACTICE

txt="""
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

match = re.findall("Dutch", txt)
#print(match)

string2 = "Arizona 479, 501, 870. California 209, 213, 650"
dig = re.findall("\d", string2, re.IGNORECASE)
#print(dig)

sent = "The ghost that says boo haunts the loo"
doubla = re.findall("[bl]oo", sent, re.IGNORECASE)
print(doubla)
