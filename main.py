"""make.fun news-summary-01 entry: writes the pre-written 11 Nov 2026 summary.
Deterministic, no network, no model calls."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "entry.txt"), encoding="utf-8") as f:
    text = f.read()
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(text)
