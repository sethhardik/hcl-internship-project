import pytesseract
def ocr_doc(img):
	text = pytesseract.image_to_string(img)
	return text
 
