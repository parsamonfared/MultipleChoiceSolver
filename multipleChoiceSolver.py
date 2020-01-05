# import urllib
# from bs4 import BeautifulSoup
# import requests
# import webbrowser

# # q = input('question: ')
# # a = input('choices with cammas: ')
# # b = a.split(',')
# # dic = {}
# # for i in b:

# text = '“Using your own example of a context collapse, explain the importance of context using boyd & Nissenbaum.'
# text = urllib.parse.quote_plus(text)

# url = 'https://google.com/search?q=' + text

# response = requests.get(url)

# #with open('output.html', 'wb') as f:
# #    f.write(response.content)
# #webbrowser.open('output.html')

# soup = BeautifulSoup(response.text, 'lxml')
# for g in soup.find_all():
#     print(g.text)
#     print('-----')
import requests
from bs4 import BeautifulSoup
import re
from urllib.request import Request, urlopen

search = input("Search:")
results = 50 # valid options 10, 20, 30, 40, 50, and 100
page = requests.get("https://www.google.com/search?q={}&num={}".format(search, results))
soup = BeautifulSoup(page.content, "lxml")
links = soup.findAll("a")
bics = []
for link in links :
    link_href = link.get('href')
    if "url?q=" in link_href and not "webcache" in link_href:
        bics.append(link.get('href').split("?q=")[1].split("&sa=U")[0])
bics.pop()
bics.pop()
counter = 0

choice = input('choices: ')
choices = choice.split(',')
dcts = {}
for c in choices:
    dcts[c] = 0
for bic in bics:
    counter +=1
    req = Request(bic, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        beautiful = urlopen(req).read()
        soup = BeautifulSoup(beautiful, features="lxml")
        for script in soup(["script", "style"]):
            script.extract()    # rip it out
        text = soup.body.get_text()
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        texts = text.split(' ')
        print(len(texts))
        for word in texts:
            for d in dcts.keys():
                print(word)
                print(d)
                if d in word:
                    dcts[key]+=1
                 
    except:
        pass
    if counter == 1000:
        break
for d in dcts.keys():
    print(d+' : '+str(dcts[d]))
    