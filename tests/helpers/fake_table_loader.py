
import os
import random
import string
import sys
import uuid
from datetime import timedelta
from random import choice, randint
from types import SimpleNamespace

from faker import Faker
from sqlalchemy import Boolean, Date, DateTime, Float, Integer, Interval, MetaData, String
from sqlalchemy.dialects.postgresql import UUID

from lib import db_models, response_models
from lib.database_connection import SessionLocal, engine

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/.."))


# needed for connecting to the local database testing

departments_list = [
    "ICU",
    "Internal Medicine",
    "Pathology",
    "Cardiology",
    "Gastroenterology",
    "Pharmacy",
    "Diagnostic Imaging",
    "Maternity",
    "Dermatology",
    "Finance",
    "Burn",
    "Orthopedics",
    "Neurology",
    "Pain Rehabilitation",
    "Dietary",
    "Physiotherapy",
    "Outpatient",
    "Neonatal",
    "Radiology",
]

insurances_list = [
    "Framer's Insurance",
    "Allstate Insurance",
    "Cigna",
    "Aetna"
]

hospitals_list = [
    "UPMC Health",
    "Long Island Jewish Hospital",
    "Bay Area Hospital"
]


class FakeTableLoader:
    def __init__(self):
        self.fake = Faker()
        self.working_dir = os.path.dirname(os.path.abspath(__file__))
        self.tables = self.load_tables()
        self.supported_tables = self.load_crud_files()

    def load_crud_files(self):
        directory = f"{self.working_dir}/../../lib"

        # Use list comprehension to filter and transform the filenames in one go
        return [
            filename.replace("_crud.py", "")
            for _, _, filenames in os.walk(directory)
            for filename in filenames
            if filename.endswith("_crud.py")
        ]

    def load(self):
        entities = []
        session = SessionLocal()
        for table_name in self.supported_tables:
            if table_name in self.tables:
                data = []
                table = self.metadata.tables[table_name]
                row_data = self.generate_fake_row_data(table, session)
                data.append(row_data)
                entities.append((table_name, data))
        return entities

    def get_model_class(self, table_name: str):
        # convert the table_name to TableName
        class_name = table_name.name.capitalize()
        # Return the actual class its self
        return getattr(db_models, class_name)

    def load_tables(self):
        # Reflect metadata/schema from existing postgres database
        self.metadata = MetaData()
        self.metadata.reflect(bind=engine)
        return self.metadata.tables

    def get_data_type_mapper(self) -> SimpleNamespace:
        # build a namespace for easy type access
        return SimpleNamespace(
            type_maps=[
                SimpleNamespace(
                    type=DateTime,
                    fake_type=self.fake.date_time_between(
                        start_date="-30y", end_date="now"
                    ),
                ),
                SimpleNamespace(
                    type=Date,
                    fake_type=self.fake.date_time_between(
                        start_date="-30y", end_date="now"
                    ),
                ),
                SimpleNamespace(type=Boolean, fake_type=self.fake.boolean()),
                SimpleNamespace(type=Integer, fake_type=self.fake.random_int(min=1, max=1000, step=1)),
                SimpleNamespace(type=Float, fake_type=self.fake.pyfloat(positive=True)),
                SimpleNamespace(
                    type=Interval, fake_type=timedelta(seconds=randint(0, 86400))
                ),
                SimpleNamespace(type=UUID, fake_type=str(uuid.uuid4())),
                SimpleNamespace(
                    type=String,
                    fake_type=f"{' '.join([self.fake.word() for _ in range(8)])}",
                ),
            ]
        )

    def get_provider_type_mapper(self) -> SimpleNamespace:
        # build a namespace for easy type access
        return SimpleNamespace(
            provider_maps=[
                SimpleNamespace(
                    type="ssn",
                    fake_type=self.fake.ssn().replace("-", ""),
                ),
                SimpleNamespace(
                    type="first_name",
                    fake_type=self.fake.first_name(),
                ),
                SimpleNamespace(
                    type="last_name",
                    fake_type=self.fake.last_name(),
                ),
                SimpleNamespace(
                    type="position",
                    fake_type=self.fake.job(),
                ),
                SimpleNamespace(
                    type="department.name",
                    fake_type=choice(departments_list),
                ),
                SimpleNamespace(
                    type="hospital.name",
                    fake_type=choice(hospitals_list),
                ),
                SimpleNamespace(
                    type="insurance.provider_name",
                    fake_type=choice(insurances_list),
                ),
                SimpleNamespace(
                    type="physician.specialty",
                    fake_type=choice(["Anesthesiology", "Cardiology", "Dermatology", "Family Medicine", "General Surgery"])
                ),
                SimpleNamespace(
                    type="medication.name",
                    fake_type=choice(["Acetaminophen", "Loratadine", "Fluoxetine", "Amlodipine"])
                ),
                SimpleNamespace(
                    type="medication.brand",
                    fake_type=choice(["Tylenol", "Claritin", "Prozac", "Norvasc"])
                ),
                SimpleNamespace(
                    type="medication.description",
                    fake_type=choice(["Used to treat mild to moderate pain and reduce fever.",
                                      "Used to treat allergy symptoms such as runny nose, sneezing, and itchy eyes.",
                                      "A selective serotonin reuptake inhibitor (SSRI) used to treat depression, OCD, and anxiety.",
                                      "A calcium channel blocker used to treat high blood pressure and angina."])
                ),
                SimpleNamespace(type="dob", fake_type=self.fake.date_of_birth()),
                SimpleNamespace(type="gender", fake_type=choice(["MALE", "FEMALE"])),
                SimpleNamespace(type="address", fake_type=self.fake.address()),
                SimpleNamespace(type="policy_number", fake_type=''.join(random.choices(string.ascii_uppercase +
                                                                                       string.digits, k=7))),
                SimpleNamespace(type="prescription.dosage", fake_type=choice(["500 mg", "50 mg", "100 mg"])),
                SimpleNamespace(type="prescription.frequency", fake_type=f"{choice(["once", "twice"])} a {choice(["day", "week"])}"),

            ]
        )

    def get_fake_data_type(self, column):
        fake_data_type = None

        # Check data types for all columns in a table and generate fake data
        for data_type in self.get_data_type_mapper().type_maps:
            if isinstance(column.type, data_type.type):
                fake_data_type = data_type.fake_type

        # Check specific providers types for all columns in a table and generate fake data
        # This step makes the data more "realistic"
        for provider_type in self.get_provider_type_mapper().provider_maps:
            if column.name == provider_type.type or f"{
                    column.table}.{
                    column.name}" == provider_type.type:
                fake_data_type = provider_type.fake_type

        return fake_data_type

    def generate_fake_row_data(self, table: MetaData, session) -> dict:

        # loop through all table columns
        row_data = {}
        for column in table.columns:

            fake_data_type = self.get_fake_data_type(column)
            if fake_data_type is not None:
                row_data[column.name] = fake_data_type

            if column.primary_key:
                row_data[column.name] = self.fake.random_int(min=1001, max=2000, step=1)

            # loop through table relationships
            for fk in column.foreign_keys:
                fk_table = fk.column.table
                fk_column = fk.column
                data = session.query(self.get_model_class(fk_table)).limit(1).first()
                if data is not None:
                    response_model = getattr(
                        response_models, fk_table.name.capitalize()
                    )
                    response_model = response_model.validate(data.__dict__)
                    row_data[column.name] = getattr(response_model, fk_column.name)
                else:
                    row_data = self.generate_fake_row_data(fk_table, session)
        return row_data


if __name__ == "__main__":
    loader = FakeTableLoader()
    entities = loader.load()
    print(entities)
