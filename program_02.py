def Attendance(self,college):
     lst = []
     students=[]
    for student in students:
        for sheet in college:
            dic = {}
            if student == sheet.student_id.id and \
                        not sheet.present:
                dic = {
                        student: sheet.attendance_date
                    }
                lst.append(dic)
    for student in lst:
        print(student)

"""
college=attendance sheet model
fields are -->student_id
        -->present
        -->attendance_date
"""
    
