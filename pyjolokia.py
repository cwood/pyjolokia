try:
    import json
except:
    import simplejson as json

try:
    import urllib2 as urllib
except ImportError:
    import urllib

try:
    from urllib2 import Request
except ImportError:
    from urllib.request import Request
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

import base64


class Jolokia:
    '''
        pyJolokia class Jolokia is a JSON featching python class.
        It uses urllib2 and json or simplejson to do post requests
        to a jolokia URL. Then returns back a python dictionary.

        .. code-block:: python

            j4p = Jolokia('http://localhost:9199/jolokia/')
            j4p.request(type = 'read', mbean = 'java.lang:type=Threading',
                        attribute = 'ThreadCount' )
            >> { 'status' : 200, ...
    '''
    def __init__(self, url, **kwargs):
        self.url = url
        self.data = None
        self.proxyConfig = {}
        self.authConfig = {}
        self.reqConfig = {}

        self.timeout = kwargs.get('timeout', 10)

    def auth(self, **kwargs):
        '''
            Used to add auth info if using jolokia via http to access the jmx

            example

            .. code-block:: python

                j4p.auth(httpusername='user',httppassword='password')

        '''
        self.authConfig['auth'] = {}
        if 'httpusername' in kwargs:
            self.authConfig['auth']['username'] = kwargs.get('httpusername')
        if 'httppassword' in kwargs:
            self.authConfig['auth']['password'] = kwargs.get('httppassword')

    def config(self, **kwargs):
        '''
            Used to set configuration options for the request
            see: http://www.jolokia.org/reference/html/protocol.html#processing-parameters

            example

            .. code-block:: python

                j4p.config(ignoreErrors=True)
        '''
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                self.reqConfig[key] = value

    def proxy(self, url, **kwargs):
        '''
            Used to add proxy info if using jolokia as a proxy to other
            java jmx apps.

            example

            .. code-block:: python

                j4p.proxy('service:jmx:rmi://somehost:1234/some.mbean.server',
                           user = 'cwood',
                           password = 'somePassword')

        '''
        self.proxyConfig['target'] = {}
        self.proxyConfig['target']['url'] = url
        if 'user' in kwargs:
            self.proxyConfig['target']['user'] = kwargs.get('user')
        if 'password' in kwargs:
            self.proxyConfig['target']['password'] = kwargs.get('password')

    def __getJson(self):
        if isinstance(self.data, dict):
            mainRequest = self.data.copy()
            mainRequest.update(self.proxyConfig)
        else:
            mainRequest = []
            for request in self.data:
                request = request.copy()
                request.update(self.proxyConfig)
                mainRequest.append(request)

        jdata = json.dumps(mainRequest).encode('utf-8')

        authheader = None

        if self.authConfig:

            if self.authConfig['auth']['username'] and self.authConfig['auth']['password']:

                authheader = base64.standard_b64encode(
                        ('%s:%s' % (
                            self.authConfig['auth']['username'],
                            self.authConfig['auth']['password']
                          )
                        ).encode()).decode()

        try:
            request = Request(self.url, jdata,
                              {'content-type': 'application/json'})

            if authheader:
                request.add_header("Authorization", 'Basic ' + authheader)

            responseStream = urlopen(request, timeout=self.timeout)
            jsonData = responseStream.read()
        except Exception as e:
            raise JolokiaError('Could not connect. Got error %s' % (e))
        finally:
            responseStream.close()

        try:
            pythonDict = json.loads(jsonData.decode())
        except:
            raise JolokiaError("Could not decode into json. \
                    Is Jolokia running at %s" % (self.url))
        return pythonDict

    def __mkrequest(self, type, **kwargs):
        newRequest = {}
        newRequest['type'] = type
        newRequest['config'] = self.reqConfig

        if type != 'list':
            newRequest['mbean'] = kwargs.get('mbean')
        else:
            newRequest['path'] = kwargs.get('path')

        if type == 'read':
            newRequest['attribute'] = kwargs.get('attribute')
            newRequest['path'] = kwargs.get('path')
        elif type == 'write':
            newRequest['attribute'] = kwargs.get('attribute', '')
            newRequest['value'] = kwargs.get('value', '')
            newRequest['path'] = kwargs.get('path', '')
        elif type == 'exec':
            newRequest['operation'] = kwargs.get('operation')
            newRequest['arguments'] = kwargs.get('arguments')
        return newRequest

    def request(self, type, **kwargs):
        if not isinstance(self.data, dict):
            self.data = {}
        self.data = self.__mkrequest(type, **kwargs)
        response = self.__getJson()
        return response

    def add_request(self, type, **kwargs):
        new_response = self.__mkrequest(type, **kwargs)
        if not isinstance(self.data, list):
            self.data = list()
        self.data.append(new_response)

    def getRequests(self):
        response = self.__getJson()
        return response


class JolokiaError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
