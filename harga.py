from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Fungsi untuk menghitung harga final dan membulatkannya
def kalkulasi_harga_final_bulat(panjang, lebar):
    # Menghitung Luas dalam cm2
    luas_cm2 = panjang * lebar
    
    # Menghitung Benang ((Lebar/270) * 9000)
    benang = (luas_cm2 / 270) * 9000
    
    # Menghitung Sticker
    sticker = 0

    # Menghitung Pakcaging
    pakcaging = 0

    # Menghitung Kabel Ties
    kabel_ties = 0

    # Menghitung Lem
    lem = 0

    # Menghitung Kain (Lebar * 3,5)
    kain = luas_cm2 * 3.5
    
    # Menghitung Tenaga ((Benang + Sticker + Packaging + Kabel Ties + Lem + Kain) * 25%)
    tenaga = (benang + sticker + pakcaging + kabel_ties + lem + kain) * 0.25
    
    # Menghitung Drop Harga (Benang + Sticker + Packaging + Kabel Ties + Lem + Kain + Tenaga)
    drop_harga = benang + sticker + pakcaging + kabel_ties + lem + kain + tenaga
    
    # Menghitung Listrik sebagai Drop Harga * 10%
    listrik = drop_harga * 0.10
    
    # Menghitung Waktu Estimasi Kerja (Lebar * 6) dalam Menit
    waktu_estimasi_kerja_detik = luas_cm2 * 6
    
    # Mengkonversi Waktu Estimasi Kerja ke dalam Jam dan Hari
    waktu_estimasi_kerja_menit = waktu_estimasi_kerja_detik / 60
    waktu_estimasi_kerja_jam = math.ceil(waktu_estimasi_kerja_menit / 60)
    waktu_estimasi_kerja_hari = math.ceil(waktu_estimasi_kerja_jam / 24)  # Membulatkan ke atas untuk hari
    
    # Menghitung Harga Final (Listrik + Semua biaya lain)
    harga_final = listrik + benang + sticker + pakcaging + kabel_ties + lem + kain + tenaga + drop_harga
    
    # Membulatkan harga final ke atas
    harga_final_bulat = math.ceil(harga_final)
    
    # Format Harga Final menjadi Rupiah (tanpa koma)
    harga_final_rupiah = f"IDR {harga_final_bulat:,}".replace(",", ".")

    # # Menghitung Sub-total dan Down Payment
    # Total = harga_final_rupiah - DownPayment


    return {
        'luas_cm2': luas_cm2,
        'waktu_estimasi_kerja_detik': waktu_estimasi_kerja_detik,
        'waktu_estimasi_kerja_menit': waktu_estimasi_kerja_menit,
        'waktu_estimasi_kerja_jam': waktu_estimasi_kerja_jam,
        'waktu_estimasi_kerja_hari': waktu_estimasi_kerja_hari,
        'harga_final_rupiah': harga_final_rupiah
        # 'Total': Total
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    panjang = ''
    lebar = ''
    # DownPayment =''
    hasil = None
    if request.method == 'POST':
        panjang = request.form['panjang']
        lebar = request.form['lebar']
        if panjang and lebar:
            hasil = kalkulasi_harga_final_bulat(float(panjang), float(lebar))
    return render_template('index.html', panjang=panjang, lebar=lebar, hasil=hasil)

if __name__ == '__main__':
    app.run(debug=True)
