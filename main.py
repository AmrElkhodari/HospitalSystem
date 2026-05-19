from core import Hospital
import ui

def program_loop():
    while True:
        choice = ui.menu_options()
        if choice == 1:
            specialization, name, status = ui.add_patient()
            added_successfully = hospital.add_patient(name, status, specialization)
            if added_successfully:
                print('Patient added successfully')
            else:
                print('Sorry, specialization is full now. Please Try later.')
        elif choice == 2:
            print(hospital.retrieve_all_patients())
        elif choice == 3:
            specialization = ui.get_next_patient()
            patient = hospital.get_next_patient(specialization)
            if patient is None:
                print('No Patients are there')
            else:
                print(f'Patient {patient} entered to doctor')
        elif choice == 4:
            specialization, name = ui.remove_leaving_patient()
            removed_successfully = hospital.remove_leaving_patient(name, specialization)
            if removed_successfully:
                print('Patient removed successfully')
            else:
                print('No patient with such name')
        elif choice == 5:
            exit()

if __name__ == '__main__':
    hospital = Hospital()
    program_loop()