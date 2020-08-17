import tkinter as tkt
from tkinter import ttk
from tkinter import scrolledtext
import re

root = tkt.Tk()
root.title('Python Practice')

pl = {'string': str , 'list':list, 'dict' : dict , 'set': set}

# print(dir(tkt))
# print("###########################")
# print(dir(ttk))
var = tkt.StringVar()
objecttype = list
val = dir(objecttype)
val = list(filter(lambda x:not re.search('^[__|_].*[__|_]$' , x) , val ))
object = objecttype()
def do_classselector(event):
    global objecttype
    global val
    global object
    objecttype = pl[classselector.get()]
    var.set(f'practicing {classselector.get()}')
    val = dir(objecttype)
    val = list(filter(lambda x:not re.search('^[__|_].*[__|_]$' , x) , val ))
    print(val)
    methodbox['values'] = val
    object = objecttype()

classselector = ttk.Combobox(root , values = list(pl) , width = 15)
classselector.grid(row = 0 , column = 0)
classselector.bind('<<ComboboxSelected>>' , do_classselector)
#classselector.set('list')
#objecttype = pl[classselector.get()]

head = tkt.Label(textvariable = var )
var.set(f'practicing {classselector.get()}')
head.grid(row = 0 , column = 1 , columnspan = 3)




lable1 = tkt.Label(text = 'object' , width = 15)
lable1.grid(row = 1 , column = 0)

lable2 = tkt.Label(text = 'method' , width = 15)
lable2.grid(row = 1 , column = 1)

lable2 = tkt.Label(text = 'method arguments' , width = 15)
lable2.grid(row = 1 , column = 2)

objectvar = tkt.StringVar()

objectbox = tkt.Entry(root , textvariable = objectvar, width = 15 )
objectbox.grid(row =2 , column = 0 )



selectedmethod = 'None'

def addtext(*st):
    text_area.configure(state='normal')
    text_area.insert(tkt.INSERT,*st)
    text_area.configure(state='disable')

def do_combo(event):
    #object = eval(objectbox.get())
    # if not isinstance(object , objecttype):
    #     addtext(f'TypeErorr : given object is not of type \"{str(objecttype)}\"' , war)
    methodbox_value = methodbox.get()
    sig  =getattr(objecttype ,methodbox_value )
    func_arg.delete(0, tkt.END)
    addtext(sig.__doc__)
    addtext('\n')


methodbox = ttk.Combobox(root , values = []  , width = 15)
methodbox.grid(row =2 , column =1)
methodbox.bind('<<ComboboxSelected>>' , do_combo)

func_arg = tkt.Entry(root , width = 15  )
func_arg.grid(row = 2 , column = 2 )

def do_stuff():
    global object
    try: 
        object = eval(objectbox.get())
    except:
        addtext('Object cannot be empty \n' , 'war')
    if not isinstance(object, objecttype):
        addtext(f'Error : object type must be {classselector.get()}\n' , 'war')
    else:
        if methodbox.get() == '' or methodbox.get() ==  None:
            addtext('Error : please select any of the method to be performed' , 'war')
        if not func_arg.get():
            evalstring = f'object.{methodbox.get()}()'
        else:
            evalstring = f'object.{methodbox.get()}' +  f'({func_arg.get()})'
            print('i am here')
        try:
            print(evalstring)
            #print(func_arg.get())
            res = eval(evalstring)

            #print(object)
            addtext(f'The method returned = {res}\n' , 'result')
            objectbox.delete(0, tkt.END)
            objectbox.insert(0,str(object))
        except Exception as err:
            addtext(err , 'war')
            addtext('\n')

b1 = tkt.Button( root , text = 'Check' ,
               bg= 'green' , fg='white',
               font = ("Times New Roman",12,'bold'),command = do_stuff )
b1.grid(row =2 , column = 4)



text_area = scrolledtext.ScrolledText(root,
                                      wrap = tkt.WORD,
                                      width = 40,
                                      height = 10,
                                      font = ("Times New Roman",
                                              15))

text_area.grid(column = 0,row = 3 , columnspan = 4 ,pady = 10, padx = 10)
text_area.tag_config('war' , foreground = 'red')
text_area.tag_config('result' , foreground = 'green')
root.mainloop()
