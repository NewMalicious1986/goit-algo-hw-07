class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        if isinstance(reply, Comment):
            self.replies.append(reply)
        else:
            raise ValueError("Reply must be an instance of Comment")

    def remove_reply(self):
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, level=0):
        prefix = " " * (level * 4)
        if not self.is_deleted:
            print(f"{prefix}{self.author}: {self.text}")
        else:
            print(f"{prefix}{self.text}")
        for reply in self.replies:
            reply.display(level + 1)

if __name__ == "__main__":
    root_comment = Comment("Яка чудова книга!", "Бодя")
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)

    reply1.remove_reply()

    root_comment.display()
