# 국내 여행지 추천 CLI

사용자가 원하는 여행 테마를 입력하면 국내 여행지를 추천해주는 파이썬 CLI 프로그램입니다.

## 기능

- 여행 테마 기반 추천
- 추천 이유 출력
- 카카오맵 검색 링크 제공
- 추천 결과 JSON 파일 저장

## 실행 방법

```bash
python main.py
```

또는

```bash
python main.py --theme "바다" --count 3
```

## 사용 기술

- Python
- argparse
- JSON
- Kakao Map 검색 링크

## 파일 구조

```text
travel/
├─ main.py
├─ README.md
├─ requirements.txt
└─ .gitignore
```