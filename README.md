# opencv-finalexam
OCR程式碼:
pytesseract.pytesseract.tesseract_cmd = r' 您的tesseract.exe的位子'
此程式碼是要找尋tesseract.exe以利後續的偵測。
text = pytesseract.image_to_string(參數影像, lang='語言代碼')
此程式碼是利用後面語言代碼，在tesseract找尋匹配的語言包，並使用該語言包進行圖像文字偵測，語言代碼(繁體:chi_tra 英文:eng)，這裡要看你是否有裝語言包，如果沒有裝語言包將會發生錯誤。
