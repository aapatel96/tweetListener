import tweepy
import json
import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import logging
import json
import urllib


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

users = []



class listStatus:
    def __init__(self):
        self.list= None
        self.currentIndex = None
        self.mid = None

class User:
    def __init__(self,user_id):
        self.user_id = user_id
        self.listeners = []
        self.currentTrendList = []

consumer_key = 'ETijATNvEtYneYS68eYKixs5S'
consumer_secret = 'KGkf7Zqny4HtFZrLSUwJEdJXVRGF6uu1T9DQaoba5Ac8RljbtT'
access_token = '2871687840-Gp0JTqhqn19yvat7SAslLgAPDYEgXoScwqukRm2'
access_token_secret = 'AsrdusBscWazDV0F04bXXajm4xi4Nz9ZzjVE7eBvVBxWY'
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def find_user(users, user_id):
    for i in range(len(users)):
        if users[i].user_id == user_id:
            return users[i]

    return None
def html_decode(s):
    """
    Returns the ASCII decoded version of the given HTML string. This does
    NOT remove normal HTML tags like <p>.
    """
    htmlCodes = [
            ["'", '&#39;'],
            ['"', '&quot;'],
            ['>', '&gt;'],
            ['<', '&lt;'],
            ['&', '&amp;'],
            ['#','%23'],
            [' ','+'],
            ['!','%21'],
            ['"','%22']
        ]
    for code in htmlCodes:
        s = s.replace(code[1], code[0])
    return s

def start(bot, update):
    update.message.reply_text("Send me your location and I will send you twitter trends from your area")
    users.append(User(update.message.from_user.id))

def help(bot, update):
    update.message.reply_text('Send Location and I will tell you trends near you')

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def setLocation(bot,update):
    userfind = find_user(users,update.message.from_user.id)
    if userfind == None:
        update.message.reply_text("please send me the /start command and then resend your location")
        return
    lat = update.message.location.latitude
    longi = update.message.location.longitude
    location = api.trends_closest(lat,longi)
    print location
    WOEID = location[0]['woeid']
    trends = api.trends_place(WOEID)

    trendsList = trends[0]['trends']
    userfind.currentTrendList.list=trendsList
    userfind.currentTrendList.currentIndex=0
    userfind.currentTrendList.mid = update.message.message_id

    string = ''
    count = 0
    while count < 5:
    	string = string + html_decode(trendsList[count]['query'])+"\n"+trendsList[count]['url']+'\n'+"\n"
    	count = count + 1

    update.message.reply_text(string, disable_web_page_preview=True)
    with open('data.txt', 'w') as outfile:
   	    json.dump(trends, outfile)
    


def main():
    # Create the EventHandler and pass it your bot's token.
    TOKEN = "371083622:AAGfDVSKcz9fxoLIbXStsBXB__g_ZfmMbys"
    updater = Updater(TOKEN)
    PORT = int(os.environ.get('PORT', '5000'))
    # job_q= updater.job_queue

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.location,setLocation))




    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
    updater.bot.set_webhook("https://twittertrendsbot.herokuapp.com/" + TOKEN)
##    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    logger.warn('started')

    main()
