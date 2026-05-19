class Hospital:

    def __init__(self):
        self.patients = [[[] for __ in range(3)] for _ in range(20)]

    def add_patient(self, name : str, status : int, specialization_number : int) -> bool:
        specialization = self.patients[specialization_number]
        if len(specialization[0]) + len(specialization[1]) + len(specialization[2]) == 10:
            return False
        specialization[status].append(name)
        return True

    def retrieve_all_patients(self) -> str:
        answer = ''
        for idx in range(20):
            if len(self.patients[idx][0] + self.patients[idx][1] + self.patients[idx][2]) == 0:
                continue
            specialization = self.patients[idx]
            answer += f'\nSpecialization {idx + 1} : There are {len(specialization[0]) + len(specialization[1]) + len(specialization[2])} patients\n'
            for patient in specialization[2]:
                answer += f'Patient: {patient} is Super Urgent\n'
            for patient in specialization[1]:
                answer += f'Patient: {patient} is Urgent\n'
            for patient in specialization[0]:
                answer += f'Patient: {patient} is Normal\n'
        return answer

    def get_next_patient(self, specialization_number : int) -> str:
        specialization = self.patients[specialization_number]
        if len(specialization[0]) + len(specialization[1]) + len(specialization[2]) == 0:
            return None
        if len(specialization[2]) > 0:
            return specialization[2].pop(0)
        elif len(specialization[1]) > 0:
            return specialization[1].pop(0)
        else:
            return specialization[0].pop(0)

    def remove_leaving_patient (self, name : str, specialization_number : int) -> bool:
        specialization = self.patients[specialization_number]
        if len(specialization[0]) + len(specialization[1]) + len(specialization[2]) == 0:
            return False
        if name in specialization[2]:
            specialization[2].pop(specialization[2].index(name))
            return True
        elif name in specialization[1]:
            specialization[1].pop(specialization[1].index(name))
            return True
        elif name in specialization[0]:
            specialization[0].pop(specialization[0].index(name))
            return True
        else:
            return False
