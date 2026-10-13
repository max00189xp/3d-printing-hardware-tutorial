# 3D 列印機器原理講義工作紀錄

紀錄日期：2026-10-13（Asia/Taipei）
最近更新：2026-10-13，補記 GitHub 推送、圖片顯示驗證及新版工具協定。

## 任務與完成成果

依專案內的 `3D列印機器原理.pdf`，將內容改寫成分段 Markdown 講義，建立 HackMD 個人工作區資料夾，並將原稿裁圖嵌入相應段落。

- PDF 為一頁掃描圖，沒有可直接擷取的文字；內容經影像辨讀整理。
- 講義包含九個主題、學習目標、對照表、圖說及六題複習題與參考答案。
- 已裁出並上傳八張圖片，確認全部在 HackMD 正常載入。
- 已儲存 HackMD 命名版本「圖解講義完成版」、「圖解講義排版確認版」及「GitHub 公開圖片版」。
- 公開 GitHub 儲存庫已建立，教材與八張裁圖已推送至 `main`；HackMD 已改用 GitHub 圖片，八張圖片均確認正常顯示。

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
- HackMD 完成預覽：`output/handout/HackMD講義預覽.jpg`（首次使用 HackMD 圖片來源時的截圖）
- GitHub 完成預覽：`output/handout/GitHub公開儲存庫完成預覽.jpg`（本機留存，不納入提交）
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
- GitHub 閱讀版講義使用 `images/` 相對路徑；HackMD 版本已改用 `https://raw.githubusercontent.com/max00189xp/3d-printing-hardware-tutorial/main/output/handout/images/檔名.png`。
- 八張裁圖均確認存在；原始 PDF、講義、裁圖腳本與工作紀錄納入版本管理。
- `.gitignore` 排除秘密檔案、虛擬環境、`sources/` 及原頁渲染、視覺檢查中繼圖、預覽截圖。
- 初始教材提交：`5e526df95bb66116c8ed74737066e3a9e297ba9e`，已成功推送至 `origin/main`，並確認遠端與本機提交一致。
- 八張 GitHub 圖片的 HTTP HEAD 檢查皆為 `200`、`image/png`。
- HackMD 已建立命名版本「GitHub 公開圖片版」，版本 ID 為 `bd5b1973-96f3-4f58-816f-fb9433941e45`。
- 上方「圖片上傳方式與連結」保留首次建立時的 HackMD 圖片連結作為歷史紀錄；現行講義使用 GitHub 圖片。
- 首次提交與推送使用已安裝的 Git 與正常 Git Credential Manager 流程，當時未使用 GitHub CLI。

## 2026-10-13 完成紀錄與後續工具設定

- `5e526df`：加入原始 PDF、九節圖解講義、八張裁圖、README、裁圖腳本與工作紀錄，已推送。
- `c77a081`：補記 GitHub 上傳及 HackMD 圖片遷移結果，已推送。
- `d8601c4`：排除本機完成預覽截圖，已推送。這是本次紀錄更新前的最新提交。
- 檢查結果：八張本機圖片路徑均存在；八張 GitHub 原始圖片網址均回傳 `200` 與 `image/png`；HackMD 逐段檢查後，八張圖片皆成功載入。
- 上輪完成時：分支為 `main`，工作區乾淨，沒有尚未推送的提交。本輪開始時另有未追蹤的 `參考網頁/`，屬既有使用者資料，本輪不納入提交或上傳。
- 使用者新版協定確認的個人 GitHub 帳號為 `max00189xp`。
- 後續 GitHub 操作使用 CLI 完整路徑：`D:\codex\安裝Github\tools\github-cli\bin\gh.exe`；不依賴 PATH，不讀寫該工具資料夾其他檔案。
- 本輪已執行 `gh auth status` 與 `gh api user --jq '.login'`，確認正常使用 Windows 憑證區登入，活動帳號為 `max00189xp`。
- 此專案保留既有作者 `max` 與 `88412709+max00189xp@users.noreply.github.com`，不套用新專案的預設作者、不改寫全域設定。
- Git 若因沙盒與使用者的資料夾擁有者不同而拒絕操作，使用單次指令的 `-c safe.directory='D:/codex/3D列印硬體教學'`，不新增全域可信目錄設定。
- 本次僅更新 `agent.md`；提交後以 Git 歷史中的「Update project work log and GitHub tool guidance」提交與實際推送結果為準，避免在檔案內記錄尚未產生的自身 commit ID。

## 2026-10-13 HTML 互動教學網頁

- 依使用者提供的 `參考網頁/參考.html` 製作專案根目錄的 `index.html`，沿用藍白配色、幾何頁首、章節目錄、子題分頁、卡片與表格、上一頁／下一頁及進度列。
- 內容取自本機 Markdown 講義：九個原稿主題，加上課程導讀與課堂複習，共 11 個章節、20 個子頁，保留八張裁圖與原稿辨讀提醒。
- 圖片採 `output/handout/images/` 相對路徑；CSS、JavaScript 內嵌於 HTML，無外部套件、字型或網路圖片依賴，可離線閱讀。
- 新增 `build_web.py` 與 `web-layout.css` 供重建；重建不依賴未追蹤的參考 HTML。原始參考網頁保留不變，不納入本次提交。
- 功能：章節與子題切換、二十頁順序閱讀、分頁網址、鍵盤子題切換、圖片放大及 Esc 關閉、完整講義列印、手機水平導覽與表格捲動。
- 已以本機預覽檢查完整二十頁翻頁順序、一次僅顯示一個子頁、首尾按鈕狀態、跨章節翻頁、圖片放大／關閉與鍵盤分頁。
- 手機版以 390px 視窗檢查，頁面未水平溢出，材料表可在自身容器內左右捲動。
- 八張本機圖解均確認正常載入，瀏覽器未回報 JavaScript 錯誤；HTML 的圖片路徑、二十個子頁與常見秘密字串檢查通過。
- 完成預覽存於 `output/handout/HTML教學網頁完成預覽.jpg`，僅留在本機，依既有忽略規則不提交。
- 網頁為本機 HTML 與 GitHub 檔案版本，未啟用 GitHub Pages 或進行網站部署。

## 2026-10-13 公開 HTML 網站與圖片網址

- 使用者要求 HTML 圖片為可連線網址並公開網頁，授權本次 GitHub Pages 部署。
- `build_web.py` 與 `index.html` 的八張圖解改用 GitHub 公開 HTTPS 原始圖片網址；放大圖解也沿用同一網址。
- HTML 圖片需連線載入；先前的離線相對圖片版本屬歷史狀態。Markdown 閱讀版仍保留本機相對路徑。
- 公開網站網址：https://max00189xp.github.io/3d-printing-hardware-tutorial/
- 部署來源：`main` 分支根目錄；新增 `.nojekyll`，以純靜態 HTML 部署。
- `e194738` 已提交並推送 HTML 公開圖片與 Pages 準備檔案；Pages 已啟用，來源為 `main` 分支根目錄。
- 首次部署工作流程 `38406970661` 成功，Pages API 狀態為 `built`。
- 公開網站已實際開啟驗證，八張圖片的 HTTPS 網址均能在網頁正常載入；章節與子題切換正常。
- 部署完成預覽：`output/handout/GitHubPages公開網站完成預覽.jpg`（本機留存，不納入提交）。

## 2026-10-13 圖片載入效能改善

- 保留八張 PNG 原圖，新增 `optimize_images.py`，使用既有 Pillow 產生 `output/handout/images/web/*.webp`，最大閱讀寬度 900px、品質 88。
- 閱讀圖片總大小由 4,496,716 bytes 減至 514,644 bytes，減少 88.6%；已目視檢查材料比較表與關鍵組件圖，文字可辨讀。
- HTML 的 WebP 使用 GitHub Pages 公開絕對 HTTPS 網址，與網站同來源；高清 PNG 保留 GitHub 原始檔公開網址。
- 讀取目前章節文字時預載該章圖解，並提前載入下一張 WebP；已預載網址去重，不提前載入高清 PNG。
- 點選放大先顯示 WebP，再非同步載入 PNG；原圖失敗時保留 WebP，關閉或切換圖片後不接受舊請求的回應。
- 加入圖片尺寸屬性，減少載入時的版面跳動；完整列印按鈕先準備全部閱讀圖。
- 本機驗證頁 `.web-preview.html` 列入忽略規則；伺服器紀錄確認課程導讀階段已請求第一張 WebP，進入章節後請求下一張 WebP。
- 本機測試確認 HTML 一般圖片均使用 WebP、初始放大圖片沒有來源、點選後使用高清 PNG、Esc 可關閉並可繼續跨章節翻頁。
- 改善提交 `b86d3e7` 已推送，Pages 工作流程 `38409151110` 建置與部署成功。
- 公開八張 WebP 均回傳 `200 / image/webp`；逐段開啟後，八張閱讀圖均確認正常載入，瀏覽器未回報 JavaScript 錯誤。
- 公開放大視窗確認先顯示 WebP 閱讀圖，本機驗證確認 PNG 完成後切換為高清原圖；Esc 關閉與翻頁正常。
- 實際下載秒數仍依訪客網路與快取而異；88.6% 為閱讀圖片總位元組減少比例，不代表固定的時間改善比例。
