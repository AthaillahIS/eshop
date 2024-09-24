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
    
TUGAS 4
1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
  a) Cara Kerja Implementasi Login:
    1) Akses ke Halaman yang Membutuhkan Autentikasi:
      - Ketika user mencoba mengakses homepage / halaman yang dirender oleh function show_main, decorator @login_required(login_url='/login') akan memeriksa apakah user sudah login.
      - Jika user belum login, decorator ini akan redirect user ke halaman login (/login).

    2) URL Pattern untuk Login:
      - Dalam urls.py, terdapat URL pattern yang memetakan path /login/ ke function login_user:
        path('login/', login_user, name='login')
      - Sehingga saat dilakukan redirect menuju halaman login (/login) function login_user juga dijalankan.

    3) Proses GET Request untuk Halaman Login:
      - Saat pertama kali halaman /login diakses (GET request), form autentikasi baru akan dibuat dan halaman login akan dirender:
        else:
            form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, 'login.html', context)
      - AuthenticationForm() merupakan builtin form django yang diimport dari library django.contrib.auth.forms digunakan untuk menciptakan form login yang memiliki builtin fitur autentikasi. AuthenticationForm(request) akan menampilkan form login kosong kepada user (dirender dalam login.html).

    4) Proses POST Request untuk Autentikasi:
      - Ketika user mengisi form login dan menekan tombol submit, Django menerima POST request. Form akan mengambil data autentikasi yang diinput user:
        if request.method == 'POST':
          form = AuthenticationForm(data=request.POST)

    5) Validasi Autentikasi:
      - AuthenticationForm akan memanggil fungsi authenticate() untuk memvalidasi username dan password yang diinput user.
      - Jika kredensial valid, user akan berhasil login dan diarahkan ke halaman utama (home page):
        if form.is_valid():
          user = form.get_user()
          login(request, user)
          response = HttpResponseRedirect(reverse("main:show_main"))
          response.set_cookie('last_login', str(datetime.datetime.now()))
          return response
      - Fungsi login() melakukan proses login dan membuat session untuk user.
      - HttpResponseRedirect(reverse("main:show_main")) melakukan redirect halaman menuju url path path('', show_main, name='show_main'),
      - HttpResponseRedirect memungkinkan user untuk menyimpan dan mengirimkan cookie ke server.
      - response.set_cookie('last_login', str(datetime.datetime.now())) melakukan set cookie tanggal terakhir user login.

  b) Cara kerja implementasi register:
    1) Navigasi ke Halaman Register dari Halaman Login:
      - Pada halaman login.html, terdapat link yang mengarahkan user ke halaman register dengan URL pattern berikut:
        "<"a href="{% url 'main:register' %}">Register Now "<"/a>
      - Jika user mengklik link ini, akan dikirimkan GET request ke URL /register/ yang memanggil function register karena dalam urls.py, URL pattern berikut memetakan path /register/ ke function register:
        path('register/', register, name='register')

    2) GET Request untuk Halaman Register:
      - Saat user mengakses halaman /register/ (GET request), form pendaftaran baru akan dibuat menggunakan UserCreationForm dari library django.contrib.auth.forms Django:
        form = UserCreationForm()
        ...
        context = {'form': form}
        return render(request, 'register.html', context)
      - UserCreationForm akan di render dalam register.html

    3) Proses POST Request untuk Pendaftaran:
      - Ketika user mengisi form pendaftaran dan menekan submit, POST request dikirim ke server, dan UserCreationForm akan melakukan validasi proses register:
        if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              messages.success(request, 'Your account has been successfully created!')
              return redirect('main:login')
      - Jika form valid, maka data dalam form akan disimpan kedalam database oleh form.save() dan diredirect menuju halaman 
      /login oleh redirect('main:login').

  c) Cara kerja implementasi logout:
    1) Navigasi ke halaman login
      - "<"a href="{% url 'main:logout' %}">
            "<"button>Logout"<"/button>
        "<"/a>
        Tombol logout dalam main.html yang di map ke url path path('logout/', logout_user, name='logout') dalam urls.py, akan menjalankan function logout_user saat ditekan.
      - function logout_user dalam views.py akan melakukan proses autentikasi logout
        def logout_user(request):
          logout(request)
          response = HttpResponseRedirect(reverse('main:login'))
          response.delete_cookie('last_login')
          return response
      - logout(request) menerima parameter request.user untuk mengakhiri session
      - HttpResponseRedirect(reverse('main:login')) akan redirect menuju halaman login dan menjalankan function login_user karena reference login di map ke url path path('login/', login_user, name='login'), dalam urls.py.
      - HttpResponseRedirect memungkinkan server untuk delete cookies yang tersimpan dalam server menggunakan response.delete_cookie('last_login'), 'last_login' merupakan key cookie yang disimpan saat login_user

  2. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
    - Jalankan webserver
    - lakukan registrasi 2 akun dummy
    - login ke masing-masing akun
    - isi form order_entry sebanyak 3 kali untuk membuat 3 dummy data pada masing-masing akun. 

  3. Menghubungkan model Product dengan User.
    a) Mengassign foreign key untuk user dalam models.py,
      - Untuk mengambil user yang diciptakan dalam UserCreationForm, perlu di include mode User dengan 
        from django.contrib.auth.models import User
      - Assign model User menjadi foreign key / key akses model Produk lainnya.
      - STEP(tambahkan kode dibawah ini dalam models.py)
        class Entry(models.Model):
          user = models.ForeignKey(User, on_delete=models.CASCADE)

    b) Penyimpanan model Product dengan User
      - Assign model user terhubung dengan form order_entry (model Produk). form.save(commit=false) menunda penyimpanan model produk dalam database sehingga model Produk bisa di hubungkan dengan model User dengan order_entry.user = request.user.
      - Simpan model Produk dalam database menggunakan order_entry.save() 
      - STEP(tambahkan kode dibawah dalam views.py)
      def add_order_entry(request):
        ...
        order_entry = form.save(commit=False)
        order_entry.user = request.user
        order_entry.save()
        ...

    c) Akses Model Product yang Diassign dengan User
      - Entry.objects.filter(user=request.user) melakukan filter foreign key User yang diakses dengan User yang mengirimkan request/logged in
      - model Produk disimpan dalam order_entries agar bisa di render dalam file html.
      - STEP(tambahkan kode dibawah dalam views.py)
      def show_main(request):
        order_entries = Entry.objects.filter(user=request.user)
        context {
          ...
          'order_entries' : order_entries,
          ....
        }
    d) Pastikan sudah terdapat user dalam database dan lakukan migrasi data

  4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
    - Cookie dapat disimpan dalam objek response. Dalam kode views.py cookies disimpan dalam response HttpRedirect:
      response = HttpResponseRedirect(reverse("main:show_main"))
      response.set_cookie('last_login', str(datetime.datetime.now()))
    - set_cookies(key, value), menyimpan cookie dengan key value pair. 
    - Cookies kemudian akan di simpan dalam browser client. Jika user melakukan request ke web, cookies akan otomatis dikirimkan
    - Untuk menggunakan cookies, cookies perlu ditambahkan dalam aplication context sehingga dapat dirender dalam file html
      def show_main(request):
        context = {
          ...
          'last_login': request.COOKIES['last_login'],
          ...
        }
    - request.COOKIES['last_login'] mengakses cookies dengan key 'last_login'

  5. Apa perbedaan antara HttpResponseRedirect() dan redirect()
    a) HttpResponseRedirect()
      - Definisi: Ini adalah kelas respons yang mengembalikan status HTTP 302 (Found) yang menandakan bahwa sumber daya yang diminta telah dipindahkan sementara ke URL baru.
      - Penggunaan: Pemanggilan perlu menyebutkan URL secara eksplisit saat menggunakan HttpResponseRedirect(reverse('main:login')).
      - Kelebihan : Memberikan kontrol penuh atas pengaturan respons. HttpResponseRedirect() dapat menambahkan header atau cookie jika perlu sebelum mengembalikannya.

    b) redirect()
      - Definisi: redirect() adalah fungsi yang memudahkan pembuatan objek HttpResponseRedirect().
      - Penggunaan: redirect() dapat menerima URL, nama view, atau objek HttpResponseRedirect, sehingga lebih fleksibel dan mudah digunakan.
        redirect('main:show_main')
      - kelebihan: 
        - Simplicity: Mengurangi kode yang perlu ditulis. redirect() tidak perlu menggunakan reverse() secara eksplisit jika menggunakan nama view. 
        - Support for arguments: redirect() juga memungkinkan untuk menyertakan argumen untuk URL dengan cara yang lebih bersih.

  6. Jelaskan cara kerja penghubungan model Product dengan User! (tambahan dari NO.3)
    a) Definisi Model (menghubungkan model User dengan model Produk): user = models.ForeignKey(User, on_delete=models.CASCADE)
      - ForeignKey (user): Ini mendefinisikan hubungan antara Product dan User. Artinya, setiap produk terhubung dengan satu pengguna (User).
      - on_delete=models.CASCADE: Jika pengguna yang terkait dengan produk dihapus, semua produk yang terhubung dengan pengguna tersebut juga akan dihapus.

    b) Menyimpan Produk dengan Pengguna
      - form.save(commit=False): Ini menunda penyimpanan ke database, sehingga kita bisa menambahkan informasi pengguna (request.user) sebelum menyimpan produk.
      - product.user = request.user: Produk tersebut kemudian dihubungkan dengan pengguna yang sedang login.
    
    c) Mengakses Produk berdasarkan Pengguna
      - Product.objects.filter(user=request.user): Ini mengambil semua produk yang dimiliki oleh pengguna yang sedang login (request.user). Dengan ini, pengguna hanya bisa melihat dan mengakses produk mereka sendiri.


  7. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

    a) Perbedaan antara Authentication dan Authorization
      1. Authentication (Autentikasi):
        - Proses untuk memverifikasi identitas pengguna. Pada tahap ini, sistem mengecek apakah pengguna yang mencoba masuk ke sistem sesuai dengan data dalam database.
        - Contoh: Ketika pengguna memasukkan username dan password untuk login, sistem memeriksa apakah kombinasi tersebut cocok dengan data yang ada dalam database.
      2. Authorization (Otorisasi):
        - Proses untuk menentukan hak akses pengguna setelah mereka berhasil diautentikasi. Ini menentukan apa yang boleh dan tidak boleh dilakukan oleh pengguna dalam aplikasi.
        - Contoh: Setelah login, pengguna mungkin hanya memiliki akses ke halaman tertentu, dan hak akses ini bisa berbeda berdasarkan peran pengguna (misalnya, admin, pengguna biasa).

    b). Proses Login Pengguna
      - Saat pengguna melakukan login, mereka memasukkan username dan password. Ini adalah tahap authentication, di mana sistem memverifikasi kredensial tersebut. Jika autentikasi berhasil, pengguna dianggap telah terautentikasi.
      - Setelah autentikasi, sistem kemudian dapat melakukan authorization untuk menentukan halaman atau data apa yang bisa diakses oleh pengguna tersebut.

      (IMPLEMENTASI dalam kode)
      - Dalam implementasi kode ini akses otorisasi diberikan pada user yang telah melakukan login, user pertama dialihkan untuk login agar diautentikasi
        @login_required(login_url='/login'), me
      - Setelah autentikasi, user memiliki otorisasi untuk mengirimkan request dan mengakses show_main(request)

    c) Implementasi Authentication dan Authorization di Django
      - Authentication
        Model User: saat user registrasi menggunakan UserCreationForm django akan menciptakan model User dari library django.contrib.auth.forms
      - Form Autentikasi (AuthenticationForm): saat pengguna login dengan mengisi form AuthenticationForm, django akan mengecek apakah objek User ada dalam database dengan menjalankan fungsi authenticate()
      - Fungsi Autentikasi: Fungsi authenticate() digunakan untuk memverifikasi kredensial pengguna. Jika kombinasi username dan password valid, fungsi ini akan mengembalikan objek pengguna.
      
      b) Authorization
        - Group dan Permission: Django memungkinkan untuk mengatur grup dan permission untuk pengguna. Ini memungkinkan developer untuk menentukan apa yang dapat dan tidak dapat dilakukan oleh pengguna tertentu.
        - Decorator: pembatasan otorisasi dapat dilakukan menggunakan decorator seperti @login_required untuk membatasi akses ke view tertentu hanya untuk pengguna yang terautentikasi.

  8. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

    a). Cara Django Mengingat Pengguna yang Telah Login
      - Sesi (Session): Ketika pengguna berhasil login melalui fungsi login(), Django membuat sesi untuk pengguna tersebut. Django menggunakan database atau cache untuk menyimpan sesi ini. Setiap sesi diidentifikasi dengan ID sesi yang unik.

      - Cookies: Django menyimpan ID sesi di cookie pada browser pengguna. Cookie ini adalah string yang dikirimkan oleh server ke browser dan disimpan di sisi klien. Setiap kali pengguna mengunjungi situs web, cookie ini dikirim kembali ke server, memungkinkan Django untuk mengaitkan permintaan pengguna dengan sesi mereka.

    b) Proses Login dan Pengingatan Pengguna
      - Login: Ketika pengguna login, Django memanggil fungsi login(request, user), yang mengatur sesi dan menyimpan ID sesi dalam cookie.

      - Penyimpanan Cookie: Secara default, cookie sesi akan memiliki masa berlaku hingga browser ditutup.

      - Pengecekan Sesi: Pada setiap permintaan yang dilakukan oleh pengguna, Django memeriksa cookie untuk ID sesi. Jika ID sesi valid dan ada dalam penyimpanan sesi (database atau cache), Django menganggap pengguna tersebut terautentikasi dan dapat mengakses sumber daya yang dilindungi.

    c). Kegunaan Lain dari Cookies
      - Pengaturan Preferensi Pengguna: Cookies dapat digunakan untuk menyimpan preferensi pengguna seperti bahasa yang dipilih, tema, dan pengaturan tampilan lainnya.

      - Pelacakan Analitik: Cookies sering digunakan untuk mengumpulkan data analitik tentang bagaimana pengguna berinteraksi dengan situs web, membantu pemilik situs web memahami perilaku pengguna dan meningkatkan pengalaman pengguna.

      - Otentikasi: Selain menyimpan ID sesi, cookies dapat menyimpan token otentikasi untuk pengguna yang telah login untuk keperluan autentikasi yang lebih lanjut (misalnya, untuk API).

    d) Apakah Semua Cookies Aman Digunakan?
      Tidak semua cookies aman, dan ada beberapa faktor yang perlu dipertimbangkan:

      - Cookie HTTP dan Secure: Cookie yang tidak memiliki flag Secure dapat dikirim melalui koneksi yang tidak aman (HTTP). Ini dapat membuat cookie rentan terhadap serangan Man-in-the-Middle. Harus digunakan flag Secure untuk cookies yang sensitif agar hanya dikirim melalui HTTPS.

      - HttpOnly: Mengatur flag HttpOnly pada cookie mencegah akses cookie oleh JavaScript, yang membantu melindungi dari serangan Cross-Site Scripting (XSS).
      
      - SameSite: Pengaturan cookie SameSite membantu mencegah serangan Cross-Site Request Forgery (CSRF) dengan membatasi pengiriman cookie hanya pada permintaan yang berasal dari situs yang sama.
      
      - Enkripsi: Data sensitif tidak boleh disimpan dalam cookie tanpa enkripsi. Jika informasi penting disimpan dalam cookie, penting untuk mengenkripsi data tersebut agar tidak dapat dibaca jika cookie dicuri.