# TODO pip install beautifulsoup4, requests, lxml
from bs4 import BeautifulSoup
import time
import requests

#   TODO Set these variables
startPageNum = 1
endPageNum = 1
baseUrl = "https://www.nomorobo.com/lookup?page="
outputFileName = "ScammerNumbers.txt"

# w - will overwrite data in the file.
# a - will append the new data to the end of the file.
f = open(outputFileName, "w")
while startPageNum <= endPageNum:
    print("scanning page " + str(startPageNum))
    # This only works if there is a simple page counter in the url
    url = baseUrl + str(startPageNum)
    # Retrieves the page in text format
    page = requests.get(url).text
    # Sets the page up in BeautifulSoup
    soup = BeautifulSoup(page, 'lxml')

    # This for loop is where you will need to make changes depending on the content
    # that you wish to scrape from the webpage (arguably the most difficult part)
    # which will heavily depend on what webpage/content you are scraping.
    for number in soup.find_all('nobr'):
        # TODO
        f.write(number.text.strip() + "\n")

    print("page " + str(startPageNum) + " scanned successfully now sleeping 10 seconds...")
    startPageNum = startPageNum + 1
    # The sleep timer is to not stress out the web server on the other end, 10 seconds
    # is extremely conservative.
    time.sleep(10)
print("Successfully scanned " + str(startPageNum) + " pages")
f.close()
