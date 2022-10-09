# Link to katalog : https://tugas2pbp.herokuapp.com/

## Muhammad Naufal Zaky Alsar 
## 2106752041

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html

![bagan django](https://user-images.githubusercontent.com/88728529/189529895-82dcd43c-34c8-4bda-905c-4d661211a01b.png)

urls.py berguna untuk melakukan routing terhadap url dengan views.py yang bersesuaian yang dimana urls.py akan memanggil views.py. views.py berguna untuk menerima request http dan mengembalikan respons http seperti HTML. Berkas HTML berguna untuk menampilkan aplikasi yang diinginkan pada web browser. models.py berguna untuk membuat struktur data yang akan digunakan untuk website yang ingin dibuat dan models.py juga berguna untuk membaca database.

Oleh karena itu dari bagan tersebut user akan membuka project django dimana project django itu akan mengirimkan data ke urls.py yang dimana urls.py akan menentukan views.py mana yang akan digunakan setelah itu views.py tersebut akan mengambil data dari models.py yang dimana model tersebut yang akan memberitahu views.py struktur data apa yang dipakai di database dan setelah itu views.py akan mengambil data dari HTML yang dimana dengan menggabungkan HTML dan models.py maka data dari database dapat ditampilkan dalam bentuk HTML yang disusun oleh views setelah itu views akan mengirimkan HTML yang sudah terisi data dari database dengan menggunakan models.py dan yang terakhir views.py mengirimkan berkas HTML tersebut ke project django dan setelah itu project django tersebut mengirimkan berkas HTML ke pengguna.

### Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Kita memakai virtual environment supaya dapat mengelola *packages* Python untuk proyek-proyek lain agar kita tidak menginstall packages Python secara global yang dimana dapat merusak alat sistem atau proyek lainnya. Kita tetap dapat menmbuat aplikasi web berbasis Django tanpa menggunakan virtual environemnt tetapi seperti poin sebelumnya bisa saja dengan meng-*install* secara global dapat merusak alat sistem atau proyek lainnya.

### Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas

    1. Pertama saya membuat fungsi show_katalog agar dapat merender models dengan mengembalikannya dalam HTML
    2. Kedua saya melakukan routing antara views.py dengan katalog.html dengan memberikan nama file HTML yang saya ingin pakai yaitu katalog.html
    3. Ketiga saya membuat FILLME! menjadi {{nama}} agar dapat menampilkan nama saya yang sudah saya definisikan pada context pada views.py dan FILLME! kedua saya ganti menjadi {{npm}} supaya dapat menampilkan NPM saya yang sudah saya definisikan pada context pada views.py dan yang terakhir saya membuat *for loop* di katalog.html untuk menapilkan barang-barang pada katalog beserta atribut-atributnya yang sudah saya kodekan pada katalog.html
    4. Terakhir saya membuat repository secret dengan key HEROKU_API_KEY dan HEROKU_APP_NAME dan saya isikan keynya dengan value yang bersesuaian
