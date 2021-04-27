class Email:

    def __init__(self, sender, receiver, content):
        self.is_sent = False
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def send(self):
        self.is_sent = True

    def get_info(self):
        print(f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}")


list_of_emails = []
command = input()
while not command == "Stop":
    command = command.split()
    email = Email(command[0], command[1], command[2])
    list_of_emails.append(email)
    command = input()

last_line = input().split(", ")
for mail_index in last_line:
    list_of_emails[int(mail_index)].send()

for mail in list_of_emails:
    mail.get_info()
