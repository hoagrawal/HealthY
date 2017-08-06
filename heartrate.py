# -*- coding: utf8 -*-
from __future__ import print_function
import json
import requests
import config


def heartrate(user_id, period):
    # type: (object, object) -> object
    ''' (string,strig) -> string
	Fetches heart rate of given user id from fitbit api
	'''
    head = {"Authorization": "Bearer " + config.read_config("FITBIT_OAUTH_TOKEN")}
    api_base = "https://api.fitbit.com/1/user/"
    api = "/activities/heart/date/today/"
    get_request = (api_base + user_id + api + period + "d.json")
    r = requests.get(get_request, headers=head)
    resp = json.loads(r.content)
    print(json.dumps(resp))

heartrate("5T33PH","7")