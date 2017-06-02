#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy
import json
import telegram
import time

class User:
    def __init__(self,user_id):
        self.user_id = user_id
        self.listeners = []





consumer_key = 'ETijATNvEtYneYS68eYKixs5S'
consumer_secret = 'KGkf7Zqny4HtFZrLSUwJEdJXVRGF6uu1T9DQaoba5Ac8RljbtT'
access_token = '2871687840-Gp0JTqhqn19yvat7SAslLgAPDYEgXoScwqukRm2'
access_token_secret = 'AsrdusBscWazDV0F04bXXajm4xi4Nz9ZzjVE7eBvVBxWY'
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def start(bot, update):
    update.message.reply_text("Send me your location and I will send you twitter trends from your area")
    users.append(User(update.message.from_user.id))


def setListener(bot,update):
	userfind = find_user(update.message.from_user.id)
	if userfind == None:
		update.message.reply_text("please press /start and then resend info")
		return

	lat = update.message.location.latitude
	longi = update.message.location.longitude
	location = api.trends_closest(lat,longi)
	WOEID = location[0]['woeid']
	trends = api.trends_place(WOEID)

    print trends





def main():
    # Create the EventHandler and pass it your bot's token.
    TOKEN = "371083622:AAGfDVSKcz9fxoLIbXStsBXB__g_ZfmMbys"
    PORT = int(os.environ.get('PORT', '5000'))
        updater = Updater(TOKEN)


    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.location, setListener))

    dp.add_handler(CommandHandler("help", help))


    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
##    updater.start_webhook(listen="0.0.0.0",
##                      port=PORT,
##                      url_path=TOKEN)
##    updater.bot.set_webhook(heroku_url + TOKEN)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
'''
for i in range(len(trends1[0]['trends'])):
	print trends1[0]['trends'][i]
	print ('\n')
'''

