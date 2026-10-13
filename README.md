# 3D 列印機器原理教學

依《3D列印機器原理.pdf》整理的繁體中文圖解講義，包含九個主題、八張原稿裁圖、對照表與課堂複習。

## 閱讀講義

- [HTML 互動講義](index.html)：下載專案後以瀏覽器開啟 `index.html`，保留 `output/handout/images/` 圖片資料夾；支援章節、子題分頁、圖片放大與列印。
- [圖解講義](output/handout/3D列印機器原理講義.md)：使用儲存庫內的相對圖片路徑，可直接在 GitHub 閱讀。
- [HackMD 線上講義](https://hackmd.io/KYyn9hZ1QmibLLlXRzqc1w)
- [原始 PDF](3D列印機器原理.pdf)
- [工作紀錄](agent.md)

## 主題

1. 機器結構總覽
2. 擠出頭工作原理
3. 從模型到成品的列印流程
4. 皮帶與螺桿運動系統
5. 關鍵組件與作用
6. X、Y、Z 座標系統
7. PLA、ABS、PETG 材料比較
8. 操作維護與常見問題
9. 重點總結與複習

## 圖片與維護

八張圖片存於 `output/handout/images/`，GitHub 內的講義使用相對路徑。HackMD 使用公開儲存庫的原始圖片網址，兩個平台均以本專案圖片為來源。

目標公開儲存庫：`max00189xp/3d-printing-hardware-tutorial`，分支為 `main`。

講義依原稿整理；原圖座標箭頭與材料簡化敘述的閱讀提醒已寫入講義。原始 PDF 保留不變。

## HTML 網頁與重建

網頁依使用者提供的參考版型製作，採藍白配色、左側章節目錄、上方子題分頁與下方閱讀進度。共 11 個章節、20 個子頁，包含九個原稿主題、課程導讀與複習題。圖片使用本機相對路徑，閱讀不需要下載外部套件或連線載入字型。

`index.html` 包含網頁所需 CSS 與 JavaScript，可直接開啟；列印時自動展開全部章節。GitHub 的檔案頁顯示 HTML 原始碼，尚未啟用 GitHub Pages 網站部署。

修改 `output/handout/3D列印機器原理講義.md` 或 `web-layout.css` 後，以既有 Python 執行 `python build_web.py` 重建 `index.html`。產生腳本僅使用 Python 標準函式庫。原始 `參考網頁/參考.html` 保留為本機參考，不納入本次提交；重建使用已擷取的 `web-layout.css`。
