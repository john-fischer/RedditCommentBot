import praw
import bot_config
import time

def login():
	print ("Logging in...")
	r = praw.Reddit(client_id=bot_config.client_id,
				client_secret=bot_config.client_secret,
				user_agent="edgecrue:testbot1:0.0.1",
				username = bot_config.username,
				password=bot_config.password)
	print("Logged in!")
	return r
def run_bot(r):
	for comment in r.subreddit("testingground4bots").comments(limit=2):
		if "!wow" in comment.body:
			comment.reply("you better believe it")
if __name__ == "__main__":
	r = login()
	while True:
		run_bot(r)

