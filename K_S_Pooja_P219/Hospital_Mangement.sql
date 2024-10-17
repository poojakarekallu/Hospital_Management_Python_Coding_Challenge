create DATABASE Hospital_Management;

use Hospital_Management;

CREATE TABLE Patient(
    patientId varchar(5) PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    dateOfBirth DATE NOT NULL,
    gender VARCHAR(10) NOT NULL,
    contactNumber VARCHAR(15) NOT NULL,
    address VARCHAR(255) NOT NULL
);

CREATE TABLE Doctor (
    doctorId varchar(5) PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    specialization VARCHAR(50) NOT NULL,
    contactNumber VARCHAR(15) NOT NULL
);


create table Appointment(
	appointmentId int primary key, 
	patientId varchar(5) not null,
	doctorId varchar(5) not null,
	appointmentDate DATETIME not null,description varchar(50),
	FOREIGN KEY(patientId) REferences Patient(patientId),
	FOREIGN KEY (doctorId) References Doctor(DoctorId)
);

INSERT INTO Patient(patientId, firstName, lastName, dateOfBirth, gender, contactNumber, address) 
VALUES
('P1', 'Aarav', 'Kapoor', '1972-09-27', 'Male', '911166676', 'Kurnool'),
('P2', 'Mira', 'Patel', '2002-01-12', 'Female', '9756443310', 'Chennai'),
('P3', 'Ishaan', 'Verma', '1985-04-15', 'Male', '7654387663', 'Allahabad'),
('P4', 'Riya', 'Singh', '2015-05-29', 'Female', '7765423435', 'Hyderabad'),
('P5', 'Karan', 'Malhotra', '1984-11-22', 'Male', '7865431211', 'Mumbai'),
('P6', 'Anaya', 'Deshmukh', '1999-07-04', 'Female', '5556667797', 'Kadapa'),
('P7', 'Rohan', 'Bhatia', '2019-02-19', 'Male', '3378654390', 'Chittor'),
('P8', 'Tara', 'Mehta', '2020-07-22', 'Female', '7654445567', 'Chennai'),
('P9', 'Vikram', 'Nair', '2001-03-17', 'Male', '2765465434', 'Kurnool'),
('P10', 'Sara', 'Shah', '2005-10-01', 'Female', '7265223339', 'Kadapa');


INSERT INTO Doctor(doctorId, firstName, lastName, specialization, contactNumber) 
VALUES
('D01', 'Arjun', 'Mehta', 'Cardiologist', '9123456780'),
('D02', 'Neha', 'Kohli', 'Neurologist', '4329087654'),
('D03', 'Raghav', 'Sharma', 'Surgeon', '9876654654'),
('D04', 'Simran', 'Bose', 'Pediatrician', '8769806547'),
('D05', 'Dev', 'Chatterjee', 'Dermatologist', '9876543210'),
('D06', 'Ishita', 'Desai', 'Oncologist', '8907654762'),
('D07', 'Kabir', 'Nayak', 'Dermatologist', '5764789432'),
('D08', 'Anika', 'Kapoor', 'Rheumatologist', '9876867869'),
('D09', 'Rohan', 'Sen', 'Gastroenterologist', '8769806598'),
('D10', 'Aisha', 'Malik', 'Endocrinologist', '7869087651');


Insert into appointment(appointmentId,patientId,doctorId,appointmentDate,description)
Values
(1,'P10','D07','2025-01-21 10:30','Headache'),
(10,'P7','D08','2024-11-13 11:00','Hair Loss'),
(2,'P8','D09','2024-12-02 10:30','Migrane'),
(3,'P1','D10','2024-12-17 9:30','diabetes'),
(4,'P3','D03','2025-02-11 12:00','Fever'),
(5,'P4','D07','2024-11-29 11:30','Stomach Pain'),
(6,'P5','D02','2024-11-03 10:30','Allergy'),
(7,'P6'	,'D01','2024-12-01 11:00','Hyper Tension'),
(8,'P9'	,'D07','2024-12-30 12:00','Hair loss'),
(9,'P2','D04','2024-11-12 12:00','Allergy');
select * from Patient;
select * from Doctor;
select * from Appointment;








