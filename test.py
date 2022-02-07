from pymongo import MongoClient

class Conexion:

    def __init__(self, nombre):
        self.nombre = nombre

    def conectar(self):
        
        client = MongoClient('mongodb://localhost:27017')

        db = client['twitter']
        final = db['final']

        user = { "_id" : { "\$oid" : "5b0c115f5987f924300095ss3" }, "user_id" : "117660336", "name" : "Juan Amor�n", "screen_name" : "juan_amorin", "location" : "Ciudad Aut�noma de Buenos Aire", "description" : "Periodista en @eldestapeweb | Conductor de @cronicanunciada | Colaborador en @elcoheteluna <f0><U+009F><U+009A><U+0080>. \nHincha de #Banfield y devoto de @juliofalcioniDT.", "url" : "https://t.co/AbfRNaZxg5", "protected" : False, "followers_count" : 39537, "friends_count" : 735, "listed_count" : 160, "statuses_count" : 12822, "favourites_count" : 15319, "account_created_at" : { "$date" : 1267164459000 }, "verified" : True, "profile_url" : "https://t.co/AbfRNaZxg5", "profile_expanded_url" : "https://www.facebook.com/juann.amorin", "account_lang" : "es", "profile_banner_url" : "https://pbs.twimg.com/profile_banners/117660336/1498623917", "profile_background_url" : "http://abs.twimg.com/images/themes/theme1/bg.png", "profile_image_url" : "http://pbs.twimg.com/profile_images/945058314047643649/VUe7eEQP_normal.jpg" }

        # try:
        #     insertado = final.insert_one(user)
        #     print(insertado.inserted_id)
        # except ValueError:
        #   print("An exception occurred")

        actualizado = final.replace_one({'_id':{ "\$oid" : "5b0c115f5987f924300095ss3" }}, {"name":"bdm"})
        return final.find({"_id":{ "\$oid" : "5b0c115f5987f924300095ss3" }})

c = Conexion('conexion-1')
print(c.nombre)
print(c.conectar())