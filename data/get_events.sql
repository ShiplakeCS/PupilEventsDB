select count(Event.ID) as 'Count', Event.StaffID, staff.Code as 'Staff Code', EventType.Description from Event, Staff, EventType where EventTypeID = 1 and Staff.ID = Event.StaffID and Event.EventTypeID = EventType.ID group by StaffID ORDER BY count(Event.ID) DESC