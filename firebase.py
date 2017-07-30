import pyrebase
import YelpFetch

class FBData:
    def __init__(self, group):
        self.config = {
            "apiKey": "AIzaSyDtENByjPjjrXyoBWEr7Tr4to9ypS_EU38",
            "authDomain": "decisionkitchen.firebaseapp.com/",
            "databaseURL": "https://decisionkitchen.firebaseio.com/",
            "storageBucket": "decisionkitchen.appspot.com"
        }

        self.firebase = pyrebase.initialize_app(self.config)
        #self.firebase.auth().signInAnonymously()

        self.group = group
        self.db = self.firebase.database()

    def start(self):
        restraunts = self.db.child("groups").child(self.group).child("restaurants").get()
        sols = []
        if restraunts.val() != None:
            for i in restraunts.val().keys():
                mine = YelpFetch.YelpFetcher(['breakfast_brunch', 'chinese', 'diners', 'hotdogs', 'hotpot', 'italian', 'japanese', 'korean', 'mongolian', 'pizza', 'steak', 'sushi', 'tradamerican', 'vegetarian'])
                tmp=mine.search_ID(i)
                if tmp != None:
                    sols.append(mine.vectorize(tmp))

        response_base = self.db.child("groups").child(self.group).child("games").child("0").child("responses").get()
        money = []
        category = []
        deliv = []
        if response_base.val() != None:
            for i in response_base.val().values():
                money.append(i[0])
                category.append(i[1])
                deliv.append(i[2])

        for i in range(len(money)):
            curr = 0
            count = 0
            for k in zip(money[i], [1,2,3,4]):
                curr += k[0] * k[1]
                if k[0] != 0:
                    count += 1
            money[i] =  float(curr) / count
        money = sum(money) / len(money)

        #Deliv is still bad
        return sols, money, category, deliv
    # Fix authentication
    # only search good ids
    # add additional case for no categories

    def is_done(self, num_players):
        response_base = self.db.child("groups").child(self.group).child("games").child("0").child("responses").get()
        if response_base.val() == None:
            return False
        if len(response_base.val().keys()) >= num_players:
            return True
        else:
            return False

    def push_update(self, top_restaurants):
        data = {"The best restaurants in order:" : top_restaurants }
        self.db.child("groups").child(self.group).child("games").child("0").child("result").push(data)
        return True


#FBData("2120b04c-bd1e-42c8-abf1-08fd8fde8133").start()
#print(FBData().push_update([[i for i in range(20)] for k in range(20)]))