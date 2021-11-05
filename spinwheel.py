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
    while True:
        try:
            maxn = int(input(f'Input angka maks ({MINNUMBER} - {MAXNUMBER}): '))
            assert 7 <= maxn <= 99
        except:
            pass
        else:
            break

    wheel = list(range(1,maxn+1))
    strwheel = []
    for w in wheel:
        wstr = f'^{w:2d}'
        strwheel.extend([c for c in wstr])
    lenstrwheel = len(strwheel)
    lenpart = 20
    strwheel.extend(strwheel[0:lenpart])
    nrotation = random.randint(lenstrwheel,MAXROTATION*lenstrwheel)

    input('Enter untuk mulai..')
    print(format('V', f'^{lenpart}s'))
    for i in range(nrotation):
        pos = i % lenstrwheel
        part = ''.join(strwheel[pos:pos+lenpart])
        print(part, '\r', end='')

        time.sleep((i/nrotation)**2)

    print()
    strp = part[8:11]
    pointed = re.findall('\d+', strp)
    if len(pointed)==1 and strp[1] != '^':
        print('\nBerhenti pada angka', pointed[0].strip())
    else:
        print('\nTidak pada angka')

    opsi = input('\nUlangi, ya? ').lower()
    if opsi not in ['y','ya','yes']:
        break

