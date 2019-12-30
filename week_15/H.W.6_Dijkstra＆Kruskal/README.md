# Content

# Notes

- graph：有起點、終點、cost
- `addEdge`：新增edge，加上權重
    > idea：使用dict紀錄
    - u：起點
    - v：終點
    - w：權重
- 測資皆為正整數

Dijkstra先建一個權重的matrix（index由由0開始，為nxn矩陣）
  > 回傳值：input到每vertex的最短距離
  >> type dictionary
