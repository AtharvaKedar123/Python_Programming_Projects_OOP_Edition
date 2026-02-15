# Practice Problem 12

## Problem Statement

A post office wants to automate the process of allocation of letters to
different postmen based on their allocated area.\
Write a python program to implement the class diagram given below.

------------------------------------------------------------------------

## Class Diagram

                             -------------------------
                             |       PostOffice      |
                             -------------------------
                             - area_list
                             - postmen_list
                             -------------------------
                             + __init__(area_list,postmen_list)
                             + get_area_list()
                             + get_postmen_list()
                             + validate_letter(letter)
                             + allocate_posts(letter_list)
                             -------------------------
                                    <>          <>
                                     |            |
                     --------------------     ---------------------
                     |        Letter       |     |      PostMan     |
                     --------------------     ---------------------
                     + counter -> static      + counter -> static
                     - sender_area            + post_man_id
                     - receiver_area          - name
                     + letter_id              - post_list_to_deliver
                     --------------------     ---------------------
                     + __init__(sender_area,receiver_area)
                     + get_sender_area()
                     + get_receiver_area()    + __init__(name)
                                              + get_post_list_to_deliver()
                                              + get_name()

------------------------------------------------------------------------

## Class description

### Letter class:

1.  Initialize static variable counter to 1\
2.  Auto-generate attribute, letter_id starting from 1 in the
    constructor

------------------------------------------------------------------------

### PostMan class:

1.  Initialize static variable counter to 100\
2.  Auto-generate attribute, postman_id starting from 101 prefixed by
    "P" in the constructor\
3.  post_list_to_deliver: List of letter objects to be delivered by the
    postman

------------------------------------------------------------------------

### PostOffice class:

1.  area_list: List of areas available\

2.  postmen_list: List of postman objects

    Mapping between the two lists -- which means postman at index
    position 0 delivers letters in the area at index position 0 of
    area_list

3.  validate_letter(letter): Accept the letter and validate its
    receiver_area. If letter.receiver_area is present in area_list,
    return the index position of that area in area_list. Else return -1

4.  allocate_posts(letter_list): Allocate letters in the letter_list to
    the appropriate postman

    a.  For every letter in letter_list\
        • Validate letter.receiver_area\
        • If valid, append the letter to the corresponding postman's
        post_list_to_deliver\
        • Else, add it to an invalid letter list

    b.  Return invalid letter list

------------------------------------------------------------------------

Perform case sensitive comparison.

Create objects of Letter class, PostMan class and PostOffice class,
invoke appropriate methods and test your program.
