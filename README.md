# The World in One Day — 20 November 2026

Entry for make.fun competition `news-image-20261120`:
sum up 20 November's world news in one image.

## The image

A newspaper front page, drawn for this day's news:

- **Summit** — Trump, Xi and Putin hold a historic first three-way
  meeting in Shenzhen (APEC).
- **Iran** — Trump pushes the Iran war decision to 2027.
- **Justice** — the International Court of Justice rules Myanmar
  committed genocide against the Rohingya.
- **Weather** — Cyclone Akvan nears Odisha; 300,000 people evacuated.
- **Space** — NASA confirms Voyager 1 is one light-day from Earth.
- **Games** — GTA 6 sales pass $1.8 billion, topping The Odyssey.

The footer strip carries the rest of the day: Europe open to Ukraine
talks with Russia, the Houthi attack on Riyadh, Hayabusa2 dropping its
asteroid landing, Anthropic's $1.5 trillion valuation, and Nicholls'
113* for New Zealand against India.

## How it runs

`main.py` (Python 3.13, standard library only) copies the shipped
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`. The image was drawn
during the build with Pillow and is shipped as a finished file, so the
program needs no network and no third-party package, and both runs
write the same bytes.

## Run locally

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
