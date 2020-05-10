from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen


class Calculator(Screen):

    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)

    def calculate(self):
        income = int(self.ids.income.text)
        partner = int(self.ids.partner.text)
        expenses = str(self.ids.expenses.text)

        if expenses == float or "+":

            expenses_list = expenses.split("+")

            li = []
            for i in expenses_list:
                li.append(int(i))
            expenses_total = sum(li)

            if income and partner and expenses_total == int or float:
                joint_expenditure = (income + partner)
                your_percentage = (income / joint_expenditure)
                partner_percentage = (partner / joint_expenditure)

                you_pay = round((your_percentage * expenses_total))
                partner_pay = round((partner_percentage * expenses_total))

                popup = Popup(
                    title='Results',
                    content=Label
                    (text=
                     "Your share of the expenses is: " + str(you_pay) +
                     "\nYour partner's is: " + str(partner_pay)))
                popup.open()
        else:
            popup = Popup(
                title='Error',
                content=Label
                (text="You've entered invalid information in the expenses tab. Only '+' and numbers are allowed "
                 ))
            popup.open()

    def clear(self):
        self.ids.partner.text = ""
        self.ids.income.text = ""
        self.ids.expenses.text = ""


starter = Builder.load_file("my.kv")


class MyApp(App):
    def build(self):
        return starter


if __name__ == '__main__':
    MyApp().run()
