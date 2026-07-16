# Magnetic Field Mapper (磁力線マッピングシステム)

このプロジェクトは、Raspberry Piに接続された磁気センサー（BNO055など）から取得した磁束密度データと、測定した位置情報を紐づけて記録し、3次元空間上に磁力線や磁場をマッピング・可視化するためのシステムです。

---

## 📂 フォルダ・ファイル構成

* `magnetic_mapper/`
  * `data/` : 測定したCSVデータやキャリブレーション結果の保存先。
  * `src/` : ソースコードディレクトリ。
    * `sensor.py` : センサー制御・データ取得処理。
    * `recorder.py` : 位置と磁気データの記録処理。
    * `visualizer.py` : 磁力線やベクトル場の可視化処理。
  * `main.py` : プログラムのメイン実行ファイル（エントリーポイント）。
  * `requirements.txt` : 動作に必要なライブラリ一覧。
  * `README.md` : この説明ファイル。

---

## 🔌 動作環境と接続方法

### 必要ハードウェア
* Raspberry Pi
* 9軸慣性センサ BNO055 (I2C接続)

### 接続 (I2C)
* VCC -> 3.3V
* GND -> GND
* SDA -> SDA (GPIO2)
* SCL -> SCL (GPIO3)

---

## 🛠️ セットアップ手順

1. Raspberry PiのI2C通信を有効化します。
2. 必要な依存ライブラリをインストールします。
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 使い方

今後実装が進んだ際の使用方法のイメージです。

### 1. データの測定・記録
位置情報と紐づけて磁束密度を測定し、CSVに記録します。
```bash
python main.py --mode record
```

### 2. 磁力線の可視化
記録されたデータを読み込み、3Dグラフとして可視化します。
```bash
python main.py --mode visualize
```

---

## 📊 記録データのフォーマット (data/magnetic_data.csv)

保存されるデータは以下のカラム（ヘッダー）を持つCSVファイルを想定しています。

| カラム名 | 説明 | 単位 |
| :--- | :--- | :--- |
| `timestamp` | 測定した時間（UNIX時間など） | 秒 |
| `x_pos` | 測定した空間上のX座標 | mm または m |
| `y_pos` | 測定した空間上のY座標 | mm または m |
| `z_pos` | 測定した空間上のZ座標 | mm または m |
| `mag_x` | X軸方向の磁束密度 | $\mu\text{T}$ (マイクロテスラ) |
| `mag_y` | Y軸方向 of 磁束密度 | $\mu\text{T}$ (マイクロテスラ) |
| `mag_z` | Z軸方向 of 磁束密度 | $\mu\text{T}$ (マイクロテスラ) |
