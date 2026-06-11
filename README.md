본 시스템은 Google ADK와 Gemini 모델을 활용한 연구 논문 분석 멀티 에이전트 시스템이다.
논문 PDF를 입력하면 요약, 비판, 질의응답, 인사이트 도출 기능을 제공한다.

개발 프레임워크: Google ADK (Google Gemini API 연동) 

## Project Structure
research-assistant-ADK/
├── agents/
│   ├── coordinator.py
│   ├── summary_agent.py
│   ├── critic_agent.py
│   ├── qa_agent.py
│   └── insight_agent.py
├── tools/
│   ├── pdf_tools.py
│   ├── chunk_tools.py
│   ├── cache_tools.py
│   └── paper_tools.py
├── data/          # PDF 논문 직접 추가 필요
├── cache/         # 자동 생성
├── main.py
├── config.py
├── .env.example
├── requirements.txt
└── README.md

## 에이전트 구성 및 역할 
1. coordinator_agent: 전체 시스템의 진입점이자 라우터 역할을 담당한다.
2. summary_agent: 논문의 핵심 내용을 구조화된 형태로 요약한다.
3. qa_agent: 논문 내용을 기반으로 기술적인 질문에 답변한다. 
4. critic_agent: 논문을 비판적으로 검토하는 리뷰어 역할을 한다. 
5. insight_agent: 논문의 향후 연구 방향, 응용 가능성을 도출한다. 

## 적용된 에이전틱 디자인 패턴
1. Tool Use: 에이전트가 런타임에 직접 툴을 호출한다. 
2. Routing: 사용자 의도에 따라 적합한 에이전트로 요청을 분기한다. 
3. Multi-Agent: 독립된 5개의 에이전트가 상호작용한다.
4. Memory Management: InMemorySessionService 사용
5. Exception Handling & Recovery: API 호출 실패 시 retry, exponential backoff. 재시도 성공 시 정상 응답하며 최대 횟수 초과 시 Fallback 메시지를 출력한다.

## Setup
1. 가상환경 & 필수 라이브러리 설치
\```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

3. 환경변수 설정
cp .env.example .env
# .env 파일에 GEMINI_API_KEY 입력
\```

4. PDF 논문 추가
# data/ 폴더에 분석할 PDF 파일 저장

5. 실행
python main.py --pdf data/your_paper.pdf

## Example Queries
- `summarize this paper`
- `critique this paper`
- `what is self-attention?`
- `future research directions?`
