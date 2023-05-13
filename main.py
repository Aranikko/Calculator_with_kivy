from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class MainWidget(GridLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
    variable = True
    stack = False
    subtract = False
    multiply = False
    divide = False
        
    value_1 = StringProperty()
    value_2 = str()
    int_value_1 = 0
    
    def if_zero_press(self):
        if self.variable:
            self.value_1 += str(0)
        else:
            self.value_2 += str(0)
            self.value_1 += str(0)
            
    def if_one_press(self):
        if self.variable:
            self.value_1 += str(1)
        else:
            self.value_2 += str(1)
            self.value_1 += str(1)

    def if_two_press(self):
        if self.variable:
            self.value_1 += str(2)
        else:
            self.value_2 += str(2)
            self.value_1 += str(2)

    def if_three_press(self):
        if self.variable:
            self.value_1 += str(3)
        else:
            self.value_2 += str(3)
            self.value_1 += str(3)
            
    def if_four_press(self):
        if self.variable:
            self.value_1 += str(4)
        else:
            self.value_2 += str(4)
            self.value_1 += str(4)
            
    def if_five_press(self):
        if self.variable:
            self.value_1 += str(5)
        else:
            self.value_2 += str(5)
            self.value_1 += str(5)
            
    def if_six_press(self):
        if self.variable:
            self.value_1 += str(6)
        else:
            self.value_2 += str(6)
            self.value_1 += str(6)
    
    def if_seven_press(self):
        if self.variable:
            self.value_1 += str(7)
        else:
            self.value_2 += str(7)
            self.value_1 += str(7)
            
    def if_eight_press(self):
        if self.variable:
            self.value_1 += str(8)
        else:
            self.value_2 += str(8)
            self.value_1 += str(8)
            
    def if_nine_press(self):
        if self.variable:
            self.value_1 += str(9)
        else:
            self.value_2 += str(9)
            self.value_1 += str(9)
    
    def if_stack_press(self):
        self.variable = False
        self.int_value_1 = int(self.value_1)
        self.stack = True
        self.value_1 += " + "
    
    def if_subtract_pess(self):
        self.variable = False
        self.int_value_1 = int(self.value_1)
        self.value_1 += " - "
        self.subtract = True
    
    def if_multiply_press(self):
        self.variable = False
        self.int_value_1 = int(self.value_1)
        self.value_1 += " * "
        self.multiply = True
        
    def if_divide_press(self):
        self.variable = False
        self.int_value_1 = int(self.value_1)
        self.value_1 += " / "
        self.divide = True
        
    
    def if_equal_press(self):
        if self.stack and self.value_2 >= '0':
            self.value_1 = str(self.int_value_1+int(self.value_2))
            self.stack = False
        if self.subtract and self.value_2 >= '0':
            self.value_1 = str(self.int_value_1-int(self.value_2))
            self.subtract = False
        if self.multiply and self.value_2 >= '0':
            self.value_1 = str(self.int_value_1*int(self.value_2))
            self.multiply = False
        if self.divide and self.value_2 >= '1':
            self.value_1 = str(self.int_value_1/int(self.value_2))
            self.divide = False
        if self.divide and self.value_2 == '0':
            self.value_1 = "Error"
            self.divide = False
    
    def if_Clear_press(self):
        self.variable = True
        self.stack = False
        self.subtract = False
        self.multiply = False
        self.divide = False
            
        self.value_1 = str()
        self.value_2 = str()
        self.int_value_1 = 0
    
class CalculatorApp(App):
    pass

CalculatorApp().run()