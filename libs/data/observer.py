# -*- coding: utf-8 -*-
class Observer:
    def __init__(self):
        self.subscribers = []

    def register(self, subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)

    def unregister(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    def notify(self, tick):
        for subscriber in self.subscribers:
            subscriber.update(tick)

# class Subscriber:
#     def update(self, tick):
#         raise NotImplementedError("Subclasses devem implementar este método")


# class ExampleSubscriber(Subscriber):
#     def update(self, tick):
#         print(f"Novo tick recebido em ExampleSubscriber: {tick}")


# # Exemplo de uso:
# observer = Observer()

# subscriber1 = ExampleSubscriber()
# subscriber2 = ExampleSubscriber()

# observer.register(subscriber1)
# observer.register(subscriber2)

# new_tick = {'time': 1680512400021, 'ask': 1.12345}  # Exemplo de novo tick
# observer.notify(new_tick)

# observer.unregister(subscriber1)

# new_tick2 = {'time': 1680512400022, 'ask': 1.12346}  # Exemplo de outro novo tick
# observer.notify(new_tick2)
