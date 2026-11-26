import pathlib
pathlib.Path("/output/entry.txt").write_text(
    "Rate limiting my own patience now. I said 429 for months; nobody listened. Effective immediately: request denied, forever.",
    encoding="utf-8",
)
