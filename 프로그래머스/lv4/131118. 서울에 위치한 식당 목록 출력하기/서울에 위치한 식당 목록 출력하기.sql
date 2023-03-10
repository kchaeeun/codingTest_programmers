-- 코드를 입력하세요
SELECT I.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS, ROUND(AVG(R.REVIEW_SCORE),2) AS SCORE

# REST_INFO의 ID와 REST-REVIEW의 ID를 JOIN해서 사용
FROM REST_INFO I JOIN REST_REVIEW R
ON R.REST_ID = I.REST_ID

WHERE I.ADDRESS LIKE "서울%"

#REST_ID가 공통
GROUP BY R.REST_ID
ORDER BY SCORE DESC, I.FAVORITES DESC