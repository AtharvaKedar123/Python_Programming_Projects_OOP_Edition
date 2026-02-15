class Parcel:
    counter = 1   

    def __init__(self, sender_zone, receiver_zone):
        self.__sender_zone = sender_zone
        self.__receiver_zone = receiver_zone
        self.parcel_id = Parcel.counter
        Parcel.counter += 1

    def get_sender_zone(self):
        return self.__sender_zone

    def get_receiver_zone(self):
        return self.__receiver_zone


class DeliveryAgent:
    counter = 300   

    def __init__(self, name):
        self.__name = name
        DeliveryAgent.counter += 1
        self.agent_id = "A" + str(DeliveryAgent.counter)
        self.__parcel_list = []

    def get_parcel_list(self):
        return self.__parcel_list

    def get_name(self):
        return self.__name


class Courier:
    def __init__(self, zone_list, agent_list):
        self.__zone_list = zone_list
        self.__agent_list = agent_list

    def get_zone_list(self):
        return self.__zone_list

    def get_agent_list(self):
        return self.__agent_list

    def validate_parcel(self, parcel):
        if parcel.get_receiver_zone() in self.__zone_list:
            return self.__zone_list.index(parcel.get_receiver_zone())
        return -1

    def allocate_parcels(self, parcel_list):
        invalid_parcel_list = []

        for parcel in parcel_list:
            index = self.validate_parcel(parcel)

            if index != -1:
                agent = self.__agent_list[index]
                agent.get_parcel_list().append(parcel)
            else:
                invalid_parcel_list.append(parcel)

        return invalid_parcel_list



zone_list = ["North", "South", "East"]


agent1 = DeliveryAgent("Rahul")
agent2 = DeliveryAgent("Kiran")
agent3 = DeliveryAgent("Vikas")

agent_list = [agent1, agent2, agent3]


courier = Courier(zone_list, agent_list)


parcel1 = Parcel("Delhi", "North")
parcel2 = Parcel("Mumbai", "South")
parcel3 = Parcel("Chennai", "East")
parcel4 = Parcel("Goa", "West")   

parcel_list = [parcel1, parcel2, parcel3, parcel4]


invalid_parcels = courier.allocate_parcels(parcel_list)


print("---- Allocation Details ----")
for agent in courier.get_agent_list():
    print("Agent:", agent.get_name(), agent.agent_id)
    for parcel in agent.get_parcel_list():
        print("  Parcel ID:", parcel.parcel_id,
              "Receiver Zone:", parcel.get_receiver_zone())

print("\nInvalid Parcels:")
for parcel in invalid_parcels:
    print("Parcel ID:", parcel.parcel_id,
          "Receiver Zone:", parcel.get_receiver_zone())
