# myname="emobilis"
# for i in myname:
#     if i==k:

# try:
#     # code that may raise exception
#     result=1/0
# except ZeroDivisionError as e:
#     # code to handle exception
#     print(f"An error has occured {e}")
# finally:
#     # code that runs no matter what
#     print("This will always be printed")

jina=['banana','mangoes','apples']

try:
    for i in range(5):
        print(i, jina[i])
except:
        print("index out of range")
