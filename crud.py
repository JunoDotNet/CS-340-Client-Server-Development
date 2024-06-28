from pymongo import MongoClient

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Connection Variables
        HOST = 'localhost'
        PORT = 32152
        DB = 'AAC'
        COL = 'animals'

        # Initialize Connection
        self.client = MongoClient(HOST, PORT)
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        """
        Method to insert a document into the database.
        :param data: A dictionary containing the data to insert
        :return: True if insert was successful, else False
        """
        if data:
            result = self.collection.insert_one(data)
            return result.acknowledged
        else:
            raise ValueError("Data must be provided for insertion")

    def read(self, query):
        """
        Method to read documents from the database.
        :param query: A dictionary containing the query parameters
        :return: A list of matching documents
        """
        if query is not None:
            cursor = self.collection.find(query)
            return list(cursor)
        else:
            raise ValueError("Query must be provided for reading")

    def update(self, query, update_data):
        """
        Method to update documents in the database.
        :param query: A dictionary containing the query parameters to find the documents
        :param update_data: A dictionary containing the fields to update
        :return: The number of documents updated
        """
        if query is not None and update_data is not None:
            result = self.collection.update_many(query, {'$set': update_data})
            return result.modified_count
        else:
            raise ValueError("Query and update data must be provided for updating")

    def delete(self, query):
        """
        Method to delete documents from the database.
        :param query: A dictionary containing the query parameters to find the documents
        :return: The number of documents deleted
        """
        if query is not None:
            result = self.collection.delete_many(query)
            return result.deleted_count
        else:
            raise ValueError("Query must be provided for deleting")
