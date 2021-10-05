# Luas Persegi Panjang
def luasPersegiPanjang() :
  print('===> MENGHITUNG LUAS PERSEGI PANJANG <===')
  panjang = userInputValidation('Masukkan Panjang : ')
  lebar = userInputValidation('Masukkan Lebar : ')

  luas = panjang * lebar
  checkResultInt(luas, "Luas Persegi Panjang =")
  print("Luas Persegi Panjang =", luas)


# Luas Persegi
def luasPersegi() :
  print('===> MENGHITUNG LUAS PERSEGI <===')
  sisi = userInputValidation('Masukkan Panjang Sisi : ')

  luas = sisi**2
  checkResultInt(luas, "Luas Persegi =")
  print("Luas Persegi =", luas)


# Luas Segitiga Siku-Siku
def luasSegitigaSiku() :
  print('===> MENGHITUNG LUAS SEGITIGA SIKU-SIKU <===')
  alas = userInputValidation("Masukkan Alas : ")
  tinggi = userInputValidation("Masukkan Tinggi : ")
  
  luas = 0.5 * alas * tinggi
  checkResultInt(luas, "Luas Segitiga =")
  print("Luas Segitiga =", luas)


# Luas Lingkaran
def luasLingkaran() :
  print('===> MENGHITUNG LUAS LINGKARAN <===')
  phi = 3.14
  r = userInputValidation("Masukkan Jari-Jari Lingkaran : ")

  luas = phi * (r**2)
  print("Luas Lingkaran =", luas)


# Luas Belah Ketupat
def luasBelahKetupat() :
  print('===> MENGHITUNG LUAS BELAH KETUPAT <===')
  diagonal1 = userInputValidation("Masukkan Panjang Diagonal Pertama :")
  diagonal2 = userInputValidation("Masukkan Panjang Diagonal Kedua : ")

  luas = 0.5 * diagonal1 * diagonal2
  checkResultInt(luas, "Luas Belah Ketupat =")
  print("Luas Belah Ketupat =", luas)
  

# Keliling Lingkaran
def kelilingLingkaran() :
  print('===> MENGHITUNG KELILING LINGKARAN <===')
  phi = 3.14
  r = userInputValidation('Masukkan Jari-Jari Lingkaran : ')
  
  keliling = 2 * phi * r
  print("Keliling Lingkaran =", keliling)


# Keliling Segitiga Siku-Siku
def kelilingSegitigaSiku():
  print('===> MENGHITUNG KELILING SEGITIGA SIKU-SIKU <===')
  sisi1 = userInputValidation("Masukkan Panjang Sisi Pertama : ")
  sisi2 = userInputValidation("Masukkan Panjang Sisi Kedua : ")
  sisi3 = userInputValidation("Masukkan Panjang Sisi Ketiga : ")

  keliling = sisi1 + sisi2 + sisi3
  checkResultInt(keliling, "Keliling Segitiga Siku-Siku =")
  print("Keliling Segitiga Siku-Siku =", keliling)


# Keliling Persegi
def kelilingPersegi() :
  print('===> MENGHITUNG KELILING PERSEGI <===') 
  sisi = userInputValidation("Masukkan Panjang Sisi : ")

  keliling = 4 * sisi
  checkResultInt(keliling, "Keliling Persegi =")
  print("Keliling Persegi =", keliling)


# Keliling Persegi Panjang 
def kelilingPersegiPanjang() :
  print('===> MENGHITUNG KELILING PERSEGI PANJANG <===')
  panjang = userInputValidation("Masukkan Panjang : ")
  lebar = userInputValidation("Masukkan Lebar : ")
  
  keliling = 2 * (panjang + lebar)
  checkResultInt(keliling, "Keliling Persegi Panjang =")
  print("Keliling Persegi Panjang =", keliling)


# Keliling Belah Ketupat
def kelilingBelahKetupat() :
  print('===> MENGHITUNG KELILING BELAH KETUPAT <===')
  sisi = userInputValidation("Masukkan Panjang Sisi : ")
  
  keliling = 4 * sisi
  checkResultInt(keliling, "Keliling Belah Ketupat =")
  print("Keliling Belah Ketupat =", keliling)

# Pernyataan
def statement() :
  print('\nSilahkan Pilih Rumus Mana Yang Ingin Digunakan :')
  print('1. Luas Persegi Panjang')
  print('2. Luas Persegi')
  print('3. Luas Segitiga Siku-Siku')
  print('4. Luas Lingkaran')
  print('5. Luas Belah Ketupat')
  print('6. Keliling Lingkaran')
  print('7. Keliling Segitiga Siku-Siku')
  print('8. Keliling Persegi')
  print('9. Keliling Persegi Panjang')
  print('10. Keliling Belah Ketupat')


# user input validation inside the formula
def userInputValidation(message):
  while True:
    try:
      userInput = float(input(message));
      return userInput;
    except ValueError:
      print('SISTEM OTOMATIS MENOLAK HURUF\nTOLONG MASUKKIN ANGKA SAJA');
      # errMessage()
      continue; # try again until the inputted value is satisfied


# user input validation before the formula 
def userInput():
  while True:
    try:
      userInput = int(input('Pilih Angka Berdasarkan Rumus Yang Diinginkan:\n'));
      print('Anda Memilih Angka', userInput)
      return userInput
    except ValueError:
      errMessage()
      continue; # try again until the inputted value is satisfied


# Error Message
def errMessage() :
  print("WARNING!!! Masukkan Angka Diantara 1-10")


# If Result Integer, Return Integer Value
def checkResultInt(result, message) :
  if(result.is_integer()):
    print(message, int(result));
    exit();


# Check What Did user Input
def checkUserInput(userInput) :
  # errMessage() if(userInput < 1 or userInput > 10) else None
  if(userInput == 1) : luasPersegiPanjang()
  if(userInput == 2) : luasPersegi()
  if(userInput == 3) : luasSegitigaSiku()
  if(userInput == 4) : luasLingkaran()
  if(userInput == 5) : luasBelahKetupat()
  if(userInput == 6) : kelilingLingkaran()
  if(userInput == 7) : kelilingSegitigaSiku()
  if(userInput == 8) : kelilingPersegi()
  if(userInput == 9) : kelilingPersegiPanjang()
  if(userInput == 10) : kelilingBelahKetupat()
  if(userInput < 1 or userInput > 10) : errMessage()

statement();
checkUserInput(userInput());

