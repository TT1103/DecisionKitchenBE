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

with open("categories.json", "r") as file:
    b = json.load(file)
    parents = {}
    for i in b:
        for k in range(len(i["parents"])):
            parents.setdefault(i["parents"][k], [])
            parents[i["parents"][k]].extend([i["title"],i["alias"]])

# Search queries Yelp's API and returns a dict with the info.

class YelpFetcher():
	def __init__(self, aliases):
		global token
		self.authtoken = token
		self.aliases = aliases


	def search(self, lat, lon, price=[], isOpen=True, delivery=False):
		apiString = "https://api.yelp.com/v3/" + ("transactions/delivery/" if delivery else "businesses/") + "search?latitude=" + str(lat) + "&longitude=" + str(lon) + ("&categories=" + ",".join(self.aliases) + "&price=" + ",".join(price) + "&is_open=" + str(isOpen).lower() if not delivery else "")
		print(apiString)
		request = requests.get(apiString, headers={'Authorization': self.authtoken})
		return json.loads(request.text)


	def getLayered(self, json, string):
		layers = string.split(".")
		a = json
		for i in layers:
			try:
				a = a[i]
				print(a)
			except:
				return None
		return a

	def is_parent(self, given_category, potential_parent):
		try:
			for i in parents[potential_parent]:
				if given_category == i:
					return True
				else:
					if self.is_parent(given_category, i):
						return True
			return False
		except:
			return False


	def vectorize(self, json):
		# Vector format: [[American, Indian, Chinese, Sushi, Mongolian], Price, Rating, Rating_Count]
		# Return [business blob, vector]
		vector = []
		austin = []
		a = json["categories"]
		for i in self.aliases:
			for x in a:
				if (x["alias"] == i or self.is_parent(x["alias"], i)):
					austin.append(1)
					break
				if x == a[-1]:
					austin.append(0)
					break
		vector.append(austin)

		vector.append(json["price"].count("$"))
		vector.append(json["rating"])
		vector.append(json["review_count"])	
		return [json, vector]

	def vectors_nearest(self, lat, lon, full_data_bool):
		# Full_data_bool is a boolean stating whether you want all restaurant data or just the vector
		# Note that delivery/open is always bool set to true/false
		searching = self.search(lat, lon)
		values = []
		for i in searching["businesses"]:
			if full_data_bool:
				values.append(self.vectorize(i))
			else:
				values.append(self.vectorize(i)[1])
		return values



mine = YelpFetcher(["tradamerican", "indpak", "chinese", "sushi", "mongolian"])
print(mine.vectors_nearest(37.5737019, -122.3269701, False))