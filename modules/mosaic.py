#写真の中の顔を検出して自動でモザイクをかける処理
import cv2

def mosaic_to_fases(img)
    cascade_file= "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_file)
    #img = cv2.imread("photo.jpg")

    #写真の中の顔をすべて検出して周囲の四角形の座標を取得
    #検出できた顔のすべてについて[四角の左上のx座標、四角の左上のy座標、幅、高さ]の数値を取得
    face_list = face_cascade.detectMultiScale(img, scaleFactor = 1.1, minSize=(30,30))

    #モザイク処理
    #[四角の左上のx座標、四角の左上のy座標、幅、高さ]をそれぞれ変数x, y, w, hに代入
    for x, y, w, h in face_list:
        face= img[y:y+h, x:x+w]
        small_pic = cv2.resize(face, (8,8))
        mosaic = cv2.resize(small_pic,(w,h))
        img[y:y+h, x:x+w]=mosaic

return img



    #cv2.imshow("photo_processed.jpg",img)
    #cv2.waitKey()
    #cv2.destroyAllWindows()
