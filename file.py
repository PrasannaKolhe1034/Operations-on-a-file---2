with open('Codingal.txt', 'w') as file:
    file.write("Hi! I am a Penguin and Iam 1 year old.")
file.close()

with open('Codingal.txt', 'r') as file:
 data=file.readlines()
 print("Words in the file are....")
 for line in data:
    word= line.split()
    print(word)
file.close()

