from abc import ABC, abstractmethod
class ICostCalculationStrategy(ABC):
    @abstractmethod
    def calculate(self, distance, passengers, service_class, discount): pass

class FlightStrategy(ICostCalculationStrategy):
    def calculate(self, dist, pas, s_class, disc):
        price = dist * 50 * pas
        if s_class == "business": price *= 2
        if disc == "child": price *= 0.5
        return price


class TrainStrategy(ICostCalculationStrategy):
    def calculate(self, dist, pas, s_class, disc):
        price = dist * 20 * pas
        return price * 0.8 if disc == "senior" else price


class BusStrategy(ICostCalculationStrategy):
    def calculate(self, dist, pas, s_class, disc):
        return dist * 10 * pas

class TravelBookingContext:
    def __init__(self, strategy: ICostCalculationStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: ICostCalculationStrategy):
        self._strategy = strategy

    def calculate_cost(self, dist, pas, s_class, disc):
        return self._strategy.calculate(dist, pas, s_class, disc)

class IObserver(ABC):
    @abstractmethod
    def update(self, stock, price): pass

class StockExchange:
    def __init__(self):
        self._observers = {}

    def subscribe(self, stock_symbol, observer: IObserver):
        if stock_symbol not in self._observers:
            self._observers[stock_symbol] = []
        self._observers[stock_symbol].append(observer)
        print(f"Лог: Бақылаушы {stock_symbol} акциясына тіркелді.")[cite: 92]

    def set_price(self, stock_symbol, price):
        print(f"\nБиржа: {stock_symbol} жаңа бағасы — {price}$")[cite: 71, 92]
        self.notify(stock_symbol, price)

    def notify(self, stock_symbol, price):
        if stock_symbol in self._observers:
            for obs in self._observers[stock_symbol]:
                obs.update(stock_symbol, price)

class Trader(IObserver):
    def update(self, stock, price):
        print(f"[Трейдер Хабарламасы]: {stock} бағасы өзгерді: {price}$")


class TradingRobot(IObserver):
    def __init__(self, limit): self.limit = limit

    def update(self, stock, price):
        if price < self.limit:
            print(f"[Робот]: {stock} САТЫП АЛУ. Баға {price}$ шектен ({self.limit}$) төмен!")

if __name__ == "__main__":
    # 1. Стратегияны тексеру
    print("--- 1-тапсырма: Саяхат брондау ---")
    booking = TravelBookingContext(FlightStrategy())
    cost = booking.calculate_cost(dist=1000, pas=1, s_class="business", disc="none")
    print(f"Ұшақпен (Бизнес) бағасы: {cost} тг")

    booking.set_strategy(BusStrategy())
    print(f"Автобуспен бағасы: {booking.calculate_cost(1000, 1, 'economy', 'none')} тг")

    print("\n--- 2-тапсырма: Биржа саудасы ---")
    exchange = StockExchange()

    trader = Trader()
    robot = TradingRobot(limit=100)

    exchange.subscribe("AAPL", trader)
    exchange.subscribe("TSLA", robot)

    exchange.set_price("AAPL", 150)
    exchange.set_price("TSLA", 90)