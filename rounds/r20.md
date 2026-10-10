# Grok 작업 지시서 (이 파일과 refs/ 이미지는 이 저장소 안에 있음 — 이미지를 직접 열어 볼 것) — 20회차 (2026-10-10)

리뷰 페이지: https://talkverse.uk/hanja-review/ · 보기 쉬운 판: https://talkverse.uk/hanja-review/grok · 이 문서: https://talkverse.uk/hanja-review/GROK_NEXT.md?r=20 (캐시 피하려면 ?r=회차 를 붙여 읽을 것)

한 회차 = 재작업 + 새 글자 8자 안팎. 끝나면 커밋만 하면 된다(Claude 가 커밋을 감시해 검토하고 이 문서를 갱신한다).

## 0. 19회차 검토 결과

| 글자 | 판정 | 비고 |
|---|---|---|
| 不 | 통과 | B v2 不 정상 |
| 成 | 통과 | B v2 成 정상 |
| 疒 | 통과 | B v2 疒 정상 |
| 小 | 통과 | A v2 조약돌 셋 |
| 北 | 통과 | 北 읽힘 |
| 彳 | 통과 | 彳 정상 |
| 原 | 통과 | 原 정상 |
| 報 | **재작업** | B 뭉개짐 → 재작업 |
| 攴 | **재작업** | B 攴 아님 → 재작업 |
| 隹 | **재작업** | B 隹 아님 → 재작업 |
| 辵 | **재작업** | B v2 여전히 之 꼴 → 재작업 |
| 務 | **재작업** | B v2 약자 务 꼴 → 정자 務로 재작업 |
| 業 | **재작업** | B v3 아래가 月/用 — 業 아님 → 재작업 |

## 1. 재작업 6건 (새 파일명 `_v2`/`_v3`, 기존 파일 덮어쓰기 금지)

### 辵 쉬엄쉬엄 갈 착 (U8FB5) — B컷 다시
- 사유: 辵 는 之 가 아니다. 위에 彳(짧은 삐침 둘 + 세로), 아래 止(세로·짧은 가로·세로·긴 가로). 7획. refs/U8FB5_ref.png 를 열어 그대로.
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U8FB5_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U8FB5_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U8FB5_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 7획 · 상형·지사
- **이미지를 못 읽으면 아래 글자 격자(楷書 辵 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
······························
······························
················██············
················███···········
··············████············
············███···██··········
········█████····███··········
················███···········
·············████···██········
··········█████····████·······
·········█·······████·········
···············████···········
···········██████·············
·······██████··██·············
···············██·············
··········███··██··███········
··········███··███████········
··········██···██·············
·········████··██·············
········██··█████·············
·······██·····████············
······██········█████·········
·····██···········██████████··
···················██████·····
······························
······························
······························
······························
```

- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 辵 (a character component / radical, drawn alone and large) written in bold semi-cursive (行書) brushwork, exactly 7 strokes: 彳 on the top-left and 止 at the bottom, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```

### 務 힘쓸 무 (U52D9) — B컷 다시
- 사유: 정자 務(矛 + 攵 + 力) — 약자 务 금지. 11획. refs/U52D9_ref.png.
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U52D9_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U52D9_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U52D9_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 11획 · 구성 矛+⿱攵力 · 회의
- **이미지를 못 읽으면 아래 글자 격자(楷書 務 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
······························
······························
··················██··········
··················██··········
·········█████····██··········
······████████···██·███·······
···········██···███████·······
··········██····█···███·······
·········██····███··██········
·········██······████·········
··········█████···███·········
····███████··███·██·███·······
····███··██·██··███··██████···
········███···███·██··██████··
·······████··██···██·█········
·······██·█····████████·······
······██··█····████··██·······
·····██···█·····██···██·······
····██····█·····██···██·······
···█·····██····██····██·······
·······████····█····██········
·······████···█···████········
········██··██····████········
···················██·········
······························
······························
······························
······························
```

- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 務 written in bold semi-cursive (行書) brushwork, exactly 11 strokes: 矛 on the left, 攵 at top-right and 力 at bottom-right, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```

### 業 업 업 (U696D) — B컷 다시
- 사유: 業 13획: 위 业(점 둘·가로), 가운데 가로 둘 + 세로, 아래는 木 처럼 가로·삐침·파임. 아래에 月·用·國 같은 걸 붙이지 말 것. refs/U696D_ref.png.
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U696D_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U696D_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U696D_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 13획 · 구성 业+𦍎 · 회의
- **이미지를 못 읽으면 아래 글자 격자(楷書 業 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
······························
················██············
················███···········
············███·██···█········
·············██·██··███·······
·········██··██·██·██·········
··········██·██·███····██·····
··········█··██·██████████····
······██████████████··········
·····██████·██···██···········
············██··████··········
·············███████··········
··········███████·············
··············██████··········
···········██████·············
···············█████████······
·······██████████████·········
········███··█████············
············██·█·███··········
··········███··█··████········
·········███··██····█████·····
·······███····██·····██████···
······██······██··············
··············██··············
···············█··············
······························
······························
······························
```

- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 業 written in bold semi-cursive (行書) brushwork, exactly 13 strokes: a toothed top (业), a middle 羊-like section, and a bottom 木-like base, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```

### 報 갚을 보 (U5831) — B컷 다시
- 사유: 報 12획: 왼쪽 幸, 오른쪽 卩 위 又. refs/U5831_ref.png.
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U5831_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U5831_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U5831_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 12획 · 구성 幸+𠬝 · 회의
- **이미지를 못 읽으면 아래 글자 격자(楷書 報 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
······························
··········█···················
··········██··················
··········██··················
··········██·········██·······
··········██···██·██████······
··········████·████··███······
·······██████···██···██·······
··········██····██···██·······
··········██·██·██·███········
·········█████··██·███········
·····██████·██··██··█·········
···██████···██··██···██·······
········██·██···████████······
·········█·███··██···██·······
·········████···███··██·······
······█████·····█·██·██·······
··········█████·█··████·······
········████····█···██········
···██████·██····█··████·······
····██····██···█████·████·····
·········██····███····██████··
·········██····██·······███···
·········██·····█·············
··········█···················
······························
······························
······························
```

- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 報 written in bold semi-cursive (行書) brushwork, exactly 12 strokes: 幸 on the left, 𠬝 (卩 over 又) on the right, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```

### 攴 칠 복 (U6534) — B컷 다시
- 사유: 攴 4획: 위 卜, 아래 又. refs/U6534_ref.png.
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U6534_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U6534_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U6534_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 4획 · 상형·지사
- **이미지를 못 읽으면 아래 글자 격자(楷書 攴 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
······························
······························
·············███··············
··············███·············
··············██··············
··············██··············
··············██···██·········
··············███████·········
··············█████···········
··············██··············
··············██··············
··············██·█············
··············██████··········
·········██████··███··········
··········█······██···········
··········██····██············
···········███··██············
·············████·············
··············███·············
·············█████············
···········███··████··········
·········████·····█████·······
······████·········████████···
····················██████····
······························
······························
······························
······························
```

- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 攴 (a character component / radical, drawn alone and large) written in bold semi-cursive (行書) brushwork, exactly 4 strokes: 卜 on top and 又 below, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```

### 隹 새 추 (U96B9) — B컷 다시
- 사유: 隹 8획: 왼쪽 亻, 오른쪽 가로 넷과 세로, 위에 짧은 삐침. refs/U96B9_ref.png.
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U96B9_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U96B9_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U96B9_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 8획 · 상형·지사
- **이미지를 못 읽으면 아래 글자 격자(楷書 隹 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
······························
······························
··········█···················
··········███··███············
··········███···██············
··········██·····█············
·········██········████·······
·········██·····███████·······
········██··████████··········
·······███·····███············
·······███······██·██·········
······██·█······██████········
·····██··█··███████···········
····██···█······██············
···██····█······██·███········
·········█·····███████········
·········█··███████···········
········██······█·············
········██······█····█········
········██····██████████······
········███████████████·······
········██····················
········██····················
········█·····················
······························
······························
······························
······························
```

- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 隹 (a character component / radical, drawn alone and large) written in bold semi-cursive (行書) brushwork, exactly 8 strokes: a slanted head stroke, 亻 on the left and four horizontals on the right, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```

## 2. 새 글자 6자 (중요도 순, A·B 둘 다) — 파일명 `<병음>_A.jpg`/`_B.jpg`, B 는 참고 글자 첨부

### 川 내 천 (U5DDD) — 우리 5급
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U5DDD_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U5DDD_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U5DDD_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 3획 · 상형·지사
- **이미지를 못 읽으면 아래 글자 격자(楷書 川 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
······························
······························
····················██········
····················███·······
·····················██·······
········███···█······██·······
·········██···███····██·······
·········██····██····██·······
·········██····██····██·······
·········██····██····██·······
·········██····█·····██·······
·········██····█·····██·······
·········██····██····██·······
·········██····██····██·······
·········██····██····██·······
········██·····██····██·······
········██·····██····██·······
········██····███····██·······
·······██·····██·····██·······
······██·······█·····██·······
······█··············██·······
·····█···············██·······
·····················██·······
·····················██·······
······························
······························
······························
······························
```

- **A컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, three parallel wavy streams of water flowing downward, the middle one straight, the outer ones curving outward
```
- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 川 written in bold semi-cursive (行書) brushwork, exactly 3 strokes: three vertical strokes, the left one curving, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```
- 주의: 州와 혼동 주의.

### 囗 Box, Box Or Enclosure Radical (no. 31) (U56D7) — 뿌리 글자(부품) · 15자에 쓰임
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U56D7_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U56D7_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U56D7_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 3획 · 상형·지사
- **이미지를 못 읽으면 아래 글자 격자(楷書 囗 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
······························
······························
··················███·········
············███████████·······
······███████·······███·······
······██············███·······
·······█·············██·······
·······█·············██·······
·······█·············██·······
·······█·············██·······
·······█·············██·······
·······█·············██·······
·······█·············██·······
·······█·············██·······
·······█·············██·······
·······█·············██·······
······██·············██·······
······██·············██·······
······██·············██·······
······██···█████████·██·······
······█████████████████·······
······█·············███·······
····················██········
·····················█········
······························
······························
······························
······························
```

- **A컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, a square wooden fence seen from directly above, enclosing an empty plot of ground
```
- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 囗 (a character component / radical, drawn alone and large) written in bold semi-cursive (行書) brushwork, exactly 3 strokes: a square box, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```
- 주의: 口(입)와 구별 — 囗은 큰 네모.

### 告 고할 고 (U544A) — 우리 5급
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U544A_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U544A_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U544A_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 7획 · 구성 𠂒+口 · 회의
- **이미지를 못 읽으면 아래 글자 격자(楷書 告 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
······························
······························
···············███············
···············███············
···············██·············
···········█···██·············
···········██··██·············
···········██··██·████········
··········██···██████·········
··········███████·············
·········██····██·············
·········█·····██······███····
···············████████████···
···········████████████████···
····█████████·················
····████······················
················█████·········
··········████████████········
··········███······███········
···········██······██·········
···········██······██·········
···········██·····███·········
···········██████████·········
············███···············
······························
······························
······························
······························
```

- **A컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the head of an ox seen from the front with a small square wooden board tied over its mouth
```
- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 告 written in bold semi-cursive (行書) brushwork, exactly 7 strokes: 𠂒 (牛 without the lower tail) over 口, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```
- 주의: 牛 가로획 수 주의.

### 殳 창 수 (U6BB3) — 뿌리 글자(부품) · 15자에 쓰임
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U6BB3_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U6BB3_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U6BB3_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 4획 · 상형·지사
- **이미지를 못 읽으면 아래 글자 격자(楷書 殳 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
······························
······························
···············███············
···········████████···········
···········██···██············
···········██···██············
···········██···██············
···········██···██····█·······
··········███····███████······
··········██······█████·······
········███···················
·······██······████···········
···········█████████··········
··········███····██···········
················███···········
··········███···██············
············██·██·············
·············████·············
··············███·············
·············██·██············
···········███···███··········
········█████·····██████······
······████·········█████████··
·····················█████····
······························
······························
······························
······························
```

- **A컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, a hand holding up a short wooden club, the club at the top-right and the hand at the bottom, simple ink lines
```
- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 殳 (a character component / radical, drawn alone and large) written in bold semi-cursive (行書) brushwork, exactly 4 strokes: 几 on top and 又 below, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```
- 주의: 部首 갖은등글월문.

### 重 무거울 중 (U91CD) — 우리 5급
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U91CD_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U91CD_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U91CD_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 9획 · 상형·지사
- **이미지를 못 읽으면 아래 글자 격자(楷書 重 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
······························
······························
·················███··········
···············█████··········
············██████············
···········██·██··············
··············██·····█████····
············███████████████···
·····███████████··············
······██·······█···██·········
············███████████·······
·········████··█····███·······
·········██····███··██········
··········██·█████·██·········
··········██···█···██·········
···········█·███████··········
···········█████··············
···············█··············
··············██████··········
···········██████·············
···············█··············
···············█···█████······
·········████████████████·····
·······███████················
······························
······························
······························
······························
```

- **A컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, a person standing in side view bent under a large heavy sack tied to the back, feet on a ground line
```
- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 重 written in bold semi-cursive (行書) brushwork, exactly 9 strokes: a top slanted stroke, 里-like body with an extra horizontal, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```
- 주의: 里·量과 혼동 주의.

### 厶 I, Myself, Katakana Mu Radical (no. 28) (U53B6) — 뿌리 글자(부품) · 14자에 쓰임
- **참고 글자 이미지 — 네 저장소 안에 있음: `refs/U53B6_ref.png`** (talkverselab/talkversehanja, raw: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U53B6_ref.png · 사이트: https://raw.githubusercontent.com/talkverselab/talkversehanja/main/refs/U53B6_ref.png). 왼쪽 楷書 = 획 구조(그대로), 오른쪽 行楷 = 붓 느낌 · 2획 · 상형·지사
- **이미지를 못 읽으면 아래 글자 격자(楷書 厶 의 모양, █=먹)를 그대로 따라 그릴 것** — 획의 위치·길이·비율이 이 격자와 같아야 한다:

```
······························
······························
······························
······························
······························
······························
··············██··············
··············███·············
··············███·············
·············███··············
·············██···············
·············██···············
············██················
···········██·····█···········
···········██·····██··········
··········██·······███········
·········██········████·······
········██··········████······
·······██··········█████······
······███·███████████████·····
·····██████████·······███·····
·····████··············██·····
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
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, a single bent arm curling inward to clutch a small round object against the body, drawn in a few ink lines
```
- **B컷**

```
Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject, the single character 厶 (a character component / radical, drawn alone and large) written in bold semi-cursive (行書) brushwork, exactly 2 strokes: a short curved stroke turning into a dot, same position and size as the picture, hand-brushed with a real ink brush, visible dry-brush texture and slightly uneven ink edges, NOT a printed typeface
```
- 주의: 마늘모.

## 공통 규칙

1. A컷 = 사물, B컷 = 글자 붓글씨. 파일명은 내용과 일치. 2. B컷은 **참고 글자 이미지(네 저장소 `refs/<코드>_ref.png`)를 반드시 읽고/첨부하고** 왼쪽 楷書의 획 구조를 그대로(획 수·위치·길이), 오른쪽 行楷 정도의 붓 느낌으로. 참고 글자를 image-to-image 입력으로 쓸 수 있으면 그렇게(변형 약하게). **한국 정자(참고 글자 모양)** 로 — 약자 금지. 인쇄체 금지. 글자는 또렷하게. 3. 정사각형 1:1, 흰 종이, 한 사물/한 글자만, **배경 풍경·추가 요소·글씨 금지**. 4. A·B 같은 위치·크기. 5. 기존 파일 덮어쓰기 금지(`_v2`). 6. 실패작은 올리지 않는다. 7. README 표는 내용 기준으로. 8. 19회차: 새 6자 중 3자(報 攴 隹) B 실패, 재작업 6건 중 3건(辵 務 業) 또 실패. **복잡한 글자는 refs/ 이미지를 열어 보고 그대로 따라 그릴 것 — 안 보고 그리면 계속 틀린다.**

공통 스타일 블록: Traditional East Asian ink wash painting (sumi-e), pure black ink on plain white paper, no color, monochrome only, soft ink bleed and gradation, generous empty space, square 1:1 composition, centered subject
