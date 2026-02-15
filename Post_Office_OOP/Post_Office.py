class Letter:
    counter = 1   # static variable

    def __init__(self, sender_area, receiver_area):
        self.__sender_area = sender_area
        self.__receiver_area = receiver_area
        self.letter_id = Letter.counter
        Letter.counter += 1

    def get_sender_area(self):
        return self.__sender_area

    def get_receiver_area(self):
        return self.__receiver_area


class PostMan:
    counter = 100   # static variable

    def __init__(self, name):
        self.__name = name
        PostMan.counter += 1
        self.postman_id = "P" + str(PostMan.counter)
        self.__post_list_to_deliver = []

    def get_post_list_to_deliver(self):
        return self.__post_list_to_deliver

    def get_name(self):
        return self.__name


class PostOffice:
    def __init__(self, area_list, postmen_list):
        self.__area_list = area_list
        self.__postmen_list = postmen_list

    def get_area_list(self):
        return self.__area_list

    def get_postmen_list(self):
        return self.__postmen_list

    def validate_letter(self, letter):
        if letter.get_receiver_area() in self.__area_list:
            return self.__area_list.index(letter.get_receiver_area())
        return -1

    def allocate_posts(self, letter_list):
        invalid_letter_list = []

        for letter in letter_list:
            index = self.validate_letter(letter)

            if index != -1:
                postman = self.__postmen_list[index]
                postman.get_post_list_to_deliver().append(letter)
            else:
                invalid_letter_list.append(letter)

        return invalid_letter_list



area_list = ["Andheri", "Bandra", "Dadar"]


postman1 = PostMan("Ravi")
postman2 = PostMan("Amit")
postman3 = PostMan("Suresh")

postmen_list = [postman1, postman2, postman3]


post_office = PostOffice(area_list, postmen_list)


letter1 = Letter("Pune", "Andheri")
letter2 = Letter("Delhi", "Bandra")
letter3 = Letter("Goa", "Dadar")
letter4 = Letter("Chennai", "Mumbai")  

letter_list = [letter1, letter2, letter3, letter4]


invalid_letters = post_office.allocate_posts(letter_list)


print("---- Allocation Details ----")
for postman in post_office.get_postmen_list():
    print("Postman:", postman.get_name(), postman.postman_id)
    for letter in postman.get_post_list_to_deliver():
        print("  Letter ID:", letter.letter_id,
              "Receiver Area:", letter.get_receiver_area())

print("\nInvalid Letters:")
for letter in invalid_letters:
    print("Letter ID:", letter.letter_id,
          "Receiver Area:", letter.get_receiver_area())
