a = int(input("x**2'nin katsayısını giriniz: "))
b = int(input("x'in katsayısını giriniz: "))
c = int(input("Sabit terimi giriniz: "))

delta = b**2 - 4 * a * c

def is_roots_correct(x1, x2):
    equation1 = a * x1**2 + b*x1 + c 
    equation2 = a * x2**2 + b*x2 + c 
    if equation1 == 0:
        print(f"denklemin bir kökü {x1}dir.")
    else:
        pass
    if equation2 == 0:
        print(f"denklemin bir kökü {x2}dir.")
    else:
        pass


if a>0 or delta>0:
   x1 = (- b + delta**0.5) / (2* a)
   x2 = (- b - delta**0.5) / (2* a)
   is_roots_correct(x1, x2)
else:
   print("x**2'nin katsayısı 0 dan küçük olamaz.")
    