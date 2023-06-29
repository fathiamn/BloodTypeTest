print("----- Selamat Datang di Program Analisis Golongan Darah! -----")

while True:
    while True:
        print("\n\nPilihan Menu Program : ")
        print("1. Kombinasi Golongan Darah \n2. Petunjuk Program \n3. Exit Program")
        menu = int(input("\nMasukkan Pilihan Program : "))
        
        if menu == 1:
            while True:
                id = input("Nama Lengkap: ")
                print("Pilihan Kombinasi Golongan Darah: ")
                print("1. Golongan Darah A dan A \n2. Golongan Darah A dan B \n3. Golongan Darah A dan 0 \n4. Golongan Darah A dan AB\n")
                print("5. Golongan Darah B dan A \n6. Golongan Darah B dan B \n7. Golongan Darah B dan 0 \n8. Golongan Darah B dan AB\n")
                print("9. Golongan Darah 0 dan A \n10. Golongan Darah 0 dan B \n11. Golongan Darah 0 dan 0 \n12. Golongan Darah 0 dan AB\n")
                print("13. Golongan Darah AB dan A \n14. Golongan Darah AB dan B \n15. Golongan Darah AB dan 0 \n16. Golongan Darah AB dan AB\n")
                menu = int(input("\nMasukkan Pilihan Kombinasi : "))
                
                if menu == 1:
                    golDarah = "O, A" # A dengan A
                elif menu == 2:
                    golDarah = "O, A, B, AB" # A dengan B
                elif menu == 3:
                    golDarah = "O, A" # A dengan O
                elif menu == 4:
                    golDarah = "A, B, AB" # A dengan AB
                elif menu == 5:
                    golDarah = "O, A, B, AB" # B dengan A
                elif menu == 6:
                    golDarah = "O, B" # B dengan B
                elif menu == 7:
                    golDarah = "O, B" # B dengan O
                elif menu == 8:
                    golDarah = "A, B, AB" # B dengan AB
                elif menu == 9:
                    golDarah = "O, A" # O dengan A
                elif menu == 10:
                    golDarah = "O, B" # O dengan B
                elif menu == 11:
                    golDarah = "O" # O dengan O
                elif menu == 12:
                    golDarah = "A, B" # O dengan AB
                elif menu == 13:
                    golDarah = "A, B, AB" # AB dengan A
                elif menu == 14:
                    golDarah = "A, B, AB" # AB dengan B
                elif menu == 15:
                    golDarah = "A, B" # AB dengan 0
                elif menu == 16:
                    golDarah = "A, B, AB" # AB dengan AB
                else:
                    print("Tolong masukkan input dengan benar\n")
                    golDarah = "Tidak Dapat Ditentukan"
                
                print("\nHalo", id, "!")
                print("Berdasarkan tabel pewarisan golongan darah, \nKemungkinan golongan darah Anda:", golDarah)
                break
        
        elif menu == 2:
            print("Program ini akan dijalankan dengan langkah sebagai berikut: ")
            print("1. Pilih menu yang Anda inginkan, pilih menu 1 untuk melakukan kombinasi golongan darah")
            print("2. Setelah memilih menu 1, masukkan kombinasi yang sesuai dengan golongan darah ayah dan ibu Anda. Menu kombinasi tertera pada layar Anda")
            print("3. Setelah itu, program akan menampilkan hasil kombinasi golongan darah Anda")
            print("4. Apabila telah selesai menggunakan program, pilih menu 3 untuk keluar")
            break
        
        elif menu == 3:
            print("\nProgram Telah Selesai, Terima Kasih!")
            quit()
        
        elif menu < 1:
            print("Maaf, Input Invalid, Silakan Ulangi Kembali")
            continue
        
        elif menu > 3:
            print("Maaf, Input Invalid, Silakan Ulangi Kembali")
            continue
