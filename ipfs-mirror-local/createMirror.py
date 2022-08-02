from bs4 import BeautifulSoup as bs
import os, shutil, json

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


posts = list(map(parsePost, posts))

if "media" not in os.listdir(f"mirror-{username}"):
    os.mkdir(f"mirror-{username}/media")

getImageId = lambda imgPath : imgPath.split("/")[-1].split(".")[0]


def copyImage(imgPath): 
    shutil.copyfile(f"account_info_download/{imgPath}", f"mirror-{username}/media/{getImageId(imgPath)}.jpg")


# Copy all relevant pictures
copyImage(profilePicPath)

for post in posts:
    for i in post["imgsPaths"]:
        copyImage(i)

accountDic = {
    "username": username,
    "bio": bio,
    "name": name,
    "profilePic": getImageId(profilePicPath) + ".jpg",
    "posts": []
}

for post in posts:
    print(post["caption"])
    accountDic["posts"].append({
        "caption": post["caption"],
        "timestamp": post["timestamp"],
        "imgs": list(map(lambda i : getImageId(i) + ".jpg",  post["imgsPaths"]))
    })

JSONText = json.dumps(accountDic)
open(f"mirror-{username}/info.json", "w").write(JSONText)