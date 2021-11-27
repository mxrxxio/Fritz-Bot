import xbox, os
from dotenv import load_dotenv

load_dotenv()

mail = os.getenv('mail')
password = os.getenv('password')

# print(mail, password)

xbox.client.authenticate(login = mail, password = password)

def get_gamerscore(gamertag):
    return xbox.GamerProfile.from_gamertag(gamertag).gamerscore
    
def get_pic(gamertag):
    return xbox.GamerProfile.from_gamertag(gamertag).gamerpic