from unicodedata import digit

password = input('enter  new password:')
result = {}

if len(password)>=8:
    result["length"]=True
else:
    result["length"]=False
digit= False

for i in password:
     if i.isdigit():
         digit= True
result['digits']=digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase=True

result['upper-case']=uppercase
print(result)
print(result.values())
if all(result):
    print("strong password")
else:
    print("weak password")



