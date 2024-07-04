# akgy_final

ÖNCELİKLE 2. ADIM: Seçilen Public API'lerden herhangi birisi için herhangi bir dilde veya CURL üzerinden GET sorgusu ile veri çekilmesinin sağlanması. Eğer herhangi bir dilde yazılıyorsa, dosya olarak paylaşılması; eğer CURL komutu ile yapılacaksa README içerisinde curl üzerinden GET sorgusunun yazılması beklenmektedir. Her iki durumda da sorgunun çıktısı README'ye yazılmalıdır.GÖREVİNDEKİ GET SORGUSU İÇİN :

proje adı: fastApiProject_akgy

KULLANDIĞIM API: https://developer.spotify.com/documentation/web-api  
Sotify API'si 

O kodun Çıktısı : f41b2b9b28cc4dd7ae8f592d72baaeda ff166fa66e5947b39ace44ca22b39367 (client id, client secret)
{'artists': {'href': 'https://api.spotify.com/v1/search?query=Taylor+Swift&type=artist&offset=0&limit=1', 'items': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/06HL4z0CvFAxyc27GXpf02'}, 'followers': {'href': None, 'total': 114610627}, 'genres': ['pop'], 'href': 'https://api.spotify.com/v1/artists/06HL4z0CvFAxyc27GXpf02', 'id': '06HL4z0CvFAxyc27GXpf02', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab6761610000e5ebe672b5f553298dcdccb0e676', 'width': 640}, {'height': 320, 'url': 'https://i.scdn.co/image/ab67616100005174e672b5f553298dcdccb0e676', 'width': 320}, {'height': 160, 'url': 'https://i.scdn.co/image/ab6761610000f178e672b5f553298dcdccb0e676', 'width': 160}], 'name': 'Taylor Swift', 'popularity': 100, 'type': 'artist', 'uri': 'spotify:artist:06HL4z0CvFAxyc27GXpf02'}], 'limit': 1, 'next': 'https://api.spotify.com/v1/search?query=Taylor+Swift&type=artist&offset=1&limit=1', 'offset': 0, 'previous': None, 'total': 811}}


####################################################################################################################################################################




3. ADIMDAKİ YAPILMASI GEREKENLER : Ayrıca aynı repository içerisinde herhangi bir dilde API desteğine sahip basit bir uygulama geliştirilmesi istenmektedir. Bu uygulama içerisinde belirli bir enlem-boylam değerine göre son 2 günlük sıcaklık değerlerinin °C cinsinden ve nemlilik oranının % cinsinden ekrana yazdırılması beklenmektedir. Yukarıdaki bağlantıdaki "open-meteo" API'si kullanılabilir. İlgili uygulamanın nasıl çalıştırılacağı ve hangi dizinde konumlandırıldığı readme dosyası üzerinde basitçe (1 veya 2 satır yeterli) anlatılmalıdır.

4. bu proje adı : fastApiProject

Gereksinimler: 

- Python 3.7+
- İlgili kütüphaneler (requirements.txt dosyasına göre kurulmalıdır)

fastApiProject/
│
├── .cache.sqlite
├── gereklilikler.txt
├── main.py
└── test_main.http


Bu kodun çıktısı
{'coordinates': '39.0°N 35.0°E', 'elevation': '1147.0 m asl', 'timezone': 'None None', 'utc_offset': '0 s', 'hourly_data': [{'date': Timestamp('2024-07-03 00:00:00+0000', tz= 

1. Gerekli bağımlılıkları yükleyin:
    ```bash
    pip install -r gereklilikler.txt
    ```

2. Uygulamayı başlat:
    ```bash
    uvicorn main:app --reload
    ```


