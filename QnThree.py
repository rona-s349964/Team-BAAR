def decrypt(text):
    decrypted = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char)- 13 #key is 13
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26 #reverse the shifted change sign from + to - 
                elif shifted < ord('a'):
                    shifted += 26 #reverse the shifted change sign from - to + 
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26 #reverse the shifted change sign from + to - 
                elif shifted < ord('A'):
                    shifted += 26 #reverse the shifted change sign from - to + 
            decrypted += chr(shifted)
        else:
            decrypted += char
    return decrypted

code = """
        tybony_inevnoyr = 100  
        zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'] 
        qrs cebprff_ahzoref(): 
            tybony tybony_inevnoyr 
            ybpny_inevnoyr = 5 
            ahzoref = [1,2,3,4,5] 
            juvyr ybpny_inevnoyr > 0: 
                vs ybpny_inevnoyr % 2 == 0:
                    ahzoref.erzbir(ybpny_inevnoyr) 
                ybpny_inevnoyr -= 1 
            erghea ahzoref
        zl_frg = {1,2,3,4,5,5,4,3,2,1} 
        erfhyg = cebprff_ahzoref(ahzoref=z1_frg)
        qrs zbqvsl_qvpg():
                ybpny_inevnoyr = 10 
                zl_qvpg['xrl4'] = ybpny_inevnoyr 
        zbqvsl_qvpg(5) 
        qrs hcqngr_tybony(): 
            tybony tybony_inevnoyr 
            tybony_inevnoyr += 10 
        sbe v va enatr(5): 
            cevag(v) 
            v += 1 
        vs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10: 
            cevag('Pbaqvgvba zrg!') 
        vs 5 abg va zl_qvpg: 
            cevag('5 abg sbhaq va gur qvpgvbanel!') 
        cevag(tybony_inevnoyr) 
        cevag(zl_qvpg)
        cevag(zl_frg)"""
            
                


original_code = decrypt(code)
print(original_code)


#FIXING the code error q.n.3
# wrong decrypted code:
# global_variable = 100
# my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3']
# def process_numbers():
#     global global_variable
#     local_variable = 5
#     numbers = [1,2,3,4,5]
#     while local_variable > 0:
#         if local_variable % 2 == 0:
#             numbers.remove(local_variable)
#         local_variable -= 1
#     return numbers
# my_set = {1,2,3,4,5,5,4,3,2,1}
# result = process_numbers(numbers=my_set)
# def modify_dict():
#         local_variable = 10
#         my_dict['key4'] = local_variable
# modify_dict(5)
# def update_global():
#     global global_variable
#     global_variable += 10
# for i in range(5):
#     print(i)
#     i += 1
# if my_set is not None and my_dict['key4'] == 10:
#     print('Condition met!')
# if 5 not in my_dict:
#     print('5 not found in the dictionary!')
# print(global_variable)
# print(my_dict)
# print(my_set)


#syntax corrected code 
# FINAL CODE:
global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'} # dictionary ends with curly braces
def process_numbers(numbers): # parameter should be specified as during call of the function numbers argument is passed
    global global_variable
    local_variable = 5
    numbers = [1,2,3,4,5]
    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1
    return numbers
my_set = {1,2,3,4,5,5,4,3,2,1}
result = process_numbers(numbers=my_set)
def modify_dict(num): # specify num
        local_variable = 10
        my_dict['key4'] = local_variable
modify_dict(5)
def update_global():
    global global_variable
    global_variable += 10
for i in range(5):
    print(i)
    i += 1
if my_set is not None and my_dict['key4'] == 10: # 10 is found in the values of dictionary so condition met is printed
    print('Condition met!')
if 5 not in my_dict: # since 5 is in my_set but not in dictionary so it prints 5 is not found in the dictionary!
    print('5 not found in the dictionary!')
print(global_variable)
print(my_dict)
print(my_set)
