import json

from flask import Flask, request, redirect, jsonify
import favicon
import redis
import json
from urllib.parse import urlparse

app = Flask(__name__)

rds = redis.Redis(host='localhost', port=6379, db=1)


def get_domain_from_url(url):
    parsed_uri = urlparse(url)
    return 'https://{uri.netloc}'.format(uri=parsed_uri)


def get_query_count():
    key = 'QUERY_COUNT'
    count = 1
    if rds.exists(key):
        count = int(rds.get(key))
    return count


def set_query_count():
    key = 'QUERY_COUNT'
    count = 1
    if rds.exists(key):
        count = int(rds.get(key))
        count += 1
    rds.set(key, count)
    return count


def get_icon_list_from_rds(key):
    if rds.exists(key):
        # print('cached')
        cashed = rds.get(key)
        js = json.loads(cashed)
        return js
    icons = favicon.get(key)
    # rds.set('url',icons,)
    icon_list = []
    for i in icons:
        data = {
            'url': i.url,
            'width': i.width,
            'height': i.height,
            'format': i.format
        }
        icon_list.append(data)
    js_str = json.dumps(icon_list)
    rds.setex(key, 86400, js_str)
    return icon_list


@app.route('/')
def hello_world():  # put application's code here

    return ('--------------------------- <br> '
            'Query count:' + str(get_query_count()) + '<br>'
                                                      '=========================== <br> '
                                                      'Baby Favicon Tool v1.0  \r\n<br> by:obaby \r\n <br><a href="https://oba.by" target="_blank">https://oba.by</a> <br>\r\r '
                                                      '<a href="https://h4ck.org.cn" target="_blank">https://h4ck.org.cn</a>')


# http://127.0.0.1:5000/api/get_favicon?url=https://h4ck.org.cn
@app.route('/api/get_favicon')
def search():
    query = request.args.get('url')
    if '.' not in query:
        return 'invalid url'
    if not query.startswith('http'):
        query = 'http://' + query

    icons = get_icon_list_from_rds(query)
    set_query_count()
    # icons_str = json.dumps(icons)
    return jsonify(icons)


@app.route('/api/redirect_favicon')
def redirect_icon():
    query = request.args.get('url')
    if '.' not in query:
        return 'invalid url'
    if not query.startswith('http'):
        query = 'http://' + query
    set_query_count()
    icons = get_icon_list_from_rds(query)
    try:
        icon_url = icons[0]['url']
    except:
        icon_url = 'https://h4ck.org.cn/wp-content/uploads/2024/09/favicon.png'
    return redirect(icon_url, code=302)


if __name__ == '__main__':
    app.run()
