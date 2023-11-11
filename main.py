class ElectricMountainRailway:
    def __init__(self):
        # Initialize data structures for train journeys
        self.trains_up = {"09:00": 480, "11:00": 480, "13:00": 480, "15:00": 480}
        self.trains_down = {"10:00": 480, "12:00": 480, "14:00": 480, "16:00": 640}  # Extra coaches for the last train
        
        # Initialize revenue and passenger count for all times
        all_times = list(self.trains_up.keys()) + list(self.trains_down.keys())
        self.revenue = {time: 0 for time in all_times}
        self.passenger_count = {time: 0 for time in all_times}

    def purchase_ticket(self):
        # User input for ticket purchase
        departure_time = input("Enter departure time (09:00, 11:00, 13:00, 15:00): ")
        return_time = input("Enter return time (10:00, 12:00, 14:00, 16:00): ")
        num_passengers = int(input("Enter the number of passengers: "))

        # Check ticket availability
        if num_passengers <= self.trains_up.get(departure_time, 0) and num_passengers <= self.trains_down.get(return_time, 0):
            # Calculate cost with group discount
            free_tickets = num_passengers // 10
            total_cost = (num_passengers - free_tickets) * 50  # $25 up and $25 down

            # Update train availability and revenue
            self.trains_up[departure_time] -= num_passengers
            self.trains_down[return_time] -= num_passengers
            self.revenue[departure_time] += total_cost
            self.revenue[return_time] += total_cost

            # Update passenger count
            self.passenger_count[departure_time] += num_passengers
            self.passenger_count[return_time] += num_passengers

            print(f"Total cost: ${total_cost}")
        else:
            print("Not enough tickets available.")

    def display_status(self):
        # Display the status of each train journey
        for time, seats in self.trains_up.items():
            status = f"{seats} seats available" if seats > 0 else "Closed"
            print(f"Train Up at {time}: {status}")

        for time, seats in self.trains_down.items():
            status = f"{seats} seats available" if seats > 0 else "Closed"
            print(f"Train Down at {time}: {status}")

    def end_of_day_summary(self):
        # Display end of day summary
        total_passengers = sum(self.passenger_count.values())
        total_revenue = sum(self.revenue.values())
        most_popular_train = max(self.passenger_count, key=self.passenger_count.get)

        print(f"Total passengers: {total_passengers}")
        print(f"Total revenue: ${total_revenue}")
        print(f"Most popular train journey: {most_popular_train} with {self.passenger_count[most_popular_train]} passengers")

# Example usage
railway = ElectricMountainRailway()
railway.display_status()  # Show initial status
while True:
    action = input("Do you want to purchase a ticket? (yes/no): ").lower()
    if action == 'yes':
        railway.purchase_ticket()
        railway.display_status()
    else:
        break

railway.end_of_day_summary()
