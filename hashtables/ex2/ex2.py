#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    
    for i in range(0,len(route)):
        if i == 0:
            current = hash_table_retrieve(hashtable, "NONE")
        else:
            current = hash_table_retrieve(hashtable, current)
        route[i] = current
        # print("test 1", route)

    for location in route:
        if location == "NONE":
            route.remove(location)
        # print("test 2", route)
    return route

# # TEST CASE
# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")
# tickets = [ticket_1, ticket_2, ticket_3]
# assert reconstruct_trip(tickets, 3) == ["PDX", "DCA"]