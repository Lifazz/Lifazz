input_a = int(input("masukan nilai a :"))
input_b = int(input("masukan nilai b :"))
input_c = int(input("masukan nilai c :"))

if input_b < input_a and input_b < input_a :
    print(f"Nilai {input_a} lebih Besar dari {input_b} dan {input_c} ")
elif input_a < input_b and input_c < input_b :
    print(f"Nilai {input_b} Lebih Besar dari {input_a} dan {input_c} ")
elif input_b < input_c and input_a < input_c:
    print(f"Nilai {input_c} Lebih Besar dari {input_b} dan {input_a}")
elif input_a == input_b and input_a and input_b > input_c:
    print(f"Bilangan A {input_a} sama dengan bilangan B {input_b} dan dua bilangan tsb lebih besar dari {input_c}")
elif input_a == input_c and input_a and input_c > input_b:
    print(f"Bilangan A {input_a} sama dengan bilangan C {input_c} dan dua bilangan tsb lebih besar dari {input_b}")
elif input_b == input_c and input_b and input_c > input_a:
    print(f"Bilangan B {input_b} sama dengan bilangan C {input_c} dan dua bilangan tsb lebih besar dari {input_a}")
else:
    print(f"Bilangan A {input_a} Bilangan B {input_b} Bilangan C {input_c} Sama Besar")
    
