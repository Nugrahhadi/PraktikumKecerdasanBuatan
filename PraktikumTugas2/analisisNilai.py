#Library
import numpy as np 
import matplotlib.pyplot as plt 

def main ():
    nilai_siswa = []

    while True:
        try:
            input_nilai = input("Masukkan nilai siswa (ketik 'selesai' untuk mengakhiri): ")

            if input_nilai.lower() == 'selesai':
                break

            nilai = float(input_nilai)

            if 0 <= nilai <= 100:
                nilai_siswa.append(nilai)
            else:
                print("Nilai harus yang anda masukkan harus diantara 0-100!")

        except ValueError:
            print("Input tidak valid! Masukan angka atau 'selesai'")

    if not nilai_siswa:
        print("Tidak ada data yang dimasukkan.")
        return
    
    hasil_analisis = {}
    hasil_analisis['rata_rata'] = np.mean(nilai_siswa)
    hasil_analisis['nilai_tertinggi'] = np.max(nilai_siswa)
    hasil_analisis['nilai_terendah'] = np.min(nilai_siswa)
    hasil_analisis['standar_deviasi'] = np.std(nilai_siswa)

    kategori_nilai = []

    for nilai in nilai_siswa:
        if nilai >= 80:
            kategori_nilai.append('A')
        elif nilai >= 70:
            kategori_nilai.append('B')
        elif nilai >= 60:
            kategori_nilai.append('C')
        elif nilai >= 50:
            kategori_nilai.append('D')
        else:
            kategori_nilai.append('E')

    ketegori_unik = set(kategori_nilai)

    frekuensi_kategori = {}
    for kategori in ketegori_unik:
        frekuensi_kategori[kategori] = kategori_nilai.count(kategori)

    print("\nHASIL ANALISIS DATA")
    print(f"Jumlah data: {len(nilai_siswa)}")
    print(f"Rata-rata nilai: {hasil_analisis['rata-rata']:.2f}")
    print(f"Nilai tertinggi: {hasil_analisis['nilai_tertinggi']}")
    print(f"Nilai terendah: {hasil_analisis['nilai_terendah']}")
    print(f"Standar deviasi: {hasil_analisis['standar_deviasi']:.2f}")

    print("\nDistribusi Kategori Nilai:")
    for kategori, jumlah in sorted(frekuensi_kategori.items()):
        print(f"Kategori {kategori}: {jumlah} siswa")

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.hist(nilai_siswa, bins=10, color='skyblue', edgecolor='black')
    plt.title('Histogram Nilai Siswa')
    plt.xlabel('Nilai')
    plt.ylabel('Frekuensi')
    plt.grid(True, linstyle='--', alpha=0.7)

    plt.subplot(1, 2, 2)
    kategori_labels = list(frekuensi_kategori.keys())
    frekuensi = list(frekuensi_kategori.values())

    if len(kategori_labels) > 0:
        plt.pie(frekuensi, labels=kategori_labels, autopct='%1.1f%%', startangle=90, colors=['gold', 'lightgreen', 'lightcoral', 'lightskyblue', 'lightpink'])
        plt.title('Distribusi Kategori Nilai')
    else:
        plt.text(0.5, 0.5, 'Tidak ada data', horizontalalignment='center', verticalalignment='center')

    plt.tight_layout()
    plt.show()

    if __name__ == "__main__":
        print("==== PROGRAM ANALISIS NILAI SISWA ====")
        print("Program ini menganalisis nilai siswa dan menampilkan statistik dasar serta visualisasi data.")
        main()