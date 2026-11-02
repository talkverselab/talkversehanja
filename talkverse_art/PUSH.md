# How to push pictures to this repo (read before every round)

Repo: `talkverselab/talkversehanja`, branch `main`. Use **only the GitHub connector's file-push tool** (the one that takes a list of files with `path` + `content`, e.g. `push_files` / "create or update file"). Do not try `git` in the sandbox (no credentials), do not use the browser, do not test with tiny files.

For each finished picture:
1. Make it **1024×1024 JPG, quality 85**, and check the size is **under 200 KB** (if bigger, re-save at quality 80). Larger files get truncated by the connector and arrive corrupted.
2. Read the file as bytes and **base64-encode it** (standard base64, no line breaks).
3. Call the connector's push tool with: `branch: main`, `files: [{ path: "talkverse_art/ja/rNN/<rank>_<romaji>.jpg", content: "<base64>", encoding: "base64" }]` (if the tool has no `encoding` field, the base64 string goes in `content` as-is — that is how every previous round was pushed), `message: "Talkverse art ja rNN <rank>_<romaji>"`.
4. **One picture per commit.** After the last one, make the final commit message exactly `Talkverse art ja rNN done` (it can be the last picture's commit).
5. Never overwrite an existing file; a redo is `<rank>_<romaji>_v2.jpg` (or the file name given in the round table).

If one push fails, retry that single file once with quality 80; if it still fails, skip it and write which file failed in the last commit message. Do not spend time investigating upload methods — the steps above are known to work (74 rounds, ~370 files).
