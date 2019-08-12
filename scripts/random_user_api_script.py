import urllib.request

for i in range(100):
	urllib.request.urlretrieve("https://randomuser.me/api/portraits/women/" + str(i) + ".jpg", str(i) + ".jpg")
