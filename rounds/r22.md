# Grok 작업 지시서 (이 파일과 refs/ 이미지는 이 저장소 안에 있음 — 이미지를 직접 열어 볼 것) — 22회차 (2026-10-10)

리뷰 페이지: https://talkverse.uk/hanja-review/ · 보기 쉬운 판: https://talkverse.uk/hanja-review/grok · 이 문서: https://talkverse.uk/hanja-review/GROK_NEXT.md?r=22 (캐시 피하려면 ?r=회차 를 붙여 읽을 것)

한 회차 = 재작업 + 새 글자 8자 안팎. 끝나면 커밋만 하면 된다(Claude 가 커밋을 감시해 검토하고 이 문서를 갱신한다).

## 0. 21회차 검토 결과

| 글자 | 판정 | 비고 |
|---|---|---|
| 隹 | 통과 | B v3 隹 정상 |
| 參 | 통과 | 參 읽힘 |
| 彡 | 통과 | 彡 정상 |
| 在 | 통과 | 在 정상 |
| 歹 | 통과 | 歹 읽힘 |
| 求 | 통과 | 求 읽힘 |
| 冖 | 통과 | 冖 정상 |
| 辵 | 통과 | Grok 4회 실패 → Claude 렌더 B 로 대체(리뷰에서 확인) |
| 攴 | 통과 | Grok 3회 실패 → Claude 렌더 B |
| 殳 | 통과 | Grok 2회 실패 → Claude 렌더 B |
| 告 | 통과 | Grok 2회 실패 → Claude 렌더 B |

## 1. 새 글자 12자 (중요도 순, A·B 둘 다) — 파일명 `<병음>_A.jpg`/`_B.jpg`, B 는 참고 글자 첨부

### 半 반(半) 반 (U534A) — 우리 5급
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U534A_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U534A_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U534A_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 5획 · 구성 丷+⿻二丨 · 회의
- **이미지를 못 읽으면 아래 글자 격자(楷書 半 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
······························
··············██··············
··············███·············
··············███···██········
··············██····███·······
·········██···██···███········
·········███··██··██··········
··········██··██··············
··············██··············
··············███████·········
·········███████████··········
·········███████··············
···············█··············
···············████████████···
··········█████████████████···
····████████··██··············
·····██········█··············
···············█··············
···············██·············
···············█··············
···············█··············
···············█··············
···············█··············
···············█··············
······························
······························
······························
······························
```

- **A컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, an ox seen from the front split down the middle by a thin vertical gap, its two halves slightly apart
```
- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 半 written in bold semi-cursive (行書) brushwork, exactly 5 strokes: two dots on top, two horizontals and a vertical, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```
- 주의: 牛·平과 혼동 주의.

### 示 보일 시 (U793A) — 우리 5급
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U793A_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U793A_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U793A_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 5획 · 상형·지사
- **이미지를 못 읽으면 아래 글자 격자(楷書 示 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
······························
······························
······························
···············██████·········
··········███████████·········
···········█████··············
······························
······························
····················██████····
·············██████████████···
·····█████████████············
·····█████·····██·············
···············██·············
·········█·····██·············
·········█·····██···███·······
········██·····██····███······
········██·····██····████·····
·······███·····██·····███·····
·······██······██·······█·····
·······██······██·············
············█████·············
·············████·············
··············██··············
······························
······························
······························
······························
······························
```

- **A컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, a small wooden altar table with a flat top, one central leg and two short side legs, nothing on it
```
- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 示 written in bold semi-cursive (行書) brushwork, exactly 5 strokes: two horizontals on top, a vertical and two short side strokes, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```
- 주의: 부수 보일시.

### 兩 두 량 (U5169) — 우리 5급
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U5169_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U5169_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U5169_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 8획 · 구성 一+⿻巾𠓜 · 회의
- **이미지를 못 읽으면 아래 글자 격자(楷書 兩 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
······························
······························
······························
················█████·········
···········██████████·········
···········█████··············
··············██··············
··············██··············
··············██··██████······
············█████████████·····
······███████·██······███·····
·······██·····██·█·····██·····
·······██·█···██··██···█······
·······██··██·██··███··█······
·······██··█████·█████·█······
·······██··█████·█··██·█······
·······██·██·████····███······
·······████···██······██······
·······██·····██······██······
·······██·····██···█··██······
·······██·····██····████······
········█···········███·······
·····················██·······
······························
······························
······························
······························
······························
```

- **A컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, a wooden ox yoke seen from the front: a flat crossbar with two identical U-shaped loops hanging under it
```
- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 兩 written in bold semi-cursive (行書) brushwork, exactly 8 strokes: a top horizontal over a 冂 frame containing two 入 shapes, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```
- 주의: 약자 両·两 금지 — 정자 兩.

### 西 서녘 서 (U897F) — 우리 5급
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U897F_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U897F_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U897F_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 6획 · 구성 一+𠁤 · 회의
- **이미지를 못 읽으면 아래 글자 격자(楷書 西 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
······························
······························
······························
················██████········
···········██████████·········
········█████████·············
···········██···██············
···········██···██············
···········██···█·············
···········██··█████████······
···········██████████████·····
·····████████··██·····███·····
······██···██··██·····███·····
······██···██··██·····██······
······██···█····████··██······
·······██·██··········██······
·······██·█···········██······
·······██············███······
·······██·██████████·██·······
·······███████····█████·······
·······██··········████·······
···················███········
····················██········
······························
······························
······························
······························
······························
```

- **A컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, a round woven bird nest seen from the side with two short twigs sticking up from its rim
```
- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 西 written in bold semi-cursive (行書) brushwork, exactly 6 strokes: a top horizontal over a 囗-like frame with two short strokes inside, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```
- 주의: 四·酉와 혼동 주의.

### 歲 해 세 (U6B72) — 우리 5급
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U6B72_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U6B72_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U6B72_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 13획 · 구성 止+⿵戌𣥂 · 회의
- **이미지를 못 읽으면 아래 글자 격자(楷書 歲 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
······························
······························
··············██··············
··············███·············
··········█····██████·········
··········██···████···········
··········██···█··············
···········█···█████████······
········██████████············
······██████···██····███······
···············██████·██······
·······█····████████··········
·······███████··██···██·······
·······██·····██·█···██·······
·······██·██████·██·██········
·······██·████····█·██········
·······██···████··███·········
·······██·█·████···██·········
·······█·██·████··███·····█···
······██··█·███··██·██···██···
······█·····██·███···██··██···
·····██···███··█······█████···
····██···██············████···
········█···············███···
······························
······························
······························
······························
```

- **A컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, a long-handled battle axe standing upright with two bare footprints, one above and one below its blade
```
- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 歲 written in bold semi-cursive (行書) brushwork, exactly 13 strokes: 止 on top, 戌 frame with 少-like strokes inside, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```
- 주의: 약자 歳 금지 — 정자 歲.

### 爭 다툴 쟁 (U722D) — 우리 5급
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U722D_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U722D_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U722D_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 8획 · 구성 爫+⿻⿻コ一亅 · 회의
- **이미지를 못 읽으면 아래 글자 격자(楷書 爭 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
······························
·················█············
················████··········
··············█████···········
···········████·····███·······
··············█····███········
·········██···██···██·········
·········███··██··█···········
··········██·····█████········
·········██████████████·······
·········███··██····███·······
··············███··█████████··
········████████████████████··
····████████···█····██········
···············█····██········
···········███████████········
········█████████·············
···············██·············
···············██·············
···············██·············
··············███·············
············████··············
············████··············
·············███··············
··············█···············
······························
······························
······························
```

- **A컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, two hands, one from above and one from below, both gripping the same short stick and pulling
```
- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 爭 written in bold semi-cursive (行書) brushwork, exactly 8 strokes: 爫 on top, a 彐-like middle and a long hooked vertical, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```
- 주의: 약자 争 금지.

### 能 능할 능 (U80FD) — 우리 5급
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U80FD_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U80FD_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U80FD_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 10획 · 구성 䏍+𫧇 · 회의
- **이미지를 못 읽으면 아래 글자 격자(楷書 能 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
······························
······························
···············██·············
·········██····██·············
·········██····██···█·········
········███····██··███········
········██··█··██·███·········
·······██···██·████···········
······██··████·██·············
·····██████··█·██·····█·······
····████········█····███······
·····█····██····███████·······
·······██████····████·········
······██···██··██·············
······██···██···██············
······███████···█···██········
······██···██···█·████········
······██···██···███···········
······████·██···█········█····
······██···██···█·······██····
······█····██···█·······██····
·····██····██···██·····███····
·····██···███····█████████····
······█····██·····██████······
······························
······························
······························
······························
```

- **A컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, a bear sitting upright seen from the side, big head on the left, two paws raised on the right
```
- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 能 written in bold semi-cursive (行書) brushwork, exactly 10 strokes: 厶 over 月 on the left, two 匕 stacked on the right, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```
- 주의: 熊과 구별.

### 有 있을 유 (U6709) — 우리 5급
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U6709_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U6709_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U6709_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 6획 · 구성 𠂇+月 · 회의
- **이미지를 못 읽으면 아래 글자 격자(楷書 有 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
······························
··············███·············
··············███·············
··············██··············
··············██······████····
·············██████████████···
······██████████████··········
·····██████··██···············
············██················
············█····███··········
···········██████████·········
··········████·····██·········
·········██·██·····██·········
·········██·██████·██·········
········██··█████··██·········
·······██···█······██·········
·····███····█······██·········
····██······██████·██·········
···██·······█······██·········
···········██······██·········
···········██······██·········
···········██····█·██·········
···········█·····████·········
···········█······███·········
···················█··········
······························
······························
······························
```

- **A컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, a hand holding a thick cut of meat, the hand on top and the meat hanging below
```
- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 有 written in bold semi-cursive (行書) brushwork, exactly 6 strokes: 𠂇 (a slanted stroke and a horizontal) over 月, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```
- 주의: 右·友와 윗부분 같음.

### 口 입 구 (U53E3) — 우리 5급
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U53E3_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U53E3_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U53E3_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 3획 · 상형·지사
- **이미지를 못 읽으면 아래 글자 격자(楷書 口 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
······························
······························
······························
······························
······························
···················██·········
···············████████·······
·······████████████·████······
········███·········████······
········██··········███·······
········███·········██········
·········██·········██········
·········██········███········
·········██········██·········
·········██········██·········
·········██·······███·········
·········█████████████········
·········██████···············
·········██···················
······························
······························
······························
······························
······························
······························
······························
······························
······························
```

- **A컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, a pair of open lips drawn as a simple rounded square outline, nothing else
```
- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 口 written in bold semi-cursive (行書) brushwork, exactly 3 strokes: a square box, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```
- 주의: 囗과 구별 — 口는 작은 네모.

### 常 떳떳할 상 (U5E38) — 우리 5급
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U5E38_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U5E38_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U5E38_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 11획 · 구성 𫩠+巾 · 형성
- **이미지를 못 읽으면 아래 글자 격자(楷書 常 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
·············█················
·············███··············
··············██··███·········
·········██···██·████·········
·········███··█·███···········
··········██··█·······██······
·············█████████████····
······█████████·······████····
······██········███···███·····
·····██···██████████··········
·····██···██·····██···········
·····█·····█··████············
···········████···············
··············██··██··········
·············████████·········
·········███████···███········
·········██···██···██·········
·········██···██···██·········
·········██···██···██·········
·········██···██·████·········
·········█····██··███·········
··············██···█··········
··············██··············
··············█···············
··············█···············
······························
······························
······························
```

- **A컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, a tall banner on a pole, the cloth hanging straight down from a small crossbar at the top
```
- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 常 written in bold semi-cursive (行書) brushwork, exactly 11 strokes: 尚-like top (丷, 冖, 口) over 巾, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```
- 주의: 堂과 윗부분 같음.

### 工 장인 공 (U5DE5) — 우리 5급
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U5DE5_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U5DE5_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U5DE5_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 3획 · 상형·지사
- **이미지를 못 읽으면 아래 글자 격자(楷書 工 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
······························
······························
······························
······························
······························
················██████········
···········███████████········
········█████████·············
··············███·············
··············███·············
··············██··············
··············██··············
··············██··············
··············██··············
··············██··············
··············██··············
··············██··············
··············██····██████····
··········█████████████████···
····█████████████·····█████···
·····███······················
······························
······························
······························
······························
······························
······························
······························
```

- **A컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, a carpenter square tool: a flat top bar, a short vertical shaft and a wider flat bottom bar
```
- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 工 written in bold semi-cursive (行書) brushwork, exactly 3 strokes: a short top horizontal, a vertical and a long bottom horizontal, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```
- 주의: 土·干과 혼동 주의.

### 止 그칠 지 (U6B62) — 우리 5급
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U6B62_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U6B62_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U6B62_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 4획 · 상형·지사
- **이미지를 못 읽으면 아래 글자 격자(楷書 止 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
······························
······························
······························
···············███············
···············███············
················██············
················██············
················██············
················██············
················██············
················██····█·······
·········███····██·█████······
·········███····███████·······
··········██····██············
··········██····██············
··········██····██············
··········██····██············
··········██····██············
··········██····██············
··········██····██·····████···
··········██···█████████████··
·····███████████████████████··
·····█████····················
······························
······························
······························
······························
······························
```

- **A컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, a single bare footprint seen from above, toes pointing up, heel at the bottom
```
- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 止 written in bold semi-cursive (行書) brushwork, exactly 4 strokes: a vertical with a short stroke on its right, a short vertical on the left and a bottom horizontal, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```
- 주의: 正·步의 부품.

## 공통 규칙

1. A컷 = 사물, B컷 = 글자 붓글씨. 파일명은 내용과 일치. 2. B컷은 **참고 글자 이미지(네 저장소 `refs/<코드>_ref.png`)를 반드시 읽고/첨부하고** 왼쪽 楷書의 획 구조를 그대로(획 수·위치·길이), 오른쪽 行楷 정도의 붓 느낌으로. 참고 글자를 image-to-image 입력으로 쓸 수 있으면 그렇게(변형 약하게). **한국 정자(참고 글자 모양)** 로 — 약자 금지. 인쇄체 금지. 글자는 또렷하게. 3. 정사각형 1:1, 흰 종이, 한 사물/한 글자만, **배경 풍경·추가 요소·글씨 금지**. 4. A·B 같은 위치·크기. 5. 기존 파일 덮어쓰기 금지(`_v2`). 6. 실패작은 올리지 않는다. 7. README 표는 내용 기준으로. 8. 21회차 통과. 계속 틀리던 부수 글자(辵 攴 殳 告)의 B 는 Claude 가 만들었으니 더 그리지 말 것. **22회차부터는 5급 정규 글자 12자씩, 재작업은 최대 1회** — 토큰 아끼기.

공통 스타일 블록: Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject
