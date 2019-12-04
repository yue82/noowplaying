## require
- python3
- requests

## settings
- for [Google Custom Search](https://developers.google.com/custom-search)
  + write `key`(API key) and `cx`(search engine ID) to `secret/img_srch_secret`
- for Slack or Twitter
  + Slack: write `bot token` or `incoming webhooks url` (or `legacy token`) to `secret/default_slack_secret`
  + Twitter: write `CK` & `CS` & `AT` & `AS` to `secret/default_tw_secret`
- where post to
  + fix `bin/np` l.13-15
- `export PATH=$PATH;[this_repos]/bin`

## execute
```
$ np
to [tw]:  # push Enter or type slack workspace name
```
