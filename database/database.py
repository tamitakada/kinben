import sqlite3
import random
import os

class Database:

    def __init__(self):
        self.db_setup()

    def get_db(self):
        return sqlite3.connect("database.db")

    def db_setup(self):
        db = self.get_db()
        c = db.cursor()

        command = """CREATE TABLE IF NOT EXISTS kanji (
            id          INTEGER PRIMARY KEY,
            yomi        TEXT NOT NULL,
            kanji       TEXT NOT NULL,
            example     TEXT NOT NULL
        );"""
        c.execute(command)

        db.commit()
        db.close()

    def generate_unique_id(self):
        db = self.get_db()
        c = db.cursor()

        item_id = 0
        items = True
        while items:
            item_id = random.randint(10000, 99999)
            command = "SELECT * FROM kanji WHERE id = ?"
            items = c.execute(command, (item_id,)).fetchone()

        db.close()
        return item_id

    """
        Returns 1 if word is found and edited.
        Returns 0 if word with specified id is not found.
    """
    def edit_word(self, id: int, yomi="", kanji="", example=""):
        word = self.find_word_by_id(id)
        if word:
            db = self.get_db()
            c = db.cursor()

            new_yomi = yomi
            new_kanji = kanji
            new_example = example

            if not yomi: new_yomi = word["yomi"]
            if not kanji: new_kanji = word["kanji"]
            if not example: new_example = word["example"]
            
            command = "UPDATE kanji SET yomi = ?, kanji = ?, example = ? WHERE id = ?"
            c.execute(command, (new_yomi, new_kanji, new_example, id))
            
            db.commit()
            db.close()
            
            return 1
        return 0

    """
        Returns 1 if word is added successfully.
        Returns 0 if word is duplicate (not added).
    """
    def attempt_add_word(self, yomi: str, kanji: str, example: str):
        db = self.get_db()
        c = db.cursor()
        
        if self.find_word(yomi, kanji): return 0

        id = self.generate_unique_id()

        command = "INSERT INTO kanji (id, yomi, kanji, example) VALUES (?, ?, ?, ?)"
        c.execute(command, (id, yomi, kanji, example,))

        db.commit()
        db.close()
        
        return 1
        
    def search_for_word(self, query: str):
        db = self.get_db()
        c = db.cursor()

        command = f"SELECT * FROM kanji WHERE yomi LIKE '%{query}%' OR kanji LIKE '%{query}%' ORDER BY yomi"
        words = c.execute(command).fetchall()

        db.close()
        
        all_word_tuples = []
        for word in words:
            all_word_tuples.append(self.word_tuple_to_dict(word))

        return all_word_tuples

    def find_word(self, yomi: str, kanji: str):
        db = self.get_db()
        c = db.cursor()

        command = "SELECT * FROM kanji WHERE yomi = ? AND kanji = ?"
        word = c.execute(command, (yomi, kanji)).fetchone()

        db.close()

        return self.word_tuple_to_dict(word)

    def find_word_by_id(self, id: int):
        db = self.get_db()
        c = db.cursor()

        command = "SELECT * FROM kanji WHERE id = ?"
        word = c.execute(command, (id,)).fetchone()

        db.close()

        return self.word_tuple_to_dict(word)

    """
        Converts word tuple returned from sql find to a dictionary format.
    """
    def word_tuple_to_dict(self, word):
        word_dict = {"id": word[0], "yomi": word[1], "kanji": word[2]}
        if len(word[3]) > 0: word_dict["example"] = word[3]
        elif len(word[4]) > 0: word_dict["example"] = word[4]
        return word_dict

    def get_random_word(self):
        db = self.get_db()
        c = db.cursor()

        command = "SELECT * FROM kanji ORDER BY RANDOM() LIMIT 1"
        word = c.execute(command).fetchone()

        db.close()

        return self.word_tuple_to_dict(word)
