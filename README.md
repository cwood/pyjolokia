pyJolokia
================

This is a pure pyhon jolokia client. I moduled its usage after the javascript version.
Currently this will only support the protocol version 6. Also this was tested with python 2.7. 
Not sure if it is Python3, or older than python 2.4. 

Features
-------------

* Post Request
* Bulk Request
* Proxy Support
* Read, Write, List, Search is currenly working

TODO
-------------------

* Switch Between GET & POST Requests
* Add abilitie to manage requests
* Mimic simple api
* Manage bulk requests

Examples
=====================

One Request
----------------

    from pyjolokia import Jolokia
    # Enter the jolokia url
    j4p = Jolokia('http://localhost:8080/jolokia/')
    # Put in the type, the mbean, or other options. Check the jolokia users guide for more info
    # This then will return back a python dictionary of what happend to the request
    data = j4p.request(type = 'read', mbean='java.lang:type=Threading', attribute='ThreadCount')

Bulk Requsts
-----------------

    from pyjolokia import Jolokia
    # Enter the jolokia url
    j4p = Jolokia('http://localhost:8080/jolokia/')
    '''
        Put as many requests as you want. 
    '''
    j4p.add_request(type = 'read', mbean='java.lang:type=Memory')
    j4p.add_request(type = 'read', mbean='java.lang:type=Threading', attribute='ThreadCount')

    # Actull json request will be sent here
    bulkdata = j4p.getRequests()

Proxy Mode
------------------
    from pyjolokia import Jolokia
    j4p = Jolokia('http://localhost:8080/jolokia/')
    j4p.proxy(url = 'service:jmx:rmi://localhost:8080', user = 'SomeUser', password = 'somePassword')

    # Do normal requests here. All requests ill have the proxy info.
    ...
