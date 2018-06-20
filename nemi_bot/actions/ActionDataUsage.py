from rasa_core.actions import Action
from rasa_core.events import SlotSet

class ActionDataUsage(Action):
   def name(self):
      # type: () -> Text
      return "action_data_usage"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]

      cuisine = tracker.get_slot('cuisine')
      q = "select * from restaurants where cuisine='{0}' limit 1".format(cuisine)
      result = db.query(q)

      return [SlotSet("matches", result if result is not None else [])]