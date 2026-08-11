prompts = [
    {
        "title": "블로그 글 작성",
        "content": "친절하고 이해하기 쉬운 말투로 블로그 글을 작성해줘.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "이미지 생성 프롬프트",
        "content": "따뜻한 햇살이 비치는 카페에서 책을 읽는 사람의 모습을 그려줘.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "업무 자동화 아이디어",
        "content": "반복적인 업무를 자동화할 수 있는 방법을 단계별로 제안해줘.",
        "category": "자동화",
        "favorite": True
    },
    {
        "title": "영상 생성 프롬프트", 
        "content": "S1 | 0~2초 — PAIN POINT (공감 + 감정이입) &amp;gt; **넌 미래야! 엄마와 함께라면 어디라도 가요.** - **화면** : 엄마와 5살된 아들이 저녁노을이 지고 있는 풍경을 바라보는 뒷모습으로 엄마는 자녀의 어깨에, 자녀는 엄마의 허리를 감싸며 행복한 미소를 머금고 아이의 웃음소리가 자연의 바람소리와 친근하게 공감하는 장면 - **카메라** : 엄마가 자녀를 바라본다→ 자녀는 손뼉치면서 웃음소리를 내며 엄마를 바라볼때 엄마는 포옹한다 -&amp;gt;바람에 나무가 흔들리고 웃음소리와 함께  인공 얼굴 미디엄샷 (빠른 컷 전환) - **자막** : 흰색 굵은 글씨로 *엄마 참 좋아!...우리아들 웃음소리에 힘이 불끈 !* 글자가 타이핑되는 애니메이션. - **사운드** : 바람소리 + 아이의 웃음소리 → 잠시후에 새소리  S2 | 3~5초 — SOLUTION (반전 포인트) &amp;gt; **엄마가 지켜줄께 !**  - **화면** : 아이에게 거대한 폭풍이 밀려오고 엄마는 그 자녀에게로 달려가는 장면 - **카메라** : 푹풍에 아이는 손을 들어 막고 엄마는 폭풍 앞을 막아서는 슬로우 모션 - **자막** : 흰색 굵은 글씨로 *엄마가 지켜줄께 !* 글자가 아래에서 위로 올라가는 애니메이션. - **사운드** : 폭풍의 굉음 효과음 + 업비트 음악 시작 S3 | 6~8초 — RESULT (욕구 자극) &amp;gt; **Mom &amp; Child Band. 붙이는 순간 사랑은 시작되고.**  -**화면** : 엄마와 아이를 하트모양으로 감싸며 묶고 회오리처럼 돌면서 하늘로 올라갔다가 땅에 안전하게 착지하는 신나는 모습으로 웃는 장면으로 변화. s1,s2,s3 는 3개의 장면이다. 영상으로 만들어줘", 
        "category": "영상 생성", 
        "favorite": False 
    },  
]


def show_menu():
    print("\n===== 프롬프트 관리 프로그램 =====")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("0. 종료")


def add_prompt():
    print("\n===== 프롬프트 추가 =====")

    while True:
        title = input("제목: ").strip()

        if title:
            break

        print("제목은 비어 있을 수 없습니다.")

    while True:
        content = input("내용: ").strip()

        if content:
            break

        print("내용은 비어 있을 수 없습니다.")

    categories = [
        "텍스트 생성",
        "이미지 생성",
        "영상 생성",
        "페르소나",
        "자동화",
        "기타"
    ]

    print("\n카테고리를 선택하세요.")

    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    print(f"{len(categories) + 1}. 직접 입력")

    while True:
        category_choice = input("선택: ").strip()

        if category_choice.isdigit():
            number = int(category_choice)

            if 1 <= number <= len(categories):
                category = categories[number - 1]
                break

            if number == len(categories) + 1:
                category = input("카테고리 입력: ").strip()

                if category:
                    break

        print("올바른 카테고리를 선택해주세요.")

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)

    print("프롬프트가 추가되었습니다.")


def show_list():
    print("\n===== 프롬프트 목록 =====")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, 1):
        favorite = " ⭐" if prompt["favorite"] else ""

        print(
            f"{i}. {prompt['title']} "
            f"[{prompt['category']}]{favorite}"
        )


def show_by_category():
    print("\n===== 카테고리별 조회 =====")

    categories = [
        "텍스트 생성",
        "이미지 생성",
        "영상 생성",
        "페르소나",
        "자동화",
        "기타"
    ]

    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    choice = input("카테고리를 선택하세요: ").strip()

    if not choice.isdigit():
        print("잘못된 입력입니다.")
        return

    number = int(choice)

    if number < 1 or number > len(categories):
        print("잘못된 번호입니다.")
        return

    selected_category = categories[number - 1]

    found = False

    print(f"\n===== {selected_category} 프롬프트 =====")

    for i, prompt in enumerate(prompts, 1):
        if prompt["category"] == selected_category:
            favorite = " ⭐" if prompt["favorite"] else ""
            print(
                f"{i}. {prompt['title']}"
                f"{favorite}"
            )
            found = True

    if not found:
        print("해당 카테고리에 프롬프트가 없습니다.")


def search_prompt():
    print("\n===== 프롬프트 검색 =====")

    keyword = input("검색할 키워드를 입력하세요: ").strip()

    if not keyword:
        print("검색어를 입력해주세요.")
        return

    found = False

    for i, prompt in enumerate(prompts, 1):
        if (
            keyword.lower() in prompt["title"].lower()
            or keyword.lower() in prompt["content"].lower()
        ):
            favorite = " ⭐" if prompt["favorite"] else ""

            print(
                f"{i}. {prompt['title']} "
                f"[{prompt['category']}]{favorite}"
            )

            found = True

    if not found:
        print("검색 결과가 없습니다.")


def show_detail():
    print("\n===== 프롬프트 상세 보기 =====")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()

    choice = input("상세히 볼 프롬프트 번호를 입력하세요: ").strip()

    if not choice.isdigit():
        print("잘못된 번호입니다.")
        return

    number = int(choice)

    if number < 1 or number > len(prompts):
        print("존재하지 않는 프롬프트 번호입니다.")
        return

    prompt = prompts[number - 1]

    favorite = "⭐" if prompt["favorite"] else "없음"

    print("\n===== 프롬프트 상세 정보 =====")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {favorite}")
    print(f"내용: {prompt['content']}")


def toggle_favorite():
    print("\n===== 즐겨찾기 추가/해제 =====")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()

    choice = input("즐겨찾기를 변경할 프롬프트 번호를 입력하세요: ").strip()

    if not choice.isdigit():
        print("잘못된 번호입니다.")
        return

    number = int(choice)

    if number < 1 or number > len(prompts):
        print("존재하지 않는 프롬프트 번호입니다.")
        return

    prompt = prompts[number - 1]

    prompt["favorite"] = not prompt["favorite"]

    if prompt["favorite"]:
        print("즐겨찾기에 추가되었습니다.")
    else:
        print("즐겨찾기에서 해제되었습니다.")


def show_favorites():
    print("\n===== 즐겨찾기 목록 =====")

    found = False

    for i, prompt in enumerate(prompts, 1):
        if prompt["favorite"]:
            print(
                f"{i}. {prompt['title']} "
                f"[{prompt['category']}] ⭐"
            )
            found = True

    if not found:
        print("즐겨찾기한 프롬프트가 없습니다.")


def main():
    while True:
        show_menu()
        choice = input("메뉴를 선택하세요: ").strip()

        if choice == "0":
            print("프로그램을 종료합니다.")
            break

        elif choice == "1":
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
            show_favorites()

        else:
            print("잘못된 번호입니다. 다시 선택해주세요.")



if __name__ == "__main__":
    main()
