# rss-wrangler.py <!-- omit in toc -->

A Python script to parse an RSS feed, find any new (i.e. "newer than X time") items, and do things like cross-post links.

- [Installation](#installation)
- [One-time setup](#one-time-setup)
- [Running](#running)
- [Environment and dependencies setup](#environment-and-dependencies-setup)

## Installation

Requires Python 3.

Install dependencies with `pip` or `easy_install`:
```
pip install -r requirements.txt
```

## One-time setup

You will need to set up Mastodon credentials for the script to be able to post on your behalf. In a python3 shell, execute:
```python
# Replace this with the URL for the Mastodon instance you want to use
API_BASE_URL='https://mastodon.social'
# Replace with your actual login and password.
MASTODON_LOGIN='youremail@someplace.com'
MASTODON_PASSWORD='seekret'

Mastodon.create_app(
     'rss-wrangler.py',
     api_base_url = API_BASE_URL,
     to_file = 'rss_wrangler_clientcred.secret'
)
mastodon = Mastodon(
    client_id = 'rss_wrangler_clientcred.secret'
    api_base_url = API_BASE_URL
)
mastodon.log_in(MASTODON_LOGIN, MASTODON_PASSWORD,  to_file = 'usercred.secret')
```

## Running

To execute, run:
```
$ ./rss-wrangler.py
```

By default, it will post to Mastodon RSS entries that have a timestamp in the last 5 minutes. You can add this to your `crontab` to
run every 5 minutes, like so:
```
*/5 * * * * ./rss-wrangler.py
```

## Environment and dependencies setup

Create new virtual env:
```
python3 -m venv .venv
```

Activate virtual env:
```
source .venv/bin/activate
```

Install requirements:
```
pip install -r requirements.txt
```
