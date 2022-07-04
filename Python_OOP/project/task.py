

class Task:
    def __init__(self, name: str, due_date: str) -> None:
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False
 
    def change_name(self, new_name: str):
        if self.name != new_name:
            self.name = new_name
        else:
            "Name cannot be the same."
        return self.name
 
    def change_due_date(self, new_date: str):
        if self.due_date != new_date: 
            self.due_date = new_date
        else:
             "Date cannot be the same."
        return self.due_date
 
    def add_comment(self, comment: str):
        self.comments.append(comment)
        return comment
 
    def edit_comment(self, comment_number: int, new_comment: str):
        if self.comments and comment_number < len(self.comments):
            self.comments[comment_number] = new_comment
            return ', '.join(self.comments)
        else:
            return "Cannot find comment"
 
    def details(self):
        return f'Name: {self.name} - Due Date: {self.due_date}'