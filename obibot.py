import praw ,configparser,os
config = configparser.ConfigParser()

config.read('config.ini')

reddit = praw.Reddit(
    username=config['Api_keys']['username'],
    password=config['Api_keys']['password'],
    client_id=config['Api_keys']['client_id'],
    client_secret =config['Api_keys']['secret'],
    user_agent = 'Repost bot by u/Purple_scale_boi'
)
reddit.validate_on_submit =True
sub = reddit.subreddit(config['msc']['subreddit'])
bot =reddit.user.me().name
print(bot)

def main(bot):

    for comment in sub.stream.comments():
        if comment.author != bot:
            comment.reply('Hello There')
            print(f'commented on {comment.body}')
    
main(bot)