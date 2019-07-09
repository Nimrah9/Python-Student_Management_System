students = []
while True:
    print('\n............Press 1 to add new Student\'s data..............')
    print('..............Press 2 to delete Student\'s data..............')
    print('..............Press 3 to Search Student\'s data..............')
    print('..............Press 4 to Edit Student\'s data..............')
    print('..............Press 5 to Show All Students data..............')
    print('..............Press 6 to Exit..............')

    value = int(input("\n What do you want to do? "))
    if value == 1:
          student = {}
          student['Name'] = input("Enter students name: ")
          student['Age'] = int(input("Enter students age: "))
          student['rollno'] = int(input("Emter students rollno: "))
          student['major'] = input("Enter major: ")
          students.append(student)

          for i in student.items():
             print(i)
          print(students)

    elif value == 2:
        k = input("Enter the students name you want to delete: ")
        for student in students:
            if student['Name'] == k:
                del student['Name']
                del student['Age']
                del student['rollno']
                del student['major']
            else:
                print("The name is entered in not enrolled")
        print(students)

    elif value == 3:
        o = input("Enter the students name you want to search: ")
        for student in students:
            if student['Name'] == o:
                print(student['Name'])
                print(student['Age'])
                print(student['rollno'])
                print(student['major'])
    elif value == 4:
        j = input("Enter the students name whose data you want to edit: ")
        for student in students:
            if student['Name'] == j:
                student['Age'] = input("Enter the new age: ")
                student['rollno'] = input("Enter the new roll no: ")
                student['major'] = input("Enter new major: ")
        print(students)

    elif value == 5:
        print("The currently enrolled students are "+str(len(students))+ "and their data is "+ str(students))

    elif value == 6:
        break



