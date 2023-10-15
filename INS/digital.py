def simple_hash(message):
    hash_value = 0
    for char in message:
        hash_value += ord(char)
    return hash_value

if __name__ == "__main__":
    message = input("Enter the message: ").strip()
    signature = simple_hash(message)
    
    print("Message:", message)
    print("Signature:", signature)
    
    received_message = input("Enter the received message: ").strip()
    received_signature = int(input("Enter the received signature: "))
    
    if signature == received_signature and message == received_message:
        print("Signature and message verified successfully.")
    else:
        print("Signature or message verification failed.")
