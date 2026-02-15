class Patient:
    counter = 1  

    def __init__(self, name, illness):
        self.__name = name
        self.__illness = illness
        self.patient_id = Patient.counter
        Patient.counter += 1

    def get_illness(self):
        return self.__illness

    def get_name(self):
        return self.__name


class Doctor:
    counter = 500   

    def __init__(self, name):
        self.__name = name
        Doctor.counter += 1
        self.doctor_id = "D" + str(Doctor.counter)
        self.__patient_list = []

    def get_patient_list(self):
        return self.__patient_list

    def get_name(self):
        return self.__name


class Hospital:
    def __init__(self, specialization_list, doctor_list):
        self.__specialization_list = specialization_list
        self.__doctor_list = doctor_list

    def get_specialization_list(self):
        return self.__specialization_list

    def get_doctor_list(self):
        return self.__doctor_list

    def validate_patient(self, patient):
        if patient.get_illness() in self.__specialization_list:
            return self.__specialization_list.index(patient.get_illness())
        return -1

    def allocate_patients(self, patient_list):
        invalid_patient_list = []

        for patient in patient_list:
            index = self.validate_patient(patient)

            if index != -1:
                doctor = self.__doctor_list[index]
                doctor.get_patient_list().append(patient)
            else:
                invalid_patient_list.append(patient)

        return invalid_patient_list



specialization_list = ["Cardiology", "Neurology", "Orthopedics"]


doctor1 = Doctor("Dr. Sharma")
doctor2 = Doctor("Dr. Mehta")
doctor3 = Doctor("Dr. Rao")

doctor_list = [doctor1, doctor2, doctor3]


hospital = Hospital(specialization_list, doctor_list)


patient1 = Patient("Rohan", "Cardiology")
patient2 = Patient("Amit", "Neurology")
patient3 = Patient("Sneha", "Orthopedics")
patient4 = Patient("Kiran", "Dermatology")  

patient_list = [patient1, patient2, patient3, patient4]

invalid_patients = hospital.allocate_patients(patient_list)

print("---- Allocation Details ----")
for doctor in hospital.get_doctor_list():
    print("Doctor:", doctor.get_name(), doctor.doctor_id)
    for patient in doctor.get_patient_list():
        print("  Patient ID:", patient.patient_id,
              "Name:", patient.get_name(),
              "Illness:", patient.get_illness())

print("\nInvalid Patients:")
for patient in invalid_patients:
    print("Patient ID:", patient.patient_id,
          "Name:", patient.get_name(),
          "Illness:", patient.get_illness())
