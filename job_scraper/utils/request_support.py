from requests import get
from requests.exceptions import RequestException
from contextlib2 import closing
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from job_scraper.utils import log_support


def simple_get(url, accept_json=False):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    log_support.request_url(url)
    try:
        if accept_json:
            headers_req = {'User-Agent': 'Mozilla/5.0', 'accept': 'application/json'}
        else:
            headers_req = {'User-Agent': 'Mozilla/5.0'}

        with closing(get(url, stream=True, headers=headers_req, verify=False)) as resp:
            if resp.status_code == 200:
                return resp.content
            else:
                log_support.set_invalid_response(url, resp.status_code)
                return None

    except RequestException as e:
        log_support.set_invalid_request(url, e)
        return None
