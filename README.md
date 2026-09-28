# B2B 재고·매출·거래처 관리 API

기업의 상품, 거래처, 주문, 재고 및 운영 지표를 관리하기 위한 FastAPI 프로젝트입니다.

## 현재 구현 기능

- 상품 등록, 검색, 페이지네이션
- 거래처 등록 및 조회
- 재고 입출고 조정, 안전재고 이하 필터링
- 주문 생성과 재고 자동 차감
- 재고 부족 주문 차단
- 상품·거래처·주문·매출·부족재고 대시보드 집계
- FastAPI TestClient 기반 정상·실패 테스트
- FastAPI + PostgreSQL Docker Compose 실행

## 구조

```text
app/
├── core/config.py
├── database.py
├── models.py
├── schemas.py
├── repositories.py
├── services.py
├── routers/
└── main.py
```

`Router → Service → Repository → Database`로 책임을 분리했습니다.

## Docker 실행

```bash
docker compose up --build
```

- Swagger UI: http://localhost:8000/docs
- 상태 확인: http://localhost:8000/health

## 로컬 실행

기본값은 SQLite이므로 PostgreSQL 없이도 확인할 수 있습니다.

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 테스트

```bash
pytest -q
```

## 다음 개발 순서

1. CSV 거래 데이터 일괄 적재
2. JWT 로그인과 관리자·영업담당자 권한 분리
3. 거래처별 RFM 등급 및 이탈위험 점수
4. 상품별 주간 수요예측 API
5. 추천 발주량과 예상 품절일 계산
6. Streamlit 운영 대시보드 연결

