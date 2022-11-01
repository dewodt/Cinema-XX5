# Data User
list_user = [{'nama': 'moi735', 'email': 'moi735@gmail.coom', 'password': '735', 'saldo': 500000, 'riwayat': []}, {'nama': 's', 'email': 's', 'password': 's', 'saldo': 550000, 'riwayat': [{'Tanggal Beli': '13:45 31-10-2022', 'Lokasi': 'XX5 Aeon Mall BSD', 'Judul': 'Black Adam', 'Jadwal': '16:00 today', 'Ticket': 'A1', 'Total': 'Rp45.000,00'}, {'Tanggal Beli': '22:51 31-10-2022', 'Lokasi': 'XX5 Aeon Mall BSD', 'Judul': 'Black Adam', 'Jadwal': '13:30 tomorrow', 'Ticket': 'A1', 'Total': 'Rp45.000,00'}, {'Tanggal Beli': '22:51 31-10-2022', 'Lokasi': 'XX5 Aeon Mall BSD', 'Judul': 'AMSTERDAM', 'Jadwal': '13:30 tomorrow', 'Ticket': 'A1', 'Total': 'Rp40.000,00'}]}]

# Data Lokasi
location =  ['XX5 Aeon Mall BSD', 'XX5 Ciwalk Bandung', 'XX5 Plaza Indonesia']

# Data Waktu
time_str = ['13:30', '16:00', '18:30', '21:00']
time_int = [
            {'hour': 13, 'minute': 30},
            {'hour': 16, 'minute': 00},
            {'hour': 18, 'minute': 30},
            {'hour': 21, 'minute': 00},
        ]

# Data Token & Uang
list_validasi = {
    50000: {
            'gopay': '50gopay',
            'ovo': '050ovo',
            'bca': '050bca',
            'mandiri': '050mandiri',
            'bni': '050bni',
            'bri': '050bri',
        },
    100000: {
        'gopay': '100gopay',
        'ovo': '100ovo',
        'bca': '100bca',
        'mandiri': '100mandiri',
        'bni': '100bni',
        'bri': '100bri',
    },
    150000: {
        'gopay': '150gopay',
        'ovo': '150ovo',
        'bca': '150bca',
        'mandiri': '150mandiri',
        'bni': '150bni',
        'bri': '150bri',
    },
    200000: {
        'gopay': '200gopay',
        'ovo': '200ovo',
        'bca': '200bca',
        'mandiri': '200mandiri',
        'bni': '200bni',
        'bri': '200bri',
    }
}

# Data Upcoming Movie
upcoming_movie = [
    {
        'img_on': 'images/blackpanther_on.png',
        'img_off': 'images/blackpanther_off.png',
        'title': 'Black Panther: Wakanda Forever',
        'age': '-',
        'genre': 'Action, Adventure, Drama',
        'duration': '- Minutes',
        'plot': 'Rakyat Wakanda kali ini akan berjuang untuk melindungi negerinya dari campur tangan kekuatan dunia setelah kematian sang Raja T\'Challa.',
        'producer': 'Kevin Feige, Nate Moore',
        'director': 'Ryan Coogler',
        'writer': 'Ryan Coogler, Joe Robert Cole',
        'cast': 'Letitia Wright, Lupita Nyong\'o, Tenoch Huerta, Angela Bassett, Martin Freeman, Danai Gurira, Michaela Coel, Dominique Thorne, Winston Duke, Richard Schiff, Mabel Cadena',
    },
    {
        'img_on': 'images/bosslevel_on.png',
        'img_off': 'images/bosslevel_off.png',
        'title': 'BOSS LEVEL',
        'age': '17+',
        'genre': 'Action, Adventure, Comedy',
        'duration': '101 Minutes',
        'plot': 'Terperangkap dalam lingkaran waktu yang terus-menerus mengulangi hari pembunuhannya, seorang mantan agen pasukan khusus harus membuka misteri di balik kematiannya sebelum dunia hancur.',
        'producer': 'Joe Carnahan, Frank Grillo',
        'director': 'Joe Carnahan',
        'writer': 'Chris Borey, Eddie Borey, Joe Carnahan',
        'cast': 'Frank Grillo, Mel Gibson, Naomi Watts, Will Sasso, Annabelle Walls, Sheaun Mckinney, Selina Lo, Michelle Yeoh, Ken Jeong, Meadow Williams, Mathilde Ollivier, Armida Lopez',
    },
    {
        'img_on': 'images/sriasih_on.png',
        'img_off': 'images/sriasih_off.png',
        'title': 'SRI ASIH',
        'age': '-',
        'genre': 'Action, Sci-fi',
        'duration': '- Minutes',
        'plot': 'Alana tidak mengerti mengapa dia selalu dikuasai oleh kemarahan. Tapi dia selalu berusaha untuk melawannya. Dia lahir saat letusan gunung berapi yang memisahkan dia dan orang tuanya. Dia kemudian diadopsi oleh seorang wanita kaya yang berusaha membantunya menjalani kehidupan normal. Tapi saat dewasa, Alana menemukan kebenaran tentang asalnya. Dia bukan manusia biasa. Dia bisa menjadi kebaikan untuk kehidupan. Atau menjadi kehancuran bila ia tidak dapat mengendalikan amarahnya.',
        'producer': 'Bismarka Kurniawan, Wicky V. Olindo, Joko Anwar',
        'director': 'Upi',
        'writer': 'Upi, Joko Anwar',
        'cast': 'Pevita Pearce, Reza Rahadian, Christine Hakim, Jefri Nichol, Dimas Anggara, Surya Saputra, Jenny Zhang, Randy Pangalila',
    },
    {
        'img_on': 'images/tegar_on.png',
        'img_off': 'images/tegar_off.png',
        'title': 'TEGAR',
        'age': 'SU',
        'genre': 'Drama',
        'duration': '92 Minutes',
        'plot': 'Tegar (10), seorang anak berkebutuhan khusus yang menginginkan bisa seperti anak pada umumnya, berteman dan bersekolah. Di hari ulang tahunnya yang ke-10, Tegar mengutarakan impiannya kepada sang Kakek. Namun, keputusan Kakek untuk mewujudkan impian Tegar justru membuat Kakek dan Ibu berselisih. Akhirnya, Tegar memutuskan untuk pergi dari rumah demi mengejar mimpinya.',
        'producer': 'Chandra Sembiring, Surajuddin Datau',
        'director': 'Anggi Frisca',
        'writer': 'Alim Sudio, Anggi Frisca',
        'cast': 'Aldifi Tegarajasa, Deddy Mizwar, Sha Ine Febriyanti, Joanita Chatarina, M. Adhiyat, Prihartono Mirsaputra, Jamaluddin Latief',
    },
]

# Data Daftar Film
list_movie = [
    {
        'img_on': 'images/blackadam_on.png',
        'img_off': 'images/blackadam_off.png',
        'title': 'Black Adam',
        'age': 'R13',
        'genre': 'Action, Fantasy, Sci-Fi',
        'duration': '125 Minutes',
        'plot': 'Berkisah tentang sosok antihero yang mendapatkan kekuatan dari dewa mesir bernama Adam. Ia datang untuk menciptakan keadilan di dunia saat ini.',
        'producer': 'Beau Flynn, Dany Garcia, Hiram Garcia',
        'director': 'Jaume Collet-serra',
        'writer': 'Adam Sztykiel, Rory Haines, Sohrab Noshirvani',
        'cast': 'Dwayne Johnson, Viola Davis, Sarah Shahi, Pierce Brosnan, Noah Centineo, Aldis Hodge, Angel Rosario Jr., Joseph Gatt, Mohammed Amer, Quintessa Swindell',
        'price': 45000,
        'sold_seat': {
            'XX5 Aeon Mall BSD': {
                'today': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                    },
                'tomorrow': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                },
            },
            'XX5 Ciwalk Bandung': {
                'today': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                    },
                'tomorrow': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                },
            },
            'XX5 Plaza Indonesia': {
                'today': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                    },
                'tomorrow': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                },
            },
        },
    },
    {
        'img_on': 'images/amsterdam_on.png',
        'img_off': 'images/amsterdam_off.png',
        'title': 'AMSTERDAM',
        'age': 'R13',
        'genre': 'Drama, History',
        'duration': '134 Minutes',
        'plot': 'Berlatar tahun 1930-an, tiga sahabat Burt Berendsen (Christian Bale), Valerie Voze (Margot Robbie) dan Harold Woodman (John David Washington) adalah saksi pembunuhan yang akhirnya menjadi tersangka. Ketiganya berusaha mencari jalan keluar dan mengubah jalan sejarah Amerika.',
        'producer': 'Christian Bale, Matthew Budman, Anthony Katagas, Arnon Milchan, David O. Russell',
        'director': 'David O. Russell',
        'writer': 'David O. Russell',
        'cast': 'Christian Bale, Margot Robbie, John David Washington, Rami Malek, Mike Myers, Taylor Swift, Zoe Saldana, Robert De Niro, Anya Taylor-joy, Chris Rock, Michael Shannon.',
        'price': 40000,
        'sold_seat': {
            'XX5 Aeon Mall BSD': {
                'today': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                    },
                'tomorrow': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                },
            },
            'XX5 Ciwalk Bandung': {
                'today': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                    },
                'tomorrow': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                },
            },
            'XX5 XX5 Plaza Indonesia': {
                'today': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                    },
                'tomorrow': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                },
            },
        },
    },
    {
        'img_on': 'images/doctorg_on.png',
        'img_off': 'images/doctorg_off.png',
        'title': 'DOCTOR G',
        'age': 'R17+',
        'genre': 'Comedy',
        'duration': '122 Minutes',
        'plot': 'Sebuah drama komedi kampus kedokteran, Doctor G adalah tentang perjuangan yang lucu Dr. Uday Gupta, dia mempunyai keinginan untuk berspesialisasi dalam Ortopedi, tetapi terjebak di kelas Ginekologi yang semuanya perempuan.',
        'producer': 'Vineet Jain',
        'director': 'Anubhuti Kashyap',
        'writer': 'Saurabh Bharat',
        'cast': 'Ayushmann Khuranna, Rakul Preet Singh, Shefali Shah, Sheeba Chaddha, Abhinay Raj Singh, Paresh Pahuja, Jhumma Mitra, Azzy Bagria',
        'price': 40000,
        'sold_seat': {
            'XX5 Aeon Mall BSD': {
                'today': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                    },
                'tomorrow': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                },
            },
            'XX5 Ciwalk Bandung': {
                'today': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                    },
                'tomorrow': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                },
            },
            'XX5 Plaza Indonesia': {
                'today': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                    },
                'tomorrow': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                },
            },
        }, 
    },
    {
        'img_on': 'images/onepiece_on.png',
        'img_off': 'images/onepiece_off.png',
        'title': 'ONE PIECE FILM: RED',
        'age': 'R13',
        'genre': 'Animation, Adventure, Fantasy',
        'duration': '115 Minutes',
        'plot': 'Untuk pertama kalinya, Uta - penyanyi paling dicintai akan mengungkapkan dirinya kepada dunia di konser langsungnya. Suara yang ditunggu-tunggu oleh seluruh dunia akan segera bergema.',
        'producer': 'Eiichiro Oda',
        'director': 'Goro Taniguchi',
        'writer': 'Tsutomu Kuroiwa',
        'cast': 'Kazuya Nakai, Kaori Nazuka, Akemi Okamura, Kappei Yamaguchi, Mayumi Tanaka, Yuriko Yamaguchi, Hiroaki Hirata, Shuichi Ikeda',
        'price': 50000,
        'sold_seat': {
            'XX5 Aeon Mall BSD': {
                'today': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                    },
                'tomorrow': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                },
            },
            'XX5 Ciwalk Bandung': {
                'today': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                    },
                'tomorrow': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                },
            },
            'XX5 Plaza Indonesia': {
                'today': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                    },
                'tomorrow': {
                    '13:30': [[False for j in range(15)] for i in range(9)],
                    '16:00': [[False for j in range(15)] for i in range(9)],
                    '18:30': [[False for j in range(15)] for i in range(9)],
                    '21:00': [[False for j in range(15)] for i in range(9)],
                },
            },
        },
    },
]

# Daftar Sold Movie

list_movie[0]['sold_seat']['XX5 Aeon Mall BSD']['today']['16:00'][1][0] = True
list_movie[0]['sold_seat']['XX5 Aeon Mall BSD']['tomorrow']['13:30'][1][0] = True
list_movie[1]['sold_seat']['XX5 Aeon Mall BSD']['tomorrow']['13:30'][1][0] = True