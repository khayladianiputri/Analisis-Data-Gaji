# Analisis-Data-Gaji
Khayla Diani Putri_12030122140310

Interpretasi Data

•	Usia (new_usia): Usia rata-rata adalah sekitar 30 tahun, dengan standar deviasi sekitar 5.9 tahun, yang menunjukkan variasi usia dalam data. Usia minimum adalah 22 tahun dan usia maksimum adalah 40 tahun.

•	Gaji (new_gaji): Gaji rata-rata adalah 5910, dengan standar deviasi sekitar 650. Gaji minimum adalah 5000 dan gaji maksimum adalah 7000.

Jumlah Data yang Hilang dalam Setiap Kolom
plaintext
Copy code
new_usia        0
new_gaji        0
jenis_kelamin   0
dtype: int64
Interpretasi: Tidak ada data yang hilang dalam setiap kolom.
Jumlah Nilai Unik dalam Setiap Kolom
plaintext
Copy code
new_usia        10
new_gaji        10
jenis_kelamin    2
dtype: int64
Interpretasi: Kolom new_usia dan new_gaji memiliki 10 nilai unik masing-masing, menunjukkan bahwa setiap individu memiliki usia dan gaji yang berbeda. Kolom jenis_kelamin memiliki 2 nilai unik (pria dan wanita).
Tipe Data dari Setiap Kolom
plaintext
Copy code
new_usia         int64
new_gaji         int64
jenis_kelamin    object
dtype: object
Interpretasi: Kolom new_usia dan new_gaji bertipe data numerik (int64), sedangkan jenis_kelamin bertipe data objek (string).

Visualisasi Data
1.	Scatter Plot
	Interpretasi: Scatter plot menunjukkan hubungan antara usia dan gaji. Tidak ada pola yang jelas terlihat, menunjukkan bahwa gaji tidak memiliki korelasi yang kuat dengan usia dalam dataset ini.
2.	Histogram
	Interpretasi: Histogram dari gaji menunjukkan distribusi gaji yang relatif normal dengan sedikit skew ke kanan. Sebagian besar individu memiliki gaji antara 5000 hingga 7000.
3.	Box Plot
	Interpretasi: Box plot dari usia menunjukkan rentang usia dari 22 hingga 40 tahun, dengan beberapa nilai di atas usia 33, yang mungkin menunjukkan individu yang lebih tua dalam kelompok data ini.
4.	Barplot Jenis Kelamin
	Interpretasi: Barplot jenis kelamin menunjukkan jumlah yang sama antara pria dan wanita dalam dataset, dengan 5 pria dan 5 wanita.

![Screenshot 2024-06-07 133357](https://github.com/khayladianiputri/Analisis-Data-Gaji/assets/167163746/80249261-5b31-4a94-9afe-1336014a220f)

Kesimpulan
Data ini memberikan gambaran singkat tentang demografi usia, gaji, dan jenis kelamin dari 10 individu. Visualisasi menunjukkan bahwa gaji tidak secara langsung berkorelasi dengan usia, distribusi gaji cenderung normal, dan distribusi usia tidak menunjukkan outlier yang signifikan. Dataset ini seimbang dalam hal distribusi jenis kelamin, dengan jumlah pria dan wanita yang sama.
