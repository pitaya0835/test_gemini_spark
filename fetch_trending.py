import requests
import datetime
import sys

def fetch_hf_trends():
    # ⭕ 正しいソートパラメータは `trendingScore` です
    url = "https://huggingface.co/api/models?sort=trendingScore&limit=10"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # ここでエラーを検知できるようになります
        models = response.json()
    except Exception as e:
        print(f"データの取得に失敗しました: {e}")
        sys.exit(1) 

    today = datetime.date.today().strftime("%Y-%m-%d")
    
    output = f"# Hugging Face トレンドモデル Top 10 ({today})\n\n"
    output += "毎日正午に自動更新されます。\n\n"
    output += "| 順位 | モデル名 | リンク | いいね数 (Likes) |\n"
    output += "| :---: | :--- | :---: | :---: |\n"
    
    for i, model in enumerate(models, 1):
        model_id = model.get("id", "Unknown")
        likes = model.get("likes", 0)
        url_link = f"https://huggingface.co/{model_id}"
        output += f"| {i} | **{model_id}** | [リンク]({url_link}) | {likes} |\n"
        
    with open("trending.md", "w", encoding="utf-8") as f:
        f.write(output)
    print("trending.md の作成が完了しました。")

if __name__ == "__main__":
    fetch_hf_trends()
