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


if __name__ == '__main__':
    contact=Contact('aditya','singh','baridh','jamshedpur','jharkhand','831017','8969745425','aditya12@gmail.com')
    address=Addressbook()
    address.add_contact(contact)
    print(address.contact_list)