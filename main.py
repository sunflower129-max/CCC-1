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