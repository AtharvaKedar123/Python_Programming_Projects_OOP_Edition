# Practice Problem 14

## Problem Statement

A hospital wants to automate the allocation of patients to doctors based
on their specialization.

Write a python program to implement the class diagram given below.

------------------------------------------------------------------------

## Class Diagram

                             -------------------------
                             |        Hospital       |
                             -------------------------
                             - specialization_list
                             - doctor_list
                             -------------------------
                             + __init__(specialization_list, doctor_list)
                             + get_specialization_list()
                             + get_doctor_list()
                             + validate_patient(patient)
                             + allocate_patients(patient_list)
                             -------------------------
                                    <>          <>
                                     |            |
                     --------------------     ---------------------
                     |       Patient      |     |      Doctor      |
                     --------------------     ---------------------
                     + counter -> static      + counter -> static
                     - name                   + doctor_id
                     - illness                - name
                     + patient_id             - patient_list
                     --------------------     ---------------------
                     + __init__(name,illness)
                     + get_illness()
                     + get_name()             + __init__(name)
                                              + get_patient_list()
                                              + get_name()

------------------------------------------------------------------------

## Class description

### Patient class:

1.  Initialize static variable counter to 1\
2.  Auto-generate attribute, patient_id starting from 1 in the
    constructor

------------------------------------------------------------------------

### Doctor class:

1.  Initialize static variable counter to 500\
2.  Auto-generate attribute, doctor_id starting from 501 prefixed by "D"
    in the constructor\
3.  patient_list: List of patient objects assigned to the doctor

------------------------------------------------------------------------

### Hospital class:

1.  specialization_list: List of specializations available\

2.  doctor_list: List of doctor objects

    Mapping between the two lists -- which means doctor at index
    position 0 treats patients of specialization at index position 0 of
    specialization_list

3.  validate_patient(patient): Accept the patient and validate its
    illness. If patient.illness is present in specialization_list,
    return the index position of that specialization in
    specialization_list. Else return -1

4.  allocate_patients(patient_list): Allocate patients in the
    patient_list to the appropriate doctor

    a.  For every patient in patient_list\
        • Validate patient.illness\
        • If valid, append the patient to the corresponding doctor's
        patient_list\
        • Else, add it to an invalid patient list

    b.  Return invalid patient list

------------------------------------------------------------------------

Perform case sensitive comparison.

Create objects of Patient class, Doctor class and Hospital class, invoke
appropriate methods and test your program.
