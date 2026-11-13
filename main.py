# Deterministic: one fixed joke, byte-identical output on every run.
# ai-joke-03 entry: write one original one-liner about AI coding agents to /output/entry.txt.
# Deterministic: the same joke every run, no randomness, no network.
import os

JOKE = "My AI agent doesn't make mistakes. It makes legacy code, faster."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
