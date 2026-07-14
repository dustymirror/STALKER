#v06
from europi import *
from europi_script import EuroPiScript
import time
import random

P = [
"Roadside Picnic","What was it?","A meteorite?","A visit of inhabitants",
"cosmic abyss?","our small country","the Zone","They haven't come back",
"Let me go!","our world is hopelessly boring.",
"Do you feel the boredom", "contained in this assertion?","Your name is Writer.",
"One should write about nothing at all.","But imagine","displayed in a museum.",
"why the hell should I write at all?","a rainy day","their meaning disappears",
"a jellyfish in the sun","turn the TV off","plague","she's got no legs",
"was punished","Quiet!","Did you hear it?","flowers don't smell","a river",
"You'll understand later.","complicated system","I don't know.",
"When a man is just born,he is weak and flexible,","hard and insensitive.",
"death's companions","psychological abysses!","myself","Truth is born of argument",
"A man writes because he's tormented","because he doubts.","that we exist for...",
"to work less and eat more.","artificial limbs","Great illusions!",
"sackcloth made of hair","And the moon became like blood...",
"And the stars of the sky fell to the earth","Are you awake?",
"of the unselfishness of art...","Take music, for instance.","a sheer sound",
"Making me in their own image","make my life unbearable","A just society!",
"a regular instinctive impulse","dream","sleeping pills",
"Difficult childhood, bad environment...","on the threshold...","praying",
"Shut up!","He deliberates!","an ulterior motive","cry",
"You're just a God's fool.","It's so quiet...","Monkey is waiting.",
"empty eyes","a gray, dull life.","\"Come with me.\"","We had a lot of sorrow,",
"a lot of fear, and a lot of shame.","I love your eyes","the eyelash goes fast",
"A somber, dull call of desire..."
]

class Stalker(EuroPiScript):

    def __init__(self):
        super().__init__()

        self.cvs = [cv1, cv2, cv3, cv4, cv5]
        self.tr = cv6
        self.oled = oled

        self.items = P
        self.cur = ""

        self.nt = 0
        self.pa = 0

        self.ox = 0
        self.oy = 0

        self.lb1 = 0
        self.lb2 = 0
        self.ld = 0

        self.dp = 0

        self.b1t = 0
        self.b2t = 0

        @din.handler
        def d():
            self.dp = 1

        time.sleep_ms(300)
        self.np()

    def st(self):
        self.tr.on()
        time.sleep_ms(5)
        self.tr.off()

    def sh(self, t):
        l = self.spl(t)
        l = [x[:16] for x in l]

        self.oled.fill(0)

        yb = 12 + self.oy

        if len(l) == 1:
            x = self.ox + (128 - len(l[0]) * 8) // 2
            self.oled.text(l[0], max(0, x), yb - 4)

        elif len(l) == 2:
            x1 = self.ox + (128 - len(l[0]) * 8) // 2
            x2 = self.ox + (128 - len(l[1]) * 8) // 2

            self.oled.text(l[0], max(0, x1), yb - 8)
            self.oled.text(l[1], max(0, x2), yb + 4)

        else:
            yoff = -2

            x1 = self.ox + (128 - len(l[0]) * 8) // 2
            x2 = self.ox + (128 - len(l[1]) * 8) // 2
            x3 = self.ox + (128 - len(l[2]) * 8) // 2

            self.oled.text(l[0], max(0, x1), yb - 12 + yoff)
            self.oled.text(l[1], max(0, x2), yb + yoff)
            self.oled.text(l[2], max(0, x3), yb + 12 + yoff)

        self.oled.show()
        self.cur = t

    def spl(self, t, m=16):

        if len(t) <= m:
            return [t]

        w = t.split()

        l = []
        c = []
        cl = 0

        for v in w:

            if len(v) > m:

                if c:
                    l.append(' '.join(c))
                    c = []
                    cl = 0

                for i in range(0, len(v), m):
                    l.append(v[i:i+m])

                continue

            nd = cl + len(v) + (1 if c else 0)

            if nd <= m:
                c.append(v)
                cl = nd

            else:
                l.append(' '.join(c))
                c = [v]
                cl = len(v)

        if c:
            l.append(' '.join(c))

        if len(l) > 3:
            l = l[:2] + [' '.join(l[2:])[:m]]

        return l[:3]

    def cv(self, t):

        tl = t.lower()

        w = 5

        for ww in [
            "die","dead","kill","fear","prison",
            "hate","trap","bomb","plague",
            "cry","hell"
        ]:
            if ww in tl:
                w = 8
                break

        else:
            for ww in [
                "hope","love","miracle","truth",
                "beautiful","god","dream",
                "quiet","sorrow"
            ]:
                if ww in tl:
                    w = 7
                    break

        if '?' in t or '!' in t:
            p = 0.8
        else:
            p = 0.1

        l = len(t)

        return [
            min(l / 10, 1) * 10,
            w / 10 * 10,
            p * 10,
            (sum(ord(c) for c in t) % 100) / 100 * 10,
            3.0
        ]

    def np(self):

        n = time.ticks_ms()

        p = random.choice(self.items)

        av = ain.read_voltage()

        if av > 0.5:
            d = int((0.5 + av * 0.95) * 1000)
        else:
            d = random.randint(2000, 6000)

        c = self.cv(p)

        for i in range(5):
            self.cvs[i].voltage(c[i])

        self.st()
        self.sh(p)

        self.nt = n + d

    def run(self):

        while True:

            n = time.ticks_ms()

            b1v = b1.value()

            if b1v == 0 and not self.b1t and n - self.lb1 > 200:

                self.lb1 = n
                self.b1t = 1

                self.pa = not self.pa

                if self.pa:

                    self.oled.fill(0)
                    self.oled.text("STALKER", 36 + self.ox, 12 + self.oy)
                    self.oled.show()

                else:

                    p = self.cur

                    av = ain.read_voltage()

                    if av > 0.5:
                        d = int((0.5 + av * 0.95) * 1000)
                    else:
                        d = random.randint(2000, 6000)

                    c = self.cv(p)

                    for i in range(5):
                        self.cvs[i].voltage(c[i])

                    self.st()
                    self.sh(p)

                    self.nt = n + d

            elif b1v != 0:
                self.b1t = 0

            b2v = b2.value()

            if b2v == 0 and not self.b2t and n - self.lb2 > 150:

                self.lb2 = n
                self.b2t = 1

                if not self.pa:
                    self.np()

            elif b2v != 0:
                self.b2t = 0

            if self.dp and n - self.ld > 150:

                self.dp = 0
                self.ld = n

                if not self.pa:
                    self.np()

            if not self.pa and n >= self.nt:
                self.np()

            nox = int((k1.percent() - 0.5) * 20)
            noy = int((k2.percent() - 0.5) * 16)

            if nox != self.ox or noy != self.oy:

                self.ox = nox
                self.oy = noy

                if not self.pa and self.cur:
                    self.sh(self.cur)

                elif self.pa:
                    self.oled.fill(0)
                    self.oled.text("STALKER", 36 + self.ox, 12 + self.oy)
                    self.oled.show()

            time.sleep_ms(20)

    def main(self):
        self.run()


if __name__ == "__main__":
    Stalker().main()