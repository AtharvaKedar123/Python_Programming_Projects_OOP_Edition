# Practice Problem 15

## Problem Statement

A courier company wants to automate the allocation of parcels to
delivery agents based on the delivery zone.

Write a python program to implement the class diagram given below.

------------------------------------------------------------------------

## Class Diagram

                             -------------------------
                             |        Courier        |
                             -------------------------
                             - zone_list
                             - agent_list
                             -------------------------
                             + __init__(zone_list, agent_list)
                             + get_zone_list()
                             + get_agent_list()
                             + validate_parcel(parcel)
                             + allocate_parcels(parcel_list)
                             -------------------------
                                    <>          <>
                                     |            |
                     --------------------     ---------------------
                     |        Parcel       |     |   DeliveryAgent |
                     --------------------     ---------------------
                     + counter -> static      + counter -> static
                     - sender_zone            + agent_id
                     - receiver_zone          - name
                     + parcel_id              - parcel_list
                     --------------------     ---------------------
                     + __init__(sender_zone,receiver_zone)
                     + get_receiver_zone()
                     + get_sender_zone()      + __init__(name)
                                              + get_parcel_list()
                                              + get_name()

------------------------------------------------------------------------

## Class description

### Parcel class:

1.  Initialize static variable counter to 1\
2.  Auto-generate attribute, parcel_id starting from 1 in the
    constructor

------------------------------------------------------------------------

### DeliveryAgent class:

1.  Initialize static variable counter to 300\
2.  Auto-generate attribute, agent_id starting from 301 prefixed by "A"
    in the constructor\
3.  parcel_list: List of parcel objects assigned to the delivery agent

------------------------------------------------------------------------

### Courier class:

1.  zone_list: List of delivery zones\

2.  agent_list: List of delivery agent objects

    Mapping between the two lists -- which means agent at index position
    0 handles parcels of zone at index position 0 of zone_list

3.  validate_parcel(parcel): Accept the parcel and validate its
    receiver_zone. If parcel.receiver_zone is present in zone_list,
    return the index position of that zone in zone_list. Else return -1

4.  allocate_parcels(parcel_list): Allocate parcels in the parcel_list
    to the appropriate delivery agent

    a.  For every parcel in parcel_list\
        • Validate parcel.receiver_zone\
        • If valid, append the parcel to the corresponding agent's
        parcel_list\
        • Else, add it to an invalid parcel list

    b.  Return invalid parcel list

------------------------------------------------------------------------

Perform case sensitive comparison.

Create objects of Parcel class, DeliveryAgent class and Courier class,
invoke appropriate methods and test your program.
