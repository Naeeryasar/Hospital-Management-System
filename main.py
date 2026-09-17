class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Patient(Person):
    def __init__(self, name, age, patient_id, disease, fee):
        super().__init__(name, age)
        self.patient_id = patient_id
        self.disease = disease
        self.fee = fee

    def show_info(self):
        super().show_info()
        print(f"Patient ID: {self.patient_id}")
        print(f"Disease: {self.disease}")
        print(f"Medical Fee: {self.fee}")


class Admin:
    def add_patient(self, patient_list, patient):
        patient_list.append(patient)
        print("Patient added successfully.")

    def remove_patient(self, patient_list, patient_id):
        for p in patient_list:
            if p.patient_id == patient_id:
                patient_list.remove(p)
                print("Patient removed successfully.")
                return

        print("Patient not found.")

Patients = []
admin1 = Admin()

while True:
    print("\n1. Add Patient")
    print("2. Show All Patients")
    print("3. Remove Patient")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
            name = input("Patient Name: ")
            age = int(input("Patient Age: "))
            patient_id = int(input("Patient ID: "))
            disease = input("Disease: ")
            fee = float(input("Medical Fee: "))

            patient = Patient(name, age, patient_id, disease, fee)
            admin1.add_patient(Patients, patient)
