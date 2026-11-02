# How to push pictures to this repo (read before every round)

Repo: `talkverselab/talkversehanja`, branch `main`.

## The method that works (verified 2026-11-02, pushtest 138,098 B byte-identical)
Binary files cannot go through the connector's text push tool (it stores text, so a JPG arrives as a few bytes). Use **git in the sandbox with the GitHub connector's credential helper** instead — this is exactly what succeeded:
1. `git clone` the repo in the sandbox (the connector's credential helper provides auth; no token needed).
2. Copy each finished picture into the clone at its path from the round table (`talkverse_art/ja/rNN/<rank>_<romaji>.jpg`, 1024×1024 JPG, quality 85).
3. `git add` → `git commit -m "Talkverse art ja rNN <rank>_<romaji>"` → `git pull --rebase` → `git push`. One picture per commit is fine; the LAST commit message of the round must be exactly `Talkverse art ja rNN done`.
4. Verify with `github___get_file_contents` that the pushed file size equals the local file size.
Never write placeholders, never push base64 text files, never overwrite an existing picture (a redo is `_v2`, `_v3`…).

## Method C (fallback only, do not use unless git push itself fails) — chunked base64 (use this when a whole base64 string is too long for one tool call)
The connector can only write TEXT reliably and a tool call cannot carry a 150 KB file. So push the picture as **text chunks** and our ingest script reassembles the JPG:
1. Save the picture as 1024×1024 JPG quality 85 (≤ 200 KB). Base64-encode it to one line.
2. Split the base64 string into pieces small enough to paste whole into ONE tool call — **8,000 characters each** (`part1`, `part2`, …; a 150 KB picture is ~25 parts). If even that fails, use 4,000. **Never write a placeholder** (`PLACEHOLDER…`) into a part: the part's content must be the actual base64 text, copied in full.
3. Push each piece as a plain text file next to the picture path: `talkverse_art/ja/rNN/<name>.jpg.b64.part1`, `.part2`, … (one commit per part is fine, message `Talkverse art ja rNN <name> part1/5`).
4. After the last part, push a text file `talkverse_art/ja/rNN/<name>.jpg.b64.done` containing the total number of parts and the sha256 of the JPG (e.g. `parts=5\nsha256=<hex>`), commit message `Talkverse art ja rNN <name>` — for the last picture of the round use `Talkverse art ja rNN done`.
Do **not** push the .jpg itself with this method (no placeholders). The reassembled JPG is committed by our script and the part files are removed automatically.
