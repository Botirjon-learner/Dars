# Muxim kutubxonalarni import qilamiz
import requests
import cv2
import numpy as np
import imutils

# Quyidagi URL manzilni o'zingizniki bilan almashtiring
url = "http://10.152.12.241:8080/shot.jpg"

# Url dan doimiy ravishda ma'lumotlarni olish uchun while tsikli
while True:
    rasm_1 = requests.get(url)
    rasm_arr = np.array(bytearray(rasm_1.content), dtype=np.uint8)
    rasm = cv2.imdecode(rasm_arr, -1)
    rasm = imutils.resize(rasm, width=1000, height=1800)
    cv2.imshow("Android_kamera", rasm)

    # Chiqish uchun Esc tugmasini bosing

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()