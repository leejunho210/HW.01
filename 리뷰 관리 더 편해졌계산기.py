from datetime import datetime, timedelta


def get_review_counts(review_dates, start_date, end_date):
    # 날짜 문자열을 datetime 객체로 변환하는 함수
    def parse_date(date_str):
        return datetime.strptime(date_str, '%Y-%m-%d')

    # 입력된 날짜들을 datetime 객체로 변환
    try:
        review_dates = [parse_date(date) for date in review_dates]
        start_date = parse_date(start_date)
        end_date = parse_date(end_date)
    except ValueError as e:
        print("잘못된 날짜 형식이 입력되었습니다. 날짜 형식은 YYYY-MM-DD이어야 합니다.")
        return

    # 결과를 저장할 리스트
    review_counts = []

    # 2주 간격으로 리뷰 수를 계산
    current_start = start_date
    while current_start < end_date:
        current_end = current_start + timedelta(days=14)
        count = sum(current_start <= review_date < current_end for review_date in review_dates)
        review_counts.append((current_start.strftime('%Y-%m-%d'), current_end.strftime('%Y-%m-%d'), count))
        current_start = current_end

    return review_counts


# 사용자 입력 함수
def input_dates():
    review_dates = input("리뷰 날짜를 입력하세요 (YYYY-MM-DD 형식, 쉼표로 구분): ").split(',')
    start_date = input("시작 날짜를 입력하세요 (YYYY-MM-DD 형식): ")
    end_date = input("끝 날짜를 입력하세요 (YYYY-MM-DD 형식): ")
    return review_dates, start_date, end_date


# 메인 함수
def main():
    review_dates, start_date, end_date = input_dates()
    review_counts = get_review_counts(review_dates, start_date, end_date)
    if review_counts:
        print("2주 간격 리뷰 수:")
        for period_start, period_end, count in review_counts:
            print(f"{period_start} ~ {period_end}: {count}개")


if __name__ == "__main__":
    main()