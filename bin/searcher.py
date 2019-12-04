# -*- coding: utf-8 -*-


class ImageSearcher():
    url='https://www.googleapis.com/customsearch/v1'

    def __init__(self, secret_filename):
        from utility import read_secrets
        self.secrets = read_secrets('img_srch_secret')

    def search_image(self, query, img_size='large', require_field='link'):
        import requests
        import json
        from utility import check_status
        payload = {'key': self.secrets['key'],
                   'cx': self.secrets['cx'],
                   'searchType': 'image',
                   'num': 1,
                   'imgSize': img_size,
                   'q': query}
        res = requests.get(self.url, params=payload)
        if check_status(res.status_code):
            try:
                body = json.loads(res.text)
                if 'items' in body:
                    return body['items'][0][require_field]
                else:
                    return body
            except:
                return None
        return None
