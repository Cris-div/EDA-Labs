class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size_count = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.size_count += 1
        return True

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size_count -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        return self.front.data

    def size(self):
        return self.size_count

    def __str__(self):
        if self.is_empty():
            return "Queue: []"
        result = []
        current = self.front
        while current:
            result.append(str(current.data))
            current = current.next
        return f"Queue: [{', '.join(result)}]"
    
class Customer:
    def __init__(self,id,items_count):
        self.id=id
        self.items_count=items_count
        self.arrival_time = 0  
        self.checkout_time = 0 
    def __str__(self):
        return f"Customer #{self.id} ({self.items_count} items)"
    
class CheckoutLane:
    def __init__(self, id, processing_rate):
        self.id = id
        self.processing_rate = processing_rate 
        self.queue = LinkedQueue()  
        self.current_customer = None  
        self.time_remaining = 0  
        self.customers_processed = 0 
    def is_busy(self):
        return self.current_customer is not None

    def queue_length(self):
        return self.queue.size()

    def total_items_waiting(self):
        total = 0
        
        temp_queue = LinkedQueue()

        while not self.queue.is_empty():
            customer = self.queue.dequeue()
            total += customer.items_count
            temp_queue.enqueue(customer)

        while not temp_queue.is_empty():
            self.queue.enqueue(temp_queue.dequeue())

        return total

    def add_customer(self, customer):
        """Add a customer to this checkout lane."""
        self.queue.enqueue(customer)
        return True

    def start_next_customer(self, current_time):
        """Start processing the next customer in the queue."""
        if self.queue.is_empty():
            return False

        self.current_customer = self.queue.dequeue()

        self.time_remaining = self.current_customer.items_count / self.processing_rate

        print(
            f"Lane #{self.id}: Started checkout for {self.current_customer} ⏳")
        return True

    def process_time_unit(self, current_time):

        if not self.is_busy():
            return False

        self.time_remaining -= 1

        if self.time_remaining <= 0:
            self.current_customer.checkout_time = current_time

            wait_time = self.current_customer.checkout_time - \
                self.current_customer.arrival_time
            print(
                f"Lane #{self.id}: Completed checkout for {self.current_customer} (waited {wait_time} time units) ✅")

            self.customers_processed += 1
            self.current_customer = None
            return True  

        return False  


class Supermarket:

    def __init__(self):
        self.lanes = [
            CheckoutLane(1, 5),  
            CheckoutLane(2, 3),  
            CheckoutLane(3, 7)   
        ]

        self.current_time = 0
        self.customers_processed = 0
        self.total_wait_time = 0

    def select_best_lane(self, customer):
        best_lane = None
        min_wait_time = float('inf')

        for lane in self.lanes:
            estimated_wait = 0

            if lane.is_busy():
                estimated_wait += lane.time_remaining

            estimated_wait += lane.total_items_waiting() / lane.processing_rate

            if estimated_wait < min_wait_time:
                min_wait_time = estimated_wait
                best_lane = lane

        return best_lane

    def add_customer(self, customer):

        customer.arrival_time = self.current_time

        best_lane = self.select_best_lane(customer)

        best_lane.add_customer(customer)
        print(f"Customer #{customer.id} joined Lane #{best_lane.id} (estimated wait: {customer.items_count / best_lane.processing_rate:.1f} time units) 🛒")

        return best_lane.id

    def simulate_time_unit(self):
        """Simulate one time unit for the supermarket."""
        self.current_time += 1

        for lane in self.lanes:
            if not lane.is_busy():
                lane.start_next_customer(self.current_time)

            customer_finished = lane.process_time_unit(self.current_time)

            if customer_finished:
                self.customers_processed += 1

        if self.current_time % 5 == 0:
            self.print_status()

    def print_status(self):
        """Print the current status of all checkout lanes."""
        print(f"\nTime: {self.current_time} ⏱️")
        for lane in self.lanes:
            if lane.is_busy():
                print(
                    f"Lane #{lane.id}: Processing {lane.current_customer}, {lane.queue_length()} waiting")
            else:
                print(f"Lane #{lane.id}: Idle, {lane.queue_length()} waiting")

    def all_lanes_empty(self):
        """Check if all checkout lanes are empty (no customers being processed or waiting)."""
        for lane in self.lanes:
            if lane.is_busy() or not lane.queue.is_empty():
                return False
        return True

    def get_statistics(self):
        """Calculate and return supermarket statistics."""
        total_processed = sum(lane.customers_processed for lane in self.lanes)

        total_wait_time = 0
        processed_count = 0

        return {
            'total_time': self.current_time,
            'customers_processed': total_processed,
            'lanes_statistics': [
                {'lane_id': lane.id, 'customers_processed': lane.customers_processed}
                for lane in self.lanes
            ]
        }


def simulate_supermarket():

    supermarket = Supermarket()

    import random
    customers = [
        Customer(1, 15),
        Customer(2, 5),
        Customer(3, 22),
        Customer(4, 3),
        Customer(5, 10),
        Customer(6, 7),
        Customer(7, 30),
        Customer(8, 2),
        Customer(9, 12),
        Customer(10, 8)
    ]

    print("Starting supermarket checkout simulation... 🛒")

    for customer in customers:
        supermarket.add_customer(customer)

    time_limit = 50  

    for t in range(1, time_limit + 1):

        supermarket.simulate_time_unit()

        if supermarket.all_lanes_empty():
            print(f"\nAll customers processed at time {t}! 🎉")
            break

    
    stats = supermarket.get_statistics()
    print("\nSupermarket Simulation Results:")
    print(f"Total simulation time: {stats['total_time']} time units ⏱️")
    print(f"Total customers processed: {stats['customers_processed']} 👥")

    for lane_stat in stats['lanes_statistics']:
        print(
            f"Lane #{lane_stat['lane_id']}: Processed {lane_stat['customers_processed']} customers")
        
simulate_supermarket()