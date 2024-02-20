class Contact:
    
    def __init__(self,f_name,l_name,addres,city,state,zip,phn_num,email):

        self.f_name=f_name
        self.l_name=l_name
        self.addres=addres
        self.city=city
        self.state=state
        self.zip=zip
        self.phn_num=phn_num
        self.email=email

    def display(self):
        print("first name: ",self.f_name)
        print("last name: ",self.l_name)
        print("addres: ",self.addres)
        print("city: ",self.city)
        print("state: ",self.state)
        print("zip: ",self.zip)
        print("phone number: ",self.phn_num)
        print("email id: ",self.email)
        
    
#contact1=Contact("aditya","singh","vijaya garden","jsr","jharkhand","831017","8969745425","aditasinghi12@gmail.com")
#contact1.display()
    def __repr__(self) -> str:
        
        return f"\nfirst name : {self.f_name}\nlast name: {self.l_name}\naddress : {self.addres}\ncity : {self.city}\nstate :{self.state}\nzip: {self.zip}\nphn number: {self.phn_num}\nemail: {self.email}"
        
class Addressbook:

    def __init__(self):
        self.contact_list={}

    def add_contact(self, contact_obj):
        self.contact_list[contact_obj.f_name] = contact_obj

    def update_contact(self,f_name):
         if f_name in self.contact_list:
            contact=self.contact_list[f_name]
            print("enter the details (press enter to keep the existing value)")
            
            new_l_name = input(f"Last Name ({contact.l_name}): ") or contact.l_name
            new_address = input(f"Address ({contact.addres}): ") or contact.addres
            new_city = input(f"City ({contact.city}): ") or contact.city
            new_state = input(f"State ({contact.state}): ") or contact.state
            new_zip = input(f"Zip Code ({contact.zip}): ") or contact.zip
            new_phn_num = input(f"Phone Number ({contact.phn_num}): ") or contact.phn_num
            new_email = input(f"Email ({contact.email}): ") or contact.email

            # Update contact details
            contact.l_name = new_l_name
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

    def delete_contact(self,f_name):
        if f_name in self.contact_list:
            del self.contact_list[f_name]
            print("contact deleted successfuly")
        else:
            print("invalid input")

if __name__ == '__main__':
     
    address=Addressbook()
    
    while True:
        print("\n1 to add contact")
        print("2 to update contact")
        print("3 to display contact")
        print("4 to del contact") 
        print("5 to show contact using city or state")
        print("6 To EXIT")

        choice=input("enter your choice: ")

        if choice=='1':

            f_name=input("Enter your first name: ")
            l_name=input("Enter your last name: ")
            addres=input("Enter your address: ")
            city=input("Enter your city: ")
            state=input("Enter your state: ")
            zip=input("Enter your pincode: ")
            phn_num=input("Enter your phone number: ")
            email=input("Enter your email id: ")
        

            contact=Contact(f_name,l_name,addres,city,state,zip,phn_num,email)
    
            address.add_contact(contact)
            print(address.contact_list)

        elif choice=='2':

            f_name=input("enter the name of the contact first name to edit the contact details: ")
            address.update_contact(f_name)
        elif choice=='3':

            address.display_contacts()

        elif choice=='4':


            f_name=input("enter the first name to delete the contact: ")
            address.delete_contact(f_name)
        elif choice== '5':
            
            location=input("enter city or state to retrive info: ")
            contacts=address.show_cont_with_city_or_state(location)

            if contacts:
                    print(f"Contacts in {location}:")
                    for contact in contacts:
                        print(contact.display())
            else:
                    print(f"No contacts found in {location}.")
        elif choice=='6':
            print("Exiting....")
            break
        else:
            print("invalid choice") 