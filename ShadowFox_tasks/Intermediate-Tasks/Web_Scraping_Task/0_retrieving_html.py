import requests
url = "https://www.shadowfox.org.in/"
try:
    r = requests.get(url)
    # print(r.text)
    with open("file.html", "w", encoding="utf-8") as f:
        f.write(r.text)
    print("HTML saved successfully.")
except Exception as e:
    print("error retreiving the webpage: ",e)
