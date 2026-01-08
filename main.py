# ====================
# ISI UTAMA KODE
# ====================
while True:
    angka1 = input("Masukkan angka pertama (atau 'exit' untuk keluar): ")
    if angka1.lower() == 'exit':
        print("Program dihentikan. Terima kasih!")
        break

    try:
        angka1 = int(angka1)
    except ValueError:
        print("Input tidak valid, harus angka!")
        continue

    operator = input("Masukkan operator (+, -, /, *): ")

    angka2 = input("Masukkan angka kedua: ")
    
    try:
        angka2 = int(angka2)
    except ValueError:
        print("Input tidak valid, harus angka!")
        continue

    try:
        match operator:
            case '+':
                hasil = angka1 + angka2
            case '-':
                hasil = angka1 - angka2
            case '*':
                hasil = angka1 * angka2
            case '/':
                hasil = angka1 / angka2
            case _:
                print('Operator tidak valid!')
                hasil = None
    except ZeroDivisionError:
        print('Tidak bisa membagi dengan nol!')
        hasil = None

    print("\n====================")
    print("Kalkulator Sederhana")
    print("====================")
    print(f"Angka Pertama : {angka1}")
    print(f"Operator      : {operator}")
    print(f"Angka Kedua   : {angka2}")

    if hasil is not None:
        print(f"\nHasil: {angka1} {operator} {angka2} = {hasil}")
    else:
        print("\nHasil: Operasi tidak dapat dilakukan.")

    confirm = input("Apakah anda masih ingin menggunakan kalkulator lagi? (Ya/Tidak): ")
    if confirm.lower() == 'ya':
        continue
    else:
        print("Terimakasih!")
        break
