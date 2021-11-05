import random
import time
import re

MINNUMBER = 7
MAXNUMBER = 99
MAXROTATION = 3

print('RODA PUTAR')
print('~~~~~~~~~~')

while True:
    print()
    
    # input angka maksimum
    while True:
        try:
            # harus integer dan antara 7-99
            maxn = int(input(f'Input angka maks ({MINNUMBER} - {MAXNUMBER}): '))
            assert 7 <= maxn <= 99
        except:
            # kalau error, looping
            pass
        else:
            # ga ada error maka keluar loop
            break

    # generate angka 1 sd angka maksimum
    wheel = list(range(1,maxn+1))
    # generate list, setiap angka diwakili oleh 3 karakter ^ dan 2 digit
    # sebagai pita wheel yang akan spin
    strwheel = []
    for w in wheel:
        wstr = f'^{w:2d}'
        strwheel.extend([c for c in wstr])
    lenstrwheel = len(strwheel)
    # panjang pita yg tampil di layar
    lenpart = 20
    strwheel.extend(strwheel[0:lenpart])
    # rotasi tick to tick secara acak
    nrotation = random.randint(lenstrwheel,MAXROTATION*lenstrwheel)

    # power untuk mensimulasikan putaran cepat ke lambat
    pow = 4/378 * nrotation + 6
    input('Enter untuk mulai..')
    
    # cetak pita wheel yag dispin sebanyak nrotation tick to tick
    print(format('V', f'^{lenpart}s'))
    for i in range(nrotation):
        pos = i % lenstrwheel
        part = ''.join(strwheel[pos:pos+lenpart])
        print(part, '\r', end='')
        # sleep ini untuk efek cepat ke lambat
        time.sleep((i/nrotation)**pow)
        
    # selesai spin, baca dimana titik hentinya
    time.sleep(1)     
    strp = part[8:11]
    pointed = re.findall('\d+', strp)
    print()
    if len(pointed)==1 and strp[1] != '^':
        print('\nBerhenti pada angka', pointed[0].strip())
    else:
        print('\nTidak pada angka')

    # ulangi atau selesai
    opsi = input('\nUlangi, ya? ').lower()
    if opsi not in ['y','ya','yes']:
        break

