import matplotlib.pyplot as plt
class CandlestickEncoder:

    def __init__(self, high_price: float|int, open_price: float|int, close_price: float|int, low_price: float|int):
        self.high_price = high_price
        self.open_price = open_price
        self.close_price = close_price
        self.low_price = low_price

    def encoder(self) -> str :
        # decreasing bull
        if self.high_price > self.open_price > self.close_price > self.low_price:
            return 'a'
        if self.high_price == self.open_price > self.close_price > self.low_price:
            return 'b'
        if self.high_price == self.open_price > self.close_price == self.low_price:
            return 'c'
        if self.high_price > self.open_price > self.close_price == self.low_price:
            return 'd'

        # increasing bear
        if self.high_price > self.close_price > self.open_price > self.low_price:
            return 'e'
        if self.high_price == self.close_price > self.open_price > self.low_price:
            return 'f'
        if self.high_price == self.close_price > self.open_price == self.low_price:
            return 'g'
        if self.high_price > self.close_price > self.open_price == self.low_price:
            return 'h'

        # Doji
        if self.high_price > self.open_price == self.close_price > self.low_price:
            return 'i'
        if self.high_price == self.open_price == self.close_price > self.low_price:
            return 'j'
        if self.high_price == self.open_price == self.close_price == self.low_price:
            return 'k'
        if self.high_price > self.open_price == self.close_price == self.low_price:
            return 'l'

        return 'None'

    def cs_visualize(self, x:int = 0, details:bool =False, linewidth:int = 20) -> None:
        if self.close_price > self.open_price:
            color = 'green'
        elif self.close_price < self.open_price:
            color = 'red'
        else:
            color = 'black'

        plt.plot([x, x], [self.low_price, self.high_price], c=color)

        if self.open_price != self.close_price:
            plt.plot([x, x], [self.open_price, self.close_price], c=color, linewidth=linewidth)
        else:
            plt.plot([x - 0.1, x + 0.1], [self.open_price, self.close_price], c=color, linewidth=1)

        if details:
            plt.text(x + 0.01, self.high_price, 'high')
            plt.text(x + 0.01, self.low_price, 'low')
            plt.text(x + 0.01, self.close_price, 'close')
            plt.text(x + 0.01, self.open_price, 'open')