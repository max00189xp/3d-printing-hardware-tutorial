# 3D 列印機器原理講義工作紀錄

紀錄日期：2026-10-13（Asia/Taipei）

## 任務與完成成果

依專案內的 `3D列印機器原理.pdf`，將內容改寫成分段 Markdown 講義，建立 HackMD 個人工作區資料夾，並將原稿裁圖嵌入相應段落。

- PDF 為一頁掃描圖，沒有可直接擷取的文字；內容經影像辨讀整理。
- 講義包含九個主題、學習目標、對照表、圖說及六題複習題與參考答案。
- 已裁出並上傳八張圖片，確認全部在 HackMD 正常載入。
- 已儲存 HackMD 命名版本「圖解講義完成版」及「圖解講義排版確認版」。

## HackMD 位置

- 資料夾名稱：3D列印機器原理（個人工作區）
- 資料夾：https://hackmd.io/folders/1j31tGViAUIuml5dCl7N3
- 資料夾 ID：`981f9781-2aae-417c-a25b-00cbdc446ade`
- 講義名稱：3D列印機器原理｜圖解講義
- 講義：https://hackmd.io/KYyn9hZ1QmibLLlXRzqc1w
- 筆記 ID：`KYyn9hZ1QmibLLlXRzqc1w`

## 講義重點

1. **機器結構總覽**：機架、擠出系統與列印平台共同運作；X 軸為左右、Y 軸為前後、Z 軸為上下。
2. **擠出頭工作原理**：送料齒輪推進線材，加熱塊使其熔融，噴嘴擠出材料並逐層堆疊。
3. **列印流程**：3D 模型 → 切片軟體產生 G-code → 列印機執行 → 完成物件。
4. **運動系統**：原稿列出 X、Y 軸常用皮帶傳動，Z 軸常用螺桿傳動；實際移動部件依機構而定。
5. **關鍵組件**：步進馬達、熱端／噴嘴、加熱床、控制板、電源供應器與線材。
6. **座標系統**：三軸控制材料放置位置與列印高度。
7. **材料比較**：依原稿整理 PLA、ABS、PETG 的特性、優缺點與用途。
8. **維護與問題**：保持平台水平、線材乾燥與噴嘴清潔；翹曲檢查平台與附著，偏移檢查皮帶，供料中斷檢查進料路徑與線材纏繞。
9. **總結**：機械結構、擠出加熱與精準控制配合，將數位模型逐層轉為實體物件。

## 原稿辨讀與編寫注意事項

- 第 6 區的座標箭頭畫法容易誤解；講義以原稿文字「X＝左右、Y＝前後、Z＝上下」為準，保留原圖並加上提醒。
- 原稿以「擠出頭（噴嘴＋熱端）」概括列印頭；講義提醒區分送料部分與熱端／噴嘴。
- 原稿將 PLA 描述為「生物可分解、無毒、低味」；講義保留比較方向，但不把「無毒」等簡化用語當成所有產品與條件下的保證。
- 原稿的容器用途不足以判定食品接觸適用性；實際條件應查閱所用線材產品說明。
- 「線材斷料」依其列出的阻塞、纏繞原因，整理為供料中斷現象。
- 講義屬原稿內容整理，未另行進行外部技術資料查證。

## 圖片上傳方式與連結

HackMD MCP 可建立資料夾、建立與修改筆記，但目前沒有圖片上傳功能。使用者自行完成瀏覽器登入後，透過 HackMD 編輯器「插入圖片」上傳八張 PNG，取得 HackMD 圖片連結，再以 MCP 將圖片放入相應段落。此輪實際使用檔案上傳，未使用剪貼簿圖片貼上。

| 圖片 | HackMD 圖片連結 |
| --- | --- |
| 機器結構 | https://hackmd.io/_uploads/B1P0OBjozl.png |
| 擠出原理 | https://hackmd.io/_uploads/BywA_roizl.png |
| 列印流程 | https://hackmd.io/_uploads/BJPCOrsiMl.png |
| 運動系統 | https://hackmd.io/_uploads/HkDCdHioGg.png |
| 關鍵組件 | https://hackmd.io/_uploads/HJw0_Ssozx.png |
| 座標系統 | https://hackmd.io/_uploads/HyDCdBoizl.png |
| 材料比較 | https://hackmd.io/_uploads/HyvCuSijfe.png |
| 維護與問題 | https://hackmd.io/_uploads/r1vCdBioMl.png |

## 本機檔案

以下路徑皆相對於本專案資料夾 `D:\codex\3D列印硬體教學`：

- 原始 PDF：`3D列印機器原理.pdf`
- 本機圖片路徑版講義：`output/handout/3D列印機器原理講義.md`
- HackMD 圖片連結版講義：`output/handout/3D列印機器原理講義-HackMD版.md`
- HackMD 位置紀錄：`output/handout/HackMD講義連結.txt`
- 完成預覽：`output/handout/HackMD講義預覽.jpg`
- 裁圖腳本：`output/handout/crop_figures.py`
- 原頁渲染與裁圖：`output/handout/images/`

## 後續維護

- 修改 HackMD 筆記前先使用 `get_note` 取得最新內容，保留使用者後續修改，再合併本次變更。
- 實質更新後建立命名版本，並確認版本與圖片顯示正常。
- 修改裁圖時，以原 PDF 為來源，目視檢查標題、邊界與文字是否完整。
- 原始 PDF 保持不變。專案已初始化 Git，分支為 `main`。

## GitHub 公開儲存庫與圖片遷移

- 使用者授權新建公開儲存庫：`max00189xp/3d-printing-hardware-tutorial`。
- 儲存庫：https://github.com/max00189xp/3d-printing-hardware-tutorial
- origin：https://github.com/max00189xp/3d-printing-hardware-tutorial.git
- 提交作者：`max`；使用 GitHub 帳號對應的 no-reply email，僅設定於本專案。
- GitHub 閱讀版講義使用 `images/` 相對路徑；HackMD 版本準備改用 `https://raw.githubusercontent.com/max00189xp/3d-printing-hardware-tutorial/main/output/handout/images/檔名.png`。
- 八張裁圖均確認存在；原始 PDF、講義、裁圖腳本與工作紀錄納入版本管理。
- `.gitignore` 排除秘密檔案、虛擬環境、`sources/` 及原頁渲染、視覺檢查中繼圖、預覽截圖。
- 本節建立時：公開儲存庫已建立，初始提交／推送及 HackMD 圖片遷移仍待完成；以後續完成紀錄為準。
