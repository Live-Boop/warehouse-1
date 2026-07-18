import os
from pathlib import Path
import dashscope

dashscope.api_key = os.getenv("DASHSCOPE_KEY")
QUESTION_FILE = Path(__file__).parent.parent / "question.txt"
ANSWER_FILE = Path(__file__).parent.parent / "answer.txt"

def ask_llm(question):
    res = dashscope.Generation.call(model="qwen-turbo", messages=[{"role":"user","content":question}])
    return res.output.text if res.status_code==200 else "请求异常"

if __name__ == "__main__":
    question = QUESTION_FILE.read_text(encoding="utf-8")
    answer = ask_llm(question)
    ANSWER_FILE.write_text(answer, encoding="utf-8")