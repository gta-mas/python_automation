# items_in_cart = 0
# # add 2 items
#
# if items_in_cart != 2:
#     # raise Exception("Items in cart not matching")
#     pass
#
# assert (items_in_cart == 0)

#---------TRY, EXCEPT MECHANISM------------

# try:
#     with open("filelog.txt", "r") as reader:
#         reader.read()
#
# except:
#     print("File does not exist, lets continue anyway.")


try:
    with open("text.txt", "r") as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("Clearing records")