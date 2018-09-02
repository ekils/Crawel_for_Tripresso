# Crawl_for_Tripresso
</br>
<h3>1. 第一家旅行社的旅遊商品</br></h3>

<h3>2. 觀察Tripresso網站，試規劃爬取的資料如何存放在關聯資料庫</br></h3>
會有哪些Table？</br>
會有哪些Column？</br>
哪些Column是Primary Key？</br>
哪些Column是Foreign Key？</br>
哪些Column是Unique的？</br>
<h4>ANS:</br></h4>

![GitHub Logo](https://github.com/ekils/Crawel_for_Tripresso/blob/master/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202018-09-02%20%E4%B8%8A%E5%8D%8812.56.01.png)

</br>
<h3>3. 請以Python撰寫網路爬蟲，至少抓取「對方旅行社」對應內容:</br></h3>
<h4>ANS:</br></h4>
    'title': 行程名稱</br>
    'product_num': product_num,</br>
    'product_price': 價錢 ,</br>
    'product_days': 旅遊天數,</br>
    'product_total': 總團位,</br>
    'product_available': 可售位,</br>
    'product_date_normal': 出發日期 </br>

</br>
<h3>4. 將抓完的資料以2.的規劃方式儲存</br></h3>
<h3>5. 以下是第二家旅行社的商品網址，重複3.4.步驟，將資料爬取且與4.存放在同一資料區</br></h3>
<h3>6. 附上以上的內容(可用github或是壓縮檔案等方式附檔)，內容須至少包含網路爬蟲的Python程式碼，會分別抓取旅行社 步驟3. 規定的抓取內容：旅遊天數、行程名稱、出發日期、價錢、可售位、總團位。若以MySQL方式儲存，可附以MySQL匯出後檔案 (哪些是Foreign Key)</br></h3>
<h4>ANS:</br></h4>
1.設計agency為foreign key. 不同agency 會對應到相應的欄位。</br>
2.已上傳在github上，參考commmit-log.</br>

</br>
<h3>＊加分項目：</br><h3>
資料的正確性以及乾淨程度</br>
抓取兩家旅行社兩頁以上的商品資料 </br>
多抓取步驟3. 以外，而有出現在Tripesso網站上的內容</br>
使用requests而非selenium</br>
程式碼的維護性及可擴充性</br>
</br>
<h4>ANS:</br></h4>
* 由於換頁抓取必須要有click的觸發，以request 無法完成。故必須以selenium 以onclick自動化觸發換頁。</br>
* 另外基於程式碼的可維護性與可擴充性：1. 設計為輸入頁數即可抓取第一頁～輸入的頁數資料。  2.利用oop概念，設計要抓取網址為 private property </br>
* 之後或許會導入更多.py檔。 故以：if __name__ == '__main__' 維護程式碼的克靠性。<br>
* 額外抓取了在Tripesso網站上的旅遊國家與旅遊地區，並存放在table裡面








