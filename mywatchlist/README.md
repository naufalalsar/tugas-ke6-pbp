# NAMA : Muhammad Naufal Zaky Alsar

# NPM : 2106752041

# LINK HTML : https://tugas2pbp.herokuapp.com/mywatchlist/html/

# LINK JSON : https://tugas2pbp.herokuapp.com/mywatchlist/json/

# LINK XML : https://tugas2pbp.herokuapp.com/mywatchlist/xml/

## Jelaskan perbedaan antara JSON, XML, dan HTML!

Perbedaan HTML dengan XML adalah HTML lebih ditujukan untuk menampilkan data yang mudah/indah diliat user sedangkan XML hanya memfokuskan kepada transfer data/menyimpan data. Oleh karena itu, XML lebih baik dipakai jika memang tidak ada niatan untuk menampilkan data sedangkan HTML dipakai jika memang ingin menampilkan data. 

Perbedaan HTML dengan JSON adalah mirip dengan perbedaan HTML dengan XML dimana HTML lebih dipakai untuk menampilkan data dan mempercantik tampilan data sedangkan JSON dipakai untuk menyimpan data atau mentransfer data.

Perbedaan JSON dengan XML adalah :
    1. XML tidak mengsupport array sedangkan JSON mengsupport array.
    2. XML lebih susah dibaca bagi manusia untuk nama atributenya dan valuenya dibandingkan JSON.
    3. JSON tidak menggunakan endtag tidak seperti XML.
    4. JSON tidak bisa didokumentasikan(tidak bisa ada comment) sedangkan XML dapat dicomment.
    5. JSON hanya bisa menggunakan encoding UTF-8 tidak seperti XML yang bisa menggunakan beberapa encoding.

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Kita memerlukan data delivery karena untuk menampilkan/menyimpan/mengambil data kita perlu menggunakan data delivery. Misalnya di database terdapat data yang ingin kita ambil dan kita ingin kirimkan pada klien, maka kita harus menggunakan data delivery agar data dari database dapat sampai ke klien dengan format yang sudah kita tentukan. Contoh lainnya adalah jika kita ingin mendapatkan data dari klien ke server, kita harus menggunakan data delivery agar data dapat sampai ke database dengan format yang sesuai dan akhirnya datanya dapat diperoleh dan diolah.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas

### Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 pekan lalu

Pertama saya akan masuk ke command promt dan cd ke mana folder tugas pbp saya berada dan saya akan mengeksekusi code.

```
python manage.py startapp wishlist
```

Setelah itu saya akan memasukan mywatchlist ke INSTALLED_APPS di settings.py yang berada di folder project-django. Codenya :

```
INSTALLED_APPS = [
    ...,
    'mywatchlist',
]
```

### Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist

Yang saya lakukan adalah dengan pergi ke folder project_django dan ke file urls.py dan menambahkan 

```
path('mywatchlist/', include('mywatchlist.urls')),
```

Ke variable urlpattenrs, yang berguna agar urls.py pada di mywatchlist dapat diakses dan dipakai project_django. Sehingga, urls.py di mywatchlist dapat digunakan.

### Membuat sebuah model MyWatchList

Setelah itu saya pergi ke models.py yang berada di folde mywatchlist dan menambahkan code :

```
class myWatchList(models.Model):
    title = models.CharField(max_length=255)
    watched = models.CharField(max_length=3)
    rating = models.IntegerField()
    release_date = models.CharField(max_length=50)
    review = models.TextField()
```

Nantinya classnya akan bernama myWatchList yang dimana akan terdapat atribut title(judul), watched(sudah ditonton apa belum), rating(kebagusan filmnya), release_date(tanggal rilisnya dengan dimana film itu rilis saat tanggal itu), review(review film tersebut). 

Saya membuat model tersebut agar model dapat dipakai views yang dimana model tersebut akan digunakan untuk mendefinisikan atribut/data dari database.

Setelah itu saya menjalankan code 

```
python manage.py makemigrations
```

Untuk mempersiapkan migrasi skema model ke database Django lokal.

Sehabis itu, saya menjalankan code

```
python manage.py migrate
```

### Menambahkan minimal 10 data untuk objek MyWatchList yang sudah dibuat di atas

Pertama saya membuat folder yang bernama fixtures dan saya membuat file yang bernama pandorabox.json untuk membuat database saya dengan format json dan saya menambahkan data-data saya sehingga terdapat 10 objek.

Setelah itu saya pergi ke file Procfile dan menambahkan code 

```
release: sh -c 'python manage.py migrate && python manage.py loaddata pandorabox.json'
```

Agar database saya diload saat aplikasi saya dijalankan di heroku.

### Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format

HTML :

    ```
    def show_html(request):
    watchlist = myWatchList.objects.all()

    yes = 0
    no = 0
    
    for movie in watchlist:
        if(movie.watched == "Yes"):
            yes+=1
        else :
            no+=1

    if(yes >= no):
        message = "Selamat, kamu sudah banyak menonton!"
    else:
        message = "Wah, kamu masih sedikit menonton!"

    context = {
        'watchlist': watchlist,
        'nama': 'Muhammad Naufal Zaky Alsar',
        'npm' : '2106752041',
        'message' : message
        
        }
    return render(request, "kinomovies.html", context)
    ```

Code diatas adalah code yang saya digunakan untuk menampilkan data HTML-nya. watchlist berguna untuk mengambil data dari database sedangkan yes dan no digunakan untuk tau message apa yang akan ditampilkan. Setelah itu saya merender dengan file HTML yang bernama kinomovies.html yang dimana disana sudah saya definisikan akan ditampilkan kemana data yang berada di variabel context dari fungsi show_html(request). Nama berguna untuk mendefiniskan nama saya, NPM berguna untuk mendefinisikan NPM saya sedangkan message berguna untuk menampilkan message apa yang sesuai dengan banyaknya movie yang ditonton.

JSON :

    ```
    def show_json(request):

        data = myWatchList.objects.all()

        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

Code diatas berguna untuk mengirimkan data dengan tipe JSON. variabel data berguna untuk mengeload data dari database dan returnnya akan mereturn data dengan tipe JSON dengan mengserialize data menjadi JSON.

XML :

    ```
    def show_xml(request):

    data = myWatchList.objects.all()

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```

Code diatas berguna untuk mengirimkan data dengan tipe XML. variabel data berguna untuk mengeload data dari database dan returnnya akan mereturn data dengan tipe XML dengan mengserialize data menjadi XML.

### Membuat routing sehingga data di atas dapat diakses melalui URL

Saya melakukan hal itu dengan cara menambahkan code ini ke variabel urlpatterns yang berada di urls.py yang berada di folder mywatchlist

```
urlpatterns = [
    path('html/', show_html, name='show_html'),
    path('json/', show_json, name='show_json'),
    path('xml/', show_xml, name='show_xml'),
]
```

Yang dimana code tersebut berguna untuk melakukan hubungan urls yang dimasukan dengan fungsi apa yang dipanggil pada views.py. Contoh mywatchlist/html akan memanggil fungsi show_html di views.py yang berada di file views.py yang berada di folder mywatchlist yang dimana fungsi tersebut akan mengembalikan data HTML sehingga dapat ditampilkan ke browser.

### Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet

Karena repositori yang saya pakai adalah repositori tugas 2 pbp kemarin, deployment saya sudah otomatis dilakukan kecuali terdapat error yang dimana saat saya deploy tadi tidak terjadi error apapun. Sehingga, deployment saya lancar.

## Postman Screenshot

HTML :

![html postman](https://user-images.githubusercontent.com/88728529/191292088-c9614f37-21df-422c-a0ad-186df8cf8fb1.png)

JSON :

![json postman](https://user-images.githubusercontent.com/88728529/191292163-d2a2a948-374b-4d6a-be15-76df3091b3c4.png)


XML :

![xml postman](https://user-images.githubusercontent.com/88728529/191292240-b6eaed4a-0c89-4715-8bfc-2717fc07f3b5.png)




