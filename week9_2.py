import tkinter as tk
from tkinter import ttk

class FeedbackForm(tk.Tk):

    def __init__(self):
        super().__init__()

        # Creating window
        self.title('Feedback form')
        self.resizable(0, 0)
        self.geometry('230x215')
        self['bg'] = 'lightblue'

        # label for first name
        self.labelFName = ttk.Label(
            self,
            text='First name',
            background='lightblue',
            font = ('Digital-7', 13))

        # label for last name
        self.labelLName = ttk.Label(
            self,
            text='Last name',
            background='lightblue',
            font = ('Digital-7', 13))

        # label for email
        self.labelEmail = ttk.Label(
            self,
            text='Email',
            background='lightblue',
            font = ('Digital-7', 13))

        # label for phone number
        self.labelPNum = ttk.Label(
            self,
            text='Phone num.',
            background='lightblue',
            font = ('Digital-7', 13))

        # label for checking fields
        self.submitted = ttk.Label(
            self,
            text='',
            background='lightblue',
            font = ('Digital-7', 10))

        # entry for first name
        self.entryFName = ttk.Entry(
            self,
            width='10',
            font=('Digital-7', 13))

        # entry for last name
        self.entryLName = ttk.Entry(
            self,
            width='10',
            font=('Digital-7', 13))

        # entry for email
        self.entryEmail = ttk.Entry(
            self,
            width='10',
            font=('Digital-7', 13))

        # entry for phone number
        self.entryPNum = ttk.Entry(
            self,
            width='10',
            font=('Digital-7', 13))

        # button for submitting form
        self.submitForm = ttk.Button(
            self,
            text='Submit',
            command=lambda:self.submit_Form())
        
        # placements
        self.labelFName.place(x=10, y=15)
        self.entryFName.place(x=115, y=15)
        self.labelLName.place(x=10, y=50)
        self.entryLName.place(x=115, y=50)
        self.labelEmail.place(x=10, y=85)
        self.entryEmail.place(x=115, y=85)
        self.labelPNum.place(x=10, y=120)
        self.entryPNum.place(x=115, y=120)
        self.submitForm.place(x=80, y=180)

    def submit_Form(self):
        if self.check_Entries() == True:
            self.submitted.place(x=35, y=155)
            self.submitted.configure(text='Form submitted successfully')
        else:
            self.submitted.place(x=50, y=155)
            self.submitted.configure(text='All fields must be filled')

    def check_Entries(self):
        if len(self.entryFName.get()) != 0 and len(self.entryLName.get()) != 0 and len(self.entryEmail.get()) != 0 and len(self.entryPNum.get()) != 0:
            return True
        else:
            return False


if __name__ == "__main__":
    form = FeedbackForm()
    form.mainloop()