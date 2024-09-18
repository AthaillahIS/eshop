Pertanyaan : Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). 
1. Membuat projek django: Sebelum project django dibuat kita harus menciptakan virtual environment pada folder project yang akan kita gunakan. Hal ini dilakukan untuk mengatur dependencies dan memisahkan default package device kita. Untuk menciptakan virtual env langkah-langkahnya sebagai berikut: 
  - buat folder project baru
  - jalankan python -m venv env (untuk membuat virtualenv baru) 3. aktifkan virtual env menggunakan command env\Scripts\activate
  - buat file requirenment.txt yang berisi dependencies yang harus diinstall
  - lakukan command pip install requirenment untuk menginstall seluruh dependencies yang ada pada file requirenment
  - jalankan command python manage.py startproject "nama projek" untuk membuat projek baru
2. Membuat aplikasi main pada proyek tersebut Pembuatan aplikasi main dapat dilakukan dengan menjalankan
  - python manage.py startapp "nama app". Untuk meciptakan app baru
3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
  - daftarkan "nama app" pada INSTALLED_APPS project tersebut
4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut. name price description
  untuk menambahkan data dalam model, kita dapat mendefinisikan datafield yang digunakan serta tipe data yang digunakan. contoh name = models.CharField(max_length=255) Data dalam model tersebut nantinya akan bisa digunakan dalam template html sehingga data yang 
  ditampilkan sesuai dengan data dalam model. Penambahan dapat dilakukan dengan syntax {{" name "}} 3. Jika kita menambahkan data baru dalam model, maka perlu dilakukan migrasi sehingga perubahan data yang kita tambahkan dapat teregistrasi. command yang dilakukan
  adalah :
  - python manage.py makemigrations (command ini digunakan untuk meregistrasikan perubahan yang terjadi)
  - python manage.py migrate (command ini digunakan untuk melakukan perubahan yang telah diregistrasi)
5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
  - Routing dilakukan dengan meninclude path pada views.py yang merender template dari main.html. Hal ini dilakukan dengan menambahkan command path('', show_main, name='show_main') pada url pattern app.
6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
  - agar url app kita teregistrasi dalam url projek dan views.py dapat ditampilkan, maka url pada app perlu di include kedalam url project dengan menambahkan command path('', include('main.urls')) dalam url pattern projek
7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
  Agar web yang kita buat dapat diakses dapat dilihat oleh orang lain dan tidak hanya berada dalam local host saja, maka kita perlu melakukan deployment pada server. Hal ini ini dilakukan dengan mengubah ALLOWED_HOST menjadi url deployment pws. ALLOWED_HOSTS = 
  ["localhost", "127.0.0.1", "url deployment pws"]
8. Jelaskan fungsi git dalam pengembangan perangkat lunak! Git merupaka sistem kontrol versi yang bermanfaat untuk melakukan kolaborasi dalam proses pengembangan perangkat lunak. Beberapa manfaatnya adalah sebagai berikut
  - Melacak perubahan kode (riwayat perubahaan kode)
  - Kolaborasi (git memungkinkan developer untuk bekerja secara bersamaan)
  - manajemen konflik (git membantu mengelola konflik yang terjadi saat 2 developer melakukan perubahan)
  - Penyimpanan (git menyimpan repositori kita secara lengkap beserta riwayatnya)
9. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
  Framework django telah memiliki resource pembelajaran yang banyak di internet. Django juga memudahkan developer dalam membuat web karena menyediakan automasi sesuai dengan prinsipnya D.R.Y (Don't Repeat Yourself).
10. Mengapa model pada Django disebut sebagai ORM?
  Model Django disebut sebagai ORM karena django mengimplementasikan teknik Object-Relational Mapping, yang menghubungkan objek Python dengan tabel basis data relasional. Django juga menyediakan API untuk melakukan operasi basis data. Dengan ORM, developer dapat fokus pada logika aplikasi tanpa harus memikirkan detail SQL.

<img width="8359" alt="Cara Kerja Framework Django" src="https://github.com/user-attachments/assets/e9cad905-9c71-48ba-aeb8-8fee61c2c4c6">


TUGAS 3
1. Membuat input form untuk menambahkan objek model pada app sebelumnya.
  Langkah-langkah yang perlu dilakukan untuk membuat input form adlaah
  - Membuat file forms.py. File ini digunakan untuk membuat metadata dari database yang akan digunakan untuk pembuatan form
  Kode :
  model = Entry untuk merujuk model yang diguanakan
  fields = [ 'item_name', 'price', 'description', 'rating'] untuk merujuk field yang akan dirender
  - Menambahkan objek form yang akan digunakan kedalam context pada show_main agar dapat dirender ke template
  - Buat method baru untuk merespond terhadap request POST yang dilakukan saat user client mengisi form dengan menambahkan def add_order_entry(request):
  - form = OrderEntryForm(request.POST or None) Untuk melihat isi field dari Order EntryForm apakah form sudah terisi saat user melakukan request POST 
  - form.save()
    return redirect('main:show_main')
    Save isi form user jika isi form valid dan redirect ke method show_main untuk merender main.html
  - tambahkan url path pada main/urls.py untuk routing add_ordder_entry/ ke view function add_order_entry dengan menambahkan path path('add_order_entry/', add_order_entry, name='add_order_entry'),
  - Buatlah file html untuk menampilakan form. Dalam app ini filenya adalah main.html yang mengekstend base.html (file html yang mengkonfigurasi head html).
  Diakhir title and fields yang menampilkan table tambahkan button untuk memproses input form yaitu href="{% url 'main:add_order_entry' %}" href ini akan mengalihkan ke file html add_order entry yang akan menampilkan hasil input form user jika valid.
  - Tambahkan juga csrf_token dalam file add_order_entry.html untuk memastikan session form memiliki kode yang unik.

2. Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
  - fungsi views XML dan JSON digunakan agar client system dapat melihat dan memproses data dalam models dalam format XML dan JSON.
  XML dan JSON by ID digunakan untuk melihat XML dan JSON dengan ID tertentu
  - hal yang perlu dilakukan untuk menambahkan views XML dan JSON adalah dengan menambahkan fungsi yang merender XML dan JSON
  - def show_xml(request): dan def show_json(request): akan menerima request
  - data = Entry.objects.all() mengambil data dalam models Entry
  - return HttpResponse(serializers.serialize('xml', data), content_type='aplication/xml') mengubah data menjadi format xml dan memberikan respond terhadap client
  - return HttpResponse(serializers.serialize('json', data), content_type='aplication/json') mengubah data menjadi format JSON dan memberikan respond terhadap client
  - Perbedaan dari XML, JSON dan XML by ID, JSON by ID adalah filter pk by id yang dilakukan pada data = Entry.objects.filter(pk=id).

3.  Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
  - routing dilakukan dengan menambahkan path pada main/urls untuk mengakses fungsi show_xml maupun show_json
  - dilakukan dengan menambahkan path('xml/', show_xml, name='show_xml') kode ini memiliki parameter path(domain untuk diakses user, metho, reference url),
  - path('xml/str:id/', show_xml_by_id, name='show_xml_by_id'), sedangkan perbedaan show_by_id hanyalah domain yang diakses oleh user.

4. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
  Data delivery sangat penting dalam pengimplementasian sebuah platform karena berfungsi untuk memastikan bahwa informasi atau data yang dibutuhkan dapat diakses oleh pengguna atau sistem lain dengan tepat dan sesui format yang dibutuhkan. Berikut adalah beberapa kegunaannya
  - Memfasilitasi Komunikasi Antara Komponen Platform
  - Ketersediaan Data Secara Real-Time
  - Pengoptimalan Performa
  - Keamanan dan Enkripsi Data
  - Mendukung Skalabilitas
  - Integrasi Lintas Sistem

5.  Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
  Menurut saya JSON lebih baik dari XML dan lebih sering digunakan dalam pengembangan web saat ini. Hal ini karena JSON memiliki sintaks yang lebih sederhana dan mudah digunakan. JSON juga terintegrasi dengan javascript sehingga memudahkan pengembangan web menggunakan javascript. Selain itu, JSO lebih cepat melakukan pertukanan data. Akan tetapi, XML juga masih digunakan karena terdapat web browser yang masing menggunakan XML.

6. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
  Dalam Django, method is_valid() digunakan untuk memeriksa apakah data yang dimasukkan ke dalam form valid sesuai dengan aturan validasi yang ditetapkan pada form tersebut, membersihkan data, dan mengidentifikasi kesalahan. Seperti 
  - Apakah semua field yang wajib diisi telah diisi.
  - Apakah data yang dimasukkan sesuai dengan tipe data yang diharapkan (misalnya, angka di field yang diharapkan menerima angka).
  - Apakah data memenuhi batasan atau format tertentu (misalnya, email yang valid, panjang karakter, dsb).
  - is_valid() juga membersihkan data dengan menghilangkan whitespace berlebih, mengonversi tipe data, dan melakukan normalisasi sesuai dengan aturan form.

7. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
  csrf_token digunakan agar setiap session memiliki kode session yang unik dan sulit dipalsukan oleh penyerang sehingga terlindungi dari serangan Cross-Site Request Forgery (CSRF). CSRF adalah serangan di mana penyerang mengirimkan permintaan berbahaya dari situs lain atas nama pengguna yang sah, tanpa sepengetahuannya.
  - Cara Kerja csrf_token
    - Penyisipan Token: Django menambahkan token ke dalam form menggunakan {% csrf_token %} dalam template. Token ini akan dikirim sebagai bagian dari permintaan (request) saat form disubmit.

    - Validasi Token: Ketika server menerima permintaan (request), Django akan memeriksa apakah token yang dikirimkan oleh form cocok dengan token yang dihasilkan saat halaman pertama kali dimuat. Jika token tersebut cocok, permintaan dianggap sah.

    - Pencegahan Serangan: Dengan menambahkan csrf_token, server dapat memverifikasi bahwa permintaan berasal dari sumber yang tepercaya (aplikasi pengguna yang sah) dan bukan dari penyerang yang mencoba mengirimkan permintaan berbahaya dari sumber eksternal.

  Jika tidak digunakan csrf_token 
  - Penyerang dapat membuat halaman web yang secara diam-diam mengirimkan permintaan berbahaya ke server target atas nama pengguna yang sah karena tanpa token CSRF, server tidak dapat memverifikasi apakah permintaan berasal dari aplikasi yang sah.

8. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam 
  - show_xml
    ![show_xml](https://github.com/user-attachments/assets/5a68182e-3dec-49a7-924c-463c5896f9ad)
  - show_xml_by_id
    ![show_xml_by_id](https://github.com/user-attachments/assets/5bb23fbe-81a8-4c1b-9cad-296613b544ad)
  - show_json
    ![show_json](https://github.com/user-attachments/assets/41d64314-1898-4c51-9046-130387f737ab)
  - show_json_by_id
    ![show_json_by_id](https://github.com/user-attachments/assets/5308ce19-1f9c-4097-8ec9-8d84d988669c)
    
