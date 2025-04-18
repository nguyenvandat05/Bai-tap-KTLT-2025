def find_longest_words(text):
    words = text.split()
    max_length = len(max(words, key=len))
    longest_words = [word for word in words if len(word) == max_length]
    return longest_words
text = """nguyen van dat sinh vien nganh dien tu vien thong vien ky thuat cong nghe truong dai hoc vinh"""
print(find_longest_words(text))
print("Sinh viên: Nguyen Van Dat")
print(" MSSV: 235752020710019")