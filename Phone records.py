from tkinter import *
import psycopg2
# tkinter window
window = Tk()
window.title("Mobile Details")
window.configure(background="black")


conn = psycopg2.connect(dbname="Phones", user="postgres",
                        password='1234', host="localhost", port="5432")
print(conn)
cursor = conn.cursor()
# creating tables
#create_tables = "CREATE TABLE phone_details(Mobile_Name VARCHAR(255),Model_Name VARCHAR(255),PRICE VARCHAR(200))"
# cursor.execute(create_tables)
# conn.commit()


def click():
    name = text_entry1.get()
    text_entry1.delete(0, END)
    model = text_entry2.get()
    text_entry2.delete(0, END)
    price = text_entry3.get()
    text_entry3.delete(0, END)
    Data_to_insert = "INSERT INTO phone_details(Mobile_name,Model_name,PRICE) VALUES(%s,%s,%s)"
    values = (name, model, price)
    cursor.execute(Data_to_insert, values)
    conn.commit()
    print(name)


#label1 and entry1
label1 = Label(window, text="Enter Brand Name:", bg="black",
               fg="#0D7E84", font="none 12 bold").grid(row=0, column=0, sticky=W)

text_entry1 = Entry(window, width=40, bg="white")

text_entry1.grid(row=0, column=1, sticky=W)

# label2 and entry 2
label2 = Label(window, text="Enter Model Name:", bg="black",
               fg="#0D7E84", font="none 12 bold").grid(row=1, column=0, sticky=W)
text_entry2 = Entry(window, width=40)
text_entry2.grid(row=1, column=1, sticky=W)

# Label3 and entry 3
label3 = Label(window, text="Enter Phone Price:", bg="black",
               fg="#0D7E84", font="none 12 bold").grid(row=2, column=0, sticky=W)
text_entry3 = Entry(window, width=40, bg="white")
text_entry3.grid(row=2, column=1, sticky=W)

# button
Button(window, text="SUMBIT", width=10, bg="red",
       fg="white", command=click).grid(row=3, column=1, sticky=W)

window.mainloop()
