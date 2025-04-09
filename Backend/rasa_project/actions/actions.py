from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionCourseScheduleBasedOnYear(Action):
    def name(self) -> str:
        return "utter_course_schedule_based_on_year"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain) -> list:
        year = tracker.get_slot("year")
        
        if year == "3":
            dispatcher.utter_message(text="Here is the course schedule for year 3.")
        elif year == "4":
            dispatcher.utter_message(text="Here is the course schedule for year 4.")
        elif year == "5":
            dispatcher.utter_message(text="Here is the course schedule for year 5.")
        else:
            dispatcher.utter_message(text="Sorry, I couldn't find the course schedule for that year.")

        return []
