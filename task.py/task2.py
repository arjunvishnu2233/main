students = []
teachers = []

def add_student():
    name = input("Enter student name: ")
    rno = input("Enter student roll no: ")
    class_name = input("Enter student class: ")
    student = {"name": name, "rno": rno, "class": class_name, "assigned_teacher": {}}
    students.append(student)
    print(" Student added successfully!\n")

def view_students():
    if not students:
        print("No students found.\n")
        return
    print("\n--- Student List ---")
    for s in students:
        print(f"Roll No: {s['rno']}, Name: {s['name']}, Class: {s['class']}, "
              f"Teacher: {s['assigned_teacher'].get('name', 'Not Assigned')}")
    print()

def update_student():
    view_students()
    rno = input("Enter student roll no to update: ")
    for s in students:
        if s["rno"] == rno:
            s["name"] = input("Enter new name: ")
            s["class"] = input("Enter new class: ")
            print(" Student updated successfully!\n")
            return
    print(" Student not found.\n")

def delete_student():
    view_students()
    rno = input("Enter student roll no to delete: ")
    for s in students:
        if s["rno"] == rno:
            
            if s["assigned_teacher"]:
                teacher = s["assigned_teacher"]
                for t in teachers:
                    if t["tid"] == teacher["tid"]:
                        t["students"] = [st for st in t["students"] if st["rno"] != rno]
            students.remove(s)
            print(" Student deleted successfully!\n")
            return
    print(" Student not found.\n")

def add_teacher():
    tid = input("Enter teacher ID: ")
    name = input("Enter teacher name: ")
    subject = input("Enter subject: ")
    teacher = {"tid": tid, "name": name, "subject": subject, "students": []}
    teachers.append(teacher)
    print(" Teacher added successfully!\n")

def assign_teacher():
    view_students()
    rno = input("Enter student roll no to assign teacher: ")
    student = next((s for s in students if s["rno"] == rno), None)
    if not student:
        print(" Student not found.\n")
        return
    
    if not teachers:
        print(" No teachers available. Add a teacher first.\n")
        return
    
    print("\n--- Teacher List ---")
    for t in teachers:
        print(f"ID: {t['tid']}, Name: {t['name']}, Subject: {t['subject']}")
    
    tid = input("Enter teacher ID to assign: ")
    teacher = next((t for t in teachers if t["tid"] == tid), None)
    if not teacher:
        print(" Teacher not found.\n")
        return
    
    student["assigned_teacher"] = {"tid": teacher["tid"], "name": teacher["name"], "subject": teacher["subject"]}
    teacher["students"].append(student)
    print("Teacher assigned successfully!\n")

def main():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Add Teacher")
        print("6. Assign Teacher")
        print("7. Exit")
        
        choice = input("Pick one option: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            add_teacher()
        elif choice == "6":
            assign_teacher()
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.\n")

if __name__:"__main__"
main()
