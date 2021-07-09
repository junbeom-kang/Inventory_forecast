# Inventory_forecast  재고량 예측
<br><br>
<img src = "https://user-images.githubusercontent.com/59498625/114296338-c5b39100-9ae5-11eb-8ab5-731123057d15.png" width="90%" height="90%">
<br><br>

# 시나리오
1. 자신의 매장 판매 데이터를 전처리 모델에 넣는다.
2. 전처리 결과를 학습하여 머신러닝 모델생성
3. x월 xx일 (요일) ‘날씨 좋음’ 예보 정보를 모델에 입력 및 현재 품목별 재고량 등록
4. 산출된 예측 값 바탕으로 추가적으로 품목 주문( 필요 재고량 -현재 재고량)<br>
<img src="https://user-images.githubusercontent.com/59498625/114297868-2050eb00-9aee-11eb-86bc-a06638b5eecf.png" width="50%" height="50%">
<br>

## 시행착오
<img src="https://user-images.githubusercontent.com/59498625/114298346-d9182980-9af0-11eb-8425-ca4d55b2bac2.png" width="70%" height="70%">

변수들에 영향을 받아 전체 매출을 예측하는 모델을 만드려고 했으나 오차율이 너무 커서 실패 (10%이상).<br><br>
실패이유 분석을 위해 각 품목마다 매출을 분석 후 변수들에 영향을 받지 않는 품목이 존재하는 것 파악.<br><br>
*ex)아메리카노는 사람들이 매일 좋아하지만 시원한 음료는 여름에 판매량이 많다.*<br><br>
따라서 품목을 나눠서 각 품목의 재고량 예측으로 선회 후 오차율을 잡았다.<br>
