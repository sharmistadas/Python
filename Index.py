s = "Happy Raksha Bandhan"


#index()
print(s.index("p")) #2
print(s.index("a",6)) #7
print(s.index("a",7)) #7
print(s.index("h",13,20)) #17
#print(s.index("h",13,17)) # error
print(s.index("Happy")) #0
#print(s.index("sad")) # Error
print(s.index("a",18,18)) #Error 



#rindex()

print(s.rindex("a")) #18
print(s.rindex("Happy"))#0
print(s.rindex("h",8))#17
print(s.rindex("n",15,19))#15

#find()
print(s.find("b"))#-1
print(s.find("H",2))#-1
print(s.find("p",2,3))#2
print(s.find("Ban"))#13

#rfind()
print(s.rfind("n")) #19
print(s.rfind("a",6)) #18
print(s.rfind("a",14,18)) #14
print(s.rfind("dhan")) #16
print(s.rfind("z")) # -1
print(s.rfind("a",18,18)) #-1





