from datetime import datetime
import requests


def check_availability(url_str, datetime_fetched=None):
    """
    Use the web api to see if a page is available.

    https://archive.org/help/wayback_api.php
    """
    wayback_url = "http://archive.org/wayback/available"
    params = {
        'url': url_str.split('?')[0],
    }
    if datetime_fetched is not None:
        params['timestamp'] = datetime_fetched.strftime("%Y%m%d%H%M%S")

    response = requests.get(wayback_url, params=params, timeout=30)
    r_json = response.json()

    # let's be nice and convert the returned timestamp to a datetime obj
    # wayback timestamps are in the form YYYYMMDDhhmmss
    if "archived_snapshots" in r_json and \
       "closest" in r_json['archived_snapshots'] and \
       "timestamp" in r_json['archived_snapshots']['closest']:
           wb_timestamp = r_json['archived_snapshots']['closest']['timestamp']
           r_json['archived_snapshots']['closest']['datetime'] = datetime.strptime(wb_timestamp, "%Y%m%d%H%M%S")

    return r_json
