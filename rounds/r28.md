# Grok 작업 지시서 — 28회차 (2026-10-18) · B 맞춤 A컷 5자

리뷰 페이지: https://talkverse.uk/hanja-review/ (맨 위 "0. 회차 리뷰") · 이 문서: https://talkverse.uk/hanja-review/GROK_NEXT.md?r=28 · 저장소 사본: `rounds/r28.md`

## 0. 이번 회차부터 바뀐 것 — 먼저 읽을 것

1. **순서: 글자마다 B컷(글자)을 먼저 만들고, 그 B컷을 첨부해서 A컷(그림)을 만든다.** A 는 네가 만든 B 위에 겹쳐야 하므로 반드시 B → A 순서.
2. **B컷**: `claude_b/<코드>_B.jpg`(Claude 정자 렌더)를 이미지 1(획 구조), `huo_B.jpg`(네가 전에 그린 火)를 이미지 2(붓 질감)로 넣는다. 획 수·자리·비율은 이미지 1 과 같게(붓맛에 따른 작은 변형만). **붓 질감은 획의 양 끝(들어가는 머리, 빠지는 꼬리)에만** — 획 몸통은 속이 꽉 찬 매끈한 먹. 획 전체에 갈필을 넣으면 재작업(사용자 지시 2026-10-18).
3. **A컷**: 네 B컷을 첨부하고 아래 LAYOUT 대로 그림의 부위를 획 자리에 놓는다. 그림을 B 위에 겹쳤을 때 큰 덩어리가 같은 자리에 와야 통과. 아이가 3초 안에 뜻을 말할 수 있어야 한다(글자꼴을 흉내 낸 먹 덩어리가 아니라 사물로 보여야 함).
4. 한 회차 = 5자, A·B 각 1장. 파일명 `r28/<코드>_A.jpg`, `r28/<코드>_B.jpg` (1:1 정사각, 1024 이상). 끝나면 커밋 메시지 `Round 28: ...` 로 푸시만 하면 된다(Claude 가 감시·검토해 다음 회차 문서를 만든다). 자리표시 파일(PLACEHOLDER)은 올리지 말 것.
5. 그림 규칙: 먹 한 색·흰 종이·낙관·글자·배경 풍경 금지, 주인공 하나, 아이가 알아보는 요즘 모습, 무기·형벌 등 불쾌한 소재 금지. 실패작은 올리지 않는다. 기존 파일 덮어쓰기 금지(재작업은 `_v2`).

## 1. 이번 회차 5자

### 日 날 일 (U65E5) — **재작업**
- 재작업 사유: A 가 번진 네모 테두리뿐이라 해로 안 보임 → 속이 찬 둥근 해(진한 먹)에 가운데 점, 둘레는 옅은 빛 번짐. B 는 세로획이 휘어 흔들림 → 획 몸통 곧고 매끈하게, 붓맛은 끝에만
- **획 기준**: `claude_b/U65E5_B.jpg` · raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/claude_b/U65E5_B.jpg
- 획↔그림: 네모 테두리 = 해, 가운데 가로 = 해 속의 점(흑점).

- **① B컷 프롬프트** (이미지 1 = `claude_b/U65E5_B.jpg`, 이미지 2 = `huo_B.jpg`)

```
Write the Chinese character 日 with a real calligraphy brush: one bold hand-brushed character on plain off-white paper.
Image 1 is the stroke-structure reference: keep the SAME stroke count, the same stroke positions, angles, lengths, thickness and proportions, and the same framing as Image 1. Small natural variation from the brush is fine, but no stroke may be added, dropped, merged or moved. Regular script (楷書), Korean standard form, not a printed font.
Brush texture ONLY at the two ends of each stroke: a slightly pressed, rounded entry where the stroke starts, and a short dry-brush tail (flying white, a few bristle streaks) where the stroke leaves the paper. The body of every stroke stays solid, smooth, fully filled with black ink, with clean edges. No dry-brush streaks across the middle of strokes. Image 2 shows the feel of the stroke tails only; do not copy its shape and do not apply its texture to whole strokes.
Pure black ink, no color, no seal, no text, no extra marks, nothing else in the frame. Square 1:1, character centered and the same size as in Image 1.
```

- **② A컷 프롬프트** (①에서 만든 네 B컷을 첨부하고 그대로 넣기)

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, no text, no seal, no background scenery, one subject only, simple enough for a child to recognize, present-day look.
The attached image is the Chinese character that this picture will morph into. Make the picture occupy the SAME area of the frame as the character (same height, same width, same center), and lay out the parts of the picture ON the character's strokes exactly as described below. The character's stroke layout is the skeleton of the picture: paint the parts that sit on the strokes as the boldest, darkest ink of the picture, and paint the rest of the object as soft grey ink wash around them, so the character's skeleton is visible inside the picture while the whole still reads as the object (like a mountain whose three ridges are bold black peaks with misty grey slopes around them).
The subject must look like a REAL thing seen in life: a real child or adult in everyday clothes with hair and a face direction, a real animal, a real object. Never a bare silhouette, mannequin, stick figure, pictogram or abstract symbol.
SUBJECT: the sun drawn as a rounded square disc with a single short dark mark in its center, soft ink glow at the edge.
LAYOUT: the disc fills the square outline of the character and the center mark lies on the middle horizontal stroke.
```

- 저장: `r28/U65E5_B.jpg`, `r28/U65E5_A.jpg` (재작업이면 `_v2`)

### 人 사람 인 (U4EBA) — **재작업**
- 재작업 사유: A 가 맨몸 실루엣이라 실제 사람으로 안 보임 → 티셔츠·바지 입은 실제 아이가 옆으로 성큼 걷는 모습, 머리카락·얼굴 방향 보이게. 획 자리(머리~앞다리, 뒷다리)는 진한 먹, 나머지는 옅은 번짐
- **획 기준**: `claude_b/U4EBA_B.jpg` · raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/claude_b/U4EBA_B.jpg
- 획↔그림: 두 획이 만나는 꼭대기 = 머리, 왼쪽 긴 삐침 = 몸통과 앞다리, 오른쪽 파임 = 뒤로 뻗은 뒷다리.

- **① B컷 프롬프트** (이미지 1 = `claude_b/U4EBA_B.jpg`, 이미지 2 = `huo_B.jpg`)

```
Write the Chinese character 人 with a real calligraphy brush: one bold hand-brushed character on plain off-white paper.
Image 1 is the stroke-structure reference: keep the SAME stroke count, the same stroke positions, angles, lengths, thickness and proportions, and the same framing as Image 1. Small natural variation from the brush is fine, but no stroke may be added, dropped, merged or moved. Regular script (楷書), Korean standard form, not a printed font.
Brush texture ONLY at the two ends of each stroke: a slightly pressed, rounded entry where the stroke starts, and a short dry-brush tail (flying white, a few bristle streaks) where the stroke leaves the paper. The body of every stroke stays solid, smooth, fully filled with black ink, with clean edges. No dry-brush streaks across the middle of strokes. Image 2 shows the feel of the stroke tails only; do not copy its shape and do not apply its texture to whole strokes.
Pure black ink, no color, no seal, no text, no extra marks, nothing else in the frame. Square 1:1, character centered and the same size as in Image 1.
```

- **② A컷 프롬프트** (①에서 만든 네 B컷을 첨부하고 그대로 넣기)

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, no text, no seal, no background scenery, one subject only, simple enough for a child to recognize, present-day look.
The attached image is the Chinese character that this picture will morph into. Make the picture occupy the SAME area of the frame as the character (same height, same width, same center), and lay out the parts of the picture ON the character's strokes exactly as described below. The character's stroke layout is the skeleton of the picture: paint the parts that sit on the strokes as the boldest, darkest ink of the picture, and paint the rest of the object as soft grey ink wash around them, so the character's skeleton is visible inside the picture while the whole still reads as the object (like a mountain whose three ridges are bold black peaks with misty grey slopes around them).
The subject must look like a REAL thing seen in life: a real child or adult in everyday clothes with hair and a face direction, a real animal, a real object. Never a bare silhouette, mannequin, stick figure, pictogram or abstract symbol.
SUBJECT: a person in side view walking with a long stride, leaning slightly forward, arms close to the body.
LAYOUT: the head sits at the apex where the two strokes meet; the torso and the front leg run down the long left-falling stroke to its tip; the back leg stretches down and to the right along the right-falling stroke, foot at its end.
```

- 저장: `r28/U4EBA_B.jpg`, `r28/U4EBA_A.jpg` (재작업이면 `_v2`)

### 大 큰 대 (U5927) — **재작업**
- 재작업 사유: A 가 막대인간이라 실제 사람으로 안 보임 → 옷 입은 실제 아이가 정면으로 팔 벌리고 다리 벌린 모습, 머리카락·얼굴 보이게. 팔(가로획)·몸통과 두 다리(삐침·파임)는 진한 먹, 나머지 옅은 번짐
- **획 기준**: `claude_b/U5927_B.jpg` · raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/claude_b/U5927_B.jpg
- 획↔그림: 가로 = 양쪽으로 쭉 뻗은 팔, 삐침 = 몸통과 왼다리, 파임 = 오른다리, 세로가 가로 위로 솟은 부분 = 머리.

- **① B컷 프롬프트** (이미지 1 = `claude_b/U5927_B.jpg`, 이미지 2 = `huo_B.jpg`)

```
Write the Chinese character 大 with a real calligraphy brush: one bold hand-brushed character on plain off-white paper.
Image 1 is the stroke-structure reference: keep the SAME stroke count, the same stroke positions, angles, lengths, thickness and proportions, and the same framing as Image 1. Small natural variation from the brush is fine, but no stroke may be added, dropped, merged or moved. Regular script (楷書), Korean standard form, not a printed font.
Brush texture ONLY at the two ends of each stroke: a slightly pressed, rounded entry where the stroke starts, and a short dry-brush tail (flying white, a few bristle streaks) where the stroke leaves the paper. The body of every stroke stays solid, smooth, fully filled with black ink, with clean edges. No dry-brush streaks across the middle of strokes. Image 2 shows the feel of the stroke tails only; do not copy its shape and do not apply its texture to whole strokes.
Pure black ink, no color, no seal, no text, no extra marks, nothing else in the frame. Square 1:1, character centered and the same size as in Image 1.
```

- **② A컷 프롬프트** (①에서 만든 네 B컷을 첨부하고 그대로 넣기)

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, no text, no seal, no background scenery, one subject only, simple enough for a child to recognize, present-day look.
The attached image is the Chinese character that this picture will morph into. Make the picture occupy the SAME area of the frame as the character (same height, same width, same center), and lay out the parts of the picture ON the character's strokes exactly as described below. The character's stroke layout is the skeleton of the picture: paint the parts that sit on the strokes as the boldest, darkest ink of the picture, and paint the rest of the object as soft grey ink wash around them, so the character's skeleton is visible inside the picture while the whole still reads as the object (like a mountain whose three ridges are bold black peaks with misty grey slopes around them).
The subject must look like a REAL thing seen in life: a real child or adult in everyday clothes with hair and a face direction, a real animal, a real object. Never a bare silhouette, mannequin, stick figure, pictogram or abstract symbol.
SUBJECT: a child standing facing the viewer with both arms stretched straight out sideways and legs spread wide, showing how big they are.
LAYOUT: the head sits on the short part of the vertical that pokes above the horizontal stroke; the two arms lie exactly on the horizontal stroke; the torso and left leg follow the left-falling stroke, the right leg follows the right-falling stroke.
```

- 저장: `r28/U5927_B.jpg`, `r28/U5927_A.jpg` (재작업이면 `_v2`)

### 川 내 천 (U5DDD)
- **획 기준**: `claude_b/U5DDD_B.jpg` · raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/claude_b/U5DDD_B.jpg
- 획↔그림: 세 세로획 = 세 줄기 물: 왼쪽 굽은 획 = 휘어 흐르는 지류, 가운데 짧은 획, 오른쪽 긴 획 = 본류.

- **① B컷 프롬프트** (이미지 1 = `claude_b/U5DDD_B.jpg`, 이미지 2 = `huo_B.jpg`)

```
Write the Chinese character 川 with a real calligraphy brush: one bold hand-brushed character on plain off-white paper.
Image 1 is the stroke-structure reference: keep the SAME stroke count, the same stroke positions, angles, lengths, thickness and proportions, and the same framing as Image 1. Small natural variation from the brush is fine, but no stroke may be added, dropped, merged or moved. Regular script (楷書), Korean standard form, not a printed font.
Brush texture ONLY at the two ends of each stroke: a slightly pressed, rounded entry where the stroke starts, and a short dry-brush tail (flying white, a few bristle streaks) where the stroke leaves the paper. The body of every stroke stays solid, smooth, fully filled with black ink, with clean edges. No dry-brush streaks across the middle of strokes. Image 2 shows the feel of the stroke tails only; do not copy its shape and do not apply its texture to whole strokes.
Pure black ink, no color, no seal, no text, no extra marks, nothing else in the frame. Square 1:1, character centered and the same size as in Image 1.
```

- **② A컷 프롬프트** (①에서 만든 네 B컷을 첨부하고 그대로 넣기)

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, no text, no seal, no background scenery, one subject only, simple enough for a child to recognize, present-day look.
The attached image is the Chinese character that this picture will morph into. Make the picture occupy the SAME area of the frame as the character (same height, same width, same center), and lay out the parts of the picture ON the character's strokes exactly as described below. The character's stroke layout is the skeleton of the picture: paint the parts that sit on the strokes as the boldest, darkest ink of the picture, and paint the rest of the object as soft grey ink wash around them, so the character's skeleton is visible inside the picture while the whole still reads as the object (like a mountain whose three ridges are bold black peaks with misty grey slopes around them).
The subject must look like a REAL thing seen in life: a real child or adult in everyday clothes with hair and a face direction, a real animal, a real object. Never a bare silhouette, mannequin, stick figure, pictogram or abstract symbol.
SUBJECT: a stream flowing straight down the page in three parallel ribbons of water, with small ripples.
LAYOUT: the left ribbon curves slightly like the left-falling stroke, the middle ribbon is short on the short middle stroke, the right ribbon is the longest on the right vertical stroke; nothing outside the three strokes.
```

- 저장: `r28/U5DDD_B.jpg`, `r28/U5DDD_A.jpg`

### 口 입 구 (U53E3)
- **획 기준**: `claude_b/U53E3_B.jpg` · raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/claude_b/U53E3_B.jpg
- 획↔그림: 네모 테두리 = 크게 벌린 입술 윤곽.

- **① B컷 프롬프트** (이미지 1 = `claude_b/U53E3_B.jpg`, 이미지 2 = `huo_B.jpg`)

```
Write the Chinese character 口 with a real calligraphy brush: one bold hand-brushed character on plain off-white paper.
Image 1 is the stroke-structure reference: keep the SAME stroke count, the same stroke positions, angles, lengths, thickness and proportions, and the same framing as Image 1. Small natural variation from the brush is fine, but no stroke may be added, dropped, merged or moved. Regular script (楷書), Korean standard form, not a printed font.
Brush texture ONLY at the two ends of each stroke: a slightly pressed, rounded entry where the stroke starts, and a short dry-brush tail (flying white, a few bristle streaks) where the stroke leaves the paper. The body of every stroke stays solid, smooth, fully filled with black ink, with clean edges. No dry-brush streaks across the middle of strokes. Image 2 shows the feel of the stroke tails only; do not copy its shape and do not apply its texture to whole strokes.
Pure black ink, no color, no seal, no text, no extra marks, nothing else in the frame. Square 1:1, character centered and the same size as in Image 1.
```

- **② A컷 프롬프트** (①에서 만든 네 B컷을 첨부하고 그대로 넣기)

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, no text, no seal, no background scenery, one subject only, simple enough for a child to recognize, present-day look.
The attached image is the Chinese character that this picture will morph into. Make the picture occupy the SAME area of the frame as the character (same height, same width, same center), and lay out the parts of the picture ON the character's strokes exactly as described below. The character's stroke layout is the skeleton of the picture: paint the parts that sit on the strokes as the boldest, darkest ink of the picture, and paint the rest of the object as soft grey ink wash around them, so the character's skeleton is visible inside the picture while the whole still reads as the object (like a mountain whose three ridges are bold black peaks with misty grey slopes around them).
The subject must look like a REAL thing seen in life: a real child or adult in everyday clothes with hair and a face direction, a real animal, a real object. Never a bare silhouette, mannequin, stick figure, pictogram or abstract symbol.
SUBJECT: a wide open mouth seen from the front, drawn as a rounded square outline of lips, with nothing else of the face.
LAYOUT: the lips trace the three strokes of the square outline: the left side, the top-and-right side, and the bottom; the inside stays empty white.
```

- 저장: `r28/U53E3_B.jpg`, `r28/U53E3_A.jpg`
