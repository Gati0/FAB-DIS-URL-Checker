# Author: Gauthier AMPE
# This is a script to check every url in FAB-DIS file

import openpyxl, requests, click
from datetime import date 
from progress.bar import Bar
import os

@click.command()
@click.option('-f','--file', 'file', help="FAB-DIS file in xlsx format", type=str, required=True)
@click.option('-s','--sheet', 'sheet', help="Sheet name to check in FAB-DIS file", type=str, required=True)
@click.option('-c','--column', 'column', help="Column ID of url list to check", type=str, default="G")

def program(file, sheet, column):

  # Open file for write the http check result
  my_local_file = os.path.join(os.path.dirname(__file__), 'http_check_status.txt')
  daydate = date.today()
  f = open(my_local_file, 'a+')
  f.write('Check of file: {}, Date: {}'.format(file, daydate) + '\n')

  # Load the xlsx file with openpyxl
  print ("Loading file", file, "\n" "Please wait...")
  wb = openpyxl.load_workbook(file)
  print (file, "is loaded")
  ws = wb[sheet]

  # Keep single occurrence of each url in a list
  url_list= []
  for cell in ws[column]:
    if((cell.value is not None) and (cell.value != 'URL')):
        if cell.value in url_list:
            pass
        else:   
            url_list.append(cell.value)

  number_of_elements = len(url_list)

  print("Number of URL to check:", number_of_elements)

  bar = Bar('Processing', max=number_of_elements)

  # Check each url with get
  num_url_error = 0
  for url in url_list:
    try:
      status_code = requests.get(url, timeout=5).status_code
      if status_code != 200:
          f.write('url: {}, http_code: {}'.format(url, status_code) + '\n')
          num_url_error += 1
    except:
      f.write('Error on url: {}, impossible to check, this may be caused by a missing DNS'.format(url) + '\n')
      pass
    bar.next()
  bar.finish()
  print("Number of URLs in error:", num_url_error, "\n" "You can see the result in the file", my_local_file)

if __name__ == '__main__':
    program()