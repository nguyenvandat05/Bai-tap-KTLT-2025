input_str = input("Nhập danh sách số, cách nhau bởi dấu phẩy: ")
numbers = [int(x) for x in input_str.split(",")]
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Các số lẻ là:", ",".join(map(str, odd_numbers)))
print("Nguyễn Văn Đạt")
print("MSSV:235752020710019")