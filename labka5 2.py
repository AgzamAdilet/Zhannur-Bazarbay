from abc import ABC, abstractmethod

class IPaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(IPaymentStrategy):
    def pay(self, amount):
        print(f"Банк картасымен {amount} тг төленді.")


class PayPalPayment(IPaymentStrategy):
    def pay(self, amount):
        print(f"PayPal арқылы {amount} тг төленді.")


class CryptoPayment(IPaymentStrategy):
    def pay(self, amount):
        print(f"Криптовалютамен {amount} тг төленді.")

class PaymentContext:
    def __init__(self):
        self._strategy = None

    def set_strategy(self, strategy: IPaymentStrategy):
        self._strategy = strategy

    def execute_payment(self, amount):
        if self._strategy:
            self._strategy.pay(amount)
        else:
            print("Қате: Төлем әдісі таңдалмады!")

class IObserver(ABC):
    @abstractmethod
    def update(self, rate):
        pass

class ISubject(ABC):
    @abstractmethod
    def attach(self, observer: IObserver): pass

    @abstractmethod
    def detach(self, observer: IObserver): pass

    @abstractmethod
    def notify(self): pass

class CurrencyExchange(ISubject):
    def __init__(self):
        self._observers = []
        self._rate = 0

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def set_rate(self, new_rate):
        self._rate = new_rate
        self.notify()

    def notify(self):
        for observer in self._observers:
            observer.update(self._rate)

class MobileApp(IObserver):
    def update(self, rate):
        print(f"[Mobile] Жаңа курс: {rate} тг")


class NewsSite(IObserver):
    def update(self, rate):
        print(f"[News] Назар аударыңыз! Курс өзгерді: {rate} тг")


class BankSystem(IObserver):
    def update(self, rate):
        print(f"[Bank] Жүйелік деректер жаңартылды: {rate}")

if __name__ == "__main__":
    # 1. Стратегия паттернін тексеру
    print("--- Стратегия паттерні ---")
    cart = PaymentContext()

    choice = input("Төлем түрін таңдаңыз (1-Карта, 2-PayPal, 3-Крипто): ")
    if choice == "1":
        cart.set_strategy(CreditCardPayment())
    elif choice == "2":
        cart.set_strategy(PayPalPayment())
    else:
        cart.set_strategy(CryptoPayment())

    cart.execute_payment(5000)

    print("\n--- Наблюдатель паттерні ---")
    exchange = CurrencyExchange()

    app = MobileApp()
    news = NewsSite()
    bank = BankSystem()

    exchange.attach(app)
    exchange.attach(news)
    exchange.attach(bank)

    exchange.set_rate(450.5)
