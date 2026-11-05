#! WAP which yields even number 50 -70 

def even_gen():
    for i in range(50,71):
        if i % 2 == 0:
            yield i 
            print(tuple(even_gen()))