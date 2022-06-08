# opencv-finalexam
OCR
OCR 指的是光學字元辨識 (Optical Character Recognition)，是將文字影像轉換為機器可讀文字格式的程序。現在大多使用tesseract作為OCR工具，因為目前tesseract是最精準的開元工具，裡面有許多語言可以選擇。
---
在進行OCR之前，影像必須做一些處理，以免干擾字元的識別，所以我們會需要先灰階化，在對影像進行縮放、翻轉、旋轉等幾何轉換，二值化、模糊化、邊緣強化、色彩空間轉換，腐蝕、膨脹、開運算、閉運算等形態學轉換，大部分的步驟會先灰階化，接下來就看要怎麼做處理。
如果圖片經過影像處理已經沒有任何雜訊，所得到的資料將會與圖片的資料有所吻合，但如果有些雜訊沒有清除乾淨，會造成OCR判斷錯誤，讓OCR判斷出錯誤結果。
---
OCR程式碼:
```pytesseract.pytesseract.tesseract_cmd = r' 您的tesseract.exe的位子'```
此程式碼是要找尋tesseract.exe以利後續的偵測。
```text = pytesseract.image_to_string(參數影像, lang='語言代碼')```
此程式碼是利用後面語言代碼，在tesseract找尋匹配的語言包，並使用該語言包進行圖像文字偵測，語言代碼(繁體:chi_tra 英文:eng)，這裡要看你是否有裝語言包，如果沒有裝語言包將會發生錯誤。


