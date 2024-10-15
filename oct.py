# def sum(n):
#     if  n==0:
#         return 0
#     return n+sum(n-1)

# n=int(input("enter no for sums:"))
# print(f"sum of number {n} is:{sum(n)}")
def pattern(n):
    if n==0:
        return ""
    print("*"*n)
    pattern(n-1)

pattern(3)
# import pyttsx3
# engine.setProperty('voice', voices[1].id)   
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()
