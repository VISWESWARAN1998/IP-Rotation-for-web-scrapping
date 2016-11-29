# IP-Roatation-for-web-scrapping


# Purpouse:
   At each request while scrapping you will end up with different IP address, This will prevent you getting backlisted
# How to use:

# First of all you must learn about 2 different accounts:

#Free:
  1. Optimum speed
  2. Maximum of 200 ips
# API:  More IP with High Speed

# How to use:

# use this import statement:

from Rotator import IP

settings = IP()

# setting API(If free usage leave this):
    settings.set_api("your api key")

# Disable cookies:
  settings.set_cookies(False)

# Set HTTPS support:
settings.is_https(True)

# Provide user agent support:
settings.is_user_agent(True)

# Set protocol http/socks5:
settings.set_protocol("http")

# You can set the port no too:
settings.set_port(portno)

# Sort IP's from specific country:
settings.set_country("US")       ==> This is give only Proxies from USA 

# If you have to scrape Amazon or Google then this setting will make it better:

settings.Amazon(True)
  (or)
settings.Google(True)


# once the indiviual settings is done then configure the ip settings:

settings.set_ip_port()

# To get the IP

IP address will be returned in string like ip:port

ip = settings.get_ip()

# Since free account is limited to 200 we can get how many ip's we have used by:

count = settings.get_exhaust()

# Example (getting IP with Port 80 only):

from Rotator import IP


settings = IP()


settings.set_port(80)


settings.set_ip_port()


for i in range(10):
   
   print(settings.get_ip())
    
    
#output:
xxx.52.176.129:80

xxx.80.21.109:80

xxx.88.67.83:80

xxx.52.72.58:80

120.xx.72.53:80

111.xx.109.27:80

124.xx.67.19:80

xxx.98.152.138:80

212.xx.21.109:80

177.221.42.xx:80

#Further note:

Proxies taken from http://gimmeproxy.com/




