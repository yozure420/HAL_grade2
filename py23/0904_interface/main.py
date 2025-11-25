# インタフェース
# 抽象基底クラスにて、全てが抽象メソッドのクラス
# つまり、口(くち)だけの定義で、実処理は一切ない

from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class MyPlayer(Player):
    def play(self):
        print("play")

    def stop(self):
        print("stop")

mp = MyPlayer()
mp.play()
mp.stop()
