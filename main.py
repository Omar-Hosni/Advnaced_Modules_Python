import re
import time
import timeit
import zipfile
import shutil

text = 'My phone number is 408-555-1234'

phone = re.search(r'\d{3}-\d{3}-\d{4} ', text)
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

results = re.search(phone_pattern, text)

print(results.group())

search = re.search(r'cat|dog' , 'The cat is here')

print(search.span())

all = re.findall(r'.at' , 'this cat in the hat went splat')

print(all)

def func_one(n):
    return [str(num) for num in range(n)]

print(func_one(10))

def func_two(n):
    return list(map(str, range(n)))

print(func_two(10))
print("\n")
# We are going to use time module to calculate the time each of the above function takes

start_time = time.time()
result = func_one(1000000)
end_time = time.time()

elapsed_time = end_time - start_time

print(elapsed_time)

statement = ''' 
func_one(100)
'''

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

print(timeit.timeit(statement, setup, number=1000000))

#Zipping files and compressing them + Extracting files

f = open('fileone.txt' , 'w+')
f.write('ONE FILE')
f.close()

f = open('filetwo.txt', 'w+')
f.write('TWO FILE')
f.close()

comp_file = zipfile.ZipFile('comp_file.zip', 'w')

comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)

comp_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)

comp_file.close()

#Extracting the compressed file above
zip_obj = zipfile.ZipFile('comp_file.zip', 'r')

zip_obj.extractall('extracted_content')


#lets convert the extracted_content into a compressed file

dir_to_zip = 'C:\\Users\\Custom PC\\Desktop\\Python\\initial-project\\extracted_content'

output_filename = 'example'

shutil.make_archive(output_filename, 'zip', dir_to_zip)


#Extracting Files
shutil.unpack_archive('example.zip' , 'final_unzip', 'zip')
