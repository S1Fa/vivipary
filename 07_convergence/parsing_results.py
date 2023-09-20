import os

def check_3_cb(input_dir):
    path = '/public1/user/sifa/projects/vivipary/07_convergent_analy'
    files = os.listdir(os.path.join(path, input_dir))
    if 'csubst_cb_3.tsv' in files:
        print(f'{input_dir} has cb_3 !')
        return input_dir
    else:
        return

def check_4_cb(input_dir):
    path = '/public1/user/sifa/projects/vivipary/07_convergent_analy'
    files = os.listdir(os.path.join(path, input_dir))
    if 'csubst_cb_4.tsv' in files:
        print(f'{input_dir} has cb_4 !!')
        return input_dir
    else:
        return

if __name__ == "__main__":
    csubst_output_path = '/public1/user/sifa/projects/vivipary/07_convergent_analy'

    cb_3_list = []
    cb_4_list = []

    for dir in os.listdir(csubst_output_path):
        cb_3 = check_3_cb(dir)
        cb_4 = check_4_cb(dir)
        if cb_3 != None:
            cb_3_list.append(cb_3)
        if cb_4 != None:
            cb_4_list.append(cb_4)

print("========")
print(cb_3_list)
print(len(cb_3_list))
print(cb_4_list)
print(len(cb_4_list))