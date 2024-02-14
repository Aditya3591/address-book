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
        
    
contact1=Contact("aditya","singh","vijaya garden","jsr","jharkhand","831017","8969745425","aditasinghi12@gmail.com")
contact1.display()