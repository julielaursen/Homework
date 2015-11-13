
#define main function
def main():
        #create empty list called students
        students = []
        #call modify_students
        modify_students(students)

#define modify_students and pass students to it
def modify_students(students):
        counter = 0
        while counter < 12:
                #take input for 12 students and append them to student list
                name = input("Please input the student's name: ")
                counter += 1
                students.append(name)

        #print(students, '\n')
        #sort list in alphabetical order
        students.sort()
        print('Sorted order:', students, '\n')
        #sort list in reverse order
        students.sort(reverse=True)
        print('Reverse sorted order', students, '\n')
        #append instructor's name onto the list
        students.append('Rene Polanco')
        print('Students and instructor,', students, '\n')
        #insert your own name at the beginning of the list
        students.insert(0, 'Julie Laursen')
        print('Students, instructor and name:', students, '\n')

        #output the list to a file named names.txt
        outfile = open('names.txt', 'w')
        for item in students:
                outfile.write(str(item) + '\n')
        outfile.close()

        #display the contents of names.txt
        infile = open('names.txt', 'r')
        file_contents = infile.read()
        infile.close()
        print(file_contents)

        #convert list to tuple
        file_tuple = tuple(students)

#call main function
main()


