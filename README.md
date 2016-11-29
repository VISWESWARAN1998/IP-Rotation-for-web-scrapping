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

