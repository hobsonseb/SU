import argparse
import json
from datetime import datetime
from urllib.parse import quote


# 키 없이 사용할 여행지 데이터
TRAVEL_SPOTS = [
    {
        "name": "강릉",
        "region": "강원도",
        "themes": ["바다", "힐링", "카페", "맛집", "자연"],
        "reason": "동해 바다와 감성 카페, 맛집을 함께 즐기기 좋은 여행지입니다.",
        "places": ["안목해변", "경포대", "주문진", "초당순두부거리"]
    },
    {
        "name": "속초",
        "region": "강원도",
        "themes": ["바다", "시장", "맛집", "자연", "힐링"],
        "reason": "바다, 설악산, 시장 먹거리를 한 번에 즐길 수 있습니다.",
        "places": ["속초해수욕장", "속초중앙시장", "영금정", "설악산"]
    },
    {
        "name": "부산",
        "region": "부산광역시",
        "themes": ["바다", "도시", "맛집", "야경", "카페"],
        "reason": "바다와 도시 분위기를 동시에 느낄 수 있는 대표 여행지입니다.",
        "places": ["해운대", "광안리", "감천문화마을", "자갈치시장"]
    },
    {
        "name": "전주",
        "region": "전라북도",
        "themes": ["한옥", "맛집", "역사", "문화", "데이트"],
        "reason": "한옥마을과 전통 음식이 유명해 문화 여행에 좋습니다.",
        "places": ["전주한옥마을", "경기전", "남부시장", "전동성당"]
    },
    {
        "name": "경주",
        "region": "경상북도",
        "themes": ["역사", "문화", "산책", "데이트", "가족"],
        "reason": "신라 역사 유적과 야경 명소가 많아 조용한 여행에 좋습니다.",
        "places": ["첨성대", "동궁과 월지", "불국사", "황리단길"]
    },
    {
        "name": "여수",
        "region": "전라남도",
        "themes": ["바다", "야경", "맛집", "힐링", "데이트"],
        "reason": "밤바다와 해산물, 낭만적인 분위기로 유명합니다.",
        "places": ["여수밤바다", "오동도", "돌산대교", "낭만포차거리"]
    },
    {
        "name": "제주",
        "region": "제주특별자치도",
        "themes": ["자연", "바다", "힐링", "카페", "사진"],
        "reason": "자연 풍경, 바다, 감성 카페를 모두 즐길 수 있는 대표 여행지입니다.",
        "places": ["성산일출봉", "협재해수욕장", "우도", "애월카페거리"]
    },
    {
        "name": "서울",
        "region": "서울특별시",
        "themes": ["도시", "쇼핑", "맛집", "문화", "야경"],
        "reason": "교통이 편하고 쇼핑, 전시, 맛집 탐방에 적합합니다.",
        "places": ["경복궁", "홍대", "성수동", "남산서울타워"]
    },
    {
        "name": "가평",
        "region": "경기도",
        "themes": ["자연", "힐링", "가족", "데이트", "산책"],
        "reason": "서울 근교에서 자연과 여유를 느끼기 좋은 여행지입니다.",
        "places": ["남이섬", "아침고요수목원", "자라섬", "청평호"]
    },
    {
        "name": "통영",
        "region": "경상남도",
        "themes": ["바다", "섬", "맛집", "힐링", "사진"],
        "reason": "아름다운 바다 풍경과 섬 여행을 즐기기 좋습니다.",
        "places": ["동피랑마을", "통영케이블카", "중앙시장", "소매물도"]
    }
]


def score_spot(spot, user_keywords):
    """사용자가 입력한 키워드와 여행지 테마가 얼마나 맞는지 점수 계산"""
    score = 0
    for keyword in user_keywords:
        for theme in spot["themes"]:
            if keyword in theme or theme in keyword:
                score += 1
    return score


def recommend_trips(user_input, count):
    """키워드 기반으로 여행지 추천"""
    user_keywords = user_input.split()

    scored = []
    for spot in TRAVEL_SPOTS:
        score = score_spot(spot, user_keywords)
        scored.append((score, spot))

    # 점수가 높은 순서대로 정렬
    scored.sort(key=lambda x: x[0], reverse=True)

    # 점수가 모두 0이면 기본 추천
    results = [spot for score, spot in scored[:count]]

    return results


def make_map_url(place_name):
    """API 키 없이 사용할 수 있는 카카오맵 검색 URL 생성"""
    return f"https://map.kakao.com/?q={quote(place_name)}"


def save_result(data):
    """추천 결과를 JSON 파일로 저장"""
    filename = f"travel_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return filename


def main():
    parser = argparse.ArgumentParser(description="API 키 없이 사용하는 국내 여행지 추천 프로그램")
    parser.add_argument("--theme", type=str, help="원하는 여행 스타일 예: 바다 힐링 맛집")
    parser.add_argument("--count", type=int, default=3, help="추천 개수")
    args = parser.parse_args()

    if args.theme:
        user_input = args.theme
    else:
        user_input = input("어떤 여행을 원해? 예: 바다 힐링 맛집 자연 > ")

    recommendations = recommend_trips(user_input, args.count)

    result_data = {
        "user_input": user_input,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "recommendations": []
    }

    print("\n국내 여행지 추천 결과")
    print("=" * 40)

    for idx, spot in enumerate(recommendations, start=1):
        print(f"\n{idx}. {spot['name']} ({spot['region']})")
        print(f"추천 이유: {spot['reason']}")
        print("추천 장소:")

        place_infos = []

        for place in spot["places"]:
            map_url = make_map_url(place)
            print(f"  - {place}")
            print(f"    지도: {map_url}")

            place_infos.append({
                "name": place,
                "map_url": map_url
            })

        result_data["recommendations"].append({
            "name": spot["name"],
            "region": spot["region"],
            "reason": spot["reason"],
            "places": place_infos
        })

    filename = save_result(result_data)

    print("\n" + "=" * 40)
    print(f"결과가 저장되었습니다: {filename}")


if __name__ == "__main__":
    main()