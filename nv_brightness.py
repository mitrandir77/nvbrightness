import commands
import sys

MAX_REGISTER = 0x61c080
CURRENT_REGISTER = 0x61c080


def nvpeek(register):
    out = commands.getoutput("nvpeek %s" % hex(register))
    out = out.split(' ')
    return int(out[1], 16)

def nvpoke(register, value):
    commands.getoutput("nvpoke %s %s" % (hex(register), hex(value)))


MAX_VALUE = nvpeek(MAX_REGISTER)
MIN_VALUE = int('800', 16)
CURRENT_VALUE = nvpeek(CURRENT_REGISTER)

STEP = (MAX_VALUE-MIN_VALUE)/20

if len(sys.argv>1):
    cmd = sys.argv[1]

    if cmd == 'up':
        CURRENT_VALUE += STEP
        if CURRENT_VALUE > MAX_VALUE:
            CURRENT_VALUE = MAX_VALUE
        nvpoke(CURRENT_REGISTER, CURRENT_VALUE)
    elif cmd == 'down':
        CURRENT_VALUE -= STEP
        if CURRENT_VALUE < MIN_VALUE:
            CURRENT_VALUE = MIN_VALUE
        nvpoke(CURRENT_REGISTER, CURRENT_VALUE)
else:
    print "usage %s [up|down]" % sys.argv[0]
