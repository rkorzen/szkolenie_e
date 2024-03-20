import sys
import re

pattern = re.compile("\d{2}-\d{3}")


text = "123-123 23-123 17-120 4544-455"


print(dir(pattern))
print(pattern.findall(text))