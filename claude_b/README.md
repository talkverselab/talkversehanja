# claude_b — 정자 B컷 (Claude 렌더)

Claude 가 해서(楷書) 글꼴로 렌더한 **정자 B컷** 글자 이미지(속이 꽉 찬 먹). **획 구조는 이 이미지가 기준**이다.

## 배치
- `claude_b/U<코드>_B.jpg` — 한국형(kr). 예: `U706B_B.jpg` = 火
- `claude_b/jp/U<코드>_B.jpg` — 일본 신자체, kr 과 **다를 때만** (예: 學 → 学)
- `claude_b/cn/U<코드>_B.jpg` — 중국 간체, kr 과 **다를 때만** (예: 國 → 国)
- `<코드>` 는 항상 DB 의 한국형 글자 코드(U+hex). jp·cn 폴더 파일도 한국형 코드로 이름을 붙인다.
- 전체 목록·글꼴·크기: `MANIFEST.json` (`files`, 글꼴이 없어 못 만든 글자는 `skipped`)

## Raw URL
`https://raw.githubusercontent.com/talkverselab/talkversehanja/main/claude_b/<경로>`
예: `.../claude_b/U5B78_B.jpg`(學), `.../claude_b/jp/U5B78_B.jpg`(学), `.../claude_b/cn/U5B78_B.jpg`(学)

## Grok 규칙
- **모든 획을 그대로 유지**한다 — 획을 더하거나 빼거나 위치·길이를 바꾸지 말 것.
- 바꿔도 되는 것은 **획 끝의 붓 질감**(기필·수필의 먹 번짐, 붓끝 모양)뿐.

## 크기
- 2026-10-16 이전 957장: 1408px (BiauKai, 없는 글자는 Kaiti)
- 2026-10-18 추가분: 1024px (kr: BiauKai→Kaiti, cn: Kaiti→BiauKai, jp: BiauKai→Kaiti→YuMincho)
