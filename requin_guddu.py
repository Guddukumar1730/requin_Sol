class InterimGradeLetter:
    def __init__(self, assignment1, assignment2, assignment3):
        self.assignment1 = assignment1
        self.assignment2 = assignment2
        self.assignment3 = assignment3

    # checks if the student has failed or not
    def check_for_fail(self):
        return 0 in [self.assignment1, self.assignment2, self.assignment3] or \
               self.assignment1 < 50 and self.assignment2 < 50 or \
               self.assignment1 < 50 and self.assignment3 < 50 or \
               self.assignment3 < 50 and self.assignment2 < 50

    # get the weighted score based on the weightage provided in the table
    def get_weighted_assignment_scores(self):
        return self.assignment1 * 0.2 + self.assignment2 * 0.4 + self.assignment3 * 0.4
    def average_of_assignment1(self):
        return self.assignment1
    def average_of_assignment2(self):
        return self.assignment2
    def average_of_assignment3(self):
        return self.assignment3
    def average_of_final_marks(self):
        avg_final=self.get_weighted_assignment_scores()
        return avg_final

    # get grades based on the criteria provided
    def get_grades(self):

        final_marks = self.get_weighted_assignment_scores()
        if final_marks >= 85:
            return 'HD'
        elif final_marks >= 75:
            return 'D'
        elif final_marks >= 65:
            return 'C'
        elif final_marks >= 50:
            return 'P'
        elif final_marks >= 45:
            if self.check_for_fail():
                return 'F'
            elif self.assignment1 < 50 or self.assignment2 < 50:
                return 'SA'
            else:
                return 'SE'
        else:
            if self.check_for_fail():
                return 'F'
            else:
                return 'AF'

    def get_grade_dit(self):
        final_marks_dit=self.get_weighted_assignment_scores()
        if final_marks_dit>=50:
            return "CP"
        elif final_marks_dit<=49:
            return "NC"



if __name__ == "__main__":
    # run loop until user choose to exit
    while True:
        # display main menu
        print("Choose one of the following options:")
        print("1 - Enter student grade information")
        print("2 - Print all student grade information")
        print("3 - Print class performance statistics")
        print("4 - Exit")

        # read user choice
        ch = input()

        print()

        # Option 1
        if ch == "1":
            # run loop for sub-menu
            # until user choose to enter to return
            # to main menu
            bit_students = 0
            dit_students = 0
            hd_grade = 0
            d_grade = 0
            c_grade = 0
            p_grade = 0
            sp_grade = 0
            cp_grade = 0
            f_grade = 0
            af_grade = 0

            while True:
                # display sub-menu of Option 1
                print("Choose one of the following options:")
                print("1.1 - Enter a BIT student information")
                print("1.2 - Enter a DIT student information")
                print("1.3 - Go back to the main menu")

                # read user choice
                ch_sub = input()

                print()

                # Option 1.1
                if ch_sub == "1.1":

                    # no. of BIT students
                    bit_students += 1
                    # prompt user to enter student ID
                    stu_id = input("Enter student ID: ")

                    # prompt user to enter student name
                    stu_name = input("Enter student name: ")

                    # prompt user to enter marks separated by comma
                    marks = input("Enter student assessment marks (separated by comma): ")

                    # process the above marks string separated by
                    # comma and get the list of marks
                    grades = list(map(float, marks.split(",")))

                    # get the interim grade letter using get_grades() method
                    # of InterimGradeLetter function
                    grade_letter = InterimGradeLetter(*grades).get_grades()

                    # if letter grade is "SE"
                    if grade_letter == "SE":

                        # prompt user to enter marks of supplementary examm
                        se_marks = input("What is this student's supplementary examm mark: ")
                        grades[2]=se_marks


                    # if letter grade is "SA"
                    elif grade_letter == "SA":

                        # prompt user to enter marks of supplementary assessment
                        sa_marks = input("What is this student's supplementary assessment mark: ")
                        grades[2]=sa_marks



                # Option 1.2
                elif ch_sub == "1.2":
                    # no. of DIT students
                    dit_students += 1
                    # prompt user to enter student ID
                    stu_id = input("Enter student ID: ")

                    # prompt user to enter student name
                    stu_name = input("Enter student name: ")

                    # prompt user to enter marks separated by comma
                    marks = input("Enter student assessment marks (separated by comma): ")

                    # process the above marks string separated by
                    # comma and get the list of marks
                    grades = list(map(float, marks.split(",")))

                    # compute the weighted mark of the marks entered
                    # above using get_weighted_assignment_scores()
                    # of InterimGradeLetter class


                    weighted_marks = InterimGradeLetter(*grades).get_weighted_assignment_scores()
                    weighted_grade=InterimGradeLetter(*grades).get_grade_dit()

                    # if this weighted final mark is less than 50
                    if weighted_marks < 50:
                        # prompt user to enter marks of resubmission
                        resub_marks = input("What is this student's resubmission marks (separated by comma): ")
                        grades=list(map(float, resub_marks.split(",")))


                        weighted_grade = InterimGradeLetter(*grades).get_grade_dit()

                # Option 1.3
                elif ch_sub == "1.3":
                    # break the nested while loop
                    # to go to main menu
                    break

                # in case, user enter option other than 1, 2 and 3 for sub-menu of option 1
                else:
                    print("Invalid Option !!! Input should be only a whole number between 1 and 3 (both inclusive).")
                print()

        elif ch == "2":
            pass
        elif ch == "3":
            numbers_of_studnets = (bit_students + dit_students)
            number_of_bit_students = bit_students
            number_of_dit_students = dit_students
            print(f"Number of students:{numbers_of_studnets}")
            print(f"Number of BIT students:{number_of_bit_students}")
            print(f"Number of DIT students:{number_of_dit_students}")
            if grade_letter == "HD":
                hd_grade += 1
            elif grade_letter == "D":
                d_grade += 1
            elif grade_letter== "C":
                c_grade += 1
            elif grade_letter == "P":
                p_grade += 1
            elif grade_letter=="F":
                f_grade +=1
            elif grade_letter=="SA" or "SE":
                sp_grade+=1
            elif grade_letter=="AF":
                af_grade+=1
            elif weighted_grade=="CP":
                cp_grade+=1
            #student pass rate
            sum_of_grades=(hd_grade+d_grade+cp_grade+c_grade+sp_grade+p_grade)
            Student_pass_rate=sum_of_grades/numbers_of_studnets
            student_adjusted=numbers_of_studnets-af_grade
            student_pass_rate_adjusted=sum_of_grades/student_adjusted
            print(f"Student pass rate:{Student_pass_rate:.2f}")
            print(f"Student pass rate(adjusted):{student_pass_rate_adjusted:.2f}")
            grade_average1 = (InterimGradeLetter(*grades).average_of_assignment1()/ numbers_of_studnets)
            grade_average2 = (InterimGradeLetter(*grades).average_of_assignment2() / numbers_of_studnets)
            grade_average3 = (InterimGradeLetter(*grades).average_of_assignment3()/ numbers_of_studnets)
            print(f"Average mark for Assessment 1:{grade_average1:.2f}")
            print(f"Average mark for Assessment 2:{grade_average2:.2f}")
            print(f"Average mark for Assessment 3:{grade_average3:.2f}")
            avgfinal=(InterimGradeLetter(*grades).average_of_final_marks()/numbers_of_studnets)
            print(f"Average final mark:{avgfinal:.2f}")
            print(f"Number of HDs:{hd_grade}")
            print(f'Number of Ds:{d_grade}')
            print(f'Number of Cs:{c_grade}')
            print(f"Number of Ps:{p_grade}")
            print(f"Number of SPs:{sp_grade}")
            print(f"Number of CPs:{cp_grade}")
            print(f"Number of Fs:{f_grade}")




        # Option 4
        elif ch == "4":
            # break the while loop
            # to exit the program
            break

        # in case, user enter option other than 1, 2, 3 and 4 for main-menu
        else:
            print("Invalid Option !!! Input should be only a whole number between 1 and 4 (both inclusive).")

        print()