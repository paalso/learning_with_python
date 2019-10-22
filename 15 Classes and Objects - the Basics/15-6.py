# Chapter 15. Classes and Objects — the Basics
# http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html

# Exercises 6
# ============

"""
Create a new class, SMS_store. The class will instantiate SMS_store objects,
similar to an inbox or outbox on a cellphone:
    my_inbox = SMS_store()
This store can hold multiple SMS messages (i.e. its internal state will just
be a list of messages). Each message will be represented as a tuple:
(has_been_viewed, from_number, time_arrived, text_of_SMS)
The inbox object should provide these methods:

my_inbox.add_new_arrival(from_number, time_arrived, text_of_SMS)
  # Makes new SMS tuple, inserts it after other messages
  # in the store. When creating this message, its
  # has_been_viewed status is set False.

my_inbox.message_count()
  # Returns the number of sms messages in my_inbox

my_inbox.get_unread_indexes()
  # Returns list of indexes of all not-yet-viewed SMS messages

my_inbox.get_message(i)
  # Return (from_number, time_arrived, text_of_sms) for message[i]
  # Also change its state to "has been viewed".
  # If there is no message at position i, return None

my_inbox.delete(i)     # Delete the message at index i
my_inbox.clear()       # Delete all messages from inbox
Write the class, create a message store object, write tests for these methods,
and implement the methods.
"""

class SMS_store:
    """ SMS_store class holds and manipulatea multiple SMS messages """

    def __init__(self):
        """ Instantiate SMS_store object - a list of messages,
        represented as a tuple:
        (has_been_viewed, from_number, time_arrived, text_of_SMS) """
        self.messages = []
        self.count = 0

    def __str__(self):
##        s = f"count = {self.count}\n" + "\n".join(list(self.messages))
        output = ["\nGot messages. Current count = {}".format(self.count)]
        num = 0
        for msg in self.messages:
            num += 1
            read_info = "read" if msg[0] else "unread"
            from_number = msg[1]
            time_arrived = msg[2]
            text_of_SMS = msg[3]
            output.append("{0:2d} {1:8s} {2:14s} {3:6s} {4:15s}".
                format(num, read_info, from_number, time_arrived, text_of_SMS))

        return '\n'.join(output)

    def add_new_arrival(self,from_number, time_arrived, text_of_SMS):
        """ Makes new SMS tuple, inserts it after other messages in the store.
        When creating this message, its has_been_viewed status is set False. """
        self.messages.append((False, from_number, time_arrived, text_of_SMS))
        self.count += 1

    def message_count(self):
        """ Returns the number of sms messages in my_inbox """
        return self.count

    def get_unread_indexes(self):
        """ Returns list of indexes of all not-yet-viewed SMS messages """
        unread_indexes = []
        for i, el in enumerate(self.messages):
            if not el[0]: unread_indexes.append(i)
        return unread_indexes

    def get_message(self,i):
        """ Return (from_number, time_arrived, text_of_sms) for message[i]
            Also change its state to "has been viewed".
            If there is no message at position i, return None """
        if i >= self.count:
            return None
        current_msg = self.messages[i]
        if not current_msg[0]:
            viewed_msg = [True]
            viewed_msg.extend(current_msg[1:])
            self.messages[i] = viewed_msg
        return self.messages[i][1:]

    def delete(self,i):
        """ Deletes the message at index i """
        if i >= self.count:
            return None
        self.count -= 1
        self.messages.pop(i)

    def clear(self):
        """ Deletes all messages from inbox """
        self.count = 0
        self.messages = []

inbox = SMS_store()

inbox.add_new_arrival("+380675553322", "13:56", "Hi, how are you?")
inbox.add_new_arrival("+380672223335", "13:59", "Great proposal of Citybank..")
inbox.add_new_arrival("+380671234678", "14:51", "Extraenlarging of you penis, hot off..")
inbox.add_new_arrival("+380675553322", "15:05", "Call us, it gonna by jolly!")
print(inbox.message_count())

m = inbox.get_message(1)
print(m)
##inbox.clear()
print(inbox)
print(inbox.get_unread_indexes())
m = inbox.get_message(2)
print(m)
print(inbox.get_unread_indexes())
inbox.delete(0)
print(inbox)
inbox.delete(1)
print(inbox)

inbox.add_new_arrival("+380671927000", "23:59", "Грузите апельсины бочках")
print(inbox)
print(inbox.get_unread_indexes())
print(inbox.get_message(5))
