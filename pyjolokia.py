try:
    import json
except:
    import simplejson as json

import urllib2

class Jolokia:
    def __init__(self, url):
        self.url = url
        self.data = None
        self.proxyConfig = {}
    def proxy(self, url, **kwargs):
        self.proxyConfig['target'] = {}
        self.proxyConfig['target']['url'] = url
        self.proxyConfig['target']['user'] = kwargs.get('user')
        self.proxyConfig['target']['password'] = kwargs.get('password')
    def __getJson(self):
        if isinstance(self.data, dict):
            mainRequest = dict(self.data.items() + self.proxyConfig.items())
        else:
            mainRequest = []
            for request in self.data:
                request = dict(request.items() + self.proxyConfig.items())
                mainRequest.append(request)
        jdata = json.dumps(mainRequest)
        request = urllib2.Request(self.url, 
                                  jdata, 
                                  {'content-type' : 'application/json'})
        responseStream = urllib2.urlopen(request)
        jsonData = responseStream.read()

        pythonDict = json.loads(jsonData)
        return pythonDict
    def __mkrequest(self, type, **kwargs):
        newRequest = {}
        newRequest['type'] = type

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
