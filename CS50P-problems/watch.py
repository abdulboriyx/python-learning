import re


def main():
      print(parse(input('HTML: ')))

def parse(link):
      
      youtube_link = re.search(r'^<iframe.*?src="(?:https?://)?(?:www\.)?youtube\.com(?:embed)?/(.+)"></iframe>', link)

      if youtube_link:
             url = youtube_link.group(1)
             return f"https://youtu.be/{url}"
      return None
      
if __name__ == '__main__':
      main()