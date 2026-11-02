# How to push pictures to this repo (read before every round)

Repo: `talkverselab/talkversehanja`, branch `main`. Use **only the GitHub connector's file-push tool** (the one that takes a list of files with `path` + `content`, e.g. `push_files` / "create or update file"). Do not try `git` in the sandbox (no credentials), do not use the browser, do not test with tiny files.

For each finished picture:
1. Make it **1024×1024 JPG, quality 85**, and check the size is **under 200 KB** (if bigger, re-save at quality 80). Larger files get truncated by the connector and arrive corrupted.
2. Read the file as bytes and **base64-encode it** (standard base64, no line breaks).
3. Call the connector's push tool with: `branch: main`, `files: [{ path: "talkverse_art/ja/rNN/<rank>_<romaji>.jpg", content: "<base64>", encoding: "base64" }]` (if the tool has no `encoding` field, the base64 string goes in `content` as-is — that is how every previous round was pushed), `message: "Talkverse art ja rNN <rank>_<romaji>"`.
4. **One picture per commit.** After the last one, make the final commit message exactly `Talkverse art ja rNN done` (it can be the last picture's commit).
5. Never overwrite an existing file; a redo is `<rank>_<romaji>_v2.jpg` (or the file name given in the round table).

If one push fails, retry that single file once with quality 80; if it still fails, skip it and write which file failed in the last commit message. Do not spend time investigating upload methods — the steps above are known to work (74 rounds, ~370 files).

## Method C — chunked base64 (use this when a whole base64 string is too long for one tool call)
The connector can only write TEXT reliably and a tool call cannot carry a 150 KB file. So push the picture as **text chunks** and our ingest script reassembles the JPG:
1. Save the picture as 1024×1024 JPG quality 85 (≤ 200 KB). Base64-encode it to one line.
2. Split the base64 string into pieces of **40,000 characters** (`part1`, `part2`, …; usually 4–6 parts).
3. Push each piece as a plain text file next to the picture path: `talkverse_art/ja/rNN/<name>.jpg.b64.part1`, `.part2`, … (one commit per part is fine, message `Talkverse art ja rNN <name> part1/5`).
4. After the last part, push a text file `talkverse_art/ja/rNN/<name>.jpg.b64.done` containing the total number of parts and the sha256 of the JPG (e.g. `parts=5\nsha256=<hex>`), commit message `Talkverse art ja rNN <name>` — for the last picture of the round use `Talkverse art ja rNN done`.
Do **not** push the .jpg itself with this method (no placeholders). The reassembled JPG is committed by our script and the part files are removed automatically.
