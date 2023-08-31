'''slots = ['9.00','11.00','1.00']
# Alloted slots, 9:00 Red, 11:00 Green, 1:00 Blue
subjects = ['MATHS','OS','ARM','DAA','BIO']

enrolled_in_common_subjects = {}
enrolled_in_common_subjects['MATHS'] = ['BIO', 'DAA', 'OS']
enrolled_in_common_subjects['OS'] = ['ARM', 'BIO', 'MATHS']
enrolled_in_common_subjects['DAA'] = ['ARM', 'BIO', 'MATHS']
enrolled_in_common_subjects['ARM'] = ['BIO', 'DAA', 'OS']
enrolled_in_common_subjects['BIO'] = ['ARM','DAA','MATHS', 'OS']

'''

slots = ["9.00", "11.00", "1.00", "3.00"]
# Alloted slots, 9:00 Red, 11:00 Green, 1:00 Blue, 3:00 Yellow
subjects = ["MATHS", "OS", "ARM", "DAA", "BIO"]

enrolled_in_common_subjects = {}
enrolled_in_common_subjects["MATHS"] = ["ARM", "DAA", "OS"]
enrolled_in_common_subjects["OS"] = ["ARM", "BIO", "DAA", "MATHS"]
enrolled_in_common_subjects["ARM"] = ["DAA", "MATHS", "OS"]
enrolled_in_common_subjects["DAA"] = ["ARM", "BIO", "MATHS", "OS"]
enrolled_in_common_subjects["BIO"] = ["DAA", "OS"]

scheduled_time_slots = {}


def promising(subject, slot):
    for students_enrolled in enrolled_in_common_subjects.get(subject):
        students_alloted_slots = scheduled_time_slots.get(students_enrolled)
        if students_alloted_slots == slot:
            return False
    return True


def get_time_slots_for_subjects(subject):
    for slot in slots:
        if promising(subject, slot):
            return slot


def main():
    for subject in subjects:
        scheduled_time_slots[subject] = get_time_slots_for_subjects(subject)
    print(scheduled_time_slots)


main()