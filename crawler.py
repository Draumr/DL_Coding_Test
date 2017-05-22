"""
URL Crawler

Use in browser:
localhost:5000/?url=<requested url>

example: localhost:5000/?url=http://www.google.com

"""
import urllib2
import time
from datetime import datetime
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup

global start_time, data
app = Flask(__name__)
start_time = time.time()
data = {}

data['page_title'] = ""
data['app_timer'] = 0
data['system_time'] = ""
data['requests_done'] = 0
data['link_counter'] = 0

@app.route("/", methods=['GET'])
def crawler():
    """Requests info from the given url
    :param:     url
    :return:    json dict"""

    url = request.args.get('url')

    try:
        handle = urllib2.urlopen(url)
        contents = handle.read()
        soup = BeautifulSoup(contents, 'lxml')
        data['found_links'] = []
        links = soup.find_all("a")
        for link in links:
            try:
                urllib2.urlopen(link.get("href"))
                data['found_links'].append(link.get("href"))
                data['link_counter'] += 1
            except:
                pass
        data['meta_data'] = []
        meta_data = soup.find_all("meta")
        for meta in meta_data:
            data['meta_data'].append(meta.get("content"))
        data['requests_done'] += 1
        data['page_title'] = soup.title.get_text()
        data['app_timer'] = round(time.time() - start_time, 2)
        data['system_time'] = datetime.utcnow().isoformat()
    except urllib2.HTTPError as error:
        return "%d: Requested URL is %s"%(error.code, error.msg)
    except BaseException as error:
        return "%s"%(error)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
