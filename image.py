import cv2
import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


#LoggingEvenHandlerを上書きして動作を変更
class LoggingEventHandler2(LoggingEventHandler):
    def on_created(self, event):    
        print("生成されました。" + event.src_path) #デバッグ用
        print(type(event.src_path)) #デバッグ用
        img = cv2.imread(event.src_path)
        print(type(img)) #デバッグ用
        # ---以下,画像が新たにアップロードされたときに実行する処理
        

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