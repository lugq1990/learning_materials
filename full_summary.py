from collections import defaultdict
from fileinput import filename
import os


file_summary_start = """## Learning material


A repo that contains a list of files that contain materials are used to provide useful insights. 

"""


prefix = "https://github.com/lugq1990/learning_materials/tree/main"
file_extension = ".md"

file_dir = defaultdict(list)

for dir_name, folder_name, file_name_list in  os.walk('.'):
    for file_name in file_name_list:
        if dir_name.startswith('./.git') or not file_name.endswith('.md') or dir_name == '.':
            continue
        # file_path = os.path.join(dir_name, file_name)
        file_path = '/'.join([prefix, dir_name[2:], file_name])
        name = file_name.split('.')[-2]
        
        if dir_name not in file_dir:           
            file_dir[dir_name] = [{name: file_path}]
        else:
            file_dir[dir_name].append({name: file_path})
        
        
# write back into a file
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(file_summary_start)
    for key, file_list in file_dir.items():
        out_text = ""
        for i in range(len(file_list)):
            for k, v in file_list[i].items():
                if i == 0:
                    out_text += key[2:] + ":\n\n" + "[{}]({})\n".format(k, v) + "\n\n"
                else:
                    out_text += "" + "[{}]({})".format(k, v) + "\n\n"
        f.write(out_text)
        