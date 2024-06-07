import pandas as pd
import matplotlib.pyplot as plt

# Membaca file data baru
data = pd.read_csv('Khayla.csv')

# Menampilkan lima baris pertama data
print("Lima baris pertama data:")
print(data.head())

# Menampilkan informasi umum tentang data
print("\nInformasi umum tentang data:")
print(data.info())

# Menampilkan ringkasan statistik tentang data numerik
print("\nRingkasan statistik tentang data:")
print(data.describe())

# Menampilkan jumlah data yang hilang (missing values) dalam setiap kolom
print("\nJumlah data yang hilang dalam setiap kolom:")
print(data.isnull().sum())

# Menampilkan jumlah unik dari setiap nilai dalam suatu kolom
print("\nJumlah nilai unik dalam setiap kolom:")
print(data.nunique())

# Menampilkan tipe data dari setiap kolom
print("\nTipe data dari setiap kolom:")
print(data.dtypes)

# Scatter Plot
plt.subplot(2, 2, 1)
plt.scatter(data['new_usia'], data['new_gaji'], color='blue', alpha=0.5)
plt.title('Scatter Plot')
plt.xlabel('Usia')
plt.ylabel('Gaji')

# Histogram
plt.subplot(2, 2, 2)
plt.hist(data['new_gaji'].dropna(), bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Gaji')
plt.xlabel('Gaji')
plt.ylabel('Frequency')

# Box Plot
plt.subplot(2, 2, 3)
plt.boxplot(data['new_usia'].dropna())
plt.title('Box Plot of Usia')
plt.ylabel('Usia')

# Membuat data untuk barplot jenis kelamin
# Misalnya kolom 'jenis_kelamin' memiliki nilai 'pria' dan 'wanita'
gender_data = data['jenis_kelamin'].value_counts().index.tolist()
count_data = data['jenis_kelamin'].value_counts().tolist()

# Membuat barplot
plt.subplot(2, 2, 4)
plt.bar(gender_data, count_data, color=['blue', 'pink'])
plt.title('Barplot Jenis Kelamin')
plt.xlabel('Jenis Kelamin')
plt.ylabel('Jumlah')

# Menampilkan semua visualisasi dalam satu window
plt.tight_layout()
plt.show()