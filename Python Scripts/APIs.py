# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 21:31:21 2015

@author: Tommy Guan
"""

"""
Example 1: placekitten.com
"""

    from urllib2 import Request, urlopen, URLError
    
    request = Request('http://placekitten.com/')
    
    try:
    	response = urlopen(request)
    	kittens = response.read()
    	print(kittens[559:1000])
    except(URLError, e):
        print('No kittez. Got an error code:', e)

"""
Example 2
"""    
    from urllib2 import urlopen
    
    kittens = urlopen('http://placekitten.com/200/300')
    
    f = open('kittens.jpg', 'wb')
    f.write(kittens.read())
    f.close()

"""
Example 3: works for python 3
"""

    import urllib.request
    
    with urllib.request.open("http://placekitten.com") as kittens:
        response = kittens.read()
        body = response[559:1000]
    
    print(body)

"""
The Four HTML Verbs with REQUEST
"""
    """
    GET: retrieves information from the specified source.
    POST: sends new information to the specified source.
    PUT: updates existing information of the specified source.
    DELETE: removes existing information from the specified source.
    """
    import requests
    
    # Make a GET request here and assign the result to kittens:
    kittens = requests.get("http://placekitten.com")
    
    print(kittens.text[559:1000])
    
"""
Anatomy of a Request
"""
    """
    An HTTP request is made up of three parts:
    
    The request line, which tells the server what kind of request is being sent (GET, POST, etc.) and what resource it's looking for;
    The header, which sends the server additional information (such as which client is making the request)
    The body, which can be empty (as in a GET request) or contain data (if you're POSTing or PUTing information, that information is contained here).
    """
    ############ Request line #############
    # POST /learn-http HTTP/1.1
    
    ############## Header ################
    # Host: www.codecademy.com
    # Content-Type: text/html; charset=UTF-8
    
    ############### Body #################
    # Name=Eric&Age=26
    import requests

    body = {'Name': 'Eric', 'Age': '26'}
    
    # Make the POST request here, passing body as the data:
    response = requests.post("http://codecademy.com/learn-http/", data="body")
    
"""
status code
"""
    import requests
    
    response = requests.get('http://placekitten.com/')
    
    # Add your code below!
    print(response.status_code)    
    
    # print headers info
    ################## Example response ##########################
    # HTTP/1.1 200 OK
    # Content-Type: text/xml; charset=UTF-8
    
    # <?xml version="1.0" encoding="utf-8"?>
    # <string xmlns="http://www.codecademy.com/">Accepted</string>
    ##############################################################
    
    import requests
    response = requests.get("http://placekitten.com/")
    
    # print the header information from the response
    print(response.headers)
    
"""
Parsing XML
"""
    # pets.txt
    <pets>
      <pet>
        <name>Jeffrey</name>
        <species>Giraffe</species>
      </pet>
      <pet>
        <name>Gustav</name>
        <species>Dog</species>
      </pet>
      <pet>
        <name>Gregory</name>
        <species>Duck</species>
      </pet>
    </pets>
    
    # Parse data to get the names
    from xml.dom import minidom
    
    f = open('pets.txt', 'r')
    pets = minidom.parseString(f.read())
    f.close()
    
    names = pets.getElementsByTagName('name')
    for name in names:
    	print(name.firstChild.nodeValue)
     
    """
    Parsing JSON
    """
    import json
    from pprint import pprint
    
    f = open('pets2.txt', 'r')
    pets = json.loads(f.read())
    f.close()
    
    pprint(pets)