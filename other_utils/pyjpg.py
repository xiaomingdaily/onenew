import requests
image = "https://scontent-lax3-1.cdninstagram.com/vp/d81c420f9647698ff66dc76dc602ca3c/5CF1F13C/t51.2885-15/sh0.08/e35/p750x750/47693060_232697267661981_656426224119109579_n.jpg?_nc_ht=scontent-lax3-1.cdninstagram.com"
ir = requests.get(image)
if ir.status_code == 200:
    open('logo.jpg', 'wb').write(ir.content)