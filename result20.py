import requests
from bs4 import BeautifulSoup
import pandas as pd

def crawl_vote(round_num=20):
    # 特殊情況：21回網址不一樣
    if round_num == 21:
        url = "https://toho-vote.info/result"
    else:
        url = f"https://toho-vote.info/results/{round_num}"
    
    print(f"正在爬取: {url}")
    res = requests.get(url)
    res.encoding = "utf-8"  # 頁面是 UTF-8
    soup = BeautifulSoup(res.text, "html.parser")

    # 找角色結果表格（不同回數可能結構略有不同）
    # 我觀察過第20回，角色排名在 <section id="chara"> 裡的 table
    section = soup.find("section", {"id": "chara"})
    table = section.find("table")

    data = []
    for row in table.find_all("tr")[1:]:  # 跳過表頭
        cols = row.find_all("td")
        if len(cols) < 4:
            continue
        rank = cols[0].text.strip()
        name = cols[1].text.strip()
        votes = cols[2].text.strip().replace(",", "")  # 票數（去掉逗號）
        rate = cols[3].text.strip()  # 得票率

        data.append({
            "回數": round_num,
            "名次": int(rank),
            "角色": name,
            "得票數": int(votes),
            "得票率": rate
        })

    df = pd.DataFrame(data)
    return df


if __name__ == "__main__":
    df20 = crawl_vote(20)
    print(df20.head())  # 預覽前幾筆
    df20.to_csv("touhou_vote20.csv", index=False, encoding="utf-8-sig")
    print("已存成 touhou_vote20.csv")
