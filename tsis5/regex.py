import re
with open('row.txt', 'r', encoding='utf-8') as file:
    data = file.read()


# 1. 
pattern1 = r'a*b'
matches1 = re.findall(pattern1, data)
print("Matches for pattern 1:", matches1)

# 2. 
pattern2 = r'ab{2,3}'
matches2 = re.findall(pattern2, data)
print("Matches for pattern 2:", matches2)

# 3. 
pattern3 = r'[a-z]+_[a-z]+'
matches3 = re.findall(pattern3, data)
print("Matches for pattern 3:", matches3)

# 4.
pattern4 = r'[A-Z][a-z]+'
matches4 = re.findall(pattern4, data)
print("Matches for pattern 4:", matches4)

# 5. 
pattern5 = r'a.*?b'
matches5 = re.findall(pattern5, data)
print("Matches for pattern 5:", matches5)

# 6. 
pattern6 = r'[ ,.]'
replaced_text6 = re.sub(pattern6, ':', data)
print("Replaced text for pattern 6:", replaced_text6)

# 7. 
snake_case_string = "this_is_a_test_string"
camel_case_string = ''.join(word.capitalize() for word in snake_case_string.split('_'))
print("Camel case string from snake case :", camel_case_string)

# 8. 
pattern8 = r'[A-Z][a-z]*'
split_text8 = re.findall(pattern8, camel_case_string)
print("Split text for pattern 8:", split_text8)

# 9.
pattern9 = r'([A-Z][a-z]*)'
replaced_text9 = re.sub(pattern9, r' \1', camel_case_string).strip()
print("Replaced text:", replaced_text9)

# 10. 
camel_case_string = "ThisIsATestString"
snake_case_string = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_string).lower()
print("Snake case string from camel case:", snake_case_string)