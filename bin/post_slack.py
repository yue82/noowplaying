# -*- coding: utf-8 -*-


def post_slack(text, workspace, channel, username, icon_emoji):
    import json
    import requests
    from utility import read_secrets, check_status

    secret_filename = '{}_slack_secret'.format(workspace)
    secrets = read_secrets(secret_filename)

    data = {
        'text': text,
        'channel': channel,
        'username': username,
        'icon_emoji': icon_emoji,
        'link_names': 1,
        }
    post_msg_url = 'https://slack.com/api/chat.postMessage'

    if 'bot_token' in secrets:
        data['token'] = secrets['bot_token']
        res = requests.get(post_msg_url, params=data)
    elif 'inhook_url' in secrets:
        res = requests.post(secrets['inhook_url'], data=json.dumps(data))
    elif 'legacy_token' in secrets:
        data['token'] = secrets['legacy_token']
        res = requests.post(post_msg_url, data=data)
    else:
        print('Secrets NG')
        return

    if check_status(res.status_code):
        print ('Status code OK: 200')
        try:
            res_text = json.loads(res.text)
            if res_text['ok']:
                return
        except json.JSONDecodeError as e:
            if res.text == 'ok':
                return

    print ('Response text: {}'.format(res.text))
