def reverse_message(message):
    result = ""

    for ch in message:
        result = ch + result

    return result

message = input("Enter message: ")
print("Reversed:", reverse_message(message))