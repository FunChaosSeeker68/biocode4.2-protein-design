import random
def create_rnd_seq(loops): 
    file=open('results/Out_RandProtSeq.txt','w')
    ran_loops=0
    length=150
    while ran_loops < loops:
        num_in=0
        non_poler_cont=0
        poler_cont=0
        positive_cont=0
        negative_cont=0
        ran_loops=ran_loops+1
        amino_attrabute_list = ["non_poler", "positive_charge", "negative_charge","poler"]
        non_poler_list = ["A", "V", "L", "I", "P", "F", "M", "W", "G", "C"]
        poler_list = ["N" , "Q", "S", "T", "Y"]
        positive_charge_list = ["K" , "R" , "H"]
        negative_charge_list = ["D" , "E"]
        file.write("loop number:"+ran_loops)
        while num_in < length:
            if num_in ==0:
                file.write("M")
                non_poler_cont=non_poler_cont+1
                num_in = num_in+1
            elif non_poler_cont == 75:
                amino_attrabute_list.remove("non_poler")
            elif poler_cont == 45:
                amino_attrabute_list.remove("poler")
            elif positive_cont == 15:
                amino_attrabute_list.remove("positive_charge")
            elif negative_cont == 15:
                amino_attrabute_list.remove("negative_charge")
            else:
                num_in=num_in+1
                choise=random.choice(amino_attrabute_list)
                if choise == "non_poler":
                    file.write(random.choice(non_poler_list))
                elif choise == "poler":
                    file.write(random.choice(poler_list))
                elif choise == "positive_charge":
                    file.write(random.choice(positive_charge_list))
                elif choise == "negative_charge":
                    file.write(random.choice(negative_charge_list))



loops = input("give number of loops (no more then 1000)")
if loops < 1000 and loops>0 :
    create_rnd_seq(loops)