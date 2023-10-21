

def file_operations(path, additional_info, start_pos, count_chars):
    with open(path,'w') as fl:
        fl.write(additional_info)
        fl.close
    with open(path,'r') as fl:
        fl.seek(start_pos)
        str = fl.read(count_chars)
        fl.close
        return str
    

print(file_operations("D:\Programing\Python\StudyGoIT\GoIT_Tasks\module_7/file.txt","Hello",2,1))