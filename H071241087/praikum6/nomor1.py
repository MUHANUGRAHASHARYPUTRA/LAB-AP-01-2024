inventory = {}

def tampilkan_menu():
    print("\n=== Menu Inventory Barang ===")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Tampilkan Daftar Barang")
    print("4. Cari Barang")
    print("5. Update Data Barang")
    print("6. Keluar")
    
def tambah_barang():
    kode_barang = input("Masukkan Kode Barang: ")
    nama_barang = input("Masukkan Nama Barang: ")
    jumlah = int(input("Masukkan Jumlah: "))
    harga = float(input("Masukkan Harga: "))
    inventory[kode_barang] = {'nama': nama_barang, 'jumlah': jumlah, 'harga': harga}
    print(f"Barang '{nama_barang}' berhasil ditambahkan.")

def hapus_barang():
    kode_barang = input("Masukkan Kode Barang yang ingin dihapus: ")
    if kode_barang in inventory:
        del inventory[kode_barang]
        print("Barang berhasil dihapus.")
    else:
        print("Kode barang tidak ditemukan.")

def tampilkan_barang():
    if not inventory:
        print("Tidak ada barang dalam inventory.")
    else:
        print("\nDaftar Barang:")
        for kode, info in inventory.items():
            print(f"Kode: {kode}, Nama: {info['nama']}, Jumlah: {info['jumlah']}, Harga: {info['harga']}")

def cari_barang():
    kode_barang = input("Masukkan Kode Barang yang ingin dicari: ")
    if kode_barang in inventory:
        info = inventory[kode_barang]
        print(f"Barang Ditemukan - Kode: {kode_barang}, Nama: {info['nama']}, Jumlah: {info['jumlah']}, Harga: {info['harga']}")
    else:
        print("Kode barang tidak ditemukan.")

def update_barang():
    kode_barang = input("Masukkan Kode Barang yang ingin diperbarui: ")
    if kode_barang in inventory:
        nama_barang = input("Masukkan Nama Baru: ")
        jumlah = int(input("Masukkan Jumlah Baru: "))
        harga = float(input("Masukkan Harga Baru: "))
        inventory[kode_barang] = {'nama': nama_barang, 'jumlah': jumlah, 'harga': harga}
        print("Data barang berhasil diperbarui.")
    else:
        print("Kode barang tidak ditemukan.")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            hapus_barang()
        elif pilihan == '3':
            tampilkan_barang()
        elif pilihan == '4':
            cari_barang()
        elif pilihan == '5':
            update_barang()
        elif pilihan == '6':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
