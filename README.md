본 시스템은 Google ADK(Agent Development Kit)와 Gemini 모델을 활용한 연구 논문 분석 멀티 에이전트 시스템이다.
논문 PDF를 입력하면 요약, 비판적 분석, 기술 질의응답, 인사이트 도출 기능을 제공한다.
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
1. coordinator_agent
2. summary_agent
3. qa_agent
4. critic_agent
5. insight_agent

## 적용된 에이전틱 디자인 패턴
1. Tool Use
2. Routing 
3. Multi-Agent 
4. Memory Management 
5. Exception Handling & Recovery 

## Setup
1. 저장소 클론
bash
git clone https://github.com/pes23/research-assistant-ADK.git
cd research-assistant-ADK

2. 가상환경 설치
bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

3. 환경변수 설정
cp .env.example .env
# .env 파일에 GEMINI_API_KEY 입력

4. PDF 논문 추가
# data/ 폴더에 분석할 PDF 파일 저장

5. 실행
python main.py --pdf data/your_paper.pdf

## Example Queries
- `summarize this paper`
- `critique this paper`
- `what is self-attention?`
- `future research directions?`
