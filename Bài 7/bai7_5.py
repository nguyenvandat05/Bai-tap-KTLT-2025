def file_append_and_read(fname):
    with open(fname, "a") as myfile:
        myfile.write("21 vothisau\n")
        myfile.write("15082005\n")
    with open(fname, "r") as txt:
        print(txt.read())
file_append_and_read('hieu.txt')
print("Sinh viên: Nguyen Van Dat")
print(" MSSV: 235752020710019")