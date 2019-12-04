# -*- coding: utf-8 -*-


def get_twitter(secret_filename):
    from requests_oauthlib import OAuth1Session
    from utility import read_secrets

    secrets = read_secrets(secret_filename)
    twitter = OAuth1Session(secrets['CK'],
                            secrets['CS'],
                            secrets['AT'],
                            secrets['AS'])
    return twitter


def post_tweet(twitter, tweet, params={}):
    from utility import check_status
    post_url = 'https://api.twitter.com/1.1/statuses/update.json'
    data = {'status': tweet}
    if params:
        for key, value in params.items():
            data[key] = value
    res = twitter.post(post_url, params=data)

    if check_status(res.status_code):
        print ('Ok')
    else:
        print ('Error: {}'.format(res.text))


def upload_base64_img(twitter, data):
    import json
    from utility import check_status
    media_url = 'https://upload.twitter.com/1.1/media/upload.json'
    postdata = {'media_data': data}
    res = twitter.post(media_url, files=postdata)
    if check_status(res.status_code):
        try:
            body = json.loads(res.text)
            return body['media_id_string']
        except:
            return None
    return None


def post_image_tweet(twitter, tweet, data):
    media_id = upload_base64_img(twitter, data)
    if media_id:
        post_tweet(twitter, tweet, params={'media_ids': [int(media_id)]})
    else:
        print('No image')
        return
        post_tweet(twitter, tweet)
