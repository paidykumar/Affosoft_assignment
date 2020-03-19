def students(student):
    list=[]
    for i in student:
        for j in student:
            if i.split()[0]==j.split()[0] and i!=j:
                list.append(i)
    return len(list)
student=['Rosalinda Lundgren','Tilda Mckibben','Pandora Catania','Hue Granada','Hue pk','Tilda kumar','paidy kumar']
a=students(student);       
    
print(a)

"""
output=4
"""
