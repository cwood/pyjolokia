pyJolokia
================

This is a pure pyhon jolokia client. I moduled its usage after the javascript version.
Currently this will only support the protocol version 6. Also this was tested with python 2.7.
Not sure if it is Python3, or older than python 2.4.

Check the jolokia users guide for more information on how jolokia works. All options are available
on ``pyjolokia`` as joloka supports.

Check -> http://www.jolokia.org/reference/html/index.html for more information.

.. image:: https://travis-ci.org/cwood/pyjolokia.png?branch=master   
     :target: https://travis-ci.org/cwood/pyjolokia

Features
-------------

* Post Request
* Bulk Request
* Proxy Support
* Read, Write, List, Search, Exec, etc...

Setup
---------------

    $ python2.7 setup.py build
    $ python2.7 setup.py install

Examples
=====================

One Request
----------------

.. code-block:: python

    from pyjolokia import Jolokia
    # Enter the jolokia url
    j4p = Jolokia('http://localhost:8080/jolokia/')
    # Put in the type, the mbean, or other options. Check the jolokia users guide for more info
    # This then will return back a python dictionary of what happend to the request
    data = j4p.request(type = 'read', mbean='java.lang:type=Threading', attribute='ThreadCount')

Write Request
-------------------

.. code-block:: python

    from pyjolokia import Jolokia

    j4p = Jolokia('http://localhost:8080/jolokia/')
    j4p.request(type = 'write', mbean = 'java.lang:type=Memory', attribute = 'verbose', value='true')
    >> {u'request': {u'attribute': u'Verbose',
                     u'mbean': u'java.lang:type=Memory',
                     u'type': u'write',
                     u'value': u'true'},
        u'status': 200,
        u'timestamp': 1324256998,
        u'value': False}

Exec Request
-------------------------

.. code-block:: python

    from pyjolokia import Jolokia

    j4p = Jolokia('http://localhost:8080/jolokia/')
    j4p.request(type = 'exec', mbean='java.lang:type=Threading', operation='dumpAllThreads', arguments = [True, True])
    >> {u'request': {u'arguments': [True, True],
                     u'mbean': u'java.lang:type=Threading',
                     u'operation': u'dumpAllThreads',
                     u'type': u'exec'},
        u'status': 200,
        u'timestamp': 1324257601,
        u'value': [{u'blockedCount': 34,
                    u'blockedTime': -1,
                    ...

Search Request
--------------------------


.. code-block:: python

    from pyjolokia import Jolokia

    j4p = Jolokia('http://localhost:8080/jolokia/')
    j4p.request(type = 'search', mbean='java.lang:*')
    >> {u'request': {u'mbean': u'java.lang:*', u'type': u'search'},
        u'status': 200,
        u'timestamp': 1324257899,
        u'value': [u'java.lang:name=CMS Old Gen,type=MemoryPool',
                   u'java.lang:type=Memory',
                   u'java.lang:name=Code Cache,type=MemoryPool',
                   u'java.lang:type=Runtime',
                   u'java.lang:type=ClassLoading',
                   u'java.lang:name=ConcurrentMarkSweep,type=GarbageCollector',
                   u'java.lang:type=Threading',
                   u'java.lang:name=ParNew,type=GarbageCollector',
                   u'java.lang:type=Compilation',
                   u'java.lang:name=Par Eden Space,type=MemoryPool',
                   u'java.lang:name=CMS Perm Gen,type=MemoryPool',
                   u'java.lang:type=OperatingSystem',
                   u'java.lang:name=Par Survivor Space,type=MemoryPool',
                   u'java.lang:name=CodeCacheManager,type=MemoryManager']}


List Request
-----------------


.. code-block:: python

    from pyjolokia import Jolokia
    j4p = Jolokia('http://localhost:8080/jolokia/')
    j4p.request(type = 'list', path='java.lang/type=Memory')
    >> {u'request': {u'path': u'java.lang/type=Memory', u'type': u'list'},
                     u'status': 200,
                     u'timestamp': 1324258206,
        u'value': {u'attr': {u'HeapMemoryUsage': {u'desc': u'HeapMemoryUsage',
                                                  u'rw': False,
                                                  u'type': u'javax.management.openmbean.CompositeData'},
                                                  ...

Bulk Requsts
-----------------


.. code-block:: python

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

.. code-block:: python

    from pyjolokia import Jolokia
    j4p = Jolokia('http://localhost:8080/jolokia/')
    j4p.proxy(url = 'service:jmx:rmi://localhost:8080', user = 'SomeUser', password = 'somePassword')

    # Do normal requests here. All requests ill have the proxy info.
    ...

HTTP Basic Authentication
--------------------------

.. code-block:: python

    from pyjolokia import Jolokia
    j4p = Jolokia('http://localhost:8080/jolokia/')
    j4p.auth(httpusername='this', httppassword='that')

    # Do normal requests here. All requests ill have the proxy info.
    ...
