Multi-agent system for research paper analysis using Google ADK.

## Patterns Implemented
- Tool Use (Ch.5)
- Routing (Ch.2)
- Multi-Agent (Ch.7)
- Memory Management (Ch.8)
- Exception Handling & Recovery (Ch.12)

## Project Structure
\```
smart-paper-assistant/
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
├── app.py
├── config.py
├── .env.example
├── requirements.txt
└── README.md
\```

## Setup

1. 저장소 클론
\```bash
git clone https://github.com/your-id/research-assistant.git
cd research-assistant
\```

2. 가상환경 설치
\```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
\```

3. 환경변수 설정
\```bash
cp .env.example .env
# .env 파일에 GEMINI_API_KEY 입력
\```

4. PDF 논문 추가
\```bash
# data/ 폴더에 분석할 PDF 파일 저장
\```

5. 실행
\```bash
python app.py --pdf data/your_paper.pdf
\```

## Example Queries
- `summarize this paper`
- `critique this paper`
- `what is self-attention?`
- `future research directions?`
