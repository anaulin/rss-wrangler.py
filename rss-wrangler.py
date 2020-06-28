#!/usr/bin/env python3
"""
Do things with RSS feed.

To log into Mastodon:

1. For this script, as a client:
Mastodon.create_app(
     'rss-wrangler.py',
     api_base_url = 'https://social.coop'
     to_file = 'rss_wrangler_clientcred.secret'
)

2. For the specific Mastodon login to use:
mastodon = Mastodon(
    client_id = 'rss_wrangler_clientcred.secret'
    api_base_url = 'https://social.coop'
)
mastodon.log_in(
    'my_login_email@example.com',
    'incrediblygoodpassword',
    to_file = 'usercred.secret'
)
"""

import datetime
import feedparser
from mastodon import Mastodon

def toot(content):
    mastodon = Mastodon(access_token = 'usercred.secret', api_base_url = 'https://social.coop')
    mastodon.toot(content)

def wrangle(feed_url, max_age_mins=5):
    min_entry_age = datetime.datetime.now() - datetime.timedelta(minutes = max_age_mins)
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        if entry['published_parsed'] >= min_entry_age.timetuple():
            toot("I just published {}: {}".format(entry['title'], entry['link']))

if __name__ == '__main__':
    wrangle("https://anaulin.org/blog/index.xml")
