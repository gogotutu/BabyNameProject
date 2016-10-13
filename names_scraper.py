# Capital One Data Science Challenge Part 2
# Uses BeautifulSoup 4.3.2

from bs4 import BeautifulSoup
import requests
#import re

# Base URL of Behind the Name
url = "http://www.behindthename.com/names/"

# Output file to store the scraped data
file = open("NameOrigins.txt", 'a')

i = 1
# Loop until we processed all the pages
while(1):
    try:
        r = requests.get(url+str(i))
        print "Scraping %s, stay tuned..." % url+str(i)
        i += 1
    except requests.exceptions.HTTPError:
        print "Closing connection..."
        r = requests.post(url, headers={'Connection':'close'})
        break

    soup = BeautifulSoup(r.content)
    divs = soup.find_all('div', attrs={'class':'browsename'})
    if not divs:
        break

    for div in divs:
        name = div.b.string
        if not name:
            name = div.find('a').contents[0]
        name = name.encode('utf-8').lower().capitalize()

        s = div.find('a', attrs={'class':'usg'}).string
        # Remove (...) from s
        # s, _ = re.subn('\(.+\)', '', s)
        origins = s.strip().encode('utf-8').split(',')

        gender = []
        if div.find('span', attrs={'class':'masc'}):
            gender.append('M')
        if div.find('span', attrs={'class':'fem'}):
            gender.append('F')

        # Write to file
        for origin in origins:
            for g in gender:
                file.write(name.strip()+','+g+','+origin.strip()+'\r\n')
file.close()
