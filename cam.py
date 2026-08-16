import sys
import cv2
import numpy as np

import time
#### Non Ray  ( standalone)


# カメラデバイス番号（0 = デフォルトのカメラ）
# 特定のデバイスを使う場合: vdo="/dev/video2"
vdo = 0

# V4L2 バックエンドでカメラをオープン
cap = cv2.VideoCapture(vdo, cv2.CAP_V4L2)

if not cap.isOpened():
    print(f"エラー: カメラをオープンできませんでした (device={vdo})", file=sys.stderr)
    sys.exit(1)

exit_code = 0
try:
    # フレーム取得・表示ループ
    while True:
        ret, frame2 = cap.read()
        if not ret:
            print("エラー: フレームの取得に失敗しました", file=sys.stderr)
            exit_code = 1
            break

        # 取得したフレームをウィンドウに表示
        cv2.imshow('frame2', frame2)

        # 30ms 待機し、キー入力を取得（ESC = 27 で終了）
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
finally:
    # カメラとウィンドウを解放（エラー時・中断時も必ず実行）
    cap.release()
    cv2.destroyAllWindows()
sys.exit(exit_code)

