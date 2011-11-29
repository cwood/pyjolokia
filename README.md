pyJolokia
================

This is a pure pyhon jolokia client. I moduled its usage after the javascript version.

Features
-------------

* Post Request
* Bulk Request
* Proxy Support
* Read, Write, List, Search is currenly working

Example
----------------

One Request
++++++++++++++++++

    from pyjolokia.main import Jolokia
    # Enter the jolokia url
    j4p = Jolokia('http://localhost:8080/jolokia/')
    # Put in the type, the mbean, or other options. Check the jolokia users guide for more info
    # This then will return back a python dictionary of what happend to the request
    data = j4p.request(type = 'read', mbean='java.lang:type=Threading', attribute='ThreadCount')

Bulk Requsts
++++++++++++++++++++++

    from pyjolokia.main import Jolokia
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
+++++++++++++++++++++++++

    from pyjolokia.main import Jolokia
    j4p = Jolokia('http://localhost:8080/jolokia/')
    j4p.proxy(url = 'service:jmx:rmi://localhost:8080', user = 'SomeUser', password = 'somePassword')

    # Do normal requests here. All requests ill have the proxy info.
    ...
