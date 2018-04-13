-----------------------------------------
Nama : Aulia Fauzi Rahman
Email : aulia.fauzi.rahman1@gmail.com
-----------------------------------------

Terdapat 25 File yang terdiri dari :
 1 file README.txt 
 12 file program MapReduce (format .py)
 12 file output program (format .txt)

 Dataset yang digunakan terdiri dari dua file :
 1. userid-timestamp-artid-artname-traid-traname.tsv dengan kolom meliputi: userid, timestamp, artist_id, artist_name, track_id, track_song_name
 2. userid-profile.tsv dengan kolom meliputi : #id, gender, age, country, register_date

Program MapReduce yang dibuat dibagi menjadi dua bagian, bagian pertama digunakan untuk menganalisis pemutaran lagu dengan menggunkana input file :
userid-timestamp-artid-artname-traid-traname.tsv 

1.	count_artname.py menghitung keseluruhan berapa kali suatu artis/band diputar
	Output : count_artname.txt dengan format : "Nama Artis" "Jumlah diputar"

2.	count_by_user.py menghitung jumlah pemutaran lagu untuk masing-masing user
	Output : count_by_user.txt dengan format : "ProfileID" "Jumlah pemutaran lagu"

3.	count_traname.py menghitung berapa jumlah sebuah lagu diputar
	Output : count_traname.txt dengan format : "Judul lagu" "Jumlah pemutaran lagu"

4.	count_traname_annually.py menghitung berapa jumlah sebuah lagu diputar dalam satu tahun
	Output : count_traname_annually.txt dengan format : "Judul lagu" " dimainkan pada tahun" "Jumlah pemutaran lagu"

5.	count_traname_monthly.py menghitung berapa jumlah sebuah lagu diputar dalam satu bulan
	Output : count_traname_monthly.txt dengan format : "Judul lagu" " dimainkan pada tahun" "bulan" "Jumlah pemutaran lagu"

6.	sum_track_annually.py menghitung jumlah keseluruhan pemutaran lagu dalam satu tahun 
	Output : count_traname_annually.txt dengan format : "Tahun" "Jumlah pemutaran lagu"

7.	sum_track_monthly.py menghitung jumlah keseluruhan pemutaran lagu dalam satu tahun 
	Output : count_traname_monthly.txt dengan format : "Tahun" "Bulan" "Jumlah pemutaran lagu"

Bagian kedua bertujuan untuk menganalisis profil pengguna, input file : userid-profile.tsv

8. user_age.py menghitung jumlah pengguna berdasarkan umur
	Output : user_age.txt dengan format : "Umur" "Jumlah Pengguna"

9. user_country.py menghitung jumlah pengguna yang berasal dari negara tertentu 
	Output : user_country.txt dengan format : "Negara" "Jumlah Pengguna"

10. user_gender.py menghitung jumlah pengguna berdasarkan gender
	Output : user_gender.txt dengan format : "Gender" "Jumlah Pengguna"

11. user_register_date_annualy.py menghitung jumlah pengguna yang mendaftar berdasarkan tahun 
	Output : user_register_date_annualy.txt dengan format : "Tahun" "Jumlah Pengguna yang daftar"

12. user_register_date_monthly.py menghitung jumlah pengguna yang mendaftar berdasarkan tahun 
	Output : user_register_date_monthly.txt dengan format : "Tahun" "Bulan" "Jumlah Pengguna yang daftar"