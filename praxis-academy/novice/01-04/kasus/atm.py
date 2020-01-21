class ATM:
    def __init__(self,balance,withdraw,deposit):
        self.balance = balance
        self.withdraw = withdraw
        self.deposit = deposit
    
    def tambahdepo (self,tmbhdepo):
        depo = tmbhdepo
        self.balance+= depo

    def kurangbal (self,ambil):
        kurng = ambil
        self.balance-= kurng

akun = ATM(0,0,0)
def atmsederhana():
    print ("=================================")
    print ("            Simple ATM")
    print ("=================================")

    print ("    Pilih Transaksi ATM")
    print ("    1. Deposit")
    print ("    2. Withdraw")
    print ("    3. Balanced")
    print ("    4. Exit")

    pilih = input("Masukkan Pilihan: ")

    if pilih == "1":
        tmbh = input ("masukkan jumlah deposit: ")
        akun.tambahdepo(int(tmbh))
        print("total balanced anda : ",akun.balance)
        loop()
        # print ("PILIH 1")
    elif pilih == "2":
        kurang = input("masukkan jumlah withdraw: ")
        akun.kurangbal(int(kurang))
        print("sisa saldo :",akun.balance)
        loop()
    elif pilih == "3":
        if akun.balance == 0:
            print ("Saldo anda Kosong, Mohon melakukan Deposit")
            loop()
        else:
            print("total balanced anda: ",akun.balance)
            loop()
    elif pilih == "4":
        print ("Exit")
    else:
        print ("pilihan tidak tersedia")
        # loop()
def loop():
    print("====================================")
    x = input ("ingin melakukan transaksi lain: ")
    if x == "y" or x == "Y":
        atmsederhana()
    else:
        print("Terimakasih")


atmsederhana()
