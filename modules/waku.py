import cv2

def apply_mosaic_to_faces(img):
    # カスケードファイルの読み込み
    cascade_file = "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_file)

    # 画像の読み込み(確認用)
    #img = cv2.imread(image_path)

    # 顔検出
    face_list = face_cascade.detectMultiScale(img, scaleFactor=1.1, minSize=(30, 30))

 # 検出された顔に枠を描画
    for (x, y, w, h) in face_list:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # 処理済みの画像を保存(確認用)
    #cv2.imwrite(output_path, img)

    return img