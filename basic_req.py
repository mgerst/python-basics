#!/usr/bin/env python
import requests

resp = requests.get('http://google.com')
print(resp.content)
