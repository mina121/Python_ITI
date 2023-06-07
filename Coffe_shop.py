
def search(ID_Costomr):
    flag=False
    for p in list_of_climent:
        if p["ID"] == ID_Costomr :
            flag=True
            return p           
    return flag
      

list='''
    ****************************************************************************
                           Wellcom to Pachinous Coffe
    ****************************************************************************
        
        MENU:                                             
            1- Flat White                                  85 $
            2- Caramel Macchiato                           95 $
            3- Caffe Mocha                                 65 $
            4- Caffe Latte                                 80 $
            5- COFFE_MIX                                   50 $
            6- Cappuccino                                  40 $
            7- French Press                                70 $
            8- Chocolate Cappuccino                        55 $
            9- Green Tea                                   30 $
            10- Espresso Fusion                            60 $


            0- To Exit!!!!!!!!!!!!!!
                  '''

dic_list={
    1:   85,
    2:   95,
    3:   65,
    4:   80,
    5:   50,
    6:   40,
    7:   70,
    8:   55,
    9:   30,
    10:  60

}
welc='''
    ****************************************************************************
                           Wellcom to Pachinous Coffe
    ****************************************************************************
    '''  
while True:
   print(welc)
   sum_drink=0
   list_of_climent=[]
   ID_Costomr=input("Your ID  ->  ")
   
   while True:
      print(list)
      drink=int(input("your choice is -> "))
      if drink==0:
          break
      elif drink>10:
          continue
      sum_drink +=dic_list[drink]
      Costomr_Dic={
          "ID"      :ID_Costomr,
          "Drinkes" :sum_drink,
      }
      list_of_climent.append(Costomr_Dic)
      print("sum of drinkes = {}".format(sum_drink))
   