from tkinter import *
import tkinter as tk
import os
import tkinter.scrolledtext as st
import tweepy

# window
t = tk.Tk()
t.title('Twitter Crawler')
frame = Frame(t)
frame.pack()
f = ("Times bold", 25)
# Defining variables
vhash = StringVar()
tvar = StringVar()

# Taking USER input 
th = Label(frame, text = 'Enter Twitter Hashtag(include #):', font = f)
th.pack( side = TOP)
ui = Entry(frame, textvariable = vhash ,bd = 2)
ui.pack( side = TOP)

# Main code
def m_code():
	api_key = 'YOUR_API_KEY' 
	api_secret = 'YOUR_API_SECRET' 
	access_token = 'YOUR_ACCESS_TOKEN' 
	access_secret = 'YOUR_ACCESS_SECRET' 
	tweetsPerQry = 100
	maxTweets = 10000
	hashtag = vhash.get()
	authentication = tweepy.OAuthHandler(api_key, api_secret)
	authentication.set_access_token(access_token, access_secret)
	api = tweepy.API(authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
	maxId = -1
	tweetCount = 0
	while tweetCount < maxTweets:
		if(maxId <= 0):
			newTweets = api.search(q=hashtag, count=tweetsPerQry, result_type="recent", tweet_mode="extended")
		else:
			newTweets = api.search(q=hashtag, count=tweetsPerQry, max_id=str(maxId - 1), result_type="recent", tweet_mode="extended")

		if not newTweets:
			#print("Tweet End")
			break
		for tweet in newTweets:
			text_data = tweet.full_text.encode('utf-8')
			text_area.insert(tk.END, text_data)
			#print(tweet.full_text.encode('utf-8'))
		tweetCount += len(newTweets)
		tvar.set(tweetCount)	
		maxId = newTweets[-1].id

# Calling main code
tbutton = Button(frame, text='Search', fg='black', command = m_code)
tbutton.pack(side = TOP)
# Tweet count
tc = Label(frame, text = 'Tweet Count:')
tc.pack( side = TOP)
tcount = Label(frame, textvariable = tvar)
tcount.pack( side = TOP)
# Displaying data
text_area = st.ScrolledText(frame, width = 150, height = 35)
text_area.pack( side = BOTTOM)

t.mainloop()