#LAB IA DNA REPLACE 
#llpassarelli 2019

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.widget import *
from kivy.uix.gridlayout import *

word_code = "ATGATCTCGTAA"
word_template = "TACTAGAGCATT"

def codante(str):
	return str.replace("T","U")

def model(str):
	rep=""
	for l in str:
		if l == "T":
			l.replace("T","A")
		elif l =="A":
			l.replace("A","U")
		elif l == "C":
			l.replace("C","G")
		elif l == "G":
			l.replace("G","C")
		rep = rep+l
	return rep

def on_enter(instance, value):
	print('User pressed enter in', instance)	

def btn_codante_click(self):
	#print('The button <%s> is being pressed' % instance.text)
	print('text= %s' % self.textinput.text)
	self.textinput1.text = codante(self.textinput.text)

def btn_modelo_click(self):
	#print('The button <%s> is being pressed' % instance.text)
	print('text= %s' % self.textinput.text)
	self.textinput1.text = model(self.textinput.text)

class TestApp(App):
    def build(self):
		self.title = 'LLPASSARELLI - DNA - TEST'
		self.layout = GridLayout(rows=2, cols=2)
		self.textinput = TextInput(text='%s\n%s' % (word_template, word_code), multiline=False)
		self.textinput.bind(on_text_validate=on_enter)
		self.button = Button(text='Codante', on_press=lambda *a:btn_codante_click(self))
		self.button1 = Button(text='Modelo', on_press=lambda *a:btn_modelo_click(self))
		self.textinput1 = TextInput(text='OUTPUT', multiline=False)
		self.layout.add_widget(self.textinput)
		self.layout.add_widget(self.textinput1)
		self.layout.add_widget(self.button)
		self.layout.add_widget(self.button1)
		return self.layout    

TestApp().run()