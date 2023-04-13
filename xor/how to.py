#อ่านไฟล์txt 

f = open('test_file.txt', 'r')
data = f.read().split('\n')
print(data)
f.close()