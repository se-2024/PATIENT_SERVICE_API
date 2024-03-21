-- Hospital Table
INSERT INTO hospital (name, address) VALUES 
('City General Hospital', '123 Main Street'),
('Westside Medical Center', '456 Elm Street'),
('East End Clinic', '789 Oak Avenue');

-- Department Table
INSERT INTO department (name, hospital_id) VALUES 
('Emergency Medicine', 1),
('Pediatrics', 1),
('Surgery', 2),
('Cardiology', 2),
('OB/GYN', 3),
('Psychiatry', 3);

-- Employee Table
INSERT INTO employee (first_name, last_name, ssn, position, hospital_id, department_id) VALUES 
('John', 'Doe', '123456789', 'Nurse', 1, 1),
('Jane', 'Smith', '987654321', 'Physician', 1, 2),
('Emily', 'Johnson', '456123789', 'Manager', 2, NULL),
('Michael', 'Williams', '789123456', 'Nurse', 2, 3),
('Sarah', 'Brown', '321654987', 'Physician', 2, 4),
('Robert', 'Jones', '654987321', 'Manager', 3, 5);

-- Nurse Table
INSERT INTO nurse (qualification, id) VALUES 
('Registered Nurse', 1),
('Licensed Practical Nurse', 4);

-- Manager Table
INSERT INTO manager (id) VALUES 
(3),
(6);

-- Physician Table
INSERT INTO physician (specialty, id) VALUES 
('Pediatrician', 2),
('Cardiologist', 5);

-- Patient Table
INSERT INTO patient (first_name, last_name, physician_id, dob, ssn, gender, address) VALUES 
('Alice', 'Anderson', 2, '1990-05-15', '111223333', 'Female', '123 Maple Street'),
('Bob', 'Clark', 5, '1985-08-20', '444556666', 'Male', '456 Pine Avenue'),
('Carol', 'Evans', 2, '1976-03-10', '777889999', 'Female', '789 Oak Lane');

-- Insurance Table
INSERT INTO insurance (patient_id, provider_name, policy_number) VALUES 
(1, 'ABC Insurance', '123456'),
(2, 'XYZ Insurance', '789012'),
(3, 'DEF Insurance', '345678');

-- Appointment Table
INSERT INTO appointment (patient_id, physician_id, appointment_date, description) VALUES 
(1, 2, '2024-03-18 09:00:00', 'Annual checkup'),
(2, 5, '2024-03-19 10:30:00', 'Cardiology consultation'),
(3, 2, '2024-03-20 14:00:00', 'Pediatric follow-up');

-- Medication Table
INSERT INTO medication (name, brand, description) VALUES 
('Ibuprofen', 'Advil', 'Pain reliever'),
('Amoxicillin', 'Amoxil', 'Antibiotic'),
('Lisinopril', 'Prinivil', 'Blood pressure medication');

-- Prescription Table
INSERT INTO prescription (patient_id, prescribing_physician_id, medication_id, prescription_date, quantity, dosage, frequency, start_date, end_date, refills_available) VALUES 
(1, 2, 1, '2024-03-18', 30, '200mg', 'Twice daily', '2024-03-18', '2024-04-17', 1),
(2, 5, 2, '2024-03-19', 20, '500mg', 'Three times daily', '2024-03-19', '2024-04-18', 0),
(3, 2, 3, '2024-03-20', 60, '10mg', 'Once daily', '2024-03-20', '2024-04-19', 2);

-- Room Table
INSERT INTO room (room_type_id, available) VALUES 
(1, TRUE),
(2, TRUE),
(3, TRUE),
(4, TRUE);
