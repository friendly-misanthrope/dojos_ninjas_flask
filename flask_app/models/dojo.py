from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    db_name = "dojos_ninjas"

    def __repr__(self):
        return f"\nDojo Name: {self.name}\n"
    
    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos ( name ) VALUES ( %(name)s );"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db_name).query_db(query)

        dojos = []

        for dojo in results:
            dojos.append(cls(dojo))
        
        return dojos

    
    @classmethod
    def one_dojo_all_ninjas(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas on dojos.id = ninjas.dojo_id WHERE id = %(id)s;"

        results = connectToMySQL(cls.db_name).query_db(query, data)
        one_dojo = cls(results[0])
        
        for dojo in results:
            ninja = {
                "id": dojo['ninjas.id'],
                "first_name": dojo['first_name'],
                "last_name": dojo['last_name'],
                "age": dojo['age'],
                "created_at": dojo['ninjas.created_at'],
                "updated_at": dojo['ninjas.updated_at']
            }
        
        dojo.ninjas.append(Ninja(ninja))
        return one_dojo