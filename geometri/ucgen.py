print("1)pisagor teoremi \n 2)üçgende alan")
choice = input("işlemi seçiniz: ")

def pythagoras(a, b):
    if a==b:
        print(f"Hipotrenüs = {a} kök2")
    if b ==2*a:
        print(f"{b}kök5")
    if a ==2*b:
        print(f"{b}kök5")
    else:
        c = (a**2 + b**2)**0.5
        print(f"Hipotenüs = {c}")

def area(h,a):
    area = (h*a)/2
    print(f"Üçgenin alanı = {area}")



if choice == "1":
    a = int(input("A kenarını giriniz: "))
    b = int(input("B kenarını giriniz: "))
    pythagoras(a,b)
elif choice == "2":
    h = int(input("Yüksekliği giriniz veya bir dik kenarı: "))
    a = int(input("Tabanı giriniz veya diğer dik kenarı: "))
    area(h,a)
