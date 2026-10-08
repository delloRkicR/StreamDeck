# StreamDeck

Numpad'deki 1-9 tuşlarına istediğiniz işlemleri atayıp klavyenizi bir stream deck'e dönüştüren hafif bir uygulama. Numpad'i olan tüm klavyelerde çalışır.

## Özellikler

- Numpad 1-9 tuşlarının her birine ayrı bir işlem atama
- Uygulama açma, site adresi açma
- Hafif ve kurulumu kolay
- Ücretsiz ve açık kaynak

## Kurulum

Python 3.x gerekli.

    git clone https://github.com/delloRkicR/StreamDeck.git
    cd StreamDeck
    pip install -r requirements.txt

## Kullanım

    python main.py

Tuş atamaları `main.py` dosyasında yapılır. Dosyada `#numpad1` ... `#numpad9` yazan bölümleri bulun ve ilgili tuşa açmak istediğiniz uygulamayı ya da site adresini yazın.

## Exe olarak derleme

    pip install pyinstaller
    pyinstaller NumpadLauncher.spec

Çıktı `dist/` klasöründe oluşur. Hazır exe için Releases sayfasına bakın.

## Katkı

Hata bulursanız Issue açabilir, düzeltme veya yeni özellik için Pull Request gönderebilirsiniz.

## Lisans

Bu proje [MIT Lisansı](LICENSE) ile paylaşılmıştır.
