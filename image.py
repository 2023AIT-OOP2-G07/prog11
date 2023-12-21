import cv2
import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


#LoggingEvenHandlerを上書きして動作を変更
class LoggingEventHandler2(LoggingEventHandler):
    def on_created(self, event):
        file_absolute_path = event.src_path
        file_name = event.src_path.split("/")[-1]
        print("生成されました。" + event.src_path) #デバッグ用
        print("生成されたファイルの名前は " + file_name + "です。") #デバッグ用
        # ---以下,画像が新たにアップロードされたときに実行する処理

        #画像読み込み
        img = cv2.imread(file_absolute_path)
        print(img)
        #cv2.imwrite("./static/images/gray/"+file_name, img) ここで書き込みできる
        

    def on_deleted(self, event):
        print("削除されました" + event.src_path)

if __name__ == "__main__":
    path = "./static/images/upload"
    event_handler = LoggingEventHandler2()
    observer = Observer()       #監視オブジェクト生成
    observer.schedule(          #監視設定
        event_handler,
        path,
        recursive=True
        )
    observer.start()            #監視開始
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()