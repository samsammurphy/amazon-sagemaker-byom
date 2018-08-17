"""

Regex recap from: https://www.youtube.com/watch?v=sZyAn2TW7GY


Identifiers 

\   escape character
\d  any number
\D  anything but a number
\s  a space
\S  anything but a space
\w  any character
\W  anything but a character
.   any character, except newline
\b  whitespace around words
\.  a full stop

Modifiers

+      match 1 or more of something
?      match 0 or 1
*      match 0 or more of something
$      match the end of a string
^      match the beginning of a string
|      match something OR something else
[]     range
{x}    expecting x amount of something
{x, y} expecting between x and y amount

White Space Characters

\n  newline
\s  a space
\t  tab
\e  escape (rarely used)
\f  form feed (rarely used)
\r  return (rarely used)


DON'T FORGET

If you want to literally use any of these symbols..

. + * ? [ ] $ ^ () {} | \

then you will have to escape them (e.g. \., \+, etc.)


MORE ON RANGES

[A-Z] any capital letter
[a-z] any lower case letter
[1-5] any number between 1 and 5
[A-Za-z1-5] search for any of the above
"""

import re
import sys

def name_check(name):
    """
    Check container name will be valid

    Amazon ECR container name
    must satisy ^[a-zA-Z0-9](-*[a-zA-Z0-9])*

    Amazon ECR endpoint name
    dash '-' not allowed 

    Docker
    must be lower case
    """

    # lower case alpha numeric
    p = re.compile('[a-z0-9]+')

    m = p.match(name)

    if m:
      length = m.span()[1]
      if length == len(name):
        return f'The name "{name}" is valid'

    return f'The name "{name}" is NOT VALID !!!'