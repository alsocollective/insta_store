# from django.test import TestCase
import shopify

session = shopify.Session("shopify-birthday-suit.myshopify.com","b75c4c45ad21d7cf2d2528c0eca61bbf")
shopify.ShopifyResource.activate_session(session)
for page in shopify.Page.find():
	print page

exit()
# Create your tests here.
"""
path:/login/finalize/,
GET:<QueryDict: {u'shop': 
	[u'shopify-birthday-suit.myshopify.com'], 
	u'timestamp': [u'1423164953'], u'code': 
	[u'bd9498da7f4e705e34a278f0ad47d033'], 
	u'hmac': [u'75a09052531c7f3638e4bf14cfed4cd3f478178820d3c5f3bb85d7c4fbf40e82'], 
	u'signature': [u'b75c4c45ad21d7cf2d2528c0eca61bbf']}>,
POST:<QueryDict: {}>,
COOKIES:{'_ga': 'GA1.2.797033592.1412197245',
 'csrftoken': 'XJK5JrFmtFe6Rp5HPDRKFQbhZE9TC0pX',
 'sessionid': 'itvltcros9s4zq2jixr17x8c6om0xoai'},
META:{'CONTENT_LENGTH': '',
 'CONTENT_TYPE': 'text/plain',
 u'CSRF_COOKIE': u'XJK5JrFmtFe6Rp5HPDRKFQbhZE9TC0pX',
 'DJANGO_SETTINGS_MODULE': 'home.settings',
 'GATEWAY_INTERFACE': 'CGI/1.1',
 'HOME': '/home/bohdan',
 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, sdch',
 'HTTP_ACCEPT_LANGUAGE': 'en-US,en;q=0.8,et;q=0.6',
 'HTTP_CACHE_CONTROL': 'max-age=0',
 'HTTP_CONNECTION': 'keep-alive',
 'HTTP_COOKIE': '_ga=GA1.2.797033592.1412197245; sessionid=itvltcros9s4zq2jixr17x8c6om0xoai; csrftoken=XJK5JrFmtFe6Rp5HPDRKFQbhZE9TC0pX',
 'HTTP_HOST': 'shop.bohdananderson.com:8000',
 'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.94 Safari/537.36',
 'LANG': 'en_US.UTF-8',
 'LC_CTYPE': 'en_US.UTF-8',
 'LOGNAME': 'bohdan',
 'MAIL': '/var/mail/bohdan',
 'OLDPWD': '/srv/www',
 'PATH': '/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games',
 'PATH_INFO': u'/login/finalize/',
 'PWD': '/srv/www/shop.bohdananderson.com',
 
 'QUERY_STRING': '
 		code=bd9498da7f4e705e34a278f0ad47d033
 		&hmac=75a09052531c7f3638e4bf14cfed4cd3f478178820d3c5f3bb85d7c4fbf40e82
 		&shop=shopify-birthday-suit.myshopify.com
 		&signature=b75c4c45ad21d7cf2d2528c0eca61bbf
 		&timestamp=1423164953',

 'REMOTE_ADDR': '135.23.138.145',
 'REMOTE_HOST': '',
 'REQUEST_METHOD': 'GET',
 'RUN_MAIN': 'true',
 'SCRIPT_NAME': u'',
 'SERVER_NAME': 'vps.server.com',
 'SERVER_PORT': '8000',
 'SERVER_PROTOCOL': 'HTTP/1.1',
 'SERVER_SOFTWARE': 'WSGIServer/0.1 Python/2.6.6',
 'SHELL': '/bin/sh',
 'SHLVL': '1',
 'SSH_CLIENT': '135.23.138.145 59890 22',
 'SSH_CONNECTION': '135.23.138.145 59890 107.161.159.46 22',
 'SSH_TTY': '/dev/pts/0',
 'TERM': 'xterm-color',
 'TZ': 'UTC',
 'USER': 'bohdan',
 'XDG_SESSION_COOKIE': 'fc2d1933812ac0ddab9d2d8600003c16-1423157590.627980-340976253',
 '_': '/usr/bin/python',
 'wsgi.errors': <open file '<stderr>', mode 'w' at 0xb73d10d0>,
 'wsgi.file_wrapper': <class wsgiref.util.FileWrapper at 0x8cde17c>,
 'wsgi.input': <socket._fileobject object at 0x93029ec>,
 'wsgi.multiprocess': False,
 'wsgi.multithread': True,
 'wsgi.run_once': False,
 'wsgi.url_scheme': 'http',
 'wsgi.version': (1, 0)}>

"""