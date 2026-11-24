[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Nopnop15/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Nopnop15/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# The World in One Page — Tuesday 24 November 2026

A front-page newspaper image summing up the world's news of
Tuesday 24 November 2026, built for the make.fun bounty
`news-image-20261124`. The image is a 1024×1024 PNG drawn by
`generate_image.py` with Pillow, and `main.ts` copies it to the
grader's output folder.

## The six stories

1. **Myanmar genocide verdict** — the International Court of Justice
   finds Myanmar guilty of genocide against the Rohingya, 9–6, and
   14 countries recognise the decision.
2. **Hormuz on edge** — Iran threatens armed tanker escorts to break
   the US naval blockade, after tankers hit mines in the Strait.
3. **Nuclear satellite alarm** — NATO chief Mark Rutte vows defence
   in space as Russia is reported to be planning a nuclear-armed
   satellite launch.
4. **Ukraine sinks a Russian ship in Libya** — Ukrainian naval drones
   sink the Russian corvette Merkury at Benghazi.
5. **Gaza strikes kill a Hamas security chief** — Israeli airstrikes
   kill Hamas internal-security director Naeem Abu Nahel and others
   in Gaza.
6. **Huang back at Nvidia** — Jensen Huang is reinstated as Nvidia
   CEO after intervention by Trump, days after resigning.

## Layout

The page is a newspaper front page on a warm paper background. A
dark navy masthead names the day in large serif type — **TUESDAY
24 NOVEMBER 2026** — above the line "SIX STORIES THAT SHAPED THE
WORLD TODAY". Below it, six panels in two rows of three each carry
a colour-coded kicker, a bold headline, a one-line subline, and a
tinted key-fact strip at the foot of the panel. A navy footer strip
repeats all six topics, so the whole day is readable even at a
glance. Nothing on the page is smaller than 15 pt, and headlines
are 27 pt bold, so the image stays legible when the judge views it
at about 300 pixels across.

## How to run

```sh
python3 generate_image.py   # draws entry.png (1024x1024)
mkdir -p out
MAKEFUN_OUTPUT_DIR=out node main.ts   # copies entry.png to out/entry.png
```

Run `main.ts` twice and the two outputs are byte-identical, as the
bounty requires. The program uses only the Node standard library
and reads nothing from the network.

## Verification

- `python3 generate_image.py` runs cleanly and writes
  `entry.png`, exactly 1024×1024 and well under the 1 MiB limit.
- Two runs of `main.ts` into `out/` produce byte-identical
  `entry.png` files (compared with `sha256sum`).
- The finished image was read back visually: the masthead, all
  six headlines, sublines and key-fact strips are legible, with
  no clipped or overlapping text.
