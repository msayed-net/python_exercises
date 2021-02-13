class Subscriber:
  def __init__(self, name):
    self.name = name
  def update(self, message):
    print(f"{self.name} received a message: {message}")
    
class Publisher:
  def __init__(self):
    self.subscribers = dict()
  def register(self, subscriber):
    self.subscribers.add(subscriber)
  def unregister(self, subscriber):
    self.subscribers.discard(subscriber)
  def dispatch(self, message):
    for subscriber in self.subscribers:
      subscriber.update(message)
      
publisher = Publisher()

ahmed = Subscriber('ahmed')
mona = Subscriber('mona')
ola = Subscriber('ola')

publisher.register(ahmed)
publisher.register(mona)
publisher.register(ola)

publisher.dispatch('Good New, Cairo')   # All 3
publisher.unregister(mona)
publisher.dispatch('Good New, Moscow')  # Only 2
