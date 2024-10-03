#! python3
#searchpypi.py - Opens search results.

import webbrowser, bs4, sys, requests, logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


logging.debug('Start of the program')
print('Searching...')
res = requests.get('https://pypi.org/search/?=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
logging.debug('request is %(res)s')

#TODO: Retrieve top search result links.    
soup = bs4.BeautifulSoup(res.text, 'lxml')
logging.debug('Soup is retrieving top result')
#TODO: Open browser tab for each result
linkElems = soup.select('.package-snippet')
if linkElems == []:
    logging.critical('linkElems is empty')
numOpen = min(5, len(linkElems))
for link in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[link].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
logging.debug('End of program.')


