# Crawel_for_Tripresso
</br>
1. 第一家旅行社的旅遊商品</br>

2. 觀察Tripresso網站，試規劃爬取的資料如何存放在關聯資料庫</br>
會有哪些Table？</n>
會有哪些Column？</n>
哪些Column是Primary Key？</n>
哪些Column是Foreign Key？</n>
哪些Column是Unique的？</n>
ANS:</n>


</br>
3. 請以Python撰寫網路爬蟲，至少抓取「對方旅行社」對應內容:</br>
ANS:</n>
    'title': 行程名稱</n>
    'product_num': product_num,</n>
    'product_price': 價錢 ,</n>
    'product_days': 旅遊天數,</n>
    'product_total': 總團位,</n>
    'product_available': 可售位,</n>
    'product_date_normal': 出發日期 </n>

</br>
4. 將抓完的資料以2.的規劃方式儲存</n>
5. 以下是第二家旅行社的商品網址，重複3.4.步驟，將資料爬取且與4.存放在同一資料區</n>

6. 附上以上的內容(可用github或是壓縮檔案等方式附檔)，內容須至少包含
網路爬蟲的Python程式碼，會分別抓取以下兩家旅行社
https://www.gloriatour.com.tw/
http://www.orangetour.com.tw/
步驟3. 規定的抓取內容：旅遊天數、行程名稱、出發日期、價錢、可售位、總團位
若以MySQL方式儲存，可附以MySQL匯出後檔案
若以SQLite檔案儲存，可附上該檔案
若以csv/json 方式儲存，請附圖說明以何種欄位關聯(哪些是Foreign Key)

＊加分項目：
資料的正確性以及乾淨程度
抓取兩家旅行社兩頁以上的商品資料
多抓取步驟3. 以外，而有出現在Tripesso網站上的內容
使用requests而非selenium
程式碼的維護性及可擴充性
