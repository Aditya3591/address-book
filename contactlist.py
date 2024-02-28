import csv
import json
class Contact:
    
    def __init__(self,first_name,last_name,addres,city,state,zip,phn_num,email):

        self.first_name=first_name
        self.last_name=last_name
        self.addres=addres
        self.city=city
        self.state=state
        self.zip=zip
        self.phn_num=phn_num
        self.email=email

    def display(self):
        print("first name: ",self.first_name)
        print("last name: ",self.last_name)
        print("addres: ",self.addres)
        print("city: ",self.city)
        print("state: ",self.state)
        print("zip: ",self.zip)
        print("phone number: ",self.phn_num)
        print("email id: ",self.email)
        
    # def __repr__(self) -> str:
        
    #     return f"\nfirst name : {self.first_name}\nlast name: {self.last_name}\naddress : {self.addres}\ncity : {self.city}\nstate :{self.state}\nzip: {self.zip}\nphn number: {self.phn_num}\nemail: {self.email}"
        
class Addressbook:

    def __init__(self, name):
        self.name = name
        self.contact_list={}

    def add_contact(self, contact_obj):
        self.contact_list[contact_obj.first_name] = contact_obj

    def update_contact(self,first_name):
         if first_name in self.contact_list:
            contact=self.contact_list[first_name]
            print("enter the details (press enter to keep the existing value)")
            
            new_l_name = input(f"Last Name ({contact.last_name}): ") or contact.last_name
            new_address = input(f"Address ({contact.addres}): ") or contact.addres
            new_city = input(f"City ({contact.city}): ") or contact.city
            new_state = input(f"State ({contact.state}): ") or contact.state
            new_zip = input(f"Zip Code ({contact.zip}): ") or contact.zip
            new_phn_num = input(f"Phone Number ({contact.phn_num}): ") or contact.phn_num
            new_email = input(f"Email ({contact.email}): ") or contact.email

            # Update contact details
            contact.last_name = new_l_name
            contact.address = new_address
            contact.city = new_city
            contact.state = new_state
            contact.zip = new_zip
            contact.phn_num = new_phn_num
            contact.email = new_email
            print("Contact edited successfully.")
         else:
            print("Contact not found.")

    def show_cont_with_city_or_state(self,location):
            contact_list1=[]
            for contact in self.contact_list.values():
                if contact.city.lower()==location.lower() or contact.state.lower()==location.lower():
                    contact_list1.append(contact)
            return contact_list1
        #  if (city in self.contact_list.values()  or state in self.contact_list.values()):
        #     # self.contact_list[state]
        #      print("shown bir")
            

    def display_contacts(self):
        
        for obj in self.contact_list.values():
            obj.display()

    def delete_contact(self,first_name):
        if first_name in self.contact_list:
            del self.contact_list[first_name]
            print("contact deleted successfuly")
        else:
            print("invalid input")
    
    #     try:
    #         with open(f"{filename}.csv",'w',newline=' ') as file:
    #             fieldname=['first name','last name','address','city','state','zip','phone number','email']
    #             writer = csv.DictWriter(file, fieldnames=fieldname)
    #             writer.writeheader()
    #             for contact in self.contact_list.values():
    #                 writer.writerow(contact)

    #             reader=csv.DictReader(file)
    #             for data in reader:
    #                 print(data)

    #     except FileNotFoundError:
    #         print("file not found")

class AddressSystem:

    def __init__(self):

        self.address_book_dict={}
    
    def add_address_book_dict(self,book_obj):
        self.address_book_dict[book_obj.name] = book_obj

    def delete_address_book(self,name):
        del self.address_book_dict[name]
        print("the book is deleted successfully")

    def get_address_book_name(self,name):
        return self.address_book_dict.get(name)
    def display(self):
        return self.address_book_dict
    
    def convert_to_csv_file(self, book_name):
        try:
            book = self.address_book_dict.get(book_name)
            if book:
                print(f"Contacts in {book_name} address book:")
                book.display_contacts()  

                
                with open('addresbook.csv', 'w', newline='') as file:
                    fieldnames = ['first_name', 'last_name', 'addres', 'city', 'state', 'zip', 'phn_num', 'email']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    for contact in book.contact_list.values():
                        writer.writerow(vars(contact))  

                print(f"{book_name} address book converted to CSV successfully.")
            else:
                print(f"Address book '{book_name}' not found.")
        except FileNotFoundError:
            print("File not found.")


    def convert_to_json_file(self,bookname):
        try:
            book=self.address_book_dict.get(book_name)
            if book:
                print(f"contacts in {book_name} address book :")
                book.display_contacts()

                with open('addressbook1.json','w',) as file:
                    contacts_data=[]
                    for contact in book.contact_list.values():
                        contacts_data.append(vars(contact))
                        
                    json.dump(contacts_data,file,indent=4)
                      
                    file.write('\n')
                        
            else:
                print("addres book not found")
        except FileNotFoundError:
            print("File not found")
    


 

if __name__ == '__main__':
    print ("Welcome to address book system")
    multi_book=AddressSystem()
    while True:
        print("1 to add address book name ")
        print("2 to enter an update  a address book name ")
        print("3 to get address book name ")
        print("4 To convert it into csv file")
        print("5 to convert to json file")
        print("6 to exit")
        
        choice=input("enter your choice")
        if choice=='1':

            book_name=input("enter the address book name :")
            book = multi_book.get_address_book_name(book_name)
            if not book:
                book = Addressbook(book_name)
            # create contact obj
            
            contact=Contact('Aditya','Singh','bradh','jsr','jharkhand','831004','89697454','aditya12@gmail.com')
            
            
            book.add_contact(contact) 
            multi_book.add_address_book_dict(book)
            print(multi_book.display())
               

        elif choice=='2':
             name=input("enter the address book name")
             book=multi_book.get_address_book_name(name)
             book_loop='yes'
             while(book_loop!='no'):
                print("\n1 to add contact")
                print("2 to update contact")
                print("3 to display contact")
                print("4 to del contact") 
                print("5 to show contact using city or state")
                print("7 to exit")

                choice=input("enter your choice: ")

                if choice=='1':

                    first_name=input("Enter your first name: ")
                    last_name=input("Enter your last name: ")
                    addres=input("Enter your address: ")
                    city=input("Enter your city: ")
                    state=input("Enter your state: ")
                    zip=input("Enter your pincode: ")
                    phn_num=input("Enter your phone number: ")
                    email=input("Enter your email id: ")
                

                    contact=Contact(first_name,last_name,addres,city,state,zip,phn_num,email)
            
                    book.add_contact(contact)
                    print(book.contact_list)

                elif choice=='2':

                    first_name=input("enter the name of the contact first name to edit the contact details: ")
                    book.update_contact(first_name)
                elif choice=='3':

                    book.display_contacts()

                elif choice=='4':


                    first_name=input("enter the first name to delete the contact: ")
                    book.delete_contact(first_name)
                elif choice== '5':
                    
                    location=input("enter city or state to retrive info: ")
                    contacts=book.show_cont_with_city_or_state(location)

                    if contacts:
                            print(f"Contacts in {location}:")
                            for contact in contacts:
                                print(contact.display())
                    else:
                            print(f"No contacts found in {location}.")
                

                # elif choice=='6':

                #     file_name=input("enter the csv file name ")
                #     book.convert_to_csv_file(file_name)
                elif choice=='7':
                    print("Exiting....")
                    break
                else:
                    print("invalid choice")

        elif choice=='3':
            book_name=input("enter the addres book name")
            print(multi_book.get_address_book_name(book_name))

            
        elif choice == '4':
            book_name = input("Enter the address book name to convert to CSV: ")
            multi_book.convert_to_csv_file(book_name)
                        
        elif choice=='5':
            book_name=input("enter the address book name:")
            multi_book.convert_to_json_file(book_name)

        elif choice=='6':
            print("Exiting....")
            break