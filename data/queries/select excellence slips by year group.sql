select count(Event.ID), YearGroup.Description from Event, FormGroup, YearGroup where Event.EventTypeID = 1 and Event.FormGroupID = FormGroup.ID and  FormGroup.YearGroupID = YearGroup.ID group by YearGroup.ID