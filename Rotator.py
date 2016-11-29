# SWAMI KARUPPASWAMI THUNNAI

import json
import requests
class IP:
    __ipPort = ""
    __apiKey = ""
    __cookies = True
    __userAgent = False
    __https = False
    __protocol = ""
    __port = 0
    __country = ""
    __amazon = False
    __google = False
    __query = "http://gimmeproxy.com/api/getProxy?"
    __exhaust = 0
    def set_api(self,api):
        self.__apiKey = api
    def set_cookies(self,cookies):
        self.__cookies = cookies
    def is_user_agent(self,agent):
        self.__userAgent = agent
    def is_https(self,condition):
        self.__https = condition
    def set_protocol(self,protocol):
        self.__protocol = protocol
    def set_port(self,port):
        self.__port = port
    def set_country(self,country):
        self.__country = country
    def Amazon(self,amazon):
        self.__amazon = amazon
    def Google(self,google):
        self.__google = google
    def set_ip_port(self):
        if self.__apiKey != "":
            self.__query+"&api_key="+self.api_key
        if self.__cookies == False:
            self.__query+"&cookies=false"
        if self.__userAgent == True:
            self.__query+"&user-agent=true"
        if self.__https == True:
            self.__query+"&supportsHttps=true"
        if self.__protocol != "":
            self.__query+"&protocol="+self.__protocol
        if self.__port!=0:
            self.__query+="&port="+str(self.__port)
        if self.__country!="":
            self.__query+"&country="+self.__country
        if self.__amazon==True:
            self.__query+"&websites=amazon"
        if self.__amazon==True:
            self.__query+"&websites=google"
        return self.__query
    def get_ip(self):
        r = requests.get(self.__query).json()
        ip = r
        self.__ipPort = ip['ipPort']
        return self.__ipPort
    def get_exhaust(self):
        return self.__exhaust













