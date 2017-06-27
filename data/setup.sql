/** Remove and create fresh EventType table **/
DROP TABLE IF EXISTS EventType;
CREATE TABLE EventType (ID INT PRIMARY KEY NOT NULL, Description TEXT NOT NULL);
/** Populate EventType table **/
INSERT INTO EventType (ID, Description) VALUES
(1, 'EXC'),
(2, 'INF');

/** Remove and create fresh House table **/
DROP TABLE IF EXISTS House;
CREATE TABLE House (ID INT PRIMARY KEY NOT NULL, Description TEXT NOT NULL);
/** Populate House table **/
INSERT INTO House (ID, Description) VALUES
  (1, 'Burr'),
  (2, 'Everett'),
  (3, 'Orchard'),
  (4, 'Skipwith'),
  (5, 'Welsh'),
  (6, 'Lower School');

/** Remove and create fresh YearGroup table **/
DROP TABLE IF EXISTS YearGroup;
CREATE TABLE YearGroup (ID INT PRIMARY KEY NOT NULL, Description TEXT NOT NULL);
/** Populate YearGroup table **/
INSERT INTO YearGroup (ID, Description) VALUES
  (1, 'Year 7'),
  (2, 'Year 8'),
  (3, 'Year 9'),
  (4, 'Year 10'),
  (5, 'Year 11'),
  (6, 'Year 12'),
  (7, 'Year 13');

/** Remove an create emoty Staff table **/
DROP TABLE IF EXISTS Staff;
CREATE TABLE Staff (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, StaffCode TEXT NOT NULL, Description TEXT);

/** Remove and create empty FormGroup table **/
DROP TABLE IF EXISTS FormGroup;
CREATE TABLE IF NOT EXISTS FormGroup (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Description TEXT NOT NULL, Size INTEGER, HouseID INT NOT NULL, YearGroupID INT NOT NULL);

/** Remove and create empty Event table **/
DROP TABLE IF EXISTS Event;
CREATE TABLE IF NOT EXISTS Event (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, EventTypeID INT NOT NULL, StaffID INT NOT NULL, FormGroupID INT NOT NULL);
