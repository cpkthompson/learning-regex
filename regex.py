# Matching numbers only: ^[0-9]+$
# ^[\d]+$

import re

with open('test.txt', 'r') as f:
    test_string = f.read()
    regex = re.compile(r'^([0-9]+)$', re.MULTILINE)
    result = regex.findall(test_string)
    # print(result)

# Matching years
# \b - Word boundary
# (19|20) - Matches either '19' or '20' using the OR (|) operand.
# \d{2} - Two digits, same as [0-9]{2}
# \b - Word boundary
# \s - explicit space character
# \b searches for a place where a word character is not followed or preceded by another word-character
# so it is searching for the absence of a word character
# \s is searching explicitly for a space character.
import re
import urllib.request
import operator

# Download wiki page
url = "https://en.wikipedia.org/wiki/Diplomatic_history_of_World_War_II"
html = urllib.request.urlopen(url).read()

# Find all mentioned years in the 20th or 21st century
regex = r"\b(?:19|20)\d{2}\b"
matches = re.findall(regex, str(html))

# Form a dict of the number of occurrences of each year
year_counts = dict((year, matches.count(year)) for year in set(matches))

# Print the dict sorted in descending order
# for year in sorted(year_counts, key=year_counts.get, reverse=True):
#   print(year, year_counts[year])


# Matching time
r'\b([01]?[0-9]|2[0-3]):([0-5]\d)\b'


# Matching date
# DAY/MONTH/Year
r'\b(0?[1-9]|[12]\d|3[01])([\/\-])(1[0-2]|0?[1-9])\2([19]|[20]\d{2})\b'

# ^ - Start of input
# [^@\s] - Match any character except for @ and whitespace \s
# + - 1+ times
# @ - Match the '@' symbol
# [^@\s]+ - Match any character except for @ and whitespace), 1+ times
# \. - Match the '.' character.
# \w{2,6} - Match any word character (letter, digit, or underscore), 2-6 times
# $ - End of input
r'^([^@\s])+@[^@\s]+\.\w{2,6}$'

# Extras
# \/ - Match / symbol (we have escape the / character)
# \*+ - Match one or more * symbols (again, we have to escape the * character with \).
# (.*) - Match any character (besides a newline \n), any number of times
# \*+ - Match one or more * characters
# \/ - Match closing / symbol.
r'(\/\*+)(.*)(\*+\/)'
