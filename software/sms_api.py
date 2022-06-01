import configparser
import os
import requests

from requests.api import request

config = configparser.ConfigParser()
config.read('config.cfg')

SMS_API_KEY = os.environ.get('SMS_API_KEY') or config['DEFAULT']['SMS_API_KEY']

def send_sms(sender, phone, message):
	url = f'https://panel.smspoint.ee/gateway/{SMS_API_KEY}/api.v1/send?output=json'
	payload = {
		'sender': sender,
		'phone': phone,
		'message': requests.utils.quote(message)
	}
	return requests.get(url, params=payload).json()

if __name__ == '__main__':
	print(send_sms('CentarNIT', '38161', 'test again with url encoding :D'))