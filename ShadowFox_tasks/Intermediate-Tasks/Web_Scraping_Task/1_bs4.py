from bs4 import BeautifulSoup
import csv
with open("file.html", "r", encoding="utf-8") as f:
    html = f.read()
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())
print("Title tag: ", soup.title) #<title> The Dormouse's Story  </title>
print("Title tag name: ",soup.title.name) #u'title'
print("Title tag string: ",soup.title.string) #u'The Dormouse's story'
print("parent tag of the title: ", soup.title.parent.name) # u'head'
print("first paragraph tag: ",soup.p) # <p class="title"><b>The Dormouse's story</b></p>
print("class attribute of first paragraph: ",soup.p['class']) # u'title'
print("first anchor tag: ",soup.a) # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
print("all anchor tags: ",soup.find_all('a')) 
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
print("tags with id=link3: ",soup.find(id="link3")) # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# data extraction for storage
links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        links.append(href)
#Save data
try :
    with open("links.csv", "w", newline ="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Links"])
        for l in links:
            writer.writerow([l])
    print("data saved to link.csv.")
except Exception as e:
    print("Error saving CSV: ",e)
