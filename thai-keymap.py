#!/usr/bin/env python3
TH_normal = (
    '๏฿/-ภถุึคตจขช'
    'ๆไำพะัีรนยบลฅ'
    'ฟหกดเ้่าสวง'
    'ผปแอิืทมใฝ'
)
TH_shift = (
    '๛ๅ๑๒๓๔ู๎๕๖๗๘๙'
    '๐"ฎฑธํ๊ณฯญฐ,ฃ'
    'ฤฆฏโฌ็๋ษศซ.'
    '()ฉฮฺ์?ฒฬฦ'
)
US_normal = (
    '`1234567890-='
    'qwertyuiop[]\\'
    'asdfghjkl;\''
    'zxcvbnm,./'
)
US_shift = (
    '~!@#$%^&*()_+'
    'QWERTYUIOP{}|'
    'ASDFGHJKL:"'
    'ZXCVBNM<>?'
)
KB = [
    '0x11','0x12','0x13','0x14','0x15','0x16','0x17','0x18','0x19','0x1a','0x1b','0x1c','0x1d',
    '0x27','0x28','0x29','0x2a','0x2b','0x2c','0x2d','0x2e','0x2f','0x30','0x31','0x32','0x33',
    '0x3c','0x3d','0x3e','0x3f','0x40','0x41','0x42','0x43','0x44','0x45','0x46',
    '0x4c','0x4d','0x4e','0x4f','0x50','0x51','0x52','0x53','0x54','0x55',
]
SPECIAL = ['\\', '\'']

print('TH chars = %d' % len(TH_normal + TH_shift))
print('US chars = %d' % len(US_normal + US_shift))
print('KB keys = %d' % len(KB))


def th_to_hex(th_char):
    us_in_th = ['/','-','"',',','.','(',')','?']
    if th_char in us_in_th:
        if th_char in SPECIAL:
            return f"'\{th_char}'    "
        return f"'{th_char}'     "
    return '0x%s' % str(th_char.encode()).replace('\\x','').replace("'","")[1:]


with open('th.keymap','w') as th_keymap:
    with open('us.keymap','r') as us_keymap:
        for line in us_keymap:
            if line.startswith('Key 0x'):
                key = line.split(' ')[1]
                if key in KB:
                    index = KB.index(key)
                    if US_normal[index] in SPECIAL:
                        us_normal = "'\%s'    " % US_normal[index]
                    else:
                        us_normal = "'%s'     " % US_normal[index]
                    if US_shift[index] in SPECIAL:
                        us_shift = "'\%s'    " % US_shift[index]
                    else:
                        us_shift = "'%s'     " % US_shift[index]
                    th_normal = th_to_hex(TH_normal[index])
                    th_shift =  th_to_hex(TH_shift[index])
                    line = line.replace(us_normal, th_normal)
                    line = line.replace(us_shift, th_shift)
            th_keymap.write(line)

