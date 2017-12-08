select count(Event.ID), YearGroup.Description, House.Description from Event, FormGroup, YearGroup, House where Event.EventTypeID = 1 and Event.FormGroupID = FormGroup.ID and  FormGroup.YearGroupID = YearGroup.ID and FormGroup.HouseID = House.ID group by YearGroup.ID, House.ID