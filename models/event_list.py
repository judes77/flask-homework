from models.event import *

event1 = Event("18th September", "dog show", "30 humans and 10 dogs", "main hall", "afternoon event")
event2 = Event("19th September", "dachshund tea party", "30 humans and 12 dachshunds", "main hall and outside", "afternoon event") 
events = [event1, event2]

def add_new_event(event):
    events.append(event)
