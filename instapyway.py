import instapy
from instapy import InstaPy

user = ""
password = ""
gecko_path = "/media/buddhi/buddhiHDD/fiver/soclose/Insta_Scrapper/geckodriver"
userneedtoscrape = ""
#instapy uses this internally
session = InstaPy(username=user, password=password,geckodriver_path= gecko_path)
session.login()
followers = session.grab_followers(username=userneedtoscrape,amount=11000)
textfile = open('instapywayfollowers.txt', 'a+')


for element in followers:
    textfile.write(element + "\n")

session.end()
