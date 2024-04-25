import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

count = 0

while True:
    ret, frame = cap.read()             # 讀取影片的每一幀
    if not ret:
        print("Cannot receive frame")   # 如果讀取錯誤，印出訊息
        break
    cv2.putText(frame, f"{count}", (10, 470), 0, 1, (255, 0, 0), 2)
    cv2.imshow('Test', frame)     # 如果讀取成功，顯示該幀的畫面
    if cv2.waitKey(1) == 13:      # 每一毫秒更新一次，直到按下 q 結束
        cv2.imwrite('photo.jpg', frame)
        break
    count += 1
cap.release()                           # 所有作業都完成後，釋放資源
cv2.destroyAllWindows()                 # 結束所有視窗