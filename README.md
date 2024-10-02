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

    1) Cara Kerja Implementasi Login:
      
      1) Akses ke Halaman yang Membutuhkan Autentikasi:
        - Ketika user mencoba mengakses homepage / halaman yang dirender oleh function
         show_main, decorator @login_required(login_url='/login') akan memeriksa apakah user
         sudah login.
        - Jika user belum login, decorator ini akan redirect user ke halaman login (/login).

      2) URL Pattern untuk Login:
        - Dalam urls.py, terdapat URL pattern yang memetakan path /login/ ke function login_user:
          path('login/', login_user, name='login')
        - Sehingga saat dilakukan redirect menuju halaman login (/login) function login_user
        juga dijalankan.

      3) Proses GET Request untuk Halaman Login:
        - Saat pertama kali halaman /login diakses (GET request), form autentikasi baru akan 
        dibuat dan halaman login akan dirender:
          else:
              form = AuthenticationForm(request)
          context = {'form': form}
          return render(request, 'login.html', context)
        - AuthenticationForm() merupakan builtin form django yang diimport dari library 
        django.contrib.auth.forms digunakan untuk menciptakan form login yang memiliki 
        builtin fitur autentikasi. AuthenticationForm(request) akan menampilkan form login 
        kosong kepada user (dirender dalam login.html).

      4) Proses POST Request untuk Autentikasi:
        - Ketika user mengisi form login dan menekan tombol submit, Django menerima POST 
        request. Form akan mengambil data autentikasi yang diinput user:
          if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)

      5) Validasi Autentikasi:
        - AuthenticationForm akan memanggil fungsi authenticate() untuk memvalidasi username 
        dan password yang diinput user.
        - Jika kredensial valid, user akan berhasil login dan diarahkan ke halaman utama 
        (home page):
          if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        - Fungsi login() melakukan proses login dan membuat session untuk user.
        - HttpResponseRedirect(reverse("main:show_main")) melakukan redirect halaman menuju 
        url path path('', show_main, name='show_main'),
        - HttpResponseRedirect memungkinkan user untuk menyimpan dan mengirimkan cookie ke server.
        - response.set_cookie('last_login', str(datetime.datetime.now())) melakukan set 
        cookie tanggal terakhir user login.

    2) Cara kerja implementasi register:

      1) Navigasi ke Halaman Register dari Halaman Login:
        - Pada halaman login.html, terdapat link yang mengarahkan user ke halaman register 
        dengan URL pattern berikut:
          "<"a href="{% url 'main:register' %}">Register Now "<"/a>
        - Jika user mengklik link ini, akan dikirimkan GET request ke URL /register/ yang 
        memanggil function register karena dalam urls.py, URL pattern berikut memetakan 
        path /register/ ke function register:
          path('register/', register, name='register')

      2) GET Request untuk Halaman Register:
        - Saat user mengakses halaman /register/ (GET request), form pendaftaran baru akan 
        dibuat menggunakan UserCreationForm dari library django.contrib.auth.forms Django:
          form = UserCreationForm()
          ...
          context = {'form': form}
          return render(request, 'register.html', context)
        - UserCreationForm akan di render dalam register.html

      3) Proses POST Request untuk Pendaftaran:
        - Ketika user mengisi form pendaftaran dan menekan submit, POST request dikirim ke 
        server, dan UserCreationForm akan melakukan validasi proses register:
          if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        - Jika form valid, maka data dalam form akan disimpan kedalam database oleh form.save
        () dan diredirect menuju halaman /login oleh redirect('main:login').

    3) Cara kerja implementasi logout:

      1) Navigasi ke halaman login
        - "<"a href="{% url 'main:logout' %}">
              "<"button>Logout"<"/button>
          "<"/a>
          Tombol logout dalam main.html yang di map ke url path path('logout/', logout_user, 
          name='logout') dalam urls.py, akan menjalankan function logout_user saat ditekan.
        - function logout_user dalam views.py akan melakukan proses autentikasi logout
          def logout_user(request):
            logout(request)
            response = HttpResponseRedirect(reverse('main:login'))
            response.delete_cookie('last_login')
            return response
        - logout(request) menerima parameter request.user untuk mengakhiri session
        - HttpResponseRedirect(reverse('main:login')) akan redirect menuju halaman login dan 
        menjalankan function login_user karena reference login di map ke url path path
        ('login/', login_user, name='login'), dalam urls.py.
        - HttpResponseRedirect memungkinkan server untuk delete cookies yang tersimpan dalam 
        server menggunakan response.delete_cookie('last_login'), 'last_login' merupakan key 
        cookie yang disimpan saat login_user

  2. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang 
  telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

    1) Step
      - Jalankan webserver
      - lakukan registrasi 2 akun dummy
      - login ke masing-masing akun
      - isi form order_entry sebanyak 3 kali untuk membuat 3 dummy data pada masing-masing akun. 

  3. Menghubungkan model Product dengan User.

    1) Mengassign foreign key untuk user dalam models.py,
      - Untuk mengambil user yang diciptakan dalam UserCreationForm, perlu di include mode 
      User dengan from django.contrib.auth.models import User
      - Assign model User menjadi foreign key / key akses model Produk lainnya.
      - STEP(tambahkan kode dibawah ini dalam models.py)
        class Entry(models.Model):
          user = models.ForeignKey(User, on_delete=models.CASCADE)

    2) Penyimpanan model Product dengan User
      - Assign model user terhubung dengan form order_entry (model Produk). form.save
      (commit=false) menunda penyimpanan model produk dalam database sehingga model Produk 
      bisa di hubungkan dengan model User dengan order_entry.user = request.user.
      - Simpan model Produk dalam database menggunakan order_entry.save() 
      - STEP(tambahkan kode dibawah dalam views.py)
      def add_order_entry(request):
        ...
        order_entry = form.save(commit=False)
        order_entry.user = request.user
        order_entry.save()
        ...

    3) Akses Model Product yang Diassign dengan User
      - Entry.objects.filter(user=request.user) melakukan filter foreign key User yang 
      diakses dengan User yang mengirimkan request/logged in
      - model Produk disimpan dalam order_entries agar bisa di render dalam file html.
      - STEP(tambahkan kode dibawah dalam views.py)
      def show_main(request):
        order_entries = Entry.objects.filter(user=request.user)
        context {
          ...
          'order_entries' : order_entries,
          ....
        }
      
    4) Pastikan sudah terdapat user dalam database dan lakukan migrasi data

  4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

    1) Penjelasan
    
      - Cookie dapat disimpan dalam objek response. Dalam kode views.py cookies disimpan 
      dalam response HttpRedirect:
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
      - set_cookies(key, value), menyimpan cookie dengan key value pair. 
      - Cookies kemudian akan di simpan dalam browser client. Jika user melakukan request ke 
      web, cookies akan otomatis dikirimkan
      - Untuk menggunakan cookies, cookies perlu ditambahkan dalam aplication context 
      sehingga dapat dirender dalam file html
        def show_main(request):
          context = {
            ...
            'last_login': request.COOKIES['last_login'],
            ...
          }
      - request.COOKIES['last_login'] mengakses cookies dengan key 'last_login'

  5. Apa perbedaan antara HttpResponseRedirect() dan redirect()

    1) HttpResponseRedirect()
      - Definisi: Ini adalah kelas respons yang mengembalikan status HTTP 302 (Found) yang 
      menandakan bahwa sumber daya yang diminta telah dipindahkan sementara ke URL baru.
      - Penggunaan: Pemanggilan perlu menyebutkan URL secara eksplisit saat menggunakan 
      HttpResponseRedirect(reverse('main:login')).
      - Kelebihan : Memberikan kontrol penuh atas pengaturan respons. HttpResponseRedirect() 
      dapat menambahkan header atau cookie jika perlu sebelum mengembalikannya.

    2) redirect()
      - Definisi: redirect() adalah fungsi yang memudahkan pembuatan objek 
      HttpResponseRedirect().
      - Penggunaan: redirect() dapat menerima URL, nama view, atau objek 
      HttpResponseRedirect, sehingga lebih fleksibel dan mudah digunakan.
        redirect('main:show_main')
      - kelebihan: 
        - Simplicity: Mengurangi kode yang perlu ditulis. redirect() tidak perlu menggunakan 
        reverse() secara eksplisit jika menggunakan nama view. 
        - Support for arguments: redirect() juga memungkinkan untuk menyertakan argumen 
        untuk URL dengan cara yang lebih bersih.

  6. Jelaskan cara kerja penghubungan model Product dengan User! (tambahan dari NO.3)

    1) Definisi Model (menghubungkan model User dengan model Produk): user = models.
    ForeignKey(User, on_delete=models.CASCADE)
      - ForeignKey (user): Ini mendefinisikan hubungan antara Product dan User. Artinya, 
      setiap produk terhubung dengan satu pengguna (User).
      - on_delete=models.CASCADE: Jika pengguna yang terkait dengan produk dihapus, semua 
      produk yang terhubung dengan pengguna tersebut juga akan dihapus.

    2) Menyimpan Produk dengan Pengguna
      - form.save(commit=False): Ini menunda penyimpanan ke database, sehingga kita bisa 
      menambahkan informasi pengguna (request.user) sebelum menyimpan produk.
      - product.user = request.user: Produk tersebut kemudian dihubungkan dengan pengguna 
      yang sedang login.
    
    3) Mengakses Produk berdasarkan Pengguna
      - Product.objects.filter(user=request.user): Ini mengambil semua produk yang dimiliki 
      oleh pengguna yang sedang login (request.user). Dengan ini, pengguna hanya bisa 
      melihat dan mengakses produk mereka sendiri.


  7. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

    1) Perbedaan antara Authentication dan Authorization
      1. Authentication (Autentikasi):
        - Proses untuk memverifikasi identitas pengguna. Pada tahap ini, sistem mengecek 
        apakah pengguna yang mencoba masuk ke sistem sesuai dengan data dalam database.
        - Contoh: Ketika pengguna memasukkan username dan password untuk login, sistem 
        memeriksa apakah kombinasi tersebut cocok dengan data yang ada dalam database.
      2. Authorization (Otorisasi):
        - Proses untuk menentukan hak akses pengguna setelah mereka berhasil diautentikasi. 
        Ini menentukan apa yang boleh dan tidak boleh dilakukan oleh pengguna dalam aplikasi.
        - Contoh: Setelah login, pengguna mungkin hanya memiliki akses ke halaman tertentu, 
        dan hak akses ini bisa berbeda berdasarkan peran pengguna (misalnya, admin, pengguna 
        biasa).

    2) Proses Login Pengguna
      - Saat pengguna melakukan login, mereka memasukkan username dan password. Ini adalah 
      tahap authentication, di mana sistem memverifikasi kredensial tersebut. Jika 
      autentikasi berhasil, pengguna dianggap telah terautentikasi.
      - Setelah autentikasi, sistem kemudian dapat melakukan authorization untuk menentukan 
      halaman atau data apa yang bisa diakses oleh pengguna tersebut.

      (IMPLEMENTASI dalam kode)
      - Dalam implementasi kode ini akses otorisasi diberikan pada user yang telah melakukan 
      login, user pertama dialihkan untuk login agar diautentikasi
        @login_required(login_url='/login'), me
      - Setelah autentikasi, user memiliki otorisasi untuk mengirimkan request dan mengakses 
      show_main(request)

    3) Implementasi Authentication dan Authorization di Django
      - Authentication
        Model User: saat user registrasi menggunakan UserCreationForm django akan 
        menciptakan model User dari library django.contrib.auth.forms
        - Form Autentikasi (AuthenticationForm): saat pengguna login dengan mengisi form 
        AuthenticationForm, django akan mengecek apakah objek User ada dalam database dengan 
        menjalankan fungsi authenticate()
        - Fungsi Autentikasi: Fungsi authenticate() digunakan untuk memverifikasi kredensial 
        pengguna. Jika kombinasi username dan password valid, fungsi ini akan mengembalikan 
        objek pengguna.
      
      - Authorization
        - Group dan Permission: Django memungkinkan untuk mengatur grup dan permission untuk 
        pengguna. Ini memungkinkan developer untuk menentukan apa yang dapat dan tidak dapat 
        dilakukan oleh pengguna tertentu.
        - Decorator: pembatasan otorisasi dapat dilakukan menggunakan decorator seperti 
        @login_required untuk membatasi akses ke view tertentu hanya untuk pengguna yang 
        terautentikasi.

  8. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

    1) Cara Django Mengingat Pengguna yang Telah Login
      - Sesi (Session): Ketika pengguna berhasil login melalui fungsi login(), Django 
      membuat sesi untuk pengguna tersebut. Django menggunakan database atau cache untuk 
      menyimpan sesi ini. Setiap sesi diidentifikasi dengan ID sesi yang unik.

      - Cookies: Django menyimpan ID sesi di cookie pada browser pengguna. Cookie ini adalah 
      string yang dikirimkan oleh server ke browser dan disimpan di sisi klien. Setiap kali 
      pengguna mengunjungi situs web, cookie ini dikirim kembali ke server, memungkinkan 
      Django untuk mengaitkan permintaan pengguna dengan sesi mereka.

    2) Proses Login dan Pengingatan Pengguna
      - Login: Ketika pengguna login, Django memanggil fungsi login(request, user), yang 
      mengatur sesi dan menyimpan ID sesi dalam cookie.

      - Penyimpanan Cookie: Secara default, cookie sesi akan memiliki masa berlaku hingga 
      browser ditutup.

      - Pengecekan Sesi: Pada setiap permintaan yang dilakukan oleh pengguna, Django 
      memeriksa cookie untuk ID sesi. Jika ID sesi valid dan ada dalam penyimpanan sesi 
      (database atau cache), Django menganggap pengguna tersebut terautentikasi dan dapat 
      mengakses sumber daya yang dilindungi.

    3) Kegunaan Lain dari Cookies
      - Pengaturan Preferensi Pengguna: Cookies dapat digunakan untuk menyimpan preferensi 
      pengguna seperti bahasa yang dipilih, tema, dan pengaturan tampilan lainnya.

      - Pelacakan Analitik: Cookies sering digunakan untuk mengumpulkan data analitik 
      tentang bagaimana pengguna berinteraksi dengan situs web, membantu pemilik situs web 
      memahami perilaku pengguna dan meningkatkan pengalaman pengguna.

      - Otentikasi: Selain menyimpan ID sesi, cookies dapat menyimpan token otentikasi untuk 
      pengguna yang telah login untuk keperluan autentikasi yang lebih lanjut (misalnya, 
      untuk API).

    4) Apakah Semua Cookies Aman Digunakan?
      Tidak semua cookies aman, dan ada beberapa faktor yang perlu dipertimbangkan:

      - Cookie HTTP dan Secure: Cookie yang tidak memiliki flag Secure dapat dikirim melalui 
      koneksi yang tidak aman (HTTP). Ini dapat membuat cookie rentan terhadap serangan 
      Man-in-the-Middle. Harus digunakan flag Secure untuk cookies yang sensitif agar hanya 
      dikirim melalui HTTPS.

      - HttpOnly: Mengatur flag HttpOnly pada cookie mencegah akses cookie oleh JavaScript, 
      yang membantu melindungi dari serangan Cross-Site Scripting (XSS).
      
      - SameSite: Pengaturan cookie SameSite membantu mencegah serangan Cross-Site Request 
      Forgery (CSRF) dengan membatasi pengiriman cookie hanya pada permintaan yang berasal 
      dari situs yang sama.
      
      - Enkripsi: Data sensitif tidak boleh disimpan dalam cookie tanpa enkripsi. Jika 
      informasi penting disimpan dalam cookie, penting untuk mengenkripsi data tersebut agar 
      tidak dapat dibaca jika cookie dicuri.
    
TUGAS 5
  1. Implementasikan fungsi untuk menghapus dan mengedit product.
    1) Langkah yang dilakukan.
      1. Edit
        -  Buat file html yang menampilkan order dalam entries. Dalam kode ini yaitu file order_card.html.
        - File order_card.html merender meta data model yang telah diisi oleh user, beserta tombol edit<"a 
        href="{% url 'main:edit_order' order_entry.pk %} ...> Edit <"/a> dan tombol delete <"a href="{% url 
        'main:delete_order' order_entry.pk %}" <"/a>
        -  Tombol edit memanggil reference url path('edit-order/<uuid:id>', edit_order, name='edit_order'), 
        sehingga user function edit_order akan dijalankan dan user akan di redirect menuju domain /edit-order
        - user melakukan request GET 
        -  Function akan mengambil objek order berdasarkan pk id order:
          order = Entry.objects.get(pk = id)
        - edit_order.html akan dirender
          context = {'form': form}
          return render(request, "edit_order.html", context)
        - Flexbox Layout dalam edit_order.html:
          html
          <div class="flex flex-col min-h-screen bg-gray-200">
          flex: Mengatur elemen sebagai flex container, memungkinkan penggunaan model flexbox untuk tata 
          letak.
          flex-col: Menetapkan arah sumbu utama ke kolom, sehingga elemen anak disusun secara vertikal.
          min-h-screen: Memberikan tinggi minimal setara dengan tinggi viewport, memastikan elemen mengambil 
          setidaknya seluruh tinggi layar.
          bg-gray-200: Mengatur latar belakang elemen menjadi warna abu-abu muda.

          - Container:
          <div class="container mx-auto px-5 py-10 mt-16 max-w-lg">
          container: Mengatur elemen dengan lebar maksimum, secara otomatis memusatkan konten.
          mx-auto: Mengatur margin kiri dan kanan otomatis, memusatkan elemen dalam kontainer.
          px-5: Menambahkan padding horizontal (kiri dan kanan) sebesar 20px.
          py-10: Menambahkan padding vertikal (atas dan bawah) sebesar 40px.
          mt-16: Memberikan margin atas sebesar 64px.
          max-w-lg: Mengatur lebar maksimum elemen menjadi besar (lebar yang telah ditentukan dalam Tailwind).

          - Typography:
          <h1 class="text-4xl font-extrabold text-center mb-6 text-gray-900">
          text-4xl: Mengatur ukuran font menjadi 36px.
          font-extrabold: Mengatur berat font menjadi ekstra tebal.
          text-center: Menyelaraskan teks ke tengah.
          mb-6: Menambahkan margin bawah sebesar 24px.
          text-gray-900: Mengatur warna teks menjadi abu-abu gelap.
          Formulir dan Input:

          <div class="flex flex-col">
          flex: Mengatur elemen sebagai flex container.
          flex-col: Menyusun elemen anak secara vertikal, seperti label, input, dan kesalahan.
          
          - Teks Bantuan dan Kesalahan:
          <p class="mt-1 text-xs text-gray-500">{{ field.help_text }}</p>
          <p class="mt-1 text-xs text-red-600">{{ error }}</p>
          mt-1: Menambahkan margin atas sebesar 4px.
          text-xs: Mengatur ukuran font menjadi sangat kecil.
          text-gray-500: Mengatur warna teks menjadi abu-abu menengah untuk teks bantuan.
          text-red-600: Mengatur warna teks menjadi merah untuk menandakan kesalahan.
          
          - Tombol:
          <button type="submit" class="bg-gray-900 text-white font-semibold px-6 py-3 rounded-lg hover:bg-gray-700 w-full">
          bg-gray-900: Mengatur latar belakang tombol menjadi warna abu-abu gelap.
          text-white: Mengatur warna teks tombol menjadi putih.
          font-semibold: Mengatur berat font menjadi semi-tebal.
          px-6: Menambahkan padding horizontal (kiri dan kanan) sebesar 24px.
          py-3: Menambahkan padding vertikal (atas dan bawah) sebesar 12px.
          rounded-lg: Memberikan sudut melengkung pada tombol.
          hover:bg-gray-700: Mengubah latar belakang tombol menjadi abu-abu lebih terang saat di-hover.
          w-full: Mengatur lebar tombol agar memenuhi seluruh lebar kontainer.
          
          - Ruang Antar Elemen:
          <div class="space-y-5">
          space-y-5: Menambahkan jarak vertikal antara elemen anak sebesar 20px, kecuali elemen terakhir.

        - Saat user menekan button sava change dan isi form sudah benar maka user akan mengirimkan POST 
        Request dan redirect ke page / yang dirender function show_main     
        if form.is_valid() and request.method == "POST":
          form.save()
          return HttpResponseRedirect(reverse('main:show_main'))
      
      2. Delete
      - jika user menekan tombol delete maka user akan melakukan GET request untuk delete metadata order 
      sesuai dengan primary key id order
      def delete_order(request, id):
          order = Entry.objects.get(pk = id)
          order.delete()
          return HttpResponseRedirect(reverse('main:show_main'))
      - kemudian user akan di redirect ke home page

  2. Kustomisasi halaman login, register, dan tambah product semenarik mungkin.
    1) Implementasi tailwind css pada halaman login
      - Container Utama:
      <div class="min-h-screen bg-gray-100 text-gray-900 py-6 flex flex-col justify-center items-center">
      min-h-screen: Memberikan tinggi minimum yang sama dengan tinggi layar, sehingga elemen mengambil 
      seluruh tinggi layar.
      bg-gray-100: Mengatur latar belakang menjadi warna abu-abu terang.
      text-gray-900: Mengatur warna teks menjadi abu-abu gelap.
      py-6: Menambahkan padding vertikal (atas dan bawah) sebesar 24px.
      flex: Mengatur elemen sebagai flex container.
      flex-col: Menyusun elemen anak secara vertikal.
      justify-center: Menyelaraskan elemen anak di tengah secara vertikal.
      items-center: Menyelaraskan elemen anak di tengah secara horizontal.
      Judul Halaman:

      - Judul Halaman:
      <div class="relative py-3 sm:w-96 mx-auto text-center">
          <h2 class="text-2xl font-gray-900 text-extrabold">Login to your account</h2>
      </div>
      relative: Mengatur posisi elemen relatif, memungkinkan penempatan elemen anak dengan posisi absolut di 
      dalamnya.
      py-3: Menambahkan padding vertikal sebesar 12px.
      sm:w-96: Mengatur lebar elemen menjadi 384px pada ukuran layar kecil dan lebih besar.
      mx-auto: Mengatur margin kiri dan kanan otomatis untuk memusatkan elemen.
      text-center: Menyelaraskan teks ke tengah.
      text-2xl: Mengatur ukuran font menjadi 24px.
      font-gray-900: Mengatur warna font menjadi abu-abu gelap.
      text-extrabold: Mengatur berat font menjadi ekstra tebal.
      Formulir Login:

      - Formulir Login:
      <form class="mt-8 space-y-6 w-full max-w-xs" method="POST" action="">
      mt-8: Menambahkan margin atas sebesar 32px.
      space-y-6: Menambahkan jarak vertikal antara elemen anak sebesar 24px.
      w-full: Mengatur lebar formulir agar memenuhi seluruh lebar kontainer.
      max-w-xs: Mengatur lebar maksimum formulir menjadi sangat kecil (20rem atau 320px).
      Kotak Input:

      - Kotak Input:
      <div class="mt-4 bg-white shadow-md rounded-lg">
          <div class="h-2 bg-gray-900 rounded-t-md"></div>
          <div class="px-8 py-6">
      mt-4: Menambahkan margin atas sebesar 16px.
      bg-white: Mengatur latar belakang kotak menjadi putih.
      shadow-md: Menambahkan bayangan medium untuk memberikan efek kedalaman.
      rounded-lg: Memberikan sudut melengkung pada kotak.
      h-2: Mengatur tinggi elemen menjadi 8px untuk bagian atas kotak.
      bg-gray-900: Mengatur latar belakang bagian atas kotak menjadi abu-abu gelap.
      rounded-t-md: Memberikan sudut melengkung pada bagian atas kotak.
      px-8: Menambahkan padding horizontal (kiri dan kanan) sebesar 32px.
      py-6: Menambahkan padding vertikal (atas dan bawah) sebesar 24px.
      Label dan Input:

      - Label dan Input:
      <label for="username" class="block font-semibold">Username</label>
      <input id="username" name="username" type="text" required class="border w-full h-12 px-3 py-2 mt-2 
      hover:outline-none focus:outline-none focus:ring-1 focus:ring-gray-900 rounded-md" 
      placeholder="Username">
      block: Mengatur elemen sebagai blok, membuatnya mengambil lebar penuh.
      font-semibold: Mengatur berat font menjadi semi-tebal.
      border: Menambahkan border pada input.
      w-full: Mengatur lebar input agar memenuhi seluruh lebar kontainer.
      h-12: Mengatur tinggi input menjadi 48px.
      px-3: Menambahkan padding horizontal (kiri dan kanan) sebesar 12px.
      py-2: Menambahkan padding vertikal (atas dan bawah) sebesar 8px.
      mt-2: Menambahkan margin atas sebesar 8px.
      hover:outline-none: Menghapus outline saat di-hover.
      focus:outline-none: Menghapus outline saat input mendapatkan fokus.
      focus:ring-1: Menambahkan ring saat input mendapatkan fokus dengan ketebalan 1px.
      focus:ring-gray-900: Mengatur warna ring saat fokus menjadi abu-abu gelap.
      rounded-md: Memberikan sudut melengkung pada input.
      Tombol Kirim:

      - Tombol Kirim:
      <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border 
      border-transparent text-sm font-medium rounded-md text-white bg-gray-900 hover:bg-gray-700 
      focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
      group: Menandai elemen sebagai grup untuk mengatur efek hover atau fokus pada elemen anak.
      relative: Mengatur posisi elemen relatif.
      w-full: Mengatur lebar tombol agar memenuhi seluruh lebar kontainer.
      flex: Mengatur tombol sebagai flex container.
      justify-center: Menyelaraskan konten di dalam tombol ke tengah secara horizontal.
      py-2: Menambahkan padding vertikal sebesar 8px.
      px-4: Menambahkan padding horizontal sebesar 16px.
      border border-transparent: Menambahkan border transparan untuk menjaga ukuran tombol.
      text-sm: Mengatur ukuran font menjadi kecil.
      font-medium: Mengatur berat font menjadi medium.
      rounded-md: Memberikan sudut melengkung pada tombol.
      text-white: Mengatur warna teks tombol menjadi putih.
      bg-gray-900: Mengatur latar belakang tombol menjadi abu-abu gelap.
      hover:bg-gray-700: Mengubah latar belakang tombol menjadi abu-abu lebih terang saat di-hover.
      focus:outline-none: Menghapus outline saat tombol mendapatkan fokus.
      focus:ring-2: Menambahkan ring saat tombol mendapatkan fokus dengan ketebalan 2px.
      focus:ring-offset-2: Menambahkan offset pada ring saat fokus.
      focus:ring-indigo-500: Mengatur warna ring saat fokus menjadi indigo.
      Pesan Kesalahan:

      - Pesan Kesalahan:
      <ul class="text-red-500">
      text-red-500: Mengatur warna teks menjadi merah, digunakan untuk menampilkan pesan kesalahan.
      Tautan Registrasi:

      - Tautan Registrasi:
      <a href="{% url 'main:register' %}" class="text-indigo-700 hover:text-indigo-300">Register Now</a>
      text-indigo-700: Mengatur warna teks menjadi indigo gelap.
      hover:text-indigo-300: Mengubah warna teks menjadi indigo lebih terang saat di-hover.
    
    2) Implementasi tailwind css registrasi
    
      - Container Utama:
      <div class="min-h-screen bg-gray-100 text-gray-900 py-6 flex flex-col justify-center items-center">
      <div>: Elemen pembungkus untuk konten yang diatur.
      Tailwind CSS:
      min-h-screen: Memberikan tinggi minimum yang sama dengan tinggi layar, memastikan elemen mengambil seluruh tinggi layar.
      bg-gray-100: Mengatur latar belakang menjadi warna abu-abu terang.
      text-gray-900: Mengatur warna teks menjadi abu-abu gelap.
      py-6: Menambahkan padding vertikal (atas dan bawah) sebesar 24px.
      flex: Mengatur elemen sebagai flex container, memungkinkan penggunaan model flexbox untuk tata letak.
      flex-col: Menyusun elemen anak dalam kolom vertikal.
      justify-center: Menyelaraskan elemen anak di tengah secara vertikal.
      items-center: Menyelaraskan elemen anak di tengah secara horizontal.
      Judul Halaman:

      - Judul Halaman:
      <div class="relative py-3 sm:w-96 mx-auto text-center">
          <h2 class="text-2xl font-gray-900 text-extrabold">Create your account</h2>
      </div>
      <div>: Elemen pembungkus untuk judul.
      <h2>: Elemen judul tingkat dua yang menunjukkan bagian penting dari konten.
      Tailwind CSS:
      relative: Mengatur posisi elemen relatif, memungkinkan penempatan elemen anak dengan posisi absolut di 
      dalamnya.
      py-3: Menambahkan padding vertikal sebesar 12px.
      sm:w-96: Mengatur lebar elemen menjadi 384px pada ukuran layar kecil dan lebih besar.
      mx-auto: Mengatur margin kiri dan kanan otomatis untuk memusatkan elemen.
      text-center: Menyelaraskan teks ke tengah.
      text-2xl: Mengatur ukuran font menjadi 24px.
      font-gray-900: Mengatur warna font menjadi abu-abu gelap.
      text-extrabold: Mengatur berat font menjadi ekstra tebal.
      Formulir Pendaftaran:

      - Formulir Pendaftaran:
      <form class="mt-8 space-y-6 w-full max-w-xs" method="POST">
      <form>: Elemen formulir yang digunakan untuk mengumpulkan data dari pengguna.
      Tailwind CSS:
      mt-8: Menambahkan margin atas sebesar 32px.
      space-y-6: Menambahkan jarak vertikal antara elemen anak sebesar 24px.
      w-full: Mengatur lebar formulir agar memenuhi seluruh lebar kontainer.
      max-w-xs: Mengatur lebar maksimum formulir menjadi sangat kecil (20rem atau 320px).
      method="POST": Menyatakan bahwa formulir akan mengirimkan data menggunakan metode POST.
      Kotak Input:

      - Kotak Input:
      <div class="mt-4 bg-white shadow-md rounded-lg">
          <div class="h-2 bg-gray-900 rounded-t-md"></div>
          <div class="px-8 py-6">
      <div>: Elemen pembungkus untuk kotak input.
      Tailwind CSS:
      mt-4: Menambahkan margin atas sebesar 16px.
      bg-white: Mengatur latar belakang kotak menjadi putih.
      shadow-md: Menambahkan bayangan medium untuk memberikan efek kedalaman.
      rounded-lg: Memberikan sudut melengkung pada kotak.
      h-2: Mengatur tinggi elemen menjadi 8px untuk bagian atas kotak.
      bg-gray-900: Mengatur latar belakang bagian atas kotak menjadi abu-abu gelap.
      rounded-t-md: Memberikan sudut melengkung pada bagian atas kotak.
      px-8: Menambahkan padding horizontal (kiri dan kanan) sebesar 32px.
      py-6: Menambahkan padding vertikal (atas dan bawah) sebesar 24px.
      Field Formulir:

      - Field Formulir:
      {% for field in form %}
          <div>
              <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-black">
                  {{ field.label }}
              </label>
              <div class="relative">
                  <div class="border border-gray-300 rounded-md">
                      {{ field }}
                  </div>
                  <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                      {% if field.errors %}
                          <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                              <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                          </svg>
                      {% endif %}
                  </div>
              </div>
              {% if field.errors %}
                  {% for error in field.errors %}
                      <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                  {% endfor %}
              {% endif %}
          </div>
      {% endfor %}
      <label>: Elemen label untuk memberi nama pada input.
      <div>: Elemen pembungkus untuk input dan kesalahan.
      <svg>: Ikon yang ditampilkan jika ada kesalahan.
      Tailwind CSS:
      mb-2: Menambahkan margin bawah pada label sebesar 8px.
      font-semibold: Mengatur berat font menjadi semi-tebal untuk label.
      text-black: Mengatur warna teks label menjadi hitam.
      border border-gray-300: Menambahkan border pada input dengan warna abu-abu muda.
      rounded-md: Memberikan sudut melengkung pada input.
      absolute inset-y-0 right-0 pr-3: Mengatur posisi ikon (jika ada kesalahan) ke kanan input.
      flex items-center: Mengatur elemen sebagai flex container dengan item yang diselaraskan secara vertikal.
      text-red-500: Mengatur warna ikon kesalahan menjadi merah.
      mt-1: Menambahkan margin atas pada pesan kesalahan.
      text-sm: Mengatur ukuran font pesan kesalahan menjadi kecil.
      text-red-600: Mengatur warna teks pesan kesalahan menjadi merah gelap.
      Tombol Kirim:

      - Tombol Kirim:
      <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border 
      border-transparent text-sm font-medium rounded-md text-white bg-gray-900 hover:bg-gray-700 
      focus:outline-none focus:ring-1 focus:ring-offset-1 focus:ring-gray-500">
          Register
      </button>
      <button>: Elemen tombol untuk mengirimkan formulir.
      Tailwind CSS:
      group: Menandai elemen sebagai grup untuk mengatur efek hover atau fokus pada elemen anak.
      relative: Mengatur posisi elemen relatif.
      w-full: Mengatur lebar tombol agar memenuhi seluruh lebar kontainer.
      flex: Mengatur tombol sebagai flex container.
      justify-center: Menyelaraskan konten di dalam tombol ke tengah secara horizontal.
      py-2: Menambahkan padding vertikal sebesar 8px.
      px-4: Menambahkan padding horizontal sebesar 16px.
      border border-transparent: Menambahkan border transparan untuk menjaga ukuran tombol.
      text-sm: Mengatur ukuran font menjadi kecil.
      font-medium: Mengatur berat font menjadi medium.
      rounded-md: Memberikan sudut melengkung pada tombol.
      text-white: Mengatur warna teks tombol menjadi putih.
      bg-gray-900: Mengatur latar belakang tombol menjadi abu-abu gelap.
      hover:bg-gray-700: Mengubah latar belakang tombol menjadi abu-abu lebih terang saat di-hover.
      focus:outline-none: Menghapus outline saat tombol mendapatkan fokus.
      focus:ring-1: Menambahkan ring saat tombol mendapatkan fokus dengan ketebalan 1px.
      focus:ring-offset-1: Menambahkan offset pada ring saat fokus.
      focus:ring-gray-500: Mengatur warna ring saat fokus menjadi abu-abu.
      Pesan Kesalahan:

      - Pesan Kesalahan:
      {% if messages %}
      <div class="mt-4">
          {% for message in messages %}
          <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
              <span class="block sm:inline">{{ message }}</span>
          </div>
          {% endfor %}
      </div>
      {% endif %}
      <div>: Elemen pembungkus untuk pesan kesalahan.
      <span>: Elemen untuk teks pesan kesalahan.
      Tailwind CSS:
      mt-4: Menambahkan margin atas sebesar 16px pada div yang membungkus pesan.
      bg-red-100: Mengatur latar belakang pesan menjadi merah muda terang.
      border border-red-400: Menambahkan border pada pesan dengan warna merah.
      text-red-700: Mengatur warna teks pesan menjadi merah gelap.
      px-4: Menambahkan padding horizontal sebesar 16px.
      py-3: Menambahkan padding vertikal sebesar 12px.
      rounded: Memberikan sudut melengkung pada pesan.
      relative: Mengatur posisi elemen relatif.
      Tautan Login:

      - Tautan Login:
      <p class="text-sm text-black">
          Already have an account?
          <a href="{% url 'main:login' %}" class="font-medium text-indigo-600 hover:text-indigo-400">
              Login here
          </a>
      </p>
      <p>: Elemen paragraf untuk teks informasi.
      <a>: Elemen tautan yang memungkinkan pengguna untuk berpindah ke halaman login.
      Tailwind CSS:
      text-sm: Mengatur ukuran font menjadi kecil.
      text-black: Mengatur warna teks menjadi hitam.
      font-medium: Mengatur berat font tautan menjadi medium.
      text-indigo-600: Mengatur warna teks tautan menjadi indigo gelap.
      hover:text-indigo-400: Mengubah warna teks tautan menjadi indigo lebih terang saat di-hover.

    3) Implementasi tailwind css pada page tambah produk
      - Container Utama:
      <div class="flex flex-col min-h-screen bg-gray-200">
      flex: Mengatur elemen sebagai flex container, memungkinkan penggunaan model flexbox untuk tata letak.
      flex-col: Menyusun elemen anak dalam kolom vertikal.
      min-h-screen: Memberikan tinggi minimum setara dengan tinggi layar, memastikan elemen mengambil setidaknya seluruh tinggi layar.
      bg-gray-200: Mengatur latar belakang elemen menjadi warna abu-abu muda.
      Container Dalam:

      - Container Dalam:
      <div class="container mx-auto px-5 py-10 mt-16 max-w-lg">
      container: Memberikan lebar maksimum pada elemen, biasanya dengan ukuran yang sesuai untuk perangkat desktop.
      mx-auto: Mengatur margin kiri dan kanan otomatis untuk memusatkan elemen.
      px-5: Menambahkan padding horizontal (kiri dan kanan) sebesar 20px.
      py-10: Menambahkan padding vertikal (atas dan bawah) sebesar 40px.
      mt-16: Menambahkan margin atas sebesar 64px.
      max-w-lg: Mengatur lebar maksimum elemen menjadi besar (lebar yang telah ditentukan dalam Tailwind).
      Judul Halaman:

      - Judul Halaman:
      <h1 class="text-4xl font-extrabold text-center mb-6 text-gray-900">Add Order</h1>
      text-4xl: Mengatur ukuran font menjadi 36px.
      font-extrabold: Mengatur berat font menjadi ekstra tebal.
      text-center: Menyelaraskan teks ke tengah.
      mb-6: Menambahkan margin bawah sebesar 24px.
      text-gray-900: Mengatur warna teks menjadi abu-abu gelap.
      Kotak Formulir:

      - Kotak Formulir:
      <div class="bg-white rounded-lg shadow-lg p-8">
      bg-white: Mengatur latar belakang kotak menjadi putih.
      rounded-lg: Memberikan sudut melengkung pada kotak.
      shadow-lg: Menambahkan bayangan besar untuk efek kedalaman.
      p-8: Menambahkan padding di semua sisi sebesar 32px.
      Formulir:

      - Formulir:
      <form method="POST" class="space-y-5">
      method="POST": Menyatakan bahwa formulir akan mengirimkan data menggunakan metode POST.
      space-y-5: Menambahkan jarak vertikal antara elemen anak sebesar 20px.
      Field Formulir:

      - Field Formulir: (untuk setiap metadata input form akan dibuat segmen div agar setap input field dapat menjadi item flexbox)
      {% for field in form %}
          <div class="flex flex-col">
              <label for="{{ field.id_for_label }}" class="text-sm font-medium text-gray-800 mb-2">
                  {{ field.label }}
              </label>
              <div class="relative">
                  {{ field }} 
              </div>
              {% if field.help_text %}
                  <p class="mt-1 text-xs text-gray-500">{{ field.help_text }}</p>
              {% endif %}
              {% for error in field.errors %}
                  <p class="mt-1 text-xs text-red-600">{{ error }}</p>
              {% endfor %}
          </div>
      {% endfor %}
      flex flex-col: Mengatur elemen sebagai flex container dengan elemen anak disusun dalam kolom vertikal.
      text-sm: Mengatur ukuran font menjadi kecil untuk label.
      font-medium: Mengatur berat font menjadi medium untuk label.
      text-gray-800: Mengatur warna teks label menjadi abu-abu gelap.
      mb-2: Menambahkan margin bawah pada label sebesar 8px.
      relative: Mengatur posisi relatif pada div yang membungkus input, memungkinkan penggunaan posisi absolut pada elemen anak jika diperlukan.
      mt-1: Menambahkan margin atas pada teks bantuan dan kesalahan.
      text-xs: Mengatur ukuran font menjadi sangat kecil untuk teks bantuan dan kesalahan.
      text-gray-500: Mengatur warna teks bantuan menjadi abu-abu.
      text-red-600: Mengatur warna teks kesalahan menjadi merah.
      Tombol Simpan:

      - Tombol Simpan:
      <div class="flex justify-center">
          <button type="submit" class="bg-gray-900 text-white font-semibold px-6 py-3 rounded-lg hover:bg-gray-700 w-full">
              Save Changes
          </button>
      </div>
      flex justify-center: Mengatur elemen sebagai flex container dan menyelaraskan konten di dalamnya ke tengah.
      bg-gray-900: Mengatur latar belakang tombol menjadi abu-abu gelap.
      text-white: Mengatur warna teks tombol menjadi putih.
      font-semibold: Mengatur berat font menjadi semi-tebal.
      px-6: Menambahkan padding horizontal pada tombol sebesar 24px.
      py-3: Menambahkan padding vertikal pada tombol sebesar 12px.
      rounded-lg: Memberikan sudut melengkung pada tombol.
      hover:bg-gray-700: Mengubah latar belakang tombol menjadi abu-abu lebih terang saat di-hover.
      w-full: Mengatur lebar tombol agar memenuhi seluruh lebar kontainer.
      

  3. Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi 
  berikut:
    1) Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
      - Pesan Ketika Tidak Ada Data Order:
      {% if not order_entries %}
      <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
      flex: Mengatur elemen sebagai flex container.
      flex-col: Menyusun elemen anak dalam kolom vertikal.
      items-center: Menyelaraskan elemen anak di tengah secara horizontal.
      justify-center: Menyelaraskan elemen anak di tengah secara vertikal.
      min-h-[24rem]: Memberikan tinggi minimum sebesar 24rem (384px).
      p-6: Menambahkan padding di semua sisi sebesar 24px.
      
      - Gambar dan Teks:
      <img src="{% static 'image/sad-icon.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
      <p class="text-center text-gray-600 mt-4">No order data available in the e-shop.</p>
      w-32: Mengatur lebar gambar menjadi 128px.
      h-32: Mengatur tinggi gambar menjadi 128px.
      mb-4: Menambahkan margin bawah sebesar 16px.
      text-center: Menyelaraskan teks ke tengah.
      text-gray-600: Mengatur warna teks menjadi abu-abu sedang.
      mt-4: Menambahkan margin atas sebesar 16px.
      Kolom untuk Order Entries:
    
    2) Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product 
    dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).
      Iterasi pencetakkan card order
      <div class="columns-1 sm:columns-2 lg:columns-3 w-full">
      {% for order_entry in order_entries %}
      - Syntax ini akan mengiterasi setiap order yang ada dalam order entries
          {% include 'order_card.html' with order_entry=order_entry %}
      - melakukan including html yang ada dalam order_card.html menggunakan konteks variable order_entry ke variable baru order_entry.html. Yang artinya order_card.html akan di render di hiro section main.html.
      {% endfor %}
      - end loop
      columns-1: Mengatur jumlah kolom menjadi satu secara default. Ini berarti bahwa pada perangkat dengan ukuran layar kecil, semua elemen anak akan ditampilkan dalam satu kolom.
      sm:columns-2: Mengatur jumlah kolom menjadi dua pada ukuran layar kecil (small) dan lebih besar. Ketika layar mencapai lebar minimum yang ditentukan untuk ukuran kecil (biasanya 640px), elemen anak akan disusun dalam dua kolom.
      lg:columns-3: Mengatur jumlah kolom menjadi tiga pada ukuran layar besar (large) dan lebih besar. Setelah layar mencapai lebar minimum yang ditentukan untuk ukuran besar (biasanya 1024px), elemen anak akan disusun dalam tiga kolom.
      w-full: Mengatur lebar elemen agar memenuhi seluruh lebar kontainer induknya. Ini memastikan bahwa div ini mengisi seluruh ruang horizontal yang tersedia.

      - Container order_card:
      <div class="relative break-inside-avoid flex flex-col items-center min-h-screen bg-gray-100">
      <div>: Elemen pembungkus utama untuk konten.
      Tailwind CSS:
      relative: Mengatur posisi elemen relatif, memungkinkan penempatan elemen anak dengan posisi absolut di dalamnya jika diperlukan.
      break-inside-avoid: Mencegah pemecahan elemen di dalam kontainer, berguna untuk tata letak yang responsif.
      flex: Mengatur elemen sebagai flex container, memungkinkan penggunaan model flexbox untuk tata letak.
      flex-col: Menyusun elemen anak dalam kolom vertikal.
      items-center: Menyelaraskan elemen anak di tengah secara horizontal.
      min-h-screen: Memberikan tinggi minimum setara dengan tinggi layar, memastikan elemen mengambil setidaknya seluruh tinggi layar.
      bg-gray-100: Mengatur latar belakang elemen menjadi warna abu-abu terang.
      Container untuk Konten:

      - Container untuk Konten order_card:
      <div class="container mx-auto px-4 py-8 mt-16 max-w-3xl">
      <div>: Elemen pembungkus untuk konten rincian pesanan.
      Tailwind CSS:
      container: Memberikan lebar maksimum pada elemen.
      mx-auto: Mengatur margin kiri dan kanan otomatis untuk memusatkan elemen.
      px-4: Menambahkan padding horizontal (kiri dan kanan) sebesar 16px.
      py-8: Menambahkan padding vertikal (atas dan bawah) sebesar 32px.
      mt-16: Menambahkan margin atas sebesar 64px.
      max-w-3xl: Mengatur lebar maksimum elemen menjadi ukuran 3xl (48rem atau 768px).
      Kotak Rincian Pesanan:

      - Konten Rincian Pesanan order_card:
      <div class="relative bg-white shadow-md rounded-lg mb-6 border border-gray-300 w-full">
      <div>: Elemen pembungkus untuk rincian pesanan.
      Tailwind CSS:
      relative: Mengatur posisi elemen relatif.
      bg-white: Mengatur latar belakang kotak menjadi putih.
      shadow-md: Menambahkan bayangan medium untuk memberikan efek kedalaman.
      rounded-lg: Memberikan sudut melengkung pada kotak.
      mb-6: Menambahkan margin bawah sebesar 24px.
      border border-gray-300: Menambahkan border pada kotak dengan warna abu-abu muda.
      w-full: Mengatur lebar kotak agar memenuhi seluruh lebar kontainer.
      Konten Rincian Pesanan:

      - Kotak Rincian Pesanan order_cart:
      <div class="p-4">
          <h3 class="font-bold text-lg text-gray-800">{{ order_entry.item_name }}</h3>
          <p class="text-gray-600">Date: {{ order_entry.date }}</p>
          <p class="text-gray-800 font-semibold">Price: {{ order_entry.price }}</p>
          <p class="text-gray-700">Description: {{ order_entry.description }}</p>
          <p class="text-gray-700 font-semibold">Rating: {{ order_entry.rating }}</p>
      </div>
      <div>: Elemen untuk menampung konten rincian pesanan.
      <h3>: Elemen judul tingkat tiga untuk nama item.
      <p>: Elemen paragraf untuk informasi lainnya.
      Tailwind CSS:
      p-4: Menambahkan padding di semua sisi sebesar 16px.
      font-bold: Mengatur berat font menjadi tebal untuk nama item.
      text-lg: Mengatur ukuran font menjadi besar (20px) untuk nama item.
      text-gray-800: Mengatur warna teks menjadi abu-abu gelap untuk nama item.
      text-gray-600: Mengatur warna teks menjadi abu-abu sedang untuk tanggal.
      font-semibold: Mengatur berat font menjadi semi-tebal untuk harga dan rating.
      text-gray-700: Mengatur warna teks menjadi abu-abu untuk deskripsi dan rating.

    1) Implementasi tailwind css pada homepage
    
      - Container Utama:
      <div class="overflow-x-hidden px-4 md:px-8 pb-8 pt-24 min-h-screen bg-gray-100 flex flex-col">
      overflow-x-hidden: Mencegah elemen melampaui lebar kontainer, sehingga tidak ada scroll horizontal.
      px-4: Menambahkan padding horizontal (kiri dan kanan) sebesar 16px.
      md:px-8: Menambahkan padding horizontal sebesar 32px pada ukuran layar menengah ke atas (md).
      pb-8: Menambahkan padding bawah sebesar 32px.
      pt-24: Menambahkan padding atas sebesar 96px, memberikan jarak dari bagian atas halaman.
      min-h-screen: Memberikan tinggi minimal setara dengan tinggi layar, memastikan elemen mengambil setidaknya seluruh tinggi layar.
      bg-gray-100: Mengatur latar belakang elemen menjadi warna abu-abu terang.
      flex: Mengatur elemen sebagai flex container.
      flex-col: Menyusun elemen anak dalam kolom vertikal.
      Flexbox Row untuk Informasi:


      - Flexbox Row untuk Informasi:
      <div class="flex flex-row mb-6 p-4 rounded-lg bg-white shadow-md">
      flex: Mengatur elemen ini sebagai flex container.
      flex-row: Menyusun elemen anak dalam satu baris (horizontal).
      mb-6: Menambahkan margin bawah sebesar 24px.
      p-4: Menambahkan padding di semua sisi sebesar 16px.
      rounded-lg: Memberikan sudut melengkung pada elemen.
      bg-white: Mengatur latar belakang elemen menjadi putih.
      shadow-md: Menambahkan bayangan medium untuk efek kedalaman.
      Elemen Informasi:

      - Elemen Informasi:
      <div class="flex-grow">
      flex-grow: Membuat elemen ini tumbuh untuk mengisi ruang yang tersedia dalam flex container, memungkinkan distribusi ruang yang merata antara elemen.
      Teks dan Link untuk Login Terakhir:

      - Teks dan Link untuk Login Terakhir:
      <h5 class="bg-gray-900 text-white font-bold py-2 px-4 rounded-lg">Last Login: {{ last_login }}</h5>
      bg-gray-900: Mengatur latar belakang menjadi abu-abu gelap.
      text-white: Mengatur warna teks menjadi putih.
      font-bold: Mengatur berat font menjadi tebal.
      py-2: Menambahkan padding vertikal (atas dan bawah) sebesar 8px.
      px-4: Menambahkan padding horizontal (kiri dan kanan) sebesar 16px.
      rounded-lg: Memberikan sudut melengkung pada elemen.
      Tautan untuk Menambahkan Entitas Order Baru:

      - Tautan untuk Menambahkan Entitas Order Baru
      <a href="{% url 'main:add_order_entry' %}" class="bg-gray-900 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded-lg">
      bg-gray-900: Mengatur latar belakang menjadi abu-abu gelap.
      hover:bg-gray-700: Mengubah latar belakang menjadi abu-abu lebih terang saat mouse di-hover.
      text-white: Mengatur warna teks menjadi putih.
      font-bold: Mengatur berat font menjadi tebal.
      py-2: Menambahkan padding vertikal sebesar 8px.
      px-4: Menambahkan padding horizontal sebesar 16px.
      rounded-lg: Memberikan sudut melengkung pada elemen.
      Pesan Ketika Tidak Ada Data Order:

      - Kolom untuk Order Entries:
      <div class="columns-1 sm:columns-2 lg:columns-3 w-full">
      columns-1: Menyusun elemen dalam satu kolom secara default.
      sm:columns-2: Mengubah menjadi dua kolom pada ukuran layar kecil (sm).
      lg:columns-3: Mengubah menjadi tiga kolom pada ukuran layar besar (lg).
      w-full: Mengatur lebar elemen agar memenuhi seluruh lebar kontainer.


  4.  Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
    1) Button edit dan hapus produk
      - Tombol edit dan hapus
      <div class="flex justify-end p-2">
          <a href="{% url 'main:edit_order' order_entry.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md mr-2">
              Edit
          </a>
          <a href="{% url 'main:delete_order' order_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
              Delete
          </a>
      </div>
      <div>: Elemen untuk menyusun tombol Edit dan Hapus.
      <a>: Elemen tautan untuk tombol Edit dan Hapus.
      Tailwind CSS:
      flex: Mengatur elemen sebagai flex container.
      justify-end: Menyelaraskan elemen anak ke kanan.
      p-2: Menambahkan padding pada tombol sebesar 8px.
      bg-yellow-500: Mengatur latar belakang tombol Edit menjadi kuning.
      hover:bg-yellow-600: Mengubah latar belakang tombol Edit menjadi kuning lebih gelap saat di-hover.
      text-white: Mengatur warna teks tombol menjadi putih.
      rounded-full: Memberikan sudut melengkung penuh pada tombol.
      transition duration-300: Menambahkan efek transisi selama 300ms pada perubahan warna.
      shadow-md: Menambahkan bayangan medium pada tombol.
      mr-2: Menambahkan margin kanan sebesar 8px untuk tombol Edit agar tidak terlalu dekat dengan tombol Hapus.


  5. Navbar
    1) Untuk device berukuran medium
      -  Navigasi Utama:
      <nav class="bg-gray-900 shadow-lg fixed top-0 left-0 z-40 w-screen">
      <nav>: Elemen semantik yang menunjukkan bahwa bagian ini adalah navigasi.
      Tailwind CSS:
      bg-gray-900: Mengatur latar belakang navbar menjadi warna abu-abu gelap.
      shadow-lg: Menambahkan bayangan besar untuk memberikan efek kedalaman pada navbar.
      fixed: Mengatur navbar agar tetap di atas saat menggulir halaman.
      top-0 left-0: Menempatkan navbar di sudut kiri atas layar.
      z-40: Menentukan lapisan z-index, memastikan navbar berada di atas elemen lainnya.
      w-screen: Mengatur lebar navbar agar memenuhi lebar layar.
      Container untuk Konten:

      - Container untuk Konten:
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div>: Elemen pembungkus untuk konten navbar.
      Tailwind CSS:
      max-w-7xl: Mengatur lebar maksimum container menjadi ukuran yang ditentukan oleh Tailwind.
      mx-auto: Mengatur margin kiri dan kanan otomatis untuk memusatkan container.
      px-4 sm:px-6 lg:px-8: Menambahkan padding horizontal, dengan ukuran yang berbeda untuk ukuran layar kecil, sedang, dan besar.
      Flex Container untuk Navbar:

      - Flex Container untuk Navbar:
      <div class="flex items-center justify-between h-16">
      <div>: Elemen untuk menyusun konten navbar.
      Tailwind CSS:
      flex: Mengatur elemen sebagai flex container.
      items-center: Menyelaraskan elemen anak di tengah secara vertikal.
      justify-between: Menyebar elemen anak sehingga jarak antara mereka maksimal.
      h-16: Mengatur tinggi navbar menjadi 64px.
      Judul Logo:

      - Judul Logo:
      <div class="text-2xl flex items-center font-bold text-white">
          E-Shop
      </div>
      <div>: Elemen untuk menampilkan logo atau judul.
      Tailwind CSS:
      text-2xl: Mengatur ukuran font menjadi 24px.
      flex items-center: Mengatur elemen sebagai flex container dan menyelaraskan elemen di tengah secara vertikal.
      font-bold: Mengatur berat font menjadi tebal.
      text-white: Mengatur warna teks menjadi putih.
      Link Navigasi untuk Pengguna Terautentikasi:

      - Link Navigasi untuk Pengguna Terautentikasi:
      <div class="hidden md:flex justify-center flex-grow">
          {% if user.is_authenticated %}
              <a href="{% url 'main:show_main' %}" class="text-center text-gray-400 text-xl py-2 px-4 hover:text-gray-50">
                  Home
              </a>
              <a class="text-center text-gray-400 text-xl py-2 px-4 hover:text-gray-50">
                  Products
              </a>
              <a class="text-center text-gray-400 text-xl py-2 px-4 hover:text-gray-50">
                  Categories
              </a>
              <a class="text-center text-gray-400 text-xl py-2 px-4 hover:text-gray-50">
                  Cart
              </a>
          {% endif %}
      </div>
      <div>: Elemen untuk menampung tautan navigasi.
      Tailwind CSS:
      hidden md:flex: Menyembunyikan elemen pada layar kecil, menampilkannya sebagai flex container pada layar sedang ke atas.
      justify-center: Menyelaraskan elemen anak ke tengah secara horizontal.
      flex-grow: Memungkinkan div untuk tumbuh mengisi ruang yang tersisa.
      Tautan Logout dan Login/Register:

      - Tautan Logout dan Login/Register:
      <div class="hidden md:flex">
          {% if user.is_authenticated %}
              <span class="text-gray-400 m-auto mx-3">Welcome, {{ user.username }}</span>
              <a href="{% url 'main:logout' %}" class="text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                  Logout
              </a>
          {% else %}
              <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mr-2">
                  Login
              </a>
              <a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                  Register
              </a>
          {% endif %}
      </div>
      <span>: Elemen untuk menampilkan pesan selamat datang jika pengguna sudah terautentikasi.
      <a>: Elemen untuk tautan.
      Tailwind CSS:
      text-gray-400: Mengatur warna teks menjadi abu-abu muda.
      m-auto mx-3: Mengatur margin otomatis dan menambahkan margin horizontal.
      bg-red-500: Mengatur latar belakang tombol logout menjadi merah.
      hover:bg-red-600: Mengubah latar belakang tombol menjadi merah lebih gelap saat di-hover.
      font-bold: Mengatur berat font menjadi tebal untuk tombol.
      py-2 px-4: Menambahkan padding vertikal dan horizontal pada tombol.
      rounded: Memberikan sudut melengkung pada tombol.
      transition duration-300: Menambahkan efek transisi pada perubahan warna.
      Hamburger Button untuk Menu Mobile:

    2) Untuk device mobile  
      - Hamburger Button untuk Menu Mobile:
      <button class="md:hidden flex items-center p-2 text-gray-400 hover:text-white focus:outline-none mobile-menu-button" aria-label="Toggle navigation">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path>
          </svg>
      </button>
      <button>: Elemen untuk tombol hamburger, yang digunakan untuk menampilkan menu mobile.
      Tailwind CSS:
      md:hidden: Menyembunyikan tombol pada layar sedang ke atas.
      flex items-center: Mengatur elemen sebagai flex container dan menyelaraskan elemen di tengah secara vertikal.
      p-2: Menambahkan padding sebesar 8px.
      text-gray-400: Mengatur warna teks menjadi abu-abu muda.
      hover:text-white: Mengubah warna teks menjadi putih saat di-hover.
      focus:outline-none: Menghapus outline saat tombol mendapatkan fokus.
      <svg>: Ikon yang ditampilkan dalam tombol hamburger, terdiri dari tiga garis horizontal.
      Menu Mobile:

      - Menu Mobile
      <div class="mobile-menu hidden md:hidden bg-gray-900 text-white px-4 w-full">
      <div>: Elemen untuk menu mobile.
      Tailwind CSS:
      mobile-menu: Kelas yang digunakan untuk menandai elemen menu mobile.
      hidden md:hidden: Menyembunyikan elemen pada semua ukuran layar hingga md (ukuran layar sedang).
      bg-gray-900: Mengatur latar belakang menu menjadi warna abu-abu gelap.
      text-white: Mengatur warna teks menjadi putih.
      px-4: Menambahkan padding horizontal sebesar 16px.
      w-full: Mengatur lebar menu agar memenuhi seluruh lebar kontainer.
      JavaScript untuk Mengontrol Menu Mobile:

      - JavaScript menambahkan listener tombol hamburger:
      <script>
          const btn = document.querySelector("button.mobile-menu-button");
          const menu = document.querySelector(".mobile-menu");

          btn.addEventListener("click", () => {
              menu.classList.toggle("hidden");
          });
      </script>
      <script>: Tag untuk menyisipkan JavaScript.
      JavaScript:
      Mengambil elemen tombol hamburger dan menu mobile.
      Menambahkan event listener pada tombol untuk mengubah kelas menu ketika tombol diklik, menampilkan atau menyembunyikan menu mobile.

  6. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
    Berikut adalah urutan prioritas spesifisitas selector CSS dari yang terendah ke yang tertinggi:

    1) Universal Selector (*): Selector ini memiliki spesifisitas terendah dan akan diterapkan pada semua elemen jika tidak ada aturan lain yang lebih spesifik.

    2) Type Selector (Element Selector): Selector ini mengacu pada jenis elemen HTML. Contohnya, div, p, h1, dll. Spesifisitasnya lebih tinggi daripada universal selector.

    3) Class Selector (.classname): Selector ini mengacu pada kelas yang diterapkan pada elemen. Setiap kelas yang ditambahkan pada elemen akan meningkatkan spesifisitas. Jika elemen memiliki beberapa kelas, spesifisitasnya dihitung dari jumlah kelas tersebut.

    4) Attribute Selector ([attribute]): Selector ini mencocokkan elemen berdasarkan atributnya. Contohnya, [type="text"] atau [href]. Spesifisitasnya setara dengan class selector.

    5) Pseudo-class Selector (:pseudo-class): Selector ini mencocokkan elemen berdasarkan keadaan tertentu. Contohnya, :hover, :focus, atau :nth-child(). Spesifisitasnya juga setara dengan class selector.

    6) ID Selector (#idname): Selector ini mengacu pada ID unik dari elemen. ID harus unik dalam halaman, sehingga selector ini memiliki spesifisitas yang lebih tinggi.

    7) Inline Styles: Gaya yang diterapkan langsung pada elemen menggunakan atribut style memiliki prioritas tertinggi. Contoh: <div style="color: red;">.

    8) !important Rule: Aturan ini dapat diterapkan pada properti CSS untuk meningkatkan prioritasnya, terlepas dari spesifisitas lainnya. Contoh: color: red !important;.
  
  2. Responsive design adalah konsep penting dalam pengembangan aplikasi web karena beberapa alasan berikut:
    1) Pengalaman Pengguna yang Lebih Baik
    Dengan responsive design, aplikasi web dapat menyesuaikan tampilan dan 
    fungsionalitasnya berdasarkan ukuran layar perangkat pengguna (desktop, 
    tablet, smartphone). Ini meningkatkan kenyamanan dan kepuasan pengguna.
    2) Meningkatkan Aksesibilitas
    Aplikasi yang responsif memungkinkan pengguna dengan berbagai jenis 
    perangkat untuk mengakses konten dengan cara yang mudah. Hal ini penting 
    karena pengguna menggunakan berbagai perangkat dengan ukuran layar yang 
    berbeda.
    3) Efisiensi Pengembangan
    Mengembangkan satu versi aplikasi yang responsif lebih efisien 
    dibandingkan dengan membuat versi terpisah untuk berbagai perangkat. Ini 
    menghemat waktu dan sumber daya dalam pemeliharaan dan pembaruan.

  3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
    1)  Margin
    Definisi: Margin adalah ruang di luar batas elemen. Ini menciptakan jarak 
    antara elemen tersebut dan elemen lain di sekitarnya.
    Fungsi: Menentukan seberapa jauh elemen harus dipisahkan dari elemen lain.
    Implementasi:
    Anda dapat mengatur margin dengan satu atau lebih dari empat nilai: 
    margin, margin-top, margin-right, margin-bottom, dan margin-left.
    Nilai dapat ditentukan dalam piksel (px), persen (%), em, rem, dll.
    Contoh CSS
      .element {
      margin: 20px; /* Semua sisi akan memiliki margin 20px */
      }
      /* Margin yang berbeda untuk setiap sisi */
      .element {
        margin-top: 10px;
        margin-right: 15px;
        margin-bottom: 20px;
        margin-left: 5px;
      }
    2) Border
      Definisi: Border adalah garis yang mengelilingi elemen, berada diantara 
      margin dan padding.
      Fungsi: Menyediakan batas visual untuk elemen dan dapat meningkatkan 
      estetika halaman.
      Implementasi:
      Anda dapat mengatur border dengan properti border, border-width, 
      border-style, dan border-color.
      Contoh border style termasuk solid, dashed, dotted, double, dan none.
      Contoh CSS
        .element {
        border: 2px solid black; /* Border 2px, solid, dan berwarna hitam */
        }
        /* Border dengan pengaturan yang lebih spesifik */
        .element {
          border-width: 1px;
          border-style: dashed;
          border-color: red;
        }
    3) Padding
      Definisi: Padding adalah ruang di dalam batas elemen, antara konten 
      elemen dan border.
      Fungsi: Memberikan jarak antara konten dan tepi elemen, sehingga konten 
      tidak menempel pada batas.
      Implementasi:
      Anda dapat mengatur padding dengan properti padding, padding-top, 
      padding-right, padding-bottom, dan padding-left.
      Nilai dapat ditentukan dalam piksel (px), persen (%), em, rem, dll.
      Contoh CSS
      .element {
      padding: 10px; /* Semua sisi akan memiliki padding 10px */
      }

      /* Padding yang berbeda untuk setiap sisi */
      .element {
        padding-top: 5px;
        padding-right: 15px;
        padding-bottom: 10px;
        padding-left: 20px;
      }
  4. 
    Berikut adalah penjelasan tentang masing-masing konsep serta kegunaannya:
    1) Flex
      1. Kontainer Flex
      Definisi: Kontainer flex adalah elemen induk yang menggunakan properti display: flex atau display: inline-flex. Ini membuat semua elemen anak di dalam kontainer berperilaku sebagai item flex.
      2. Item Flex
      Definisi: Item flex adalah elemen anak yang ada di dalam kontainer flex. Mereka akan beradaptasi dengan ukuran kontainer dan dapat diatur dalam berbagai cara.
      3. Arah Flex
      flex-direction: Properti ini menentukan arah item flex dalam kontainer. Nilai yang bisa digunakan antara lain:
      row: Item disusun secara horizontal (default).
      row-reverse: Item disusun secara horizontal dari kanan ke kiri.
      column: Item disusun secara vertikal.
      column-reverse: Item disusun secara vertikal dari bawah ke atas.
      4. Penyelarasan dan Distribusi
      justify-content: Properti ini digunakan untuk mengatur distribusi ruang di sepanjang sumbu utama (main axis). Nilai yang umum digunakan antara lain:

      flex-start: Item ditempatkan di awal sumbu.
      flex-end: Item ditempatkan di akhir sumbu.
      center: Item ditempatkan di tengah.
      space-between: Ruang di antara item didistribusikan secara merata, tanpa ruang di awal dan akhir.
      space-around: Ruang di antara item didistribusikan secara merata dengan ruang di awal dan akhir.
      align-items: Digunakan untuk mengatur penyelarasan item flex di sepanjang sumbu silang (cross axis). Nilai yang digunakan antara lain:

      flex-start: Item diselaraskan ke atas (untuk flex-direction: column) atau ke kiri (untuk flex-direction: row).
      flex-end: Item diselaraskan ke bawah (untuk flex-direction: column) atau ke kanan (untuk flex-direction: row).
      center: Item diselaraskan di tengah sumbu silang.
      baseline: Item diselaraskan berdasarkan garis dasar teks.
      stretch: Item diperluas untuk mengisi ruang sumbu silang (default).
      5. Ukuran Item Flex
      flex-grow: Menentukan seberapa banyak item flex dapat tumbuh untuk mengisi ruang yang tersedia. Nilai default adalah 0, yang berarti item tidak tumbuh.

      flex-shrink: Menentukan seberapa banyak item flex dapat menyusut ketika ruang dalam kontainer kurang. Nilai default adalah 1, yang berarti item dapat menyusut.

      flex-basis: Menentukan ukuran awal item sebelum ruang dibagi. Nilai ini bisa berupa ukuran tetap (misalnya, 200px) atau auto (ukuran konten).

      flex: Merupakan shorthand untuk mengatur flex-grow, flex-shrink, dan flex-basis dalam satu properti. Contoh: flex: 1 1 200px;.
    
    2) Grid Layout
      1. Prinsip Dasar Grid Layout
      - Grid layout memungkinkan desainer untuk mengelola elemen dalam dua dimensi (horizontal dan vertikal) secara bersamaan. 

      - Desain Responsif: Salah satu kekuatan grid adalah kemampuannya untuk menyesuaikan diri dengan berbagai ukuran layar dan orientasi perangkat. Desain responsif memastikan bahwa tata letak tetap terlihat baik dan fungsional, terlepas dari apakah pengguna mengaksesnya melalui smartphone, tablet, atau desktop.

      2. Komponen Grid
      - Kontainer Grid: Ini adalah elemen induk yang menampung semua item grid. Kontainer grid didefinisikan dengan menggunakan display: grid atau display: inline-grid, yang memungkinkan konten di dalamnya mengikuti struktur grid.

      - Item Grid: Elemen anak di dalam kontainer grid, setiap item grid dapat diposisikan dan diatur sesuai dengan struktur yang telah ditetapkan. Item grid dapat berupa teks, gambar, tombol, atau elemen lainnya.

      - Garis Grid: Garis-garis ini memisahkan kolom dan baris dalam grid. Mereka digunakan sebagai referensi untuk memposisikan item grid di dalam grid.

      - Sel Grid: Ruang antara dua garis grid yang berdekatan. Setiap sel dapat diisi dengan satu atau lebih item grid, memungkinkan penempatan elemen yang lebih dinamis.

      - Area Grid: Area persegi panjang yang didefinisikan oleh garis grid. Area ini dapat diberi nama untuk meningkatkan keterbacaan kode dan memudahkan pemeliharaan. Misalnya, area yang dinamai dapat digunakan untuk mendefinisikan area header, footer, dan konten utama dalam layout.

      3. Memposisikan Grid Item
      - grid-column: Menentukan kolom mana yang harus ditempati oleh sebuah item. Misalnya, grid-column: 1 / 3; akan membuat item mengambil ruang dari kolom pertama hingga kolom kedua (tidak termasuk kolom ketiga).

      - grid-row: Menentukan baris mana yang harus ditempati oleh sebuah item. Contoh: grid-row: 2 / 4; akan membuat item mengambil ruang dari baris kedua hingga ketiga.

      - grid-area: Ini adalah singkatan untuk mendefinisikan baik penempatan baris maupun kolom, sering digunakan ketika Anda telah mendefinisikan area grid yang dinamai. Misalnya, grid-area: header; akan menempatkan item di area yang dinamai "header".

