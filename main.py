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

# 메인 루프
def main():
    while True:
        choice = show_menu()
        if choice == '1':
            add_prompt()
        elif choice == '2':
            show_list()
        # ... 나머지 조건문 작성
        elif choice == '0':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()
    def show_list():
        print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("저장된 프롬프트가 없습니다.")
    else:
        for i, p in enumerate(prompts, 1):
            star = "⭐" if p["favorite"] else ""
            print(f"{i}. [{p['category']}] {p['title']} {star}")