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
    from pyjolokia.main import Jolokia
    # Enter the jolokia url
    j4p = Jolokia('http://localhost:8080/jolokia/')
    # Put in the type, the mbean, or other options. Check the jolokia users guide for more info
    # This then will return back a python dictionary of what happend to the request
    data = j4p.request(type = 'read', mbean='java.lang:type=Threading', attribute='ThreadCount')

