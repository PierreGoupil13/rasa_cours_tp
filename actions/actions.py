# Database Part
import sqlite3

import datetime
# This is a simple example for a custom action which utters "Hello World!"
import random
from typing import Any, Text, Dict, List
from datetime import datetime
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect('restaurant.db')
        self.cursor = self.conn.cursor()

    def create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor().execute("CREATE TABLE IF NOT EXISTS reservation(code INTEGER, date TEXT, num_people INTEGER)")

    def retrieve_entry(self, code):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM reservation WHERE code=?", (code,))
            return cursor.fetchone()

    def insert_entry(self, code, date, num_people):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor().execute("INSERT INTO reservation (code, date, num_people) VALUES (?, ?, ?)",
                                  (code, date, num_people))
            conn.commit()


class Reservation:
    def __init__(self, code, date, num_people):
        self.date = date
        self.code = code
        # self.name = None
        self.num_people = num_people
        # Add more attributes as needed

    def __str__(self):
        return f"Reservation details: Date={self.date}, Time={self.code}, Num People={self.num_people}"
        # Customize this method to return a string representation of the reservation object


class ActionNewReservation(Action):

    def name(self) -> Text:
        return "action_save_date_ask_number_people"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        db = Database("restaurant.db")
        db.create_table()

        date_rasa = tracker.get_slot("date")
        date_final = datetime.now().strftime('%Y-%m-%d')  # %H:%M:%S'
        response = f"Vous avez reservé pour : {date_final}"

        dispatcher.utter_message(text=response)

        return [SlotSet("date_convertie", date_final)]


class ActionGetPeople(Action):

    def name(self) -> Text:
        return "action_get_people_ask_confirmation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        number_of_people = tracker.get_slot("people")

        response = f"Vous avez reservé pour : {number_of_people} personne(s)"
        # Ask for the reservation date
        dispatcher.utter_message(text=response)

        return []


class ActionConfirmation(Action):

    def name(self) -> Text:
        return "action_ask_confirmation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        date = tracker.get_slot("date_convertie")
        people = tracker.get_slot("people")
        code = random.randint(1, 1000)

        db = Database("restaurant.db")
        db.insert_entry(code, date, people)

        response = (f"Vous avez reservé pour {people} personnes pour le {date}"
                    f", votre numero de reservation est le {code}")

        dispatcher.utter_message(text=response)

        return []


class AskReservationCode(Action):

    def name(self) -> Text:
        return "action_ask_reservation_code"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        code = int(tracker.get_slot("code"))
        db = Database("restaurant.db")
        result = db.retrieve_entry(code)
        reservation = Reservation(result[0], result[1], result[2])
        print(reservation)
        response = f"Je suis une demande de code! Voici votre code : {code}"
        dispatcher.utter_message(text=response)
        dispatcher.utter_message(text=reservation.__str__())

        return []


class TellMenu(Action):

    def name(self) -> Text:
        return "action_give_daily_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Je suis le menu!")

        return []


class GiveAllergens(Action):

    def name(self) -> Text:
        return "action_give_allergens"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Je suis une liste d'allergene")

        return []


class GiveAllMenu(Action):

    def name(self) -> Text:
        return "action_whole_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Je suis la carte")

        return []
