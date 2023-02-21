-- 코드를 입력하세요
SELECT ROUND(AVG(DAILY_FEE), 0) AS AVERAGE_FEE      #의 DAILY_FEE의 평균을 AVERAGE_FEE라는 이름으로 지정한다.
FROM CAR_RENTAL_COMPANY_CAR     #테이블 이름으로 부터
WHERE CAR_TYPE = 'SUV';         #CAR_TYPE이 'SUV'인