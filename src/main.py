import pandas as pd
import json
from pathlib import Path

CSV_file = Path(__file__).parent.parent/"data"/"scores.csv"
output_file = Path(__file__).parent.parent/"result.json"

def process():
    df = pd.read_csv(CSV_file)
    scores = df['score']

    grades = {
    "平均分数":round(float(scores.mean()),2),
    "最大值":int(scores.max()),
    "最小值":int(scores.min())
    }

    pass_df = df[df['score'] >= 60]
    pass_list = pass_df.to_dict('records')

    final_grades = {
        "统计数据":grades,
        "及格学生":pass_list
    }
    with open(output_file,'w',encoding='utf-8') as f:
        json.dump(final_grades,f,ensure_ascii=False,indent=4)
    print(f"处理完成,结果保存至{output_file}")

if __name__ == "__main__":
    process()