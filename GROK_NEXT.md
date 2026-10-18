# Grok 작업 지시서 — 27회차 (2026-10-18) · B 맞춤 A컷 5자

리뷰 페이지: https://talkverse.uk/hanja-review/ (맨 위 "0. 회차 리뷰") · 이 문서: https://talkverse.uk/hanja-review/GROK_NEXT.md?r=27 · 저장소 사본: `rounds/r27.md`

## 0. 이번 회차부터 바뀐 것 — 먼저 읽을 것

1. **B컷(글자)은 이미 있다**: `claude_b/<코드>_B.jpg` (Claude 가 정자로 렌더). 네가 할 B 작업은 **이 이미지를 입력으로 넣고 붓 질감만 바꾸는 것**(획은 한 획도 바꾸지 않는다). 질감 참고는 `huo_B.jpg`(네가 전에 그린 火).
2. **A컷(그림)은 B컷 획 배치 위에 그린다**: B컷 이미지를 첨부(또는 저장소에서 읽고)하고, 아래 LAYOUT 대로 그림의 부위를 획 자리에 놓는다. 그림을 B 위에 겹쳤을 때 큰 덩어리가 같은 자리에 와야 통과.
3. 한 회차 = 5자, A·B 각 1장. 파일명 `r27/<코드>_A.jpg`, `r27/<코드>_B.jpg` (1:1 정사각, 1024 이상). 끝나면 커밋 메시지 `Round 27: ...` 로 푸시만 하면 된다(Claude 가 감시·검토해 다음 회차 문서를 만든다).
4. 그림 규칙: 먹 한 색·흰 종이·낙관·글자·배경 풍경 금지, 주인공 하나, 아이가 알아보는 요즘 모습, 무기·형벌 등 불쾌한 소재 금지. 실패작은 올리지 않는다. 기존 파일 덮어쓰기 금지.

## 1. 이번 회차 5자

### 人 사람 인 (U4EBA)
- **B컷 원본(획 기준)**: `claude_b/U4EBA_B.jpg` · raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/claude_b/U4EBA_B.jpg
- 획↔그림: 두 획이 만나는 꼭대기 = 머리, 왼쪽 긴 삐침 = 몸통과 앞다리, 오른쪽 파임 = 뒤로 뻗은 뒷다리.

- **A컷 프롬프트** (B컷 이미지를 첨부하고 그대로 넣기)

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, no text, no seal, no background scenery, one subject only, simple enough for a child to recognize, present-day look.
The attached image is the Chinese character that this picture will morph into. Make the picture occupy the SAME area of the frame as the character (same height, same width, same center), and lay out the parts of the picture ON the character's strokes exactly as described below. The character's stroke layout is the skeleton of the picture.
SUBJECT: a person in side view walking with a long stride, leaning slightly forward, arms close to the body.
LAYOUT: the head sits at the apex where the two strokes meet; the torso and the front leg run down the long left-falling stroke to its tip; the back leg stretches down and to the right along the right-falling stroke, foot at its end.
```

- **B컷 프롬프트** (이미지 1 = `claude_b/U4EBA_B.jpg`, 이미지 2 = `huo_B.jpg` 를 함께 넣고 image edit)

```
Image 1 is the character 人 to edit. Image 2 is ONLY a brush-texture reference.
Keep every stroke of Image 1 exactly as it is: same strokes, count, positions, angles, thickness, proportions and framing. Do not redraw or restyle the shape, and do not copy the shape of Image 2.
Change only the ink rendering of Image 1 so it matches the brush feel of Image 2: dry-brush streaks (flying white) inside thick strokes, ragged bristle edges, darker ink pooling at stroke starts, scratchy fading tails, textured off-white rice paper.
Pure black ink, no color, no seal, no text, no extra marks. Square 1:1, same size.
```

- 저장: `r27/U4EBA_A.jpg`, `r27/U4EBA_B.jpg`

### 大 큰 대 (U5927)
- **B컷 원본(획 기준)**: `claude_b/U5927_B.jpg` · raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/claude_b/U5927_B.jpg
- 획↔그림: 가로 = 양쪽으로 쭉 뻗은 팔, 삐침 = 몸통과 왼다리, 파임 = 오른다리, 세로가 가로 위로 솟은 부분 = 머리.

- **A컷 프롬프트** (B컷 이미지를 첨부하고 그대로 넣기)

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, no text, no seal, no background scenery, one subject only, simple enough for a child to recognize, present-day look.
The attached image is the Chinese character that this picture will morph into. Make the picture occupy the SAME area of the frame as the character (same height, same width, same center), and lay out the parts of the picture ON the character's strokes exactly as described below. The character's stroke layout is the skeleton of the picture.
SUBJECT: a child standing facing the viewer with both arms stretched straight out sideways and legs spread wide, showing how big they are.
LAYOUT: the head sits on the short part of the vertical that pokes above the horizontal stroke; the two arms lie exactly on the horizontal stroke; the torso and left leg follow the left-falling stroke, the right leg follows the right-falling stroke.
```

- **B컷 프롬프트** (이미지 1 = `claude_b/U5927_B.jpg`, 이미지 2 = `huo_B.jpg` 를 함께 넣고 image edit)

```
Image 1 is the character 大 to edit. Image 2 is ONLY a brush-texture reference.
Keep every stroke of Image 1 exactly as it is: same strokes, count, positions, angles, thickness, proportions and framing. Do not redraw or restyle the shape, and do not copy the shape of Image 2.
Change only the ink rendering of Image 1 so it matches the brush feel of Image 2: dry-brush streaks (flying white) inside thick strokes, ragged bristle edges, darker ink pooling at stroke starts, scratchy fading tails, textured off-white rice paper.
Pure black ink, no color, no seal, no text, no extra marks. Square 1:1, same size.
```

- 저장: `r27/U5927_A.jpg`, `r27/U5927_B.jpg`

### 山 메 산 (U5C71)
- **B컷 원본(획 기준)**: `claude_b/U5C71_B.jpg` · raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/claude_b/U5C71_B.jpg
- 획↔그림: 가운데 세로 = 가장 높은 봉우리, 양쪽 세로 = 낮은 봉우리, 바닥 가로 = 산기슭.

- **A컷 프롬프트** (B컷 이미지를 첨부하고 그대로 넣기)

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, no text, no seal, no background scenery, one subject only, simple enough for a child to recognize, present-day look.
The attached image is the Chinese character that this picture will morph into. Make the picture occupy the SAME area of the frame as the character (same height, same width, same center), and lay out the parts of the picture ON the character's strokes exactly as described below. The character's stroke layout is the skeleton of the picture.
SUBJECT: a mountain with three peaks, the middle peak tallest, drawn with bold ink and a flat base.
LAYOUT: the tall middle peak rises on the central vertical stroke; the left and right peaks rise on the two shorter side verticals; the flat foot of the mountain lies on the bottom horizontal stroke.
```

- **B컷 프롬프트** (이미지 1 = `claude_b/U5C71_B.jpg`, 이미지 2 = `huo_B.jpg` 를 함께 넣고 image edit)

```
Image 1 is the character 山 to edit. Image 2 is ONLY a brush-texture reference.
Keep every stroke of Image 1 exactly as it is: same strokes, count, positions, angles, thickness, proportions and framing. Do not redraw or restyle the shape, and do not copy the shape of Image 2.
Change only the ink rendering of Image 1 so it matches the brush feel of Image 2: dry-brush streaks (flying white) inside thick strokes, ragged bristle edges, darker ink pooling at stroke starts, scratchy fading tails, textured off-white rice paper.
Pure black ink, no color, no seal, no text, no extra marks. Square 1:1, same size.
```

- 저장: `r27/U5C71_A.jpg`, `r27/U5C71_B.jpg`

### 日 날 일 (U65E5)
- **B컷 원본(획 기준)**: `claude_b/U65E5_B.jpg` · raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/claude_b/U65E5_B.jpg
- 획↔그림: 네모 테두리 = 해, 가운데 가로 = 해 속의 점(흑점).

- **A컷 프롬프트** (B컷 이미지를 첨부하고 그대로 넣기)

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, no text, no seal, no background scenery, one subject only, simple enough for a child to recognize, present-day look.
The attached image is the Chinese character that this picture will morph into. Make the picture occupy the SAME area of the frame as the character (same height, same width, same center), and lay out the parts of the picture ON the character's strokes exactly as described below. The character's stroke layout is the skeleton of the picture.
SUBJECT: the sun drawn as a rounded square disc with a single short dark mark in its center, soft ink glow at the edge.
LAYOUT: the disc fills the square outline of the character and the center mark lies on the middle horizontal stroke.
```

- **B컷 프롬프트** (이미지 1 = `claude_b/U65E5_B.jpg`, 이미지 2 = `huo_B.jpg` 를 함께 넣고 image edit)

```
Image 1 is the character 日 to edit. Image 2 is ONLY a brush-texture reference.
Keep every stroke of Image 1 exactly as it is: same strokes, count, positions, angles, thickness, proportions and framing. Do not redraw or restyle the shape, and do not copy the shape of Image 2.
Change only the ink rendering of Image 1 so it matches the brush feel of Image 2: dry-brush streaks (flying white) inside thick strokes, ragged bristle edges, darker ink pooling at stroke starts, scratchy fading tails, textured off-white rice paper.
Pure black ink, no color, no seal, no text, no extra marks. Square 1:1, same size.
```

- 저장: `r27/U65E5_A.jpg`, `r27/U65E5_B.jpg`

### 木 나무 목 (U6728)
- **B컷 원본(획 기준)**: `claude_b/U6728_B.jpg` · raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/claude_b/U6728_B.jpg
- 획↔그림: 가로 = 양쪽으로 뻗은 가지, 세로 = 줄기, 삐침·파임 = 양쪽으로 벌어진 뿌리.

- **A컷 프롬프트** (B컷 이미지를 첨부하고 그대로 넣기)

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, no text, no seal, no background scenery, one subject only, simple enough for a child to recognize, present-day look.
The attached image is the Chinese character that this picture will morph into. Make the picture occupy the SAME area of the frame as the character (same height, same width, same center), and lay out the parts of the picture ON the character's strokes exactly as described below. The character's stroke layout is the skeleton of the picture.
SUBJECT: a young tree with a straight trunk, two branches spreading sideways, and two roots spreading at the base, only a few leaves.
LAYOUT: the two branches lie on the horizontal stroke, the trunk on the vertical stroke, the left root on the left-falling stroke and the right root on the right-falling stroke.
```

- **B컷 프롬프트** (이미지 1 = `claude_b/U6728_B.jpg`, 이미지 2 = `huo_B.jpg` 를 함께 넣고 image edit)

```
Image 1 is the character 木 to edit. Image 2 is ONLY a brush-texture reference.
Keep every stroke of Image 1 exactly as it is: same strokes, count, positions, angles, thickness, proportions and framing. Do not redraw or restyle the shape, and do not copy the shape of Image 2.
Change only the ink rendering of Image 1 so it matches the brush feel of Image 2: dry-brush streaks (flying white) inside thick strokes, ragged bristle edges, darker ink pooling at stroke starts, scratchy fading tails, textured off-white rice paper.
Pure black ink, no color, no seal, no text, no extra marks. Square 1:1, same size.
```

- 저장: `r27/U6728_A.jpg`, `r27/U6728_B.jpg`
