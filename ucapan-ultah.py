print('Halo selamat datang! ini siapa ya')
nama=input('Coba masukin nama kamu disini ya:')
nama_asli='Random'

if nama==nama_asli:
    print('Halo', nama, '!')
else:
    print('Ga usah boong ya, aku tahu nama kamu kok!')

print('Kenalin, aku program yang dibuat oleh Orang Baik')
print('')
print('')
umur=int(input('Umur kamu berapa?'))
umur_asli=100001

if umur==umur_asli:
    print('Gapapa sih cuma nanya aja hehe')
else:
    print('Ga usah khawatir, cuma nanya aja kok!')

print('')
print('')

ultah=input('Hari ini kamu ultah ga?(yes/no):')

while ultah!='yes':
    ultah=input('Boong lu pasti, aku tanya lagi, hari ini kamu ultah ga?')
print('')
print('')
banyak=int(input('Mau diucapin berapa kali?'))
while banyak<=0:
    banyak=int(input('Serius. mau diucapin berapa kali?'))

for i in range (banyak):
    print('HAPPY BIRTHDAY KAMU! <3')

while True:
    pass