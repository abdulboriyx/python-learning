def main():
      file_name = input('File Name: ').lower()
      get_file(file_name)
def get_file(dot):
      dot = dot.strip()

      if ('.jpeg' in dot or '.jpg' in dot):
            print('img/jpeg')
      elif ('.pdf' in dot):
            print('file/pdf')
      elif ('.zip' in dot):
            print('file/zip')
      elif ('.gif' in dot):
            print('img/gif')
      else:
            print('application/octet-stream')

main()
