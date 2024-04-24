-- This schema provides a comprehensive foundation for a hospital management system,
-- outlining the key entities involved and their interrelationships.
-- Adjustments may be required based on specific system requirements,
-- such as adding or modifying tables and relationships.

-- uncomment the below statements to recreate the schema
DROP TYPE IF EXISTS _roomType CASCADE;
DROP TABLE IF EXISTS hospital CASCADE;
DROP TABLE IF EXISTS department CASCADE;
DROP TABLE IF EXISTS employee CASCADE;
DROP TABLE IF EXISTS nurse CASCADE;
DROP TABLE IF EXISTS manager CASCADE;
DROP TABLE IF EXISTS physician CASCADE;
DROP TABLE IF EXISTS patient CASCADE;
DROP TABLE IF EXISTS insurance CASCADE;
DROP TABLE IF EXISTS appointment CASCADE;
DROP TABLE IF EXISTS medication CASCADE;
DROP TABLE IF EXISTS prescription CASCADE;
DROP TABLE IF EXISTS room_type CASCADE;
DROP TABLE IF EXISTS room CASCADE;

-- Hospital Table
CREATE TABLE hospital (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL
);

-- Department Table
-- Each department is related to one hospital,
-- but a hospital can have multiple departments
CREATE TABLE department (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    hospital_id INT NOT NULL,
    FOREIGN KEY (hospital_id) REFERENCES hospital(id)
);

-- Employee Table (generic employee, includes nurses, physicians and managers)
-- employee is a general table that can represent any employee within the hospital,
-- including those who might not directly interact with patients.
CREATE TABLE employee (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    ssn VARCHAR(9) NOT NULL,
    position VARCHAR(255),
    hospital_id INT NOT NULL,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES department(id),
    FOREIGN KEY (hospital_id) REFERENCES hospital(id)
);

-- Extension of Employee Table for Nurses
-- employees but have specific roles and additional information.
CREATE TABLE nurse (
    id SERIAL PRIMARY KEY,
    qualification VARCHAR(255),
    FOREIGN KEY (id) REFERENCES employee(id)
);

-- Extension of Employee Table for Managers
-- employees but have specific roles and additional information.
CREATE TABLE manager (
    id SERIAL PRIMARY KEY,
    FOREIGN KEY (id) REFERENCES employee(id)
);

-- Extension of Employee Table for Physician Table
-- employees but have specific roles and additional information.
CREATE TABLE physician (
    id SERIAL PRIMARY KEY,
    specialty VARCHAR(255),
    FOREIGN KEY (id) REFERENCES employee(id)
);

-- Patient Table
CREATE TABLE patient (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    physician_id INT NOT NULL,
    dob DATE NOT NULL,
    ssn VARCHAR(9) NOT NULL,
    gender VARCHAR(50),
    address VARCHAR(255),
    FOREIGN KEY (physician_id) REFERENCES physician(id)
);

-- Insurance Table
-- patient and insurance are directly related,
-- as each patient can have an associated insurance policy.
CREATE TABLE insurance (
    id SERIAL PRIMARY KEY,
    patient_id INT NOT NULL,
    provider_name VARCHAR(255) NOT NULL,
    policy_number VARCHAR(255) NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patient(id)
);

-- Appointment Table
-- appointment connects patients with physicians,
-- allowing for the scheduling and tracking of visits.
CREATE TABLE appointment (
    id SERIAL PRIMARY KEY,
    patient_id INT NOT NULL,
    physician_id INT NOT NULL,
    appointment_date TIMESTAMP NOT NULL,
    description TEXT,
    FOREIGN KEY (patient_id) REFERENCES patient(id),
    FOREIGN KEY (physician_id) REFERENCES physician(id)
);

-- Medication Table
-- medication and prescription tables manage the prescriptions
-- given to patients, with the prescription table linking patients
-- to their prescribed medications and detailing the dosage and frequency.
CREATE TABLE medication (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    brand VARCHAR(255) NOT NULL,
    description TEXT
);

-- Prescription Table (associates patients with medications)
-- This table structure allows for the management of prescriptions,
-- including tracking how many refills are available for each prescription.
-- It can be further extended or modified to meet specific requirements,
-- such as adding expiration dates for prescriptions or refills, handling
-- renewal requests, etc

CREATE TABLE prescription (
    id SERIAL PRIMARY KEY,
    patient_id INT NOT NULL,
    -- the physician who prescribed the medication from the physician table.
    prescribing_physician_id INT NOT NULL,
    medication_id INT NOT NULL,
    prescription_date DATE NOT NULL,
    -- specifies how much medication is dispensed with the prescription.
    quantity INT NOT NULL,
    -- provides information on how the medication should be taken (e.g., 500 mg).
    dosage TEXT,
    -- describes how often the medication should be taken (e.g., twice a day).
    frequency TEXT,
    start_date DATE,
    end_date DATE,
    -- indicating the number of times the prescription can be refilled. A value of 0 would indicate that no refills are available.
    refills_available INT NOT NULL DEFAULT 0, -- Indicates the number of refills available
    FOREIGN KEY (patient_id) REFERENCES patient(id),
    FOREIGN KEY (medication_id) REFERENCES medication(id),
    FOREIGN KEY (prescribing_physician_id) REFERENCES physician(id)
);

CREATE TABLE room_type (
    id SERIAL PRIMARY KEY,
    type VARCHAR(25)
);

INSERT INTO room_type (type) VALUES ('surgery');
INSERT INTO room_type (type) VALUES ('ICU');
INSERT INTO room_type (type) VALUES ('maternity');
INSERT INTO room_type (type) VALUES ('mental_health');

CREATE TABLE room (
    id SERIAL PRIMARY KEY,
    room_type_id INT NOT NULL,
    -- room is available until someone explicitly books it
    available BOOLEAN NOT NULL DEFAULT TRUE
);

-- Adding some data to hospital table to populate existing hospitals
-- Hospital data
INSERT INTO
    hospital (name, address)
VALUES (
        'John Hopkins', 'Baltimore, MD'
    ),
    ('Mount Sinai', 'New York, NY');

-- Department data
INSERT INTO
    department (name, hospital_id)
VALUES ('Emergency', 1),
    ('Pediatric', 1),
    ('OR', 2);

-- Room types
INSERT INTO
    room_type (type)
VALUES ('surgery'),
    ('ICU'),
    ('maternity'),
    ('mental_health');

-- Rooms for each room type
INSERT INTO
    room (room_type_id, available)
VALUES (1, TRUE),
    (2, TRUE),
    (3, TRUE),
    (4, TRUE);

-- Employees: physicians, nurses, managers
-- Note: Need to populate employee before nurses, physicians, and managers
INSERT INTO
    employee (
        first_name, last_name, ssn, position, hospital_id, department_id
    )
VALUES (
        'Alice', 'Smith', '123456789', 'Physician', 1, 1
    ),
    (
        'Bob', 'Johnson', '987654321', 'Nurse', 1, 2
    ),
    (
        'Carol', 'Williams', '123459876', 'Manager', 1, 2
    );

-- Physician
INSERT INTO physician (id, specialty) VALUES (1, 'Cardiology');

-- Nurse
INSERT INTO nurse (id, qualification) VALUES (2, 'Registered Nurse');

-- Manager
INSERT INTO manager (id) VALUES (3);

-- Patients and their details
INSERT INTO
    patient (
        first_name, last_name, physician_id, dob, ssn, gender, address
    )
VALUES (
        'John', 'Doe', 1, '1985-02-15', '555123456', 'Male', '123 Elm St, Baltimore, MD'
    ),
    (
        'Jane', 'Roe', 1, '1990-07-23', '555987654', 'Female', '456 Oak St, Baltimore, MD'
    );

-- Insurance for patients
INSERT INTO
    insurance (
        patient_id, provider_name, policy_number
    )
VALUES (1, 'HealthCo', 'POL123'),
    (2, 'WellnessInsure', 'POL456');

-- Medications
INSERT INTO
    medication (name, brand, description)
VALUES (
        'Lisinopril', 'Prinivil', 'Treats high blood pressure'
    ),
    (
        'Metformin', 'Glucophage', 'Treats type 2 diabetes'
    );

-- Prescriptions for patients
INSERT INTO
    prescription (
        patient_id, prescribing_physician_id, medication_id, prescription_date, quantity, dosage, frequency, start_date, end_date, refills_available
    )
VALUES (
        1, 1, 1, '2023-04-01', 30, '10 mg', 'once a day', '2023-04-01', '2023-05-01', 3
    ),
    (
        2, 1, 2, '2023-04-01', 60, '500 mg', 'twice a day', '2023-04-01', '2023-07-01', 1
    );

-- Appointments for patients
INSERT INTO
    appointment (
        patient_id, physician_id, appointment_date, description
    )
VALUES (
        1, 1, '2023-05-01 10:00:00', 'Routine check-up'
    ),
    (
        2, 1, '2023-05-01 11:00:00', 'Follow-up on treatment'
    );
