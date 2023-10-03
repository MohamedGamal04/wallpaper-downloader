from bs4 import BeautifulSoup
import requests
import os
import random
import string
print("\nwelcome to wallpapers download program for https://wallhaven.cc soup\n")
while True:
    Random = 0
    multi=0
    User = input("Please enter a profile (If random leave it blank): ")
    if User == "":
        print(User.join(random.choices(string.ascii_letters + string.digits, k=6)))
        Random = 1
    while True:
        try:
            multi_check=input("Do u want to download multiple pages (Y,N)").upper()
            if multi_check=="Y":multi=1
            break
        except Exception: print("Please type Y or N")
    while True:
        try:
            PageNum = int(
                input("Please enter the page number (bigger than 0)\n"))
            break
        except:
            print("please enter a number bigger than 0")
    if Random == 0:
        url = f"https://wallhaven.cc/user/{User}/uploads?page={PageNum}"
    else:
        url = f"https://wallhaven.cc/random?seed={User}&page={PageNum}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    web_imgs = soup.find_all("img", {"class": "lazyload"})
    if web_imgs == []:
        print("Profile not found")
        continue
    print("Creating a wallpaper folder...")
    try:
        os.mkdir(os.path.dirname(os.path.realpath(__file__))+"\\wallpaper")
        print("done! the program will continue...")
    except Exception:
        print("folder already exist the program will continue...")
    for i in web_imgs:
        SmallImg = str(i)[46:-10]
        BigImg = SmallImg.replace("th", "w").replace("small", "full")
        BigImg = BigImg.replace(BigImg[31:], "wallhaven-"+BigImg[31:])
        print("link: "+BigImg)
        BigImg_url = requests.get(BigImg)
        if BigImg_url.status_code == 404:
            BigImg = BigImg.replace("jpg", "png")
        img = requests.get(BigImg).content
        WallpaperName = BigImg[41:-4]
        try:
            with open(fos.path.dirname(os.path.realpath(__file__))+"\\wallpaper\\wallpaper-{WallpaperName}.jpg", "r") as f:
                f.read(img)
        except FileNotFoundError:
            pass
        except TypeError:
            print("Wallpaper already downloaded...\n")
            continue
        with open(os.path.dirname(os.path.realpath(__file__))+f"\\wallpaper\\wallpaper-{WallpaperName}.jpg", "wb") as f:
            f.write(img)
        print(os.path.dirname(os.path.realpath(__file__))+f"wallpaper-{WallpaperName}.jpg completed...\n")
