# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 15:44:49 2015

@author: Tommy Guan
"""

"""
Structure: Doesn't work in python 3 due to urllib2 change. Need to figure out.
"""
    import urllib, json
    
    url     = 'https://stage.wepayapi.com/v2/checkout/create'
    headers = {
               'Content-Type': 'application/json',
               'User-Agent': 'Codecademy WePay Demo',
               'Authorization': 'Bearer STAGE_df1684a1c7b91f0de51b72e5890891b92d34e47fb3cb48d4dbd8d2a89fa253cc'
              }
    params  = {
    		   'account_id': 161624111,
    		   'short_description': 'A brand new soccer ball',
    		   'type': 'GOODS',
    		   'amount': '24.95'
    		  }
    request = urllib.request.Request(url, json.dumps(params), headers)
    
    try:
    	response = urllib.request.urlopen(request, timeout=30).read()
    	print(json.loads(response))
    except urllib.error.HTTPError as e:
    	print(e)
     
"""
Using WePay Python SDK
"""

    from wepay import WePay
    wepay = WePay()
    wepay = WePay(access_token='STAGE_df1684a1c7b91f0de51b72e5890891b92d34e47fb3cb48d4dbd8d2a89fa253cc')
    response = wepay.call('/checkout/create', {
        'account_id': 161624111,
    	'short_description': 'A brand new soccer ball',
    	'type': 'GOODS',
    	'amount': '24.95'
    })
    
    print(response)