import time


class Producer:
    """Define the 'resource-intensive' object to instantiate"""

    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you now!")

# The goal is not to bother the producer until he is available


class Proxy:
    """Define the 'relatively less resource-intensive' proxy object to instantiate"""

    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """Check if Producer is available"""
        print("Artist checking if Producer is available...")

        if self.occupied == 'No':
            # if the producer is available, create a producer object
            self.producer = Producer()
            time.sleep(2)
            # make the producer meet the guest
            self.producer.meet()
        else:
            time.sleep(2)
            print("Producer is busy!")


# instantiate a Proxy
p = Proxy()
# make the proxy: Artist produce until Producer is available
p.produce()
# change the state to 'occupied'
print()
p.occupied = 'Yes'
p.produce()
