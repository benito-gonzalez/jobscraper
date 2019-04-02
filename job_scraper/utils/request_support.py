from requests import get
from requests.exceptions import RequestException
from requests.exceptions import HTTPError
from contextlib2 import closing
from job_scraper.utils import log_support
from django.conf import settings
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def simple_get(url, accept_json=False):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    log_support.request_url(url)
    if accept_json:
        headers_req = {'User-Agent': 'Mozilla/5.0', 'accept': 'application/json'}
    else:
        headers_req = {'User-Agent': 'Mozilla/5.0'}

    with closing(get(url, stream=True, headers=headers_req, verify=False,  timeout=60)) as resp:
        if not settings.DEBUG:
            time.sleep(0.5)

        if resp.status_code == 200:
            return resp.content
        else:
            raise HTTPError("Invalid response from " + url + " HTTP %d" % resp.status_code)
