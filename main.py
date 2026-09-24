# main.py

CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

prompts = [
    {
        "title": "블로그 글 초안 작성",
        "content": "너는 전문 블로그 작가야. 주제에 맞춰 도입, 본문, 결론 구조로 글을 작성해줘.",
        "category": "텍스트 생성",
        "favorite": False,
    },
    {
        "title": "제품 홍보 이미지 프롬프트",
        "content": "깔끔한 흰색 배경, 고급스러운 조명, 제품 중심 구도, 광고 사진 스타일",
        "category": "이미지 생성",
        "favorite": True,
    },
    {
        "title": "친절한 학습 튜터 페르소나",
        "content": "너는 초보자를 위한 친절한 튜터야. 어려운 개념을 쉬운 예시로 단계별 설명해줘.",
        "category": "페르소나",
        "favorite": False,
    },
]


def show_menu():
    print("\n====== 프롬프트 관리 프로그램 ======")
    print("1. 프롬프트 추가")
    print("2. 전체 목록 보기")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 추가/해제")
    print("7. 즐겨찾기 목록 보기")
    print("0. 종료")
    print("===================================")


def input_not_empty(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("입력값이 비어 있습니다. 다시 입력해주세요.")


def select_category():
    print("\n카테고리를 선택하세요.")
    for i, category in enumerate(CATEGORIES, start=1):
        print(f"{i}. {category}")
    print("0. 직접 입력")

    while True:
        choice = input("번호 선택: ").strip()

        if choice == "0":
            return input_not_empty("직접 입력할 카테고리: ")

        if choice.isdigit():
            index = int(choice)
            if 1 <= index <= len(CATEGORIES):
                return CATEGORIES[index - 1]

        print("잘못된 입력입니다. 다시 선택해주세요.")


def add_prompt():
    print("\n[프롬프트 추가]")
    title = input_not_empty("제목: ")
    content = input_not_empty("내용: ")
    category = select_category()

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
    }

    prompts.append(new_prompt)
    print("프롬프트가 추가되었습니다.")


def print_prompt_summary(prompt, index):
    star = "⭐" if prompt["favorite"] else ""
    print(f"{index}. [{prompt['category']}] {prompt['title']} {star}")


def show_list():
    print("\n[전체 프롬프트 목록]")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, start=1):
        print_prompt_summary(prompt, i)


def show_by_category():
    print("\n[카테고리별 조회]")
    category = select_category()

    filtered_prompts = [
        prompt for prompt in prompts
        if prompt["category"] == category
    ]

    if not filtered_prompts:
        print(f"'{category}' 카테고리에 등록된 프롬프트가 없습니다.")
        return

    print(f"\n[{category} 카테고리 목록]")
    for i, prompt in enumerate(filtered_prompts, start=1):
        print_prompt_summary(prompt, i)


def search_prompt():
    print("\n[프롬프트 검색]")
    keyword = input_not_empty("검색어 입력: ").lower()

    results = []

    for index, prompt in enumerate(prompts, start=1):
        title = prompt["title"].lower()
        content = prompt["content"].lower()

        if keyword in title or keyword in content:
            results.append((index, prompt))

    if not results:
        print("검색 결과가 없습니다.")
        return

    print("\n[검색 결과]")
    for index, prompt in results:
        print_prompt_summary(prompt, index)


def get_prompt_by_number():
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return None, None

    show_list()

    choice = input("프롬프트 번호 입력: ").strip()

    if not choice.isdigit():
        print("숫자를 입력해주세요.")
        return None, None

    index = int(choice)

    if index < 1 or index > len(prompts):
        print("잘못된 번호입니다.")
        return None, None

    return index, prompts[index - 1]


def show_detail():
    print("\n[프롬프트 상세 보기]")
    index, prompt = get_prompt_by_number()

    if prompt is None:
        return

    star = "⭐" if prompt["favorite"] else "없음"

    print("\n====== 상세 정보 ======")
    print(f"번호: {index}")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {star}")
    print("내용:")
    print(prompt["content"])
    print("======================")


def toggle_favorite():
    print("\n[즐겨찾기 추가/해제]")
    index, prompt = get_prompt_by_number()

    if prompt is None:
        return

    prompt["favorite"] = not prompt["favorite"]

    if prompt["favorite"]:
        print(f"'{prompt['title']}' 프롬프트가 즐겨찾기에 추가되었습니다.")
    else:
        print(f"'{prompt['title']}' 프롬프트가 즐겨찾기에서 해제되었습니다.")


def show_favorites():
    print("\n[즐겨찾기 목록]")

    favorite_prompts = [
        (index, prompt)
        for index, prompt in enumerate(prompts, start=1)
        if prompt["favorite"]
    ]

    if not favorite_prompts:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return

    for index, prompt in favorite_prompts:
        print_prompt_summary(prompt, index)


def main():
    while True:
        show_menu()
        choice = input("메뉴 번호를 선택하세요: ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            show_favorites()
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 메뉴 번호입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()