import os, re, requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv('/home/aarjav/Documents/Automation Programs/obsidian/api-key.env')

dirs = os.walk("/home/aarjav/Documents/Second Brain/")

token = os.environ.get("api-key")

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600'
    }

def Find(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]

for dir in dirs:
    for file in dir[2]:
        if ("workspace" not in file) and (not file.startswith(".")) and not(bool(list(x for x in [".obsidian", ".stfolder", ".stversions", ".trash"] if(x in dir[0])))) and ('.md' in file):
            if dir[0][-1] != "/":
                path = dir[0] + "/" + file
            else:
                path = dir[0] + file

            with open(path, "r") as f:
                mainContent = f.read()
                initContent = mainContent
                content = mainContent
            
            strToRemove = re.findall(r"\[.*]\(.*", content)
            strToRemove += re.findall(r"```[\s\S]*```", content)
            strToRemove += re.findall(r"<iframe[\s\S]*<\/iframe\>", content)

            # replace everything found in strToRemove with ""
            for i in strToRemove: content = content.replace(i, "")
            urls = Find(content)

            linkList = []

            for i in urls:
                #  Add i to linkDict as key
                linkList.append(i) if ("notion.vip" not in i) else None
            
            for enum, i in enumerate(linkList):
                response = requests.get(i)
                soup = BeautifulSoup(response.content, 'html.parser')
                
                try:
                    title = soup.find("meta", property="og:title").get('content')
                    siteName = soup.find("meta", property="og:site_name").get('content')
                    description = soup.find("meta", property="og:description").get('content')[:100]
                except:
                    try:
                        title = soup.find("meta", property="title").get('content')
                        siteName = soup.find("meta", property="site_name").get('content')
                        description = soup.find("meta", property="description").get('content')[:100]
                    except:
                        try:
                            response = requests.post(
                                "https://api.peekalink.io/",
                                headers={"X-API-Key": token},
                                data={"link": i},
                            )
                            title = response.json()['title']
                            siteName = response.json()['name'].split('.')[0].capitalize()
                            description = response.json()['description']
                        except:
                            print(i.split('/')[2], "couldn't be changed.")
                            continue

                if 'twitter' in i:
                    print(f'[{title} - {description}]({i})')
                    mainContent = mainContent.replace(linkList[enum], f'[{title} - {description}]({i})')
                    continue
                
                if siteName.lower() in title.lower():
                    print(f'[{title}]({i})')
                    mainContent = mainContent.replace(linkList[enum], f'[{title}]({i})')
                else:
                    print(f'[{title} - {siteName}]({i})')
                    mainContent = mainContent.replace(linkList[enum], f'[{title} - {siteName}]({i})')
            
            if initContent != mainContent:
                with open(path, "w") as f:
                    f.write(mainContent)