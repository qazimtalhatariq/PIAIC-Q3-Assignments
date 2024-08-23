def manage_student_database():
    # Initialize the list to store student tuples
    student_list = []
    student_id = 1
    
    while True:
        # Ask the user for the student's name
        student_name = input("Please enter the student's name (or type 'stop' to finish): ").strip()
        
        # Stop the input process if 'stop' is entered
        if student_name.lower() == 'stop':
            break
        
        # Check for duplicate names
        if any(student_name == student[1] for student in student_list):
            print("This name is already in the list.")
        else:
            # Add the student tuple (ID, Name) to the list
            student_list.append((student_id, student_name))
            student_id += 1
    
    # Display the complete list of student tuples
    print("\nComplete List of Students (Tuples):")
    print(student_list)
    
    # Display each student's ID and name individually
    print("\nList of Students with IDs:")
    for student in student_list:
        print(f"ID: {student[0]}, Name: {student[1]}")
    
    # Total number of students
    total_students = len(student_list)
    print(f"\nTotal number of students: {total_students}")
    
    # Calculate the total length of all student names combined
    total_name_length = sum(len(student[1]) for student in student_list)
    print(f"Total length of all student names combined: {total_name_length}")
    
    # Identify the student with the longest and shortest name
    if student_list:
        longest_name_student = max(student_list, key=lambda student: len(student[1]))
        shortest_name_student = min(student_list, key=lambda student: len(student[1]))
        
        print(f"The student with the longest name is: {longest_name_student[1]}")
        print(f"The student with the shortest name is: {shortest_name_student[1]}")

# Call the function to execute the program
manage_student_database()
