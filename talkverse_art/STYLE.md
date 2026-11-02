# Talkverse language-app illustrations — shared style (for Grok)

Talkverse makes one language-learning app per language for Korean learners. These pictures go on flashcards (one word = one picture) and in short dialogue episodes. The look follows the talkverse.uk website.

## Always
- Square 1:1, 1024×1024 preferred (768×768 is acceptable if the upload fails), JPG, fully opaque.
- ONE clear subject that a learner can name in 2 seconds. Centered, filling about 70% of the frame, generous margin.
- Background: very light pastel mesh gradient fading to white — soft peach #ffd39b, pink #f5b8e6, lavender #a9a4ff and sky blue #8fe3ff blobs, mostly white near the center. No scenery unless the word needs a place (then keep it simple and light).
- Main ink / outline color: deep navy #0a2540. Highlight color: the app's accent pair (given in each round file, e.g. Japanese = orange #e88b4a / #f5c07a), plus the site's indigo #635bff used sparingly.
- People: friendly, modern, adult (20s–40s unless the word says child/parent), simple readable faces, everyday clothes. Settings and objects should feel natural for the country of the language.
- Safe for a 12+ app.

## Never
- No letters, words, numbers, captions, speech-bubble text, signs with writing, clocks with numerals, calendar digits.
- No logos, brands, recognizable products, real people, celebrities, or characters from existing anime, games, films or books. Do not imitate any named artist or studio.
- No flags, no national stereotypes or costumes unless the word itself is that thing.
- No watermarks, signatures, frames, borders, transparent backgrounds.
- Do not upload failed or placeholder files.

## Delivery
- Put files exactly at the path given in the round file. **One commit per image is fine** (upload each JPG as base64 content with the GitHub connector, the way round 01 worked). After the last image, make the last commit message `Talkverse art <lang> r<NN> done: <words>`. Claude watches the repo, reviews, and writes the next round.
- Never overwrite an existing file; a redo is `<name>_v2.jpg`.


## Per-round limit (2026-11-02)
- A round is 4 pictures (redos included). **Generate at most 6 images per round in total, including retries/repairs.** If something still fails, skip it and note it in the commit message — the next round will re-request it.

## Framing (2026-11-02)
- People are shown **full body, head to feet**; never crop heads or faces at the frame edge. Keep a margin around the subject. Output exactly 1024×1024.
- The image tool has no 1:1 output (2026-11-02). **Generate LANDSCAPE (3:2) with the subject centered and empty pastel background on both sides, then center-crop the sides to 1024×1024.** Never crop top/bottom, never pad with bars, never use portrait.
