# A컷(그림) 프롬프트 — B컷(한자) 획 배치에 맞춰 그리기 · 5급판 상형자 74자 (2026-10-18)

**원칙(사용자 지시 2026-10-18)**: 상형자는 A컷 그림이 B컷 글자와 **같은 구도·자세·형상**에서 시작해야 모핑이 납득된다.
그래서 모든 A컷 프롬프트는 ① B컷 이미지를 첨부하고 ② 그림이 글자와 같은 자리·크기를 차지하게 하며 ③ 그림의 부위를 글자의 획 하나하나에 대응시켜 적는다.

- B컷 파일: `claude_b/U<코드>_B.jpg` (이 저장소, raw: `https://raw.githubusercontent.com/talkverselab/talkversehanja/main/claude_b/U<코드>_B.jpg`). 1408×1408, 정자(楷書), 흰 바탕.
- 그림 규칙(기존 그대로): 먹 한 색·흰 종이·낙관·글자·배경 풍경 금지, 주인공 하나, 아이가 알아보는 요즘 모습, 무기·형벌·바늘 등 불쾌한 소재 금지(`rounds/r26.md` 4항).
- 결과 검사: A컷을 B컷 위에 반투명으로 겹쳤을 때 아래 "획↔그림" 대응대로 큰 덩어리가 같은 자리에 와야 통과.

## 공통 머리말 (모든 프롬프트 앞부분, 그대로 복사)

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, no text, no seal, no background scenery, one subject only, simple enough for a child to recognize, present-day look.
The attached image is the Chinese character that this picture will morph into. Make the picture occupy the SAME area of the frame as the character (same height, same width, same center), and lay out the parts of the picture ON the character's strokes exactly as described below. The character's stroke layout is the skeleton of the picture.
```

아래 각 글자의 `SUBJECT / LAYOUT` 줄을 공통 머리말 뒤에 이어 붙이면 완성 프롬프트가 된다.

---

## 2획

### 入 들 입 (U5165) — `claude_b/U5165_B.jpg`
- 획↔그림: 왼쪽 짧은 삐침 = 텐트 왼쪽 지붕선, 오른쪽 긴 파임(위로 솟음) = 오른쪽 지붕선이 꼭대기 위로 더 올라가 땅까지 길게 내려옴. 아이가 그 사이로 들어감.
```
SUBJECT: a small camping tent seen from the front with a child ducking in through the opening between its two sloping roof lines, no ground line, no guy ropes.
LAYOUT: the short left roof line follows the short left-falling stroke; the right roof line is longer, rises above the meeting point and sweeps down to the lower right exactly along the long right-falling stroke; the child is tiny and sits inside the gap under the apex, not outside the strokes.
```

### 九 아홉 구 (U4E5D) — `claude_b/U4E5D_B.jpg`
- 획↔그림: 삐침 = 어깨에서 내려오는 위팔, 乙(가로-꺾음-갈고리) = 팔꿈치에서 꺾인 아래팔과 위로 들린 손.
```
SUBJECT: one bent arm seen from the side, flexing at the elbow, the hand curling upward, nothing else of the body.
LAYOUT: the upper arm runs from the top left downward along the left-falling stroke; the forearm starts at the top, runs to the right along the horizontal part of the hooked stroke, bends down at the elbow along its vertical part and the hand curls up at the bottom right exactly where the stroke hooks.
```

### 人 사람 인 (U4EBA) — `claude_b/U4EBA_B.jpg`
- 획↔그림: 두 획이 만나는 꼭대기 = 머리, 왼쪽 긴 삐침 = 몸통과 앞다리, 오른쪽 파임 = 뒤로 뻗은 뒷다리.
```
SUBJECT: a person in side view walking with a long stride, leaning slightly forward, arms close to the body.
LAYOUT: the head sits at the apex where the two strokes meet; the torso and the front leg run down the long left-falling stroke to its tip; the back leg stretches down and to the right along the right-falling stroke, foot at its end.
```

### 八 여덟 팔 (U516B) — `claude_b/U516B_B.jpg`
- 획↔그림: 위에서 갈라져 양쪽으로 벌어지는 두 획 = 한 점에서 갈라진 두 스키 자국(또는 두 조각으로 쪼개진 떡).
```
SUBJECT: two ski tracks in snow diverging downhill from one point, drawn as two soft ink lines with nothing else.
LAYOUT: the left track runs down to the lower left along the left-falling stroke and the right track runs down to the lower right along the right-falling stroke; the two tracks do not touch at the top, leaving the same small gap as the character.
```

### 十 열 십 (U5341) — `claude_b/U5341_B.jpg`
- 획↔그림: 가로 = 가로로 묶은 막대, 세로 = 세워 묶은 막대 (끈으로 열십자로 묶음).
```
SUBJECT: two straight bamboo sticks tied together into a plus-shaped cross with a small knot of string at the center.
LAYOUT: one stick is horizontal exactly on the horizontal stroke and one is vertical exactly on the vertical stroke, crossing at the character's center; the vertical stick is slightly longer than the horizontal one.
```

### 力 힘 력 (U529B) — `claude_b/U529B_B.jpg`
- 획↔그림: 가로-꺾음-갈고리 = 괭이 머리(가로 날이 꺾여 내려가 끝이 갈고리), 삐침 = 괭이 자루.
```
SUBJECT: a garden hoe digging into soil, seen from the side, with a small pair of hands on the handle, no body.
LAYOUT: the hoe head runs along the hooked stroke: across the top, bending down and hooking at the bottom; the wooden handle runs from the upper middle down to the lower left exactly along the left-falling stroke, crossing the hoe head where the strokes cross.
```

## 3획

### 大 큰 대 (U5927) — `claude_b/U5927_B.jpg`
- 획↔그림: 가로 = 양쪽으로 쭉 뻗은 팔, 삐침 = 몸통과 왼다리, 파임 = 오른다리, 세로가 가로 위로 솟은 부분 = 머리.
```
SUBJECT: a child standing facing the viewer with both arms stretched straight out sideways and legs spread wide, showing how big they are.
LAYOUT: the head sits on the short part of the vertical that pokes above the horizontal stroke; the two arms lie exactly on the horizontal stroke; the torso and left leg follow the left-falling stroke, the right leg follows the right-falling stroke.
```

### 女 계집 녀 (U5973) — `claude_b/U5973_B.jpg`
- 획↔그림: 긴 가로 = 앞으로 모아 포갠 두 팔, 왼쪽 꺾인 획(撇点) = 몸통에서 무릎으로 꺾이는 선, 오른쪽 삐침 = 치마 자락·뒷다리.
```
SUBJECT: a woman kneeling upright on the floor (seiza), seen from the side-front, hands folded together in front of her lap, present-day clothes.
LAYOUT: her folded arms form the long horizontal stroke; her torso comes down the upper part of the left stroke and bends at the knee along its lower part; the right-falling stroke is her skirt and lower leg sweeping to the lower left.
```

### 小 작을 소 (U5C0F) — `claude_b/U5C0F_B.jpg`
- 획↔그림: 가운데 갈고리 세로 = 길쭉한 씨앗 하나, 양쪽 점 = 작은 씨앗 둘.
```
SUBJECT: three tiny seeds lying on paper, the middle one long and thin, the two side ones small and round, drawn with soft ink.
LAYOUT: the long seed stands upright on the central vertical stroke with its tip curling at the bottom like the hook; the left small seed sits on the left dot, the right small seed on the right dot, both slightly below the top of the center seed.
```

### 山 메 산 (U5C71) — `claude_b/U5C71_B.jpg`
- 획↔그림: 가운데 세로 = 가장 높은 봉우리, 양쪽 세로 = 낮은 봉우리, 바닥 가로 = 산기슭.
```
SUBJECT: a mountain with three peaks, the middle peak tallest, drawn with bold ink and a flat base.
LAYOUT: the tall middle peak rises on the central vertical stroke; the left and right peaks rise on the two shorter side verticals; the flat foot of the mountain lies on the bottom horizontal stroke.
```

### 子 아들 자 (U5B50) — `claude_b/U5B50_B.jpg`
- 획↔그림: 윗 꺾음 = 큰 머리, 갈고리 세로 = 포대기에 싸인 몸, 가로 = 양쪽으로 벌린 두 팔.
```
SUBJECT: a baby wrapped in a blanket with a large round head and both little arms stretched out to the sides.
LAYOUT: the head fills the top bent stroke; the swaddled body runs down the vertical hooked stroke; the two outstretched arms lie exactly on the horizontal stroke that crosses the body.
```

### 川 내 천 (U5DDD) — `claude_b/U5DDD_B.jpg`
- 획↔그림: 세 세로획 = 세 줄기 물: 왼쪽 굽은 획 = 휘어 흐르는 지류, 가운데 짧은 획, 오른쪽 긴 획 = 본류.
```
SUBJECT: a stream flowing straight down the page in three parallel ribbons of water, with small ripples.
LAYOUT: the left ribbon curves slightly like the left-falling stroke, the middle ribbon is short on the short middle stroke, the right ribbon is the longest on the right vertical stroke; nothing outside the three strokes.
```

### 工 장인 공 (U5DE5) — `claude_b/U5DE5_B.jpg`
- 획↔그림: 위 가로 = 손잡이 막대, 세로 = 자루, 아래 가로 = 넓은 바닥판 (땅 다지는 달구/탬퍼).
```
SUBJECT: a hand tamper tool standing upright: a flat grip bar on top, a straight shaft, and a wide flat base plate, with a small pair of hands holding the grip.
LAYOUT: the grip bar lies on the top horizontal stroke, the shaft on the vertical stroke, the base plate on the longer bottom horizontal stroke.
```

### 口 입 구 (U53E3) — `claude_b/U53E3_B.jpg`
- 획↔그림: 네모 테두리 = 크게 벌린 입술 윤곽.
```
SUBJECT: a wide open mouth seen from the front, drawn as a rounded square outline of lips, with nothing else of the face.
LAYOUT: the lips trace the three strokes of the square outline: the left side, the top-and-right side, and the bottom; the inside stays empty white.
```

### 才 재주 재 (U624D) — `claude_b/U624D_B.jpg`
- 획↔그림: 가로 = 땅 표면, 갈고리 세로 = 땅을 뚫고 올라온 줄기와 아래로 뻗은 뿌리, 삐침 = 왼쪽으로 뻗은 첫 잎.
```
SUBJECT: a seedling just breaking through the ground, one leaf unfolding to the left, its root visible below the soil line.
LAYOUT: the soil line is the horizontal stroke; the stem rises above it and the root goes below it along the vertical hooked stroke; the single leaf grows from the stem down to the left along the left-falling stroke.
```

### 久 오랠 구 (U4E45) — `claude_b/U4E45_B.jpg`
- 획↔그림: 위 삐침 = 숙인 머리와 등, 가로-꺾음 = 지팡이를 짚은 팔, 파임 = 뒤로 뻗은 다리 (오래 걷는 사람).
```
SUBJECT: a hiker in side view bent forward on a long trail, leaning on a trekking pole, taking a slow long step.
LAYOUT: the bowed head and back follow the short top left-falling stroke; the arm reaching out to the pole follows the horizontal-then-bending stroke; the rear leg stretches down to the lower right along the long right-falling stroke.
```

### 干 방패 간 (U5E72) — `claude_b/U5E72_B.jpg`
- 획↔그림: 세로 = 손잡이 자루, 위 짧은 가로 = 윗 가로대, 아래 긴 가로 = 넓은 방패 가로대.
```
SUBJECT: a simple hand-held shield seen from the front, built from a vertical pole with two crossbars, the lower one wider, like a sports goalkeeper's practice shield, no weapon.
LAYOUT: the pole lies on the vertical stroke; the short upper crossbar lies on the short top horizontal, the wide lower crossbar on the long second horizontal.
```

## 4획

### 中 가운데 중 (U4E2D) — `claude_b/U4E2D_B.jpg`
- 획↔그림: 네모 = 네모난 깃발판(또는 과녁판), 세로 = 그 한가운데를 꿰뚫고 위아래로 나온 깃대.
```
SUBJECT: a square flag or target board with a flagpole planted straight through its center, the pole sticking out above and below.
LAYOUT: the board is the square outline; the pole runs the full length of the central vertical stroke, exactly through the middle of the square.
```

### 日 날 일 (U65E5) — `claude_b/U65E5_B.jpg`
- 획↔그림: 네모 테두리 = 해, 가운데 가로 = 해 속의 점(흑점).
```
SUBJECT: the sun drawn as a rounded square disc with a single short dark mark in its center, soft ink glow at the edge.
LAYOUT: the disc fills the square outline of the character and the center mark lies on the middle horizontal stroke.
```

### 月 달 월 (U6708) — `claude_b/U6708_B.jpg`
- 획↔그림: 왼쪽 삐침과 오른쪽 갈고리 = 세워 놓은 초승달의 양쪽 테두리, 안의 가로 둘 = 달 속 구름띠(또는 분화구 줄).
```
SUBJECT: a crescent moon standing upright, slightly tilted, with two faint horizontal bands inside it like thin clouds.
LAYOUT: the left edge of the moon follows the left-falling stroke, the right edge follows the hooked stroke, and the two bands lie on the two short horizontals inside.
```

### 火 불 화 (U706B) — `claude_b/U706B_B.jpg`
- 획↔그림: 가운데 人 = 큰 불꽃(위로 뾰족, 아래가 두 갈래로 벌어짐), 왼점·오른점 = 양쪽으로 튀는 불똥.
```
SUBJECT: a campfire flame seen from the front, one tall central tongue of fire whose base splits into two, with a spark flying off on each side, no logs.
LAYOUT: the main flame's left edge runs down the long left-falling stroke and its right edge down the right-falling stroke, tip at the top of the character; the left spark sits on the left dot and the right spark on the right dot, both at mid-height.
```

### 木 나무 목 (U6728) — `claude_b/U6728_B.jpg`
- 획↔그림: 가로 = 양쪽으로 뻗은 가지, 세로 = 줄기, 삐침·파임 = 양쪽으로 벌어진 뿌리.
```
SUBJECT: a young tree with a straight trunk, two branches spreading sideways, and two roots spreading at the base, only a few leaves.
LAYOUT: the two branches lie on the horizontal stroke, the trunk on the vertical stroke, the left root on the left-falling stroke and the right root on the right-falling stroke.
```

### 心 마음 심 (U5FC3) — `claude_b/U5FC3_B.jpg`
- 획↔그림: 넓은 굽은 갈고리 = 심장(또는 하트)의 둥근 아랫부분, 세 점 = 위로 튀는 작은 두근거림 방울 셋.
```
SUBJECT: a soft heart shape lying like a bowl, drawn with one wide curved stroke, with three small drops of ink beating above it.
LAYOUT: the bowl of the heart follows the wide curved hooked stroke; the three drops sit exactly on the three dots: one on the left, two on the upper right.
```

### 手 손 수 (U624B) — `claude_b/U624B_B.jpg`
- 획↔그림: 갈고리 세로 = 손목에서 가운뎃손가락까지, 두 가로 = 양쪽으로 펼친 손가락들, 맨 위 삐침 = 끝에서 기울어진 손가락 끝.
```
SUBJECT: an open hand seen from the back with the fingers spread upward, drawn very simply.
LAYOUT: the wrist and middle finger run up the vertical hooked stroke; the spread fingers lie along the two horizontal strokes; the fingertip tilting to the left is the short top left-falling stroke.
```

### 方 모 방 (U65B9) — `claude_b/U65B9_B.jpg`
- 획↔그림: 점 + 가로 = T자 손잡이, 삐침 = 자루, 가로-꺾음-갈고리 = 흙을 파는 삽날.
```
SUBJECT: a garden spade with a T-shaped handle, seen from the side, its blade pushed into the soil.
LAYOUT: the handle grip lies on the top dot and the horizontal stroke; the shaft runs down to the lower left along the left-falling stroke; the blade follows the hooked stroke, bending down and curling at the bottom.
```

### 文 글월 문 (U6587) — `claude_b/U6587_B.jpg`
- 획↔그림: 점 = 머리, 가로 = 벌린 팔, 교차한 두 획 = 가슴의 큰 X 무늬와 벌린 다리.
```
SUBJECT: a child standing facing the viewer, arms stretched out, wearing a T-shirt with a big X pattern printed on the chest.
LAYOUT: the head is the top dot; the arms lie on the horizontal stroke; the two crossing strokes below are the X pattern running down into the two spread legs.
```

### 元 으뜸 원 (U5143) — `claude_b/U5143_B.jpg`
- 획↔그림: 위 두 가로 = 챙 넓은 모자(머리를 강조), 儿 = 두 다리.
```
SUBJECT: a child seen from the front wearing a wide flat hat, body hidden, only the hat and two legs visible, one leg stepping.
LAYOUT: the hat is the two horizontal strokes (crown and brim); the left leg follows the short left-falling stroke and the right leg follows the curved hooked stroke bending up at the end.
```

### 牛 소 우 (U725B) — `claude_b/U725B_B.jpg`
- 획↔그림: 삐침 + 첫 가로 = 두 뿔, 세로 = 얼굴 중심선(코까지), 둘째 긴 가로 = 양쪽 귀.
```
SUBJECT: an ox head seen straight from the front, drawn with a few strokes: two horns, a long face, two ears, no body.
LAYOUT: the left horn is the short top left-falling stroke and the right horn is the first short horizontal; the face runs down the vertical stroke; the two ears lie on the long second horizontal.
```

### 止 그칠 지 (U6B62) — `claude_b/U6B62_B.jpg`
- 획↔그림: 가운데 세로 = 발 길이(가운뎃발가락), 오른쪽 짧은 가로 = 바깥 발가락, 왼쪽 짧은 세로 = 엄지발가락, 바닥 가로 = 발뒤꿈치 선 (발자국).
```
SUBJECT: a single footprint seen from above with the toes pointing up, drawn as a few bold ink strokes.
LAYOUT: the long middle toe runs up the central vertical stroke; the big toe is the short left vertical; the small toe is the short horizontal on the upper right; the heel is the bottom horizontal stroke.
```

### 犬 개 견 (U72AC) — `claude_b/U72AC_B.jpg`
- 획↔그림: 大 = 앞발을 벌리고 앉은 강아지(가로 = 앞다리, 삐침·파임 = 뒷다리), 오른쪽 위 점 = 쫑긋 선 귀.
```
SUBJECT: a puppy sitting upright facing the viewer, front legs spread out to the sides, one ear standing up.
LAYOUT: the head sits where the vertical pokes above the horizontal; the front legs lie on the horizontal stroke; the hind legs follow the left-falling and right-falling strokes; the upright ear is the dot at the upper right.
```

### 片 조각 편 (U7247) — `claude_b/U7247_B.jpg`
- 획↔그림: 왼쪽 삐침·세로 = 세워 놓은 얇은 나무 조각의 왼쪽 모서리, 가로 = 조각의 윗면, 꺾음 = 오른쪽 모서리가 꺾여 내려옴.
```
SUBJECT: a thin slice of wood (a wood chip) standing on its edge, split from a log, seen from the front.
LAYOUT: the left edge of the chip follows the left-falling stroke and the left vertical; the top of the chip lies on the horizontal stroke; the right edge bends down along the hooked stroke.
```

### 比 견줄 비 (U6BD4) — `claude_b/U6BD4_B.jpg`
- 획↔그림: 왼쪽 匕 = 키를 재려고 나란히 선 아이 1, 오른쪽 匕 = 아이 2 (같은 방향, 팔을 앞으로 구부림).
```
SUBJECT: two children standing side by side facing the right, comparing their height, each drawn as a simple figure with one arm bent forward.
LAYOUT: the left child stands on the left 匕 shape: body on its vertical hooked stroke, bent arm on its short slanted stroke; the right child stands on the right 匕 shape in the same way; both the same size as the strokes.
```

## 5획

### 生 날 생 (U751F) — `claude_b/U751F_B.jpg`
- 획↔그림: 바닥 가로 = 땅, 세로 = 줄기, 가운데 두 가로 = 두 잎, 맨 위 삐침 = 왼쪽으로 휜 새 잎.
```
SUBJECT: a young sprout growing up from a flat line of soil, with two pairs of leaves and a new leaf curling at the top.
LAYOUT: the soil is the bottom horizontal stroke; the stem is the vertical stroke; the leaves lie on the two middle horizontals; the top leaf curls to the left along the short left-falling stroke.
```

### 白 흰 백 (U767D) — `claude_b/U767D_B.jpg`
- 획↔그림: 日 = 막 떠오른 해, 위 삐침 = 해 위로 뻗는 한 줄기 빛.
```
SUBJECT: the sun just risen, drawn as a rounded square disc with a center line, with one single ray of light leaning out from its top.
LAYOUT: the disc fills the 日 part (the square outline with the middle horizontal); the ray is the short left-falling stroke on top of the square.
```

### 母 어미 모 (U6BCD) — `claude_b/U6BCD_B.jpg`
- 획↔그림: 바깥 테두리(왼쪽 꺾음·오른쪽 가로-꺾음) = 아기를 감싸 안은 엄마의 둥근 몸, 가운데 긴 가로 = 안은 두 팔, 두 점 = 엄마 품속 아기의 두 손(또는 얼굴).
```
SUBJECT: a mother kneeling and holding a baby in her arms, seen from the front, her body making a soft rounded frame around the baby.
LAYOUT: the mother's body is the outer frame: left bent stroke and right horizontal-then-down stroke; her two arms hugging the baby lie on the long middle horizontal; the baby's two little hands are the two dots, upper and lower, inside the frame.
```

### 目 눈 목 (U76EE) — `claude_b/U76EE_B.jpg`
- 획↔그림: 세로로 긴 네모 = 세워 놓은 눈의 윤곽, 안의 두 가로 = 눈동자의 위아래 선.
```
SUBJECT: a single eye standing upright (turned 90 degrees), drawn as a tall rounded outline with the iris and pupil as two horizontal lines inside.
LAYOUT: the eye outline is the tall rectangle; the two lines inside sit exactly on the two short inner horizontals.
```

### 以 써 이 (U4EE5) — `claude_b/U4EE5_B.jpg`
- 획↔그림: 왼쪽 꺾은 획 = 세워 둔 삽(자루와 꺾인 날), 점 = 삽을 쥔 손, 오른쪽 人 = 삽을 쓰는 아이.
```
SUBJECT: a child on the right using a small shovel standing on the left, seen from the side.
LAYOUT: the shovel's shaft and bent blade follow the left vertical-then-bending stroke; the child's hand on the shovel is the dot; the child's body and legs are the 人 shape on the right, head at its apex.
```

### 用 쓸 용 (U7528) — `claude_b/U7528_B.jpg`
- 획↔그림: 바깥 冂 = 나무 통의 양 옆과 위, 두 가로 = 통을 두른 테 둘, 가운데 세로 = 통의 이음매(널빤지 선).
```
SUBJECT: a wooden bucket or barrel standing upright, seen from the side, bound with two hoops.
LAYOUT: the barrel's two sides and top edge form the outer frame; the two hoops lie on the two inner horizontals; the center seam between staves runs down the central vertical stroke.
```

### 立 설 립 (U7ACB) — `claude_b/U7ACB_B.jpg`
- 획↔그림: 점 = 머리, 위 가로 = 벌린 팔, 두 점(丷) = 벌리고 선 두 다리, 바닥 가로 = 땅.
```
SUBJECT: a child standing firmly on the ground facing the viewer, arms out, feet apart.
LAYOUT: the head is the top dot; the arms lie on the upper horizontal; the two legs are the two short slanted strokes in the middle; the ground is the long bottom horizontal.
```

### 田 밭 전 (U7530) — `claude_b/U7530_B.jpg`
- 획↔그림: 바깥 네모 = 밭 둘레의 두렁, 안의 십자 = 밭을 넷으로 가르는 두렁길.
```
SUBJECT: a square farm field seen from directly above, divided into four plots by two crossing footpaths.
LAYOUT: the field edge is the outer square; the two footpaths lie on the inner horizontal and inner vertical strokes, crossing at the center.
```

### 由 말미암을 유 (U7531) — `claude_b/U7531_B.jpg`
- 획↔그림: 네모와 안 십자 = 네모난 화분(밭), 위로 솟은 세로 = 화분에서 올라온 새싹 줄기.
```
SUBJECT: a square flower pot seen from above-front with a single sprout rising straight up out of its center.
LAYOUT: the pot is the square outline with the inner horizontal; the sprout's stem runs up the central vertical and pokes above the top edge exactly as the stroke does.
```

### 必 반드시 필 (U5FC5) — `claude_b/U5FC5_B.jpg`
- 획↔그림: 넓은 굽은 갈고리 + 세 점 = 하트(心), 긴 삐침 = 하트를 가로지르는 화살(큐피드 화살, 무서운 소재 아님).
```
SUBJECT: a soft heart shape with a single arrow passing diagonally through it, like a simple love-arrow emoji, drawn in ink.
LAYOUT: the heart's bowl follows the wide curved hooked stroke and its three dots are the three dots of the character; the arrow runs from the upper right to the lower left exactly along the long left-falling stroke.
```

### 末 끝 말 (U672B) — `claude_b/U672B_B.jpg`
- 획↔그림: 맨 위 긴 가로 = 나무 꼭대기의 넓은 가지, 둘째 짧은 가로 = 아래 가지, 세로 = 줄기, 삐침·파임 = 뿌리.
```
SUBJECT: a young tree whose topmost branches spread the widest, with a shorter branch below, a straight trunk and two roots.
LAYOUT: the wide top branches lie on the long top horizontal; the shorter branch on the second horizontal; the trunk on the vertical; the roots follow the left-falling and right-falling strokes.
```

### 示 보일 시 (U793A) — `claude_b/U793A_B.jpg`
- 획↔그림: 위 짧은 가로 = 상 위에 올린 접시, 둘째 긴 가로 = 상판, 갈고리 세로 = 가운데 다리, 두 점 = 양쪽 받침.
```
SUBJECT: a small low table with a plate of fruit on top, seen from the front, standing on one center leg with two little side supports.
LAYOUT: the plate is the short top horizontal; the tabletop is the long second horizontal; the center leg runs down the vertical hooked stroke; the two side supports are the two dots.
```

### 民 백성 민 (U6C11) — `claude_b/U6C11_B.jpg`
- 획↔그림: 위 네모 = 숙인 머리, 아래 氏 = 허리를 굽혀 절하는 몸과 길게 뻗은 다리 (무서운 어원 대신 "고개 숙인 사람").
```
SUBJECT: a person in side view bowing deeply with the head lowered, one leg stretched back, present-day clothes.
LAYOUT: the lowered head is the small rounded box at the top left; the bending torso follows the left vertical and the slanted stroke; the stretched leg runs to the lower right along the long hooked stroke, foot at the hook.
```

### 永 길 영 (U6C38) — `claude_b/U6C38_B.jpg`
- 획↔그림: 맨 위 점 = 샘, 갈고리 세로 = 똑바로 흘러내리는 본류, 가로-꺾음·삐침 = 왼쪽 지류들, 오른쪽 삐침·파임 = 오른쪽 지류.
```
SUBJECT: a long river seen from above: a spring at the top feeding a main stream that flows straight down, with branches spreading to both sides.
LAYOUT: the spring is the top dot; the main stream runs down the vertical hooked stroke; the left branches follow the bending stroke and the left-falling stroke; the right branch follows the short left-falling and the long right-falling stroke.
```

### 皮 가죽 피 (U76AE) — `claude_b/U76AE_B.jpg`
- 획↔그림: 위 가로-꺾음 = 벗겨져 말린 껍질 끝, 삐침·세로 = 길게 늘어진 껍질 띠, 아래 又 = 껍질을 잡아당기는 손 (바나나 껍질 벗기기).
```
SUBJECT: a hand peeling a long strip of banana peel downward, seen from the front, only the peel strip and the hand.
LAYOUT: the curled top of the peel is the horizontal-then-bending stroke; the hanging strip runs down the left-falling stroke and the vertical; the hand gripping the strip is the 又 shape at the bottom.
```

## 6획

### 行 다닐 행 (U884C) — `claude_b/U884C_B.jpg`
- 획↔그림: 왼쪽 彳 = 왼쪽 길 가장자리 두 줄, 오른쪽 亍 = 오른쪽 길 가장자리와 갈고리로 꺾이는 길 (네거리 위에서 본 모습).
```
SUBJECT: a four-way crossroads seen from directly above, drawn only by the road edges, with one tiny person walking in it.
LAYOUT: the two short road edges on the left are the two left-falling strokes plus the left vertical; the right road edges are the two horizontals and the long vertical hooked stroke; roads stay inside the strokes, no buildings.
```

### 自 스스로 자 (U81EA) — `claude_b/U81EA_B.jpg`
- 획↔그림: 세로로 긴 네모 = 코의 윤곽, 안의 두 가로 = 코의 주름(콧등 선), 위 삐침 = 미간에서 내려오는 콧대 시작.
```
SUBJECT: a nose seen from the front, drawn as a tall rounded outline with two faint creases inside, and the bridge beginning as a short slanted line at the top.
LAYOUT: the outline is the 目-like tall rectangle; the creases lie on the two inner horizontals; the bridge is the short left-falling stroke on top.
```

### 肉 고기 육 (U8089) — `claude_b/U8089_B.jpg`
- 획↔그림: 바깥 冂 = 고기 한 덩이의 윤곽, 안의 人人 = 고기의 결(마블링) 두 줄.
```
SUBJECT: a slab of meat seen from the side, like a steak hanging from the top, with two chevron-shaped lines of marbling inside.
LAYOUT: the slab's outline is the outer frame; the two chevrons lie on the two 人-shaped strokes stacked inside the frame.
```

### 合 합할 합 (U5408) — `claude_b/U5408_B.jpg`
- 획↔그림: 亼(人+가로) = 뾰족한 뚜껑, 口 = 네모난 통 (도시락 뚜껑이 통에 딱 맞음).
```
SUBJECT: a square lunch box with its peaked lid lowered onto it, seen from the front, fitting exactly.
LAYOUT: the lid's two sloping edges are the 人 strokes and its rim is the horizontal under them; the box is the square 口 at the bottom.
```

### 向 향할 향 (U5411) — `claude_b/U5411_B.jpg`
- 획↔그림: 위 삐침 = 지붕 꼭대기, 冂 = 집의 지붕선과 두 벽, 안의 口 = 벽에 난 창문.
```
SUBJECT: a small simple house seen from the front with one square window in the wall, no door, no ground.
LAYOUT: the roof peak is the short top stroke; the roof edge and the two walls are the 冂 frame; the window is the small square inside.
```

### 老 늙을 로 (U8001) — `claude_b/U8001_B.jpg`
- 획↔그림: 위 土 = 긴 머리카락과 머리, 삐침 = 굽은 등, 匕 = 다리와 짚은 지팡이.
```
SUBJECT: an elderly person in side view with long hair, bent forward, leaning on a walking stick.
LAYOUT: the head and long hair are the top 土-shaped strokes; the bent back runs down the long left-falling stroke; the legs and the walking stick are the 匕 shape at the bottom right, stick on its hooked stroke.
```

### 米 쌀 미 (U7C73) — `claude_b/U7C73_B.jpg`
- 획↔그림: 세로 = 벼 줄기, 가로 = 이삭 가지, 위 두 점과 아래 삐침·파임 = 줄기 주위에 달린 쌀알들.
```
SUBJECT: a rice stalk with grains hanging around it, drawn very simply: one stem, one side branch, and grains at six points.
LAYOUT: the stem is the vertical stroke; the branch is the horizontal; grains sit on the two top dots and along the left-falling and right-falling strokes below.
```

### 回 돌아올 회 (U56DE) — `claude_b/U56DE_B.jpg`
- 획↔그림: 바깥 네모 = 소용돌이의 바깥 물결, 안 네모 = 가운데 소용돌이 눈.
```
SUBJECT: a whirlpool seen from above, water spinning inward in a squared spiral, drawn as an outer loop and an inner loop.
LAYOUT: the outer loop is the outer square; the inner loop is the inner small square; the spiral stays inside the outer square.
```

## 7획

### 車 수레 거 (U8ECA) — `claude_b/U8ECA_B.jpg`
- 획↔그림: 가운데 긴 세로 = 바퀴 축, 가운데 네모(日) = 짐칸, 위아래 가로 = 양쪽 바퀴를 옆에서 본 모습 (위에서 내려다본 수레).
```
SUBJECT: a hand cart seen from directly above: a long axle, a square cargo box in the middle, and two wheels seen edge-on at the ends.
LAYOUT: the axle runs the whole central vertical stroke; the cargo box is the square with the inner horizontal; the two wheels are the top and bottom horizontal strokes.
```

### 足 발 족 (U8DB3) — `claude_b/U8DB3_B.jpg`
- 획↔그림: 위 口 = 무릎(둥근 무릎뼈), 아래 止 = 발 (발가락 위로).
```
SUBJECT: one bent leg seen from the front, the knee drawn as a rounded square at the top and the foot below with toes pointing up.
LAYOUT: the knee is the square 口; the foot is the 止 shape: shin and long toe on its vertical, big toe on the short left vertical, small toe on the short horizontal, heel on the bottom horizontal.
```

### 角 뿔 각 (U89D2) — `claude_b/U89D2_B.jpg`
- 획↔그림: 위 𠂊 = 휘어진 뿔 끝, 아래 冂과 가운데 세로 = 뿔 몸통, 안의 두 가로 = 뿔의 마디 줄.
```
SUBJECT: a single animal horn standing upright, its tip curving at the top, with ring-shaped ridges across its body.
LAYOUT: the curved tip is the two short strokes at the top; the horn's body is the tall 冂 frame with the central vertical; the ridges lie on the two inner horizontals.
```

### 身 몸 신 (U8EAB) — `claude_b/U8EAB_B.jpg`
- 획↔그림: 위 삐침 = 머리(코), 세로 테두리 = 등과 가슴, 안의 가로들 = 불룩한 배, 아래 긴 삐침 = 앞으로 내디딘 다리.
```
SUBJECT: a person in side view with a big round belly (an expecting mother), one leg stepping forward, present-day clothes.
LAYOUT: the head is the short top left-falling stroke; the back and chest are the tall frame; the belly bulge sits on the inner horizontals; the stepping leg runs to the lower left along the long bottom left-falling stroke.
```

## 8획

### 長 긴 장 (U9577) — `claude_b/U9577_B.jpg`
- 획↔그림: 위 세로와 가로 셋 = 길게 늘어뜨린 머리카락, 긴 가로 = 어깨, 아래 꺾음·삐침·파임 = 다리와 지팡이.
```
SUBJECT: an elderly person in side view with very long hair flowing down, leaning on a walking stick.
LAYOUT: the hair is the top vertical with the three short horizontals; the shoulders are the long horizontal; the body and legs follow the lower bending stroke and the left-falling stroke; the walking stick is the long right-falling stroke.
```

### 東 동녘 동 (U6771) — `claude_b/U6771_B.jpg`
- 획↔그림: 木 = 나무(가로 가지, 세로 줄기, 뿌리), 가운데 日 = 나무 뒤로 떠오르는 해.
```
SUBJECT: the sun rising behind a tree, the round sun sitting in the middle of the trunk, seen from the front.
LAYOUT: the tree is the 木 strokes: branches on the top horizontal, trunk on the vertical, roots on the left-falling and right-falling strokes; the sun is the square 日 in the middle, trunk passing through it.
```

### 來 올 래 (U4F86) — `claude_b/U4F86_B.jpg`
- 획↔그림: 세로 = 밀 줄기, 가로 = 가지, 양쪽 人人 = 늘어진 이삭 둘, 아래 삐침·파임 = 뿌리.
```
SUBJECT: a single wheat plant with a straight stalk, two drooping ears on either side, and roots spreading at the base.
LAYOUT: the stalk is the vertical stroke; the side branch is the horizontal; the two ears are the two 人 shapes left and right; the roots follow the bottom left-falling and right-falling strokes.
```

### 非 아닐 비 (U975E) — `claude_b/U975E_B.jpg`
- 획↔그림: 두 세로 = 새의 두 날개 뼈대, 좌우 가로 셋씩 = 서로 반대쪽으로 뻗은 깃털 (등 뒤에서 본 펼친 두 날개).
```
SUBJECT: a bird's two wings seen from behind, spread in opposite directions, each wing a spine with three feathers pointing outward, no body.
LAYOUT: the left wing's spine is the left vertical with its three feathers on the three left horizontals; the right wing's spine is the right vertical with its three feathers on the three right horizontals.
```

### 幸 다행 행 (U5E78) — `claude_b/U5E78_B.jpg`
- 획↔그림: 위 土 = 종 손잡이와 어깨, 丷 = 울리는 소리 표시 둘, 아래 干 = 종 몸통과 테 (새해 행운의 종; 수갑 어원은 쓰지 않음).
```
SUBJECT: a hand bell held upright ringing for good luck, seen from the front: a handle on top, two small sound marks, and the bell body with its rim, no hand.
LAYOUT: the handle and shoulder are the top 土 strokes; the two sound marks are the two short slanted strokes; the bell body is the lower 干: rim on its long horizontal, body on its vertical.
```

### 門 문 문 (U9580) — `claude_b/U9580_B.jpg`
- 획↔그림: 좌우 긴 세로 = 양쪽 문기둥, 위의 짧은 네모 둘 = 두 문짝 윗부분의 판, 오른쪽 갈고리 = 오른 문짝 아래 끝.
```
SUBJECT: a double-leaf gate seen from the front, two tall door panels hinged on outer posts, slightly open, no wall.
LAYOUT: the left post and panel follow the left vertical and its small square; the right post and panel follow the right vertical hooked stroke and its small square; the panels stay inside the strokes.
```

## 9획

### 食 밥 식 (U98DF) — `claude_b/U98DF_B.jpg`
- 획↔그림: 亼 = 뾰족한 뚜껑, 가운데 日 = 그릇 몸통(안의 가로 = 밥 높이), 아래 꺾음·파임 = 그릇 받침.
```
SUBJECT: a lidded rice bowl seen from the side, a peaked lid on top, the bowl showing the rice line, standing on a flared foot.
LAYOUT: the lid is the 人 strokes and the short horizontal under them; the bowl is the square with the inner horizontal; the foot follows the bottom bending stroke and the right-falling stroke.
```

### 重 무거울 중 (U91CD) — `claude_b/U91CD_B.jpg`
- 획↔그림: 위 삐침·가로 = 숙인 머리와 어깨, 가운데 日 = 등에 멘 무거운 자루, 긴 세로 = 등줄기, 아래 가로 둘 = 땅을 딛는 발.
```
SUBJECT: a person seen from the front carrying a heavy square sack on the back, bent under the weight, present-day clothes.
LAYOUT: the bowed head and shoulders are the top left-falling stroke and the first horizontal; the sack is the square 日 in the middle; the spine runs down the long vertical; the feet are the two bottom horizontals.
```

### 面 낯 면 (U9762) — `claude_b/U9762_B.jpg`
- 획↔그림: 위 가로와 삐침 = 이마와 머리카락 선, 큰 테두리 = 얼굴 윤곽, 안의 目 = 큰 눈 하나.
```
SUBJECT: a face drawn as a tall rounded outline with one single large eye inside it and a hairline across the top.
LAYOUT: the hairline is the top horizontal and the short left-falling stroke; the face outline is the big frame; the eye is the 目 shape inside, its lines on the inner horizontals.
```

### 要 요긴할 요 (U8981) — `claude_b/U8981_B.jpg`
- 획↔그림: 위 覀 = 허리에 올린 두 손과 허리띠, 아래 女 = 다리와 치마 (허리에 손 얹고 선 여인).
```
SUBJECT: a woman standing facing the viewer with both hands on her hips, present-day clothes.
LAYOUT: the hands on the hips and the waist are the top 覀 frame with its two inner verticals as the arms; the legs and skirt are the 女 strokes below: folded line on the left stroke, the long horizontal as the skirt hem.
```

### 飛 날 비 (U98DB) — `claude_b/U98DB_B.jpg`
- 획↔그림: 긴 세로 = 새의 몸통(위로 솟음), 오른쪽 위아래 두 꺾음과 점들 = 오른쪽 날개 둘의 깃털, 왼쪽 升 모양 = 왼쪽 날개와 다리.
```
SUBJECT: a bird soaring straight up, seen from below-side, long body vertical, wings on both sides with feather tips.
LAYOUT: the body runs the long central vertical; the right wing feathers follow the two bending strokes with dots on the right; the left wing and legs follow the 升-like strokes on the left.
```

## 10획 이상

### 高 높을 고 (U9AD8) — `claude_b/U9AD8_B.jpg`
- 획↔그림: 점·가로 = 뾰족 지붕, 위 口 = 망루 창, 冂 = 높은 벽, 아래 口 = 출입문.
```
SUBJECT: a tall watchtower or gatehouse seen from the front: a pointed roof, a small window high up, tall walls, and a doorway at the bottom.
LAYOUT: the roof is the top dot and horizontal; the window is the upper small square; the walls are the 冂 frame; the doorway is the lower small square.
```

### 馬 말 마 (U99AC) — `claude_b/U99AC_B.jpg`
- 획↔그림: 위 세로와 가로 셋 = 머리·눈·갈기, 긴 세로 = 목과 몸통, 오른쪽 꺾음-갈고리 = 등에서 꼬리, 아래 점 넷 = 네 다리.
```
SUBJECT: a horse rearing up in side view so that its body is nearly vertical, mane flowing, four legs beneath, tail curling.
LAYOUT: the head, eye and mane are the top vertical and the three short horizontals; the neck and body run down the long vertical; the back and tail follow the right bending hooked stroke; the four legs are the four dots at the bottom.
```

### 會 모일 회 (U6703) — `claude_b/U6703_B.jpg`
- 획↔그림: 亼 = 뾰족한 뚜껑, 가운데 = 찜통 몸체의 창살(김 구멍), 아래 曰 = 받침 그릇.
```
SUBJECT: a stacked steamer pot seen from the side: a peaked lid on top, a tall middle tier with small vent slits, and a wider base pot at the bottom.
LAYOUT: the lid is the 人 strokes and the horizontal under them; the middle tier is the strokes between, its slits on the small inner marks; the base pot is the bottom 曰 square with its inner horizontal.
```

### 樂 즐길 락 (U6A02) — `claude_b/U6A02_B.jpg`
- 획↔그림: 아래 木 = 나무 받침대(가지·기둥·다리), 좌우 幺幺 = 양쪽에 맨 실(현) 뭉치 둘, 가운데 白 = 작은 북.
```
SUBJECT: a musical instrument on a wooden stand: a small drum in the center with a bundle of strings on each side, standing on a wooden frame with spreading legs.
LAYOUT: the stand is the 木 strokes at the bottom: crossbar on the horizontal, post on the vertical, legs on the left-falling and right-falling strokes; the two string bundles are the 幺 shapes on the left and right; the drum is the 白 shape in the center.
```
