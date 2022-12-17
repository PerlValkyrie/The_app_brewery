# Regex tutorial https://www.youtube.com/watch?v=AEE9ecgLgdQ

import re   # This is the built in module

pattern = re.compile('abcd')

match = pattern.match('abcd123')
print(match)

# Accessing the span of the match
print(type(match.span()))

# re.findall()
finders = pattern.findall('123abcd abcd123 abcd abcabc acb')
print(finders)
help(re.findall)

# re.search
random_string = '123 123 234 abcd abc'

search = pattern.search(random_string)
print(search)
span = search.span()
print(span)
print(random_string[span[0] : span[1]])