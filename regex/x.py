import re

url = input('URL: ')

match = re.search(r'(?:https?://)?(?:www\.)?x\.com/([a-z0-9_]+)', url, re.IGNORECASE)
# username = re.sub(r'(https?://)?(www\.)?x\.com/', '@', url)
if match:
      print(f'Username:', match.group(1))