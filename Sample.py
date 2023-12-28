import socket

def calculate(question):
    try:
        parts = question.split()
        num1, operator, num2 = int(parts[1]), parts[2], int(parts[3].rstrip('?'))
        
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            return num1 // num2
        else:
            print("Unknown operation.")
            return None
    except Exception as e:
        print(f"Unable to calculate: {e}")
        return None

# Connection
serverName = '10.110.133.134'
serverPort = 8888

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

capitalized_name = clientSocket.recv(1024).decode()
print("Server response (capitalized name): ", capitalized_name)

name = input('My name: ')
name_message = 'HELLO ' + name + "\n"
clientSocket.send(name_message.encode())

flag = "Quiz in progress"

try:
    while True:  # This will initiate the infinite loop
        # Receiving and decoding the question
        question = clientSocket.recv(1024).decode().strip()  # strip() to remove any leading/trailing whitespaces
        
        # Check if the question is the 'Done' message
        if question == 'Done':
            flag = "Quiz completed"
            break

        # Calculate the answer (since the question is not 'Done')
        result = calculate(question)

        if result is not None:  # Check if we have a valid result to send
            answer = 'answer ' + str(result) + '\n'  # Convert result to str, add space after 'answer'
            print(question)
            print(answer)
            clientSocket.send(answer.encode())  # Send the answer
        else:
            print("Unable to calculate the answer for the question:", question)

# Catch any general exception
except Exception as e:
    print(f"An error occurred: {e}")
    flag = "An error"