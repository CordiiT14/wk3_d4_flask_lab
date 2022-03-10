from models.event import Event
import datetime

event1 = Event(datetime.date(2022, 3, 10), "Project Presentation", 20, "codeclan 1", "Presentation of final projects from E56", False)

event_list = [event1,]

def add_new_event(event):
    event_list.append(event)


