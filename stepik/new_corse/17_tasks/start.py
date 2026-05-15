#student_file = open('students.txt', 'r')

#sales_file = open('sales.txt', 'w')


#test_file = open('/home/archer73/test.txt','w')

#file = open('info.txt', 'r', encoding='utf-8')



file1 = open('students.txt', 'w')
file2 = open('customers.txt', 'w', encoding='utf-8')

print(file1.encoding)
print(file2.encoding)

file1.close()
file2.close()
