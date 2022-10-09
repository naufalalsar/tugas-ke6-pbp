# Muhammad Naufal Zaky Alsar

# 2106752041

# https://tugas2pbp.herokuapp.com/todolist/login/

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

1. Internal CSS
Kode CSS ditaruh pada di file HTMLnya. Kelebihannya adalah perubahan hanya terjadi pada satu halaman, Kekurangannya adalah perubahan hanya terjadi pada satu halaman

2. External CSS
Kode CSS ditaruh pada folder yang lain. Kelebihannya adalah html akan terlihat lebih rapih. Kekurangannya halaman belum tampil secara sempurna hingga file CSS selesai dipanggil

3. Inline CSS
Kode CSS ditaruh pada line yang diinginkan. Kelebihannya adalah hanya satu elemen yang terkena dampaknya. Kekurangannya adalah hanya satu elemen yang dapat terkena dampaknya.

## Jelaskan tag HTML5 yang kamu ketahui.

Video, tag HTML5 video dapat menampilkan video.
Audio, tag HTML5 audio dapat menampilkan audio.
Drag and Drop, seperti mendrop file pada suatu submisi (seperti di scele)

## Jelaskan tipe-tipe CSS selector yang kamu ketahui

class yang akan memilih class
element yang akan memilih element

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas

Saya menggunakan fitur-fitur bootstrap untuk membuat aplikasi saya, seperti cards, button, dan warna-warnanya. Dan juga style css sedikit.

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

Kegunaan CSRF token adalah untuk menghindari dari serangan siber. CSRF token bekerja dengan server mengirim token CSRF ke user dan mengcrosscheck dengan token user, jika user tidak mempunyai token atau tokennya tidak sama dengan yang ada server maka requestnya tidak akan di eksekusi. Jika CSRF token tidak ada di form maka input yang dikirim oleh user tidak akan di crosscheck dengan server sehingga tidak aman. CSRF tidak harus dipakai contohnya untuk method GET karena method GET didesain untuk data yang didesain untuk publik. Tetapi, jika method POST tidak dipakai dengan CSRF token maka akan tertimbul error karena method POST dipakai untuk data-data yang perlu diamankan sehingga perlu untuk dipakaikan CSRF token.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual

Bisa saja, tanpa menggunakan generator {{form.as_table}} bearti kita membuat form langsung pada HTMLnya. Contoh codingannya : 

```

<form method="POST" action="">

    {% csrf_token %}

    <table>
        <tr>
            <td>To do: </td>
            <td><input type="text" name="todo" placeholder="TO DO" class="form-control"></td>
        </tr>
                
        <tr>
            <td>Description: </td>
            <td><input type="text" name="description" placeholder="DESCRIPTION" class="form-control"></td>
        </tr>

        <tr>
            <td></td>
            <td><input class="btn login_btn" type="submit" value="Submit" href="{% url 'todolist:show' %}"></td>
        </tr>
    </table>
        
</form>

```

Dapat dilihat bahwa kita harus menulis semuanya secara manual dengan menggunakan bracket table dan isinya menggunakan tr dan td dan harus juga mendefinisikan atributnya

##  Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML

![form_handling_-_standard](https://user-images.githubusercontent.com/88728529/192574062-a13f6123-1a32-4fe8-ae28-890032f0f634.png)

Pertama yang dilakukan adalah melakukan page request terlebih dahulu ke user dan jika ini adalah request pertama user maka form akan dibuat kosong atau dalam default valuenya dan dikirim ke user. Jika user sudah mengisi form maka akan melakukan page request lagi tetapi sudah bukan pertama kalinya user memasuki data sehingga akan lanjut ke validate data jika data tidak valid maka pesan error akan muncul dan membuat user disuruh mengisi form lagi jika data sudah valid maka akan lanjut melakukan aksi dengan menyimpan data tersebut ke database dan setelah itu akan di proses oleh database dan di tampilkan ke user.

Referensi gambar : https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms
I do not own the image nor do i create the image. All credit goes to mozilla for creating the image and i do not take any monetary gain from this repo. 

##  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas

### Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya

Menjalankan python manage.py startapp todolist di commandpromt dan pergi ke settings.py di project django dan menambahkan todolist ke installed apps

###  Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist

Menambahkan todolist pada urls.py di project django

### Membuat sebuah model Task

Membuat model dengan attritbut seperti berikut :

```

user = models.ForeignKey(User, on_delete=models.CASCADE)
date = models.DateField(auto_now=True)
title = models.TextField()
description = models.TextField

```

ForeignKey berguna agar jika user dihilangkan maka task juga akan hilang, sedangkan auto_now=True agar saat task diinisialisasi maka date yang diambil adalah date sekarang

### Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik

Melakukannya sama dengan lab 3

### Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task

Menambahkan code berikut :

```

<button><a href="{% url 'todolist:create-task' %}">Tambah Task Baru</a></button>

```

Kode diatas berguna agar terdapat button yang akan menredirect user ke halaman create task agar dapat menambah task

``` 

'nama': request.user.username

<p>{{nama}}</p>

```

Kode diatas berguna agar username dapat ditampilkan ke HTML dengan mendapatkan username dari user yang sedang login

```

<button><a href="{% url 'todolist:logout' %}">Logout</a></button>

```

Kode diatas berguna agar user dapat logout dengan cara meredirect ke fungsi logout dan melakukan logout

```

<th>Judul To do</th>
<th>Tanggal</th>
<th>Deskripsi</th>

<th>{{todolist.title}}</th>
<th>{{todolist.date}}</th>
<th>{{todolist.description}}</th>

```

Kode diatas berguna agar di HTML dapat menampilkan judul, tanggal, deskripsi dari to do

### Membuat routing sehingga beberapa fungsi dapat diakses

```

path('register/', register, name='register'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
path('create-task/', tambahin, name='create-task'),
path('', show, name='show'),

```

Saya melakukannya dengan cara melakukan kode diatas dengan cara melakukan routing dengan fungsi yang benar yang berada di views.py

###  Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet

Sudah otomatis karena sudah ada workflow

### Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku

Saya melakukannya dengan cara register dan menambahkan 2 akun dan 3 task menggunakan tombol tambah task.

USER 1
username : test1
password : bakung2021

USER 2
username : test2
password : bakung2021













