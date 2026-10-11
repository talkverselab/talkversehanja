# Grok 작업 지시서 — 26회차 (다시 그리기)

리뷰 페이지: https://talkverse.uk/hanja-review/ · 이 문서: https://talkverse.uk/hanja-review/GROK_NEXT.md?r=26 · 전체 대기열: https://talkverse.uk/hanja-review/REDO.md?r=26

## 0. 방향이 바뀌었다 — 먼저 읽을 것

사용자가 지금까지의 그림을 직접 검수했고 대부분 재작업이 됐다. 이유는 하나다: **아이가 그림을 보고 뜻을 못 맞힌다.** 앞으로의 기준:

1. **초등학생(7~10세)이 그림만 보고 3초 안에 뜻을 말할 수 있어야 한다.** 어원(갑골문의 옛 물건)을 그대로 그리지 말 것. 어원보다 쉽게, 지금 시대의 일상 장면으로.
2. **그림의 윤곽이 글자 모양과 겹쳐야 한다.** 아래 각 글자의 "어느 부분이 어느 획"을 지켜 배치한다(글자의 획이 있을 자리에 그림의 선이 있게).
3. **추상적인 뜻(위·아래·같다·방향·으뜸)은 지사식**: 장면이 아니라 굵은 선과 화살표·점으로 된 단순한 도해.
4. **주인공 하나, 흰 배경, 배경 풍경·글자·낙관·색 금지.** 무섭거나 불쾌한 소재(무기, 형벌, 고깃덩이, 바늘) 금지. 옛 옷·상투 대신 요즘 아이와 어른.
5. **여러 컷**이라고 적힌 글자는 컷마다 한 장씩, 같은 구도·같은 크기로 그린다(마지막 컷이 글자 모양에 가장 가깝게).
6. **B컷(글자)은 그리지 않는다.** 글자는 Claude 가 정자(楷書)로 따로 만든다. 이번 회차부터 **A컷만**.

파일명: `redo/<코드>_A.jpg` (여러 컷이면 `redo/<코드>_A1.jpg`, `_A2.jpg` …). 예: `redo/U65E5_A.jpg`. 끝나면 커밋만 하면 된다.

## 1. 이번 회차 12자 (순서: 씨앗 → 8급 → 7급 → 6급 → 5급)

### 疒 병질 녁 (U7592) — 씨앗 · Claude 지적
- 지적: 아픈 사람이 아니라 '잠자는 사람'으로 보인다. 병·아픔을 알리는 단서가 전혀 없고 비스듬한 침대 윤곽도 疒 과 닮지 않았다.
- 새 그림: 옆에서 본 병상: 왼쪽에 세로로 선 침대 머리판(긴 삐침), 위로 덮인 이불 윗선(가로획)과 꼭대기 점=이마의 얼음주머니, 왼쪽 두 점=식은땀 방울. 아이가 체온계를 물고 누워 있게 한다.
- 파일: `redo/U7592_A.jpg`

```
Monochrome sumi-e ink-wash on plain white paper, 1:1 square, single centered subject, no text, no color: side view of a sick child lying in bed with a thermometer in the mouth and an ice pack on the forehead, a tall headboard standing vertically on the left curving down like a long diagonal stroke, the top edge of the blanket forming one horizontal line, two sweat drops floating at the left side; overall silhouette shaped like the radical 疒.
```

### 厶 사사 사 (U53B6) — 씨앗 · Claude 지적
- 지적: 몸의 어느 부분인지도 알기 어렵고 무엇을 하는지 아이가 읽을 수 없다. '내 것(사사로움)'이라는 뜻이 전혀 전해지지 않는다.
- 새 그림: 아이가 곰 인형을 품에 꼭 끌어안고 '내 거야' 하는 모습. 굽힌 팔이 ㄥ 모양의 꺾인 획이 되고, 품 안의 인형이 마지막 점이 된다.
- 파일: `redo/U53B6_A.jpg`

```
Monochrome sumi-e ink-wash on plain white paper, 1:1 square, single centered subject, no text, no color: a small child hugging a teddy bear tightly to the chest as if saying 'mine', the bent arm drawn as one bold angular line going down-left then turning right like a pointed elbow, the small bear tucked at the lower right as a round dot; silhouette resembling the shape 厶.
```

### 冖 민갓머리 멱 (U5196) — 씨앗 · Claude 지적
- 지적: '덮다'보다 '식탁·식탁보'로 읽히고, 천이 너무 길게 내려와 冖 이 아니라 冂 모양이 된다. 무엇을 덮었는지도 보이지 않는다.
- 새 그림: 밥상 위 음식 그릇에 상보(보자기)를 살짝 덮는 장면. 천은 납작한 윗선 하나와 양 끝이 짧게만 꺾여 내려오게 하고(왼쪽 짧은 점, 오른쪽 짧은 갈고리), 아래로 그릇 윤곽이 비쳐 보이게 한다. 2컷: 그릇이 보임 → 천으로 덮임.
- 파일: `redo/U5196_A.jpg`

```
Monochrome sumi-e ink-wash on plain white paper, 1:1 square, single centered subject, no text, no color: a thin cloth being laid over a bowl of food, the cloth drawn as one wide flat horizontal line with both ends bending down only a short way, the bowl faintly visible underneath; silhouette like a flat lid shape 冖, very simple.
```

### 辵 쉬엄쉬엄 갈 착 (U8FB5) — 씨앗 · Claude 지적
- 지적: 아이는 '발' 또는 '발자국'이라고 답하지 '가다'라고 답하지 않는다. 속도선 때문에 '쉬엄쉬엄'과도 반대 느낌이고 辶 모양(위 점·꺾임·아래로 길게 뻗는 받침)과도 닮지 않았다.
- 새 그림: 왼쪽 위에서 내려와 오른쪽 아래로 길게 휘어 뻗는 길 위를 아이가 천천히 걸어가는 뒷모습. 길의 긴 곡선이 받침 획(㇏), 길 위에 찍힌 발자국 두세 개가 위의 점과 꺾임, 걷는 아이가 위쪽 획들이 된다.
- 파일: `redo/U8FB5_A.jpg`

```
Monochrome sumi-e ink-wash on plain white paper, 1:1 square, no text, no color. A small child seen from the side strolling slowly along a single winding dirt path. The path starts at the upper left, drops down, then sweeps in one long curve to the lower right like a brush tail. Two or three small footprints are left behind on the upper-left part of the path. Single centered subject, lots of empty white space, no background scenery.
```

### 彳 조금 걸을 척 (U5F73) — 씨앗 · Claude 지적
- 지적: 무엇을 그린 것인지 어른도 알 수 없다. 길도 걸음도 보이지 않고 그림이 화면에서 잘려 있다.
- 새 그림: 지사 스타일: 위에서 본 갈림길(왼쪽으로 비스듬히 갈라지는 두 갈래 길 + 아래로 곧게 뻗는 길) 위에 작은 발자국이 조금씩 찍혀 있는 그림. 비스듬한 두 갈래 길이 삐침 두 획(丿丿), 아래로 뻗는 길이 세로획(丨)이 된다.
- 파일: `redo/U5F73_A.jpg`

```
Monochrome sumi-e ink-wash on plain white paper, 1:1 square, no text, no color. A simple top-down diagram of a small footpath: two short parallel lanes slanting from upper right down to the lower left, and one straight lane running vertically downward from under them, forming the shape of the left half of a crossroads. A few tiny footprints walk along the vertical lane with a small arrow showing slow forward steps. Single centered subject, clean white background.
```

### 宀 집 면 (U5B80) — 씨앗 · Claude 지적
- 지적: '집·지붕'이라는 뜻과 글자 모양(꼭대기 점+덮는 지붕)은 맞지만(경미한 수정), 좌우 산·아래 바위 등 배경이 지저분하고 옛 정자라 요즘 아이의 '집'과 거리가 있다.
- 새 그림: 배경 없이 지붕만 큰 단순한 집 한 채. 지붕 꼭대기의 작은 굴뚝(또는 꼭지)=맨 위 점, 양쪽으로 내려오다 끝이 살짝 꺾이는 지붕선=冖(왼쪽 짧은 내리획+가로획+오른쪽 갈고리), 벽은 아주 옅게.
- 파일: `redo/U5B80_A.jpg`

```
Monochrome sumi-e ink-wash on plain white paper, 1:1 square, single centered subject: a simple small house seen from the front, dominated by a wide dark roof whose two eaves end in short downward hooks, a tiny chimney knob at the very top center like a dot, walls drawn very faintly below. No mountains, no mist, no ground clutter, no text, no color.
```

### 攴 칠 복 (U6534) — 씨앗 · Claude 지적
- 지적: 아이 눈에는 '막대를 든 손/연필 쥔 손'일 뿐 '치다'라는 동작이 전혀 보이지 않는다.
- 새 그림: 북채를 든 손이 북을 '둥' 하고 내려치는 순간. 위쪽 북채(세로 막대+옆으로 튀는 짧은 선)=卜, 아래 손과 팔=又, 북은 아래쪽에 작게, 맞는 자리엔 충격선 두세 개. 2프레임 가능: 채를 든 손 → 북을 내려침.
- 파일: `redo/U6534_A.jpg`

```
Monochrome sumi-e ink-wash on plain white paper, 1:1 square, single centered subject: a hand gripping a short drumstick and striking down on a small drum, the stick held upright at the top with a small spark line flying off to the right, the hand and forearm crossing below in an X-like shape, a few short impact lines where the stick hits. No background, no text, no color.
```

### 殳 창 수 (U6BB3) — 씨앗 · Claude 지적
- 지적: '창'이 아니라 방망이·두루마리처럼 보이고 치는 동작도 없다. 攴 그림과도 거의 같아 구별이 안 된다.
- 새 그림: 긴 창(몽둥이 창)을 두 손으로 번쩍 들어 내리찌르려는 사람의 상반신. 위쪽 구부러진 창날·창끝=几 모양 윗부분, 아래 창을 쥔 손과 팔=又. 창이 화면을 대각선으로 길게 가로지르게.
- 파일: `redo/U6BB3_A.jpg`

```
Monochrome sumi-e ink-wash on plain white paper, 1:1 square, single centered subject: a hand and forearm thrusting a long spear upward, the spear tip and its curved hooked guard forming a small arch shape at the top, the gripping hand and crossed forearm forming an X-like shape below. Dynamic motion lines, no background, no text, no color.
```

### 歹 살 바른 뼈 알 (U6B79) — 씨앗 · Claude 지적
- 지적: '뼈'라는 건 한눈에 알지만(뜻은 통과에 가까움), '살을 발라낸' 느낌이 없고 대각선 뼈 하나의 윤곽이 歹(위 가로획+아래 夕)와 닮지 않아 변형이 어색하다.
- 새 그림: 다 먹고 남은 갈비뼈/생선뼈 접시. 위에 가로로 놓인 곧은 뼈 하나=맨 위 가로획, 그 아래 비스듬히 휘어 꺾인 갈비뼈=夕의 삐침과 꺾임, 가운데 작은 뼛조각=점. 살점 부스러기가 조금 붙어 '발라 먹은' 느낌.
- 파일: `redo/U6B79_A.jpg`

```
Monochrome sumi-e ink-wash on plain white paper, 1:1 square, single centered subject: picked-clean bones left after a meal, one straight bone lying horizontally on top, beneath it a curved rib bone slanting down-left then bending, and one small bone chip in the middle, tiny scraps of meat still clinging. No plate decoration, no background, no text, no color.
```

### 日 날 일 (U65E5) — 8급 · 사용자 지적
- 지적: 수평선에서 해가 떠오르는 그림
- 새 그림: 바다 수평선 위로 둥근 해가 떠오름 — 해 테두리가 네모 틀로 펴지고, 해를 가로지르는 수평선(또는 구름 한 줄)이 가운데 가로획.
- 파일: `redo/U65E5_A.jpg`

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, clean confident brush lines with only light ink bleed, generous empty space, square 1:1 composition, single centered subject, no text, no letters, no seal stamp, no background scenery; a large round sun rising over a flat sea horizon, the horizon line crossing the middle of the sun, calm water, nothing else
```

### 入 들 입 (U5165) — 8급 · 사용자 지적
- 지적: 사람이 움막 안으로 들어가는 모습
- 새 그림: 세모난 움막(텐트) 입구로 사람이 허리 숙여 들어감 — 움막의 긴 오른쪽 경사가 긴 파임, 짧은 왼쪽 경사가 삐침(꼭대기는 왼쪽으로 기움).
- 파일: `redo/U5165_A.jpg`

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, clean confident brush lines with only light ink bleed, generous empty space, square 1:1 composition, single centered subject, no text, no letters, no seal stamp, no background scenery; a person bending to step into a small triangular hut, the hut made of two leaning poles: a long right slope and a shorter left slope meeting at a peak that tilts left, entrance open in the middle
```

### 生 날 생 (U751F) — 8급 · 사용자 지적 · **2컷 이상**
- 지적: 떡잎 느낌, 잎이 더 많게
- 새 그림: 3컷: 흙 속 씨앗 → 떡잎 → 잎이 두 층으로 자란 새싹. 땅이 맨 아래 가로획, 줄기가 세로획, 잎 두 층이 가로획 2개, 왼쪽 위 어린잎이 삐침.
- 파일: `redo/U751F_A.jpg` (컷별 `redo/U751F_A1.jpg` …)

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, clean confident brush lines with only light ink bleed, generous empty space, square 1:1 composition, single centered subject, no text, no letters, no seal stamp, no background scenery; frame 1: a seed under a ground line with a tiny sprout; frame 2: a young seedling on a ground line with a straight stem, two tiers of opposite leaves, and one small new leaf at upper left
```

## 2. 남은 대기열

이번 회차 뒤로 138자가 남는다. 전체 표는 REDO.md.
