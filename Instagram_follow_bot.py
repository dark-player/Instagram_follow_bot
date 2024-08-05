''' 
This script is made by lalit wagh
thanks to spooky community 
'''

from instabot import Bot
import getpass
import signal
import sys


def signal_handler(sig, frame):
    print('Exiting gracefully...')
    sys.exit(0)
  
signal.signal(signal.SIGINT, signal_handler)

def login_to_instagram(username, password):
    bot = Bot()
    bot.login(username=username, password=password)
    return bot

def follow_users(bot, name):
    users = bot.search_users(name)
    for user in users:
        username = user['username']
        full_name = user['full_name']
        print(f"Following {username} ({full_name})")
        bot.follow(username)

if __name__ == "__main__":
    username = input("Enter your Instagram username: ")
    password = getpass.getpass("Enter your Instagram password: ")
    
    bot = login_to_instagram(username, password)
    
    name_to_follow = input("Whom to follow? Enter the name: ")
    
    follow_users(bot, name_to_follow)
    
    print("Task completed.")
