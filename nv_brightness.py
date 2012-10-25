import commands
import sys

MAX_REGISTER = 0x61c080
CURRENT_REGISTER = 0x61c084


def nvapeek(register):
    out = commands.getoutput("nvapeek %s" % hex(register))
    out = out.split(' ')
    return int(out[1], 16)

def nvapoke(register, value):
    commands.getoutput("nvapoke %s %s" % (hex(register), hex(value)))


MAX_VALUE = nvapeek(MAX_REGISTER)
MIN_VALUE = int('800', 16)
CURRENT_VALUE = nvapeek(CURRENT_REGISTER) & ~0xc0000000

STEP = (MAX_VALUE-MIN_VALUE)/20

cmd = sys.argv[1]

print CURRENT_VALUE

if cmd == 'up':
    CURRENT_VALUE += STEP
    if CURRENT_VALUE > MAX_VALUE:
        CURRENT_VALUE = MAX_VALUE
    nvapoke(CURRENT_REGISTER, CURRENT_VALUE | 0xc0000000)
elif cmd == 'down':
    CURRENT_VALUE -= STEP
    if CURRENT_VALUE < MIN_VALUE:
        CURRENT_VALUE = MIN_VALUE
    nvapoke(CURRENT_REGISTER, CURRENT_VALUE | 0xc0000000)
else:
    print "usage %s [up|down]" % sys.argv[0]
