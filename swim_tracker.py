#아침 수영 마일리지 분석기 찐 최종 코드
records = []
#프로그램 켤 때 기존 파일 읽어오기 ('r' 모드) ---
try:
    file = open("swim_data.txt", "r", encoding="utf-8")
    for line in file:
        # 줄바꿈(\n)을 없애고 쉼표(,)를 기준으로 데이터를 쪼갭니다.
        # 예: "2026-06-11,06:00,1000" -> ['2026-06-11', '06:00', '1000']
        data = line.strip().split(",")

        # 쪼갠 데이터를 다시 딕셔너리로 조립해서 리스트에 복구합니다.
        recovered_record = {
            "date": data[0],
            "wake_time": data[1],
            "distance": int(data[2]) # 거리는 계산을 위해 다시 숫자로 변환
        }
        records.append(recovered_record)
    file.close()
except FileNotFoundError:
    # 맨 처음 실행해서 아직 텍스트 파일이 없을 때는 그냥 넘어갑니다.
    pass

while True:
    print("\n---아침 수영 마일리지 ---")
    print("1. 오늘 기록 입력하기")
    print("2. 주간 통계 확인하기")
    print("3. 프로그램 종료")

    choice = input("메뉴를 선택하세요 (1/2/3): ")

    if choice == '1':
        print("\n>> 기록 입력 화면입니다.")
        date = input("오늘 날짜를 입력하세요 (예: 2026-06-11): ")
        wake_time = input("오늘 기상 시간을 입력하세요 (예: 06:00): ")
        distance = int(input("오늘 수영한 거리를 입력하세요 (m): "))

        daily_record = {
            "date": date,
            "wake_time": wake_time,
            "distance": distance
        }
        records.append(daily_record)

        # 불러오기 쉽게 쉼표(,)로만 구분해서 저장합니다.
        file = open("swim_data.txt", "a", encoding="utf-8")
        file.write(f"{date},{wake_time},{distance}\n")
        file.close()

        print(f">> 기록 완료! 오늘 {wake_time}에 일어나서 {distance}m를 수영했습니다.")

    elif choice == '2':
        print("\n>> 주간 통계 화면입니다.")

        if len(records) == 0:
            print("아직 입력된 기록이 없습니다. 1번 메뉴에서 기록을 먼저 입력해주세요.")
        else:
            total_distance = 0
            for record in records:
                total_distance = total_distance + record["distance"]

            print("\n--- 이번 주 수영 통계 ---")
            print(f"* 기록된 날짜 수: {len(records)}일")
            print(f"* 누적 총 수영 거리: {total_distance}m")

            if total_distance >= 20000:
                print("* 🧜♂️ 누적 20,000m 달성! 엄청난 갓생 루틴을 증명하셨습니다!")
            elif total_distance >= 5000:
                print("* 이번 주 기준치 5,000m 돌파! 달콤한 에그타르트 하나 드시면서 푹 쉬세요!")
            else:
                print("* 꾸준한 아침 루틴! 내일 새벽 수영도 화이팅입니다.")

    elif choice == '3':
        print("\n프로그램을 종료합니다. 내일도 상쾌한 물살 가르시길 바랄게요!")
        break

    else:
        print("\n잘못된 입력입니다. 1, 2, 3 중에서 다시 선택해주세요.")
