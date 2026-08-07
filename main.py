<<<<<<< HEAD
# 기본 데이터 (최소 3개)
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 전문 블로거입니다...",
        "category": "텍스트 생성",
        "favorite": True
    },
    # 추가로 2개 더 작성하세요!
]
# 1. 프롬프트를 저장할 바구니(리스트)를 먼저 만듭니다.
prompts = []

# 2. '추가하기' 기능을 만듭니다. (에러 1 해결)
def add_prompt():
    print("\n=== 프롬프트 추가 ===")
    title = input("제목: ")
    content = input("내용: ")
    category = input("카테고리: ")
    
    # 입력받은 내용을 딕셔너리 형태로 저장합니다.
    new_data = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }
    prompts.append(new_data)
    print("성공적으로 추가되었습니다!")

# 3. '목록 보기' 기능을 만듭니다. (에러 2 해결)
def show_list():
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("저장된 프롬프트가 없습니다.")
    else:
        for i, p in enumerate(prompts, 1):
            print(f"{i}. [{p['category']}] {p['title']}")

# --- 이 아래는 이미 작성하신 show_menu와 main 함수가 오면 됩니다 ---
=======
# 기본 데이터 (3개)
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 전문 블로거입니다. 주어진 주제로 SEO에 최적화된 블로그 글을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "코드 리뷰어",
        "content": "당신은 시니어 개발자입니다. 아래 코드를 리뷰하고 개선점을 알려주세요.",
        "category": "코딩",
        "favorite": False
    },
    {
        "title": "영어 번역가",
        "content": "당신은 전문 번역가입니다. 아래 한국어 문장을 자연스러운 영어로 번역해주세요.",
        "category": "번역",
        "favorite": True
    },
]

# ── 메뉴 출력 ──────────────────────────────────────
>>>>>>> feature/list-view
def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")
    return input("선택: ")

<<<<<<< HEAD
# 메인 루프
def main():
    while True:
        choice = show_menu()
        if choice == '1':
            add_prompt()
        elif choice == '2':
            show_list()
        # ... 나머지 조건문 작성
=======
# ── 1번: 프롬프트 추가 ─────────────────────────────
def add_prompt():
    print("\n--- 프롬프트 추가 ---")
    title    = input("제목: ")
    content  = input("내용: ")
    category = input("카테고리: ")
    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    })
    print("✅ 추가 완료!")

# ── 2번: 전체 목록 ─────────────────────────────────
def show_list():
    print("\n--- 프롬프트 목록 ---")
    if len(prompts) == 0:
        print("저장된 프롬프트가 없습니다.")
        return
    for i, p in enumerate(prompts):
        star = "⭐" if p["favorite"] else "  "
        print(f"{i+1}. {star} [{p['category']}] {p['title']}")

# ── 3번: 카테고리별 조회 ───────────────────────────
def show_by_category():
    print("\n--- 카테고리별 조회 ---")

    # 중복 없이 카테고리 목록 추출
    categories = []
    for p in prompts:
        if p["category"] not in categories:
            categories.append(p["category"])

    # 카테고리 목록 출력
    for i, c in enumerate(categories):
        print(f"{i+1}. {c}")

    choice = input("조회할 카테고리 번호: ")

    if choice.isdigit() and 1 <= int(choice) <= len(categories):
        selected = categories[int(choice) - 1]
        print(f"\n[{selected}] 프롬프트 목록:")
        for p in prompts:
            if p["category"] == selected:
                star = "⭐" if p["favorite"] else "  "
                print(f"  {star} {p['title']}")
    else:
        print("잘못된 입력입니다.")

# ── 4번: 검색 ──────────────────────────────────────
def search_prompt():
    print("\n--- 프롬프트 검색 ---")
    keyword = input("검색어: ")

    results = []
    for p in prompts:
        if keyword in p["title"] or keyword in p["content"]:
            results.append(p)

    if len(results) == 0:
        print("검색 결과가 없습니다.")
    else:
        print(f"\n🔍 '{keyword}' 검색 결과: {len(results)}개")
        for i, p in enumerate(results):
            star = "⭐" if p["favorite"] else "  "
            print(f"{i+1}. {star} [{p['category']}] {p['title']}")

# ── 5번: 상세 보기 ─────────────────────────────────
def show_detail():
    print("\n--- 프롬프트 상세 보기 ---")
    show_list()

    if len(prompts) == 0:
        return

    choice = input("상세 볼 번호: ")

    if choice.isdigit() and 1 <= int(choice) <= len(prompts):
        p = prompts[int(choice) - 1]
        star = "⭐" if p["favorite"] else "없음"
        print("\n" + "="*30)
        print(f"제목     : {p['title']}")
        print(f"카테고리 : {p['category']}")
        print(f"즐겨찾기 : {star}")
        print(f"내용     :\n{p['content']}")
        print("="*30)
    else:
        print("잘못된 입력입니다.")

# ── 6번: 즐겨찾기 관리 (토글) ─────────────────────
def manage_favorite():
    print("\n--- 즐겨찾기 관리 ---")
    show_list()

    if len(prompts) == 0:
        return

    choice = input("즐겨찾기 추가/해제할 번호: ")

    if choice.isdigit() and 1 <= int(choice) <= len(prompts):
        p = prompts[int(choice) - 1]
        p["favorite"] = not p["favorite"]   # True↔False 토글
        status = "⭐ 추가" if p["favorite"] else "❌ 해제"
        print(f"'{p['title']}' 즐겨찾기 {status} 완료!")
    else:
        print("잘못된 입력입니다.")

# ── 7번: 즐겨찾기 목록 ────────────────────────────
def show_favorites():
    print("\n--- 즐겨찾기 목록 ---")

    favorites = []
    for p in prompts:
        if p["favorite"]:
            favorites.append(p)

    if len(favorites) == 0:
        print("즐겨찾기가 없습니다.")
    else:
        print(f"총 {len(favorites)}개")
        for i, p in enumerate(favorites):
            print(f"{i+1}. ⭐ [{p['category']}] {p['title']}")

# ── 메인 루프 ──────────────────────────────────────
def main():
    while True:
        choice = show_menu()
        if   choice == '1':
            add_prompt()
        elif choice == '2':
            show_list()
        elif choice == '3':
            show_by_category()
        elif choice == '4':
            search_prompt()
        elif choice == '5':
            show_detail()
        elif choice == '6':
            manage_favorite()
        elif choice == '7':
            show_favorites()
>>>>>>> feature/list-view
        elif choice == '0':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__":
<<<<<<< HEAD
    main()
    def show_list():
        print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("저장된 프롬프트가 없습니다.")
    else:
        for i, p in enumerate(prompts, 1):
            star = "⭐" if p["favorite"] else ""
            print(f"{i}. [{p['category']}] {p['title']} {star}")
=======
    main()
>>>>>>> feature/list-view
