from bs4 import BeautifulSoup as bs
import os

# Gets the Personal Info file and turns it into a BeautifulSoup
personalInfoFileRaw = open('account_info_download/personal_information/personal_information.html').read()
personalInfoSoup = bs(personalInfoFileRaw, 'html.parser')

# Converts the info to a dict for processing
personalInfoRows = personalInfoSoup.find_all("tr")
personalInfoDic = {e[0]: e[1] for e in filter(lambda l : len(l) >= 2, map(lambda tr: [t.text for t in tr.find_all("td")], personalInfoRows))}

username = personalInfoDic.get('Username')
name = personalInfoDic.get("Name")
bio = personalInfoDic.get("Bio")
profilePicPath = personalInfoSoup.find(class_ = "pam").find("img")["src"]

if f"mirror-{username}" not in os.listdir():
    os.mkdir(f"mirror-{username}")

postsFileRaw = open('account_info_download/content/posts_1.html').read()
postSoup = bs(postsFileRaw, 'html.parser')

posts = postSoup.find_all(class_='pam')

def parsePost(post):
    imgsEls = post.find_all("img")
    imgsPaths = map(lambda im : im["src"], imgsEls)

    caption = post.find("div").text
    timestamp = post.find_all("div")[-1].text

    return {
        "imgsPaths": list(imgsPaths),
        "caption": caption,
        "timestamp": timestamp
    }


posts = map(parsePost, posts)


