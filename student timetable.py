# Student Timetable Conflict Detection

timetable = [
    ("Python", "09:00", "10:00", "Room1"),
    ("Maths", "10:00", "11:00", "Room2"),
    ("Physics", "09:30", "10:30", "Room3")
]

unavailable_rooms = ["Room3"]

print("Timetable Conflict Detection")

for i in range(len(timetable)):
    subject, start, end, room = timetable[i]

    if room in unavailable_rooms:
        print(subject, "- Room unavailable")

    for j in range(i + 1, len(timetable)):
        s2, start2, end2, room2 = timetable[j]

        if start < end2 and start2 < end:
            print(subject, "and", s2, "- Time conflict")

print("Timetable validation completed.")
