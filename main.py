import os
import asyncio
from google.adk.runners import Runner
from google.genai import types
from google.adk.sessions import InMemorySessionService

from agents.coordinator import coordinator
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", type=str, default="data/attention.pdf", help="Path to the PDF paper")
    return parser.parse_args()

#BASE_DIR   = os.path.dirname(__file__)
#PDF_PATH   = os.path.join(BASE_DIR, "data", "attention.pdf")

APP_NAME   = "research_assistant"
USER_ID    = "user_01"
SESSION_ID = "session_main"


async def run_query(runner, text, prefix="Assistant", max_retries=3):
    content = types.Content(role="user", parts=[types.Part(text=text)])

    for attempt in range(max_retries):
        try:
            async for event in runner.run_async(
                user_id=USER_ID,
                session_id=SESSION_ID,
                new_message=content
            ):
                if not event.is_final_response():
                    continue
                if not event.content or not event.content.parts:
                    continue
                for part in event.content.parts:
                    if hasattr(part, "text") and part.text:
                        print(f"\n{prefix} > {part.text}\n")
            return

        except Exception as e:
            if "503" in str(e) or "UNAVAILABLE" in str(e):
                wait = 2 ** attempt       
                print(f"[RETRY {attempt+1}/{max_retries}] {wait}초 후 재시도...")
                await asyncio.sleep(wait)
            else:
                print(f"[ERROR] {e}")
                return

    print("[FALLBACK] 서버 응답 불가. 잠시 후 다시 시도해주세요.")


async def main():
    args = parse_args()
    PDF_PATH = args.pdf

    if not os.path.exists(PDF_PATH):
        print(f"[ERROR] PDF not found: {PDF_PATH}")
        return

    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

    runner = Runner(
        app_name=APP_NAME,
        agent=coordinator,
        session_service=session_service
    )

    print("Loading paper via agent...")
    await run_query(runner, f"load paper from {PDF_PATH}", prefix="INIT")

    print("=== Research Assistant READY ===")
    print("Try: summarize / critique / future research / exit\n")

    while True:
        query = input("You > ").strip()

        if not query:
            continue
        if query.lower() == "exit":
            print("Bye!")
            break                                 

        await run_query(runner, query)


if __name__ == "__main__":
    asyncio.run(main())
