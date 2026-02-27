age = int(input("Ievadi vecumu: "))
has_license = input("Vai ir autovadītāja apliecība? (j/n): ")
is_student = input("Vai esi students? (j/n): ")
is_veteran = input("Vai esi veterāns? (j/n): ")

has_license = has_license.lower() == "j"
is_student = is_student.lower() == "j"
is_veteran = is_veteran.lower() == "j"

can_vote = age >= 18
can_rent = age >= 21 and has_license
senior_discount = age >= 65 or is_veteran
student_discount = 16 <= age <= 26 and is_student

print("\n--- Rezultāti ---")
print(f"Balsot: {'Jā' if can_vote else 'Nē'}")
print(f"Īrēt auto: {'Jā' if can_rent else 'Nē'}")
print(f"Senioru atlaide: {'Jā' if senior_discount else 'Nē'}")
print(f"Studentu atlaide: {'Jā' if student_discount else 'Nē'}")