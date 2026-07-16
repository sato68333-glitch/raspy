# -*- coding: utf-8 -*-

class DataRecorder:
    def __init__(self, filename="data/magnetic_data.csv"):
        self.filename = filename

    def record(self, position, mag_vector):
        """位置情報 (x, y, z) と 磁束密度 (mx, my, mz) を記録する"""
        pass
