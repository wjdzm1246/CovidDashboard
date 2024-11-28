# Corona Dashboard

Corona Dashboard는 **Dash**와 **Plotly**를 활용하여 COVID-19 데이터를 시각화하는 웹 애플리케이션입니다. 국가별 및 글로벌 데이터를 다양한 그래프로 제공하며, 사용자가 데이터를 손쉽게 탐색할 수 있도록 설계되었습니다.

## 주요 기능

- **버블 지도**: 국가별 확진자 수를 시각적으로 표현
- **막대 그래프**: 전 세계의 확진, 사망, 회복 데이터를 통계적으로 표시
- **라인 그래프**: 시간에 따른 특정 국가의 데이터를 추적 가능
- **데이터 테이블**: 국가별 상세 통계 제공
- **드롭다운 메뉴**: 특정 국가를 선택하여 그래프 필터링

---

## 설치 및 실행

### 요구 사항
- Python 3.7 이상
- Pandas
- Dash
- `pip` 최신 버전

### 설치 방법
1. 이 저장소를 클론합니다:
   ```bash
   git clone https://github.com/wjdzm1246/CovidDashboard.git
   cd CovidDashboard# CovidDashboard
2. 가상환경생성 & 활성:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
3. Pandas와 Dash 설치:
   ```bash
   pip install pandas
   pip install dash
4. 앱 실행:
   python main.py
5. 브라우저 실행 (로컬에서 실행 or 웹서버(ec2)  이용-main.py 구현에따라달라짐)
