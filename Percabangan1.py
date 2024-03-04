input_a = int(input("Masukan Bilangan yang akan di Bandingkan :"))
input_b = int(input("Masukan Bilangan yang akan di Bandingkan :"))

if input_a > input_b:
    print(f"{input_a} lebih besar dari {input_b}")
elif input_a > input_b:
    print(f"{input_b} lebih besar dari {input_a}")
else:
    print(f"Bilangan {input_a} sama besar Bilangan {input_b}")