#3种字符串拼接
"""
--------name of name ------
name:
age:
job:
salary:
"""
#1.字符串拼接
# name=input("name:")
# age=input("age:")
# job=input("job:")
# salary=input("salary:")
#
# msg = '''
# --------name of '''+name+''' ------
# name:'''+name+'''
# age:'''+age+'''
# job:'''+job+'''
# salary:'''+salary
# print(msg)

#2占位符（%s）
name1=input("name:")
age1=input("age:")
job1=input("job:")
salary1=input("salary:")
msg1="""
--------name of %s ------
name:%s
age:%s
job:%s
salary:%s
"""%(name1,name1,age1,job1,salary1)
print(msg1)
#3占位符（{}）
name1=input("name:")
age1=input("age:")
job1=input("job:")
salary1=input("salary:")
msg1="""
--------name of {_name} ------
name:{_name}
age:{_age}
job:{_job}
salary:{_salary}
""".format(_name=name1,_age=age1,_job=job1,_salry=salary1)
print(msg1)