import requests, sys, json

token = None

try:
	with open("./.authtoken") as f:
		token = f.readline().strip()
		print("Found auth token: " + token)
		f.close()
except:
	print("Auth token not found. Aborting!")
	sys.exit(1)

# Search queries Yelp's API and returns a dict with the info.

class YelpFetcher():
	def __init__(self):
		global token
		self.authtoken = token

	def search(self, lat, lon, categories=[], price=[], isOpen=True, delivery=False):

		apiString = "https://api.yelp.com/v3/" + ("transactions/delivery/" if delivery else "businesses/") + "search?latitude=" + str(lat) + "&longitude=" + str(lon) + ("&categories=" + ",".join(categories) + "&price=" + ",".join(price) + "&is_open=" + str(isOpen).lower() if not delivery else "")
		print(apiString)
		request = requests.get(apiString, headers={'Authorization': self.authtoken})
		return json.loads(request.text)