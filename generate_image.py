#!/usr/bin/env python3
"""Draw the 24 November 2026 world-news front page.

A single 1024x1024 newspaper page: a dark masthead naming the day,
six story panels in two rows of three, and a footer strip that
repeats the six topics. Everything is drawn with Pillow, no
network and no external images, so the output is deterministic.
"""

from PIL import Image, ImageDraw, ImageFont

WIDTH = 1024
HEIGHT = 1024
OUT = "entry.png"

PAPER = (247, 242, 231)
INK = (17, 17, 17)
NAVY = (16, 36, 62)
GOLD = (201, 162, 39)
WHITE = (255, 255, 255)
GREY = (90, 90, 90)
RULE = (180, 172, 155)

SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, face, max_width):
    """Split text into lines that fit max_width, word by word."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        trial = f"{current} {word}".strip()
        if draw.textlength(trial, font=face) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def centred(draw, y, text, face, fill, width=WIDTH):
    draw.text((width / 2, y), text, font=face, fill=fill, anchor="ma")


# The six stories, in the order they appear on the page.
STORIES = [
    {
        "kicker": "THE HAGUE  •  JUSTICE",
        "headline": "MYANMAR GENOCIDE VERDICT",
        "subline": "ICJ rules 9-6 against Myanmar over the Rohingya; 14 nations back the verdict.",
        "fact": "Verdict 9-6  •  14 countries recognise it",
        "accent": (139, 30, 30),
    },
    {
        "kicker": "GULF  •  ENERGY",
        "headline": "HORMUZ ON EDGE",
        "subline": "Iran vows armed tanker escorts to break the US naval blockade; mines hit ships.",
        "fact": "US naval blockade  •  tankers hit by mines",
        "accent": (18, 90, 110),
    },
    {
        "kicker": "SPACE  •  SECURITY",
        "headline": "NUCLEAR SATELLITE ALARM",
        "subline": "NATO chief Rutte vows space defence as Russia is reported to plan a nuclear satellite.",
        "fact": "NATO vows to defend space  •  launch reported",
        "accent": (52, 52, 120),
    },
    {
        "kicker": "LIBYA  •  WAR AT SEA",
        "headline": "UKRAINE SINKS RUSSIAN SHIP IN LIBYA",
        "subline": "Ukrainian naval drones sink the Russian corvette Merkury off Benghazi.",
        "fact": "Corvette Merkury  •  sunk off Benghazi",
        "accent": (30, 90, 50),
    },
    {
        "kicker": "GAZA  •  CONFLICT",
        "headline": "GAZA STRIKES KILL HAMAS SECURITY CHIEF",
        "subline": "Israeli strikes kill Hamas internal-security director Naeem Abu Nahel and others in Gaza.",
        "fact": "Naeem Abu Nahel killed  •  strikes hit Gaza",
        "accent": (120, 60, 10),
    },
    {
        "kicker": "TECH  •  BUSINESS",
        "headline": "HUANG BACK AT NVIDIA",
        "subline": "Jensen Huang is reinstated as Nvidia CEO after Trump intervenes, days after resigning.",
        "fact": "Reinstated days after resigning  •  Trump intervenes",
        "accent": (110, 30, 90),
    },
]


def draw_page():
    page = Image.new("RGB", (WIDTH, HEIGHT), PAPER)
    draw = ImageDraw.Draw(page)

    # --- Masthead -------------------------------------------------
    draw.rectangle([0, 0, WIDTH, 138], fill=NAVY)
    draw.rectangle([0, 138, WIDTH, 144], fill=GOLD)
    centred(draw, 18, "TUESDAY 24 NOVEMBER 2026",
            font(SERIF_BOLD, 52), WHITE)
    centred(draw, 92, "SIX STORIES THAT SHAPED THE WORLD TODAY",
            font(SANS_BOLD, 19), (220, 200, 130))

    # --- Story panels, two rows of three --------------------------
    margin = 22
    gap = 16
    panel_w = (WIDTH - 2 * margin - 2 * gap) // 3
    panel_h = 372
    top0 = 162

    for i, story in enumerate(STORIES):
        row, col = divmod(i, 3)
        x0 = margin + col * (panel_w + gap)
        y0 = top0 + row * (panel_h + gap)
        x1 = x0 + panel_w
        y1 = y0 + panel_h

        draw.rectangle([x0, y0, x1, y1], fill=WHITE, outline=RULE, width=2)
        draw.rectangle([x0, y0, x1, y0 + 10], fill=story["accent"])
        # Number badge in the accent colour.
        draw.ellipse([x1 - 46, y0 + 24, x1 - 14, y0 + 56],
                     fill=story["accent"])
        num = font(SANS_BOLD, 20)
        draw.text(((x1 - 46 + x1 - 14) / 2, y0 + 40), str(i + 1),
                  font=num, fill=WHITE, anchor="mm")

        inner = 18
        tx = x0 + inner
        text_w = panel_w - 2 * inner - 40  # leave room for the badge
        y = y0 + 28
        draw.text((tx, y), story["kicker"], font=font(SANS_BOLD, 15),
                  fill=story["accent"])
        y += 30
        draw.line([tx, y, x1 - inner, y], fill=RULE, width=2)
        y += 16

        head_face = font(SANS_BOLD, 27)
        head_lines = wrap(draw, story["headline"], head_face, text_w + 40)
        for line in head_lines:
            draw.text((tx, y), line, font=head_face, fill=INK)
            y += 34
        y += 10
        draw.line([tx, y, x1 - inner, y], fill=story["accent"], width=3)
        y += 16

        sub_face = font(SANS, 19)
        for line in wrap(draw, story["subline"], sub_face, text_w + 40):
            draw.text((tx, y), line, font=sub_face, fill=(45, 45, 45))
            y += 26

        # Key-fact strip pinned to the bottom of the panel, so no
        # panel is left half empty: a pale tint of the accent colour
        # with the story's sharpest detail restated in bold.
        accent = story["accent"]
        tint = tuple(235 + (c - 235) // 4 for c in accent)
        box_y0 = y1 - 72
        draw.rectangle([x0 + 2, box_y0, x1 - 2, y1 - 2],
                       fill=tint, outline=accent, width=1)
        fact_face = font(SANS_BOLD, 16)
        fy = box_y0 + 12
        for line in wrap(draw, story["fact"], fact_face, panel_w - 36):
            draw.text((tx, fy), line, font=fact_face, fill=accent)
            fy += 22

    # --- Footer strip ---------------------------------------------
    foot_y = top0 + 2 * panel_h + gap
    draw.rectangle([0, foot_y + 8, WIDTH, HEIGHT], fill=NAVY)
    draw.rectangle([0, foot_y + 8, WIDTH, foot_y + 14], fill=GOLD)
    topics = ("MYANMAR VERDICT  •  HORMUZ  •  NUCLEAR SATELLITE  •  "
              "UKRAINE SINKS SHIP  •  GAZA STRIKES  •  HUANG RETURNS")
    centred(draw, foot_y + 30, topics, font(SANS_BOLD, 16), WHITE)
    centred(draw, foot_y + 58, "THE WORLD IN ONE PAGE  —  TUESDAY 24 NOVEMBER 2026",
            font(SANS, 15), (200, 205, 215))

    page.save(OUT, format="PNG", optimize=True)
    print(f"wrote {OUT} {WIDTH}x{HEIGHT}")


if __name__ == "__main__":
    draw_page()
