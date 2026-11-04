import random
def create_rnd_seq(loops): 
    file=open('results/Out_RandProtSeq.txt','w')
    ran_loops=0
    length=150
    while ran_loops < loops:
        file.write("\n\t")
        times_non_poler = 0
        times_poler = 0
        times_positive = 0
        times_negative = 0
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
        file.write("loop number:"+str(ran_loops)+"\n\t")
        while num_in < length:
            if num_in ==0:
                file.write("M")
                non_poler_cont=non_poler_cont+1
                num_in = num_in+1
            elif non_poler_cont == 75 and times_non_poler == 0:
                times_non_poler=times_non_poler+1
                amino_attrabute_list.remove("non_poler")
            elif poler_cont == 45 and times_poler == 0:
                times_poler = times_poler+1
                amino_attrabute_list.remove("poler")
            elif positive_cont == 15 and times_positive == 0:
                times_positive = times_positive+1
                amino_attrabute_list.remove("positive_charge")
            elif negative_cont == 15 and times_negative == 0:
                times_negative= times_negative+1
                amino_attrabute_list.remove("negative_charge")
            else:
                num_in=num_in+1
                choise=random.choice(amino_attrabute_list)
                if choise == "non_poler":
                    non_poler_cont=non_poler_cont+1
                    file.write(random.choice(non_poler_list))
                elif choise == "poler":
                    poler_cont=poler_cont+1
                    file.write(random.choice(poler_list))
                elif choise == "positive_charge":
                    positive_cont = positive_cont+1
                    file.write(random.choice(positive_charge_list))
                elif choise == "negative_charge":
                    negative_cont = negative_cont+1
                    file.write(random.choice(negative_charge_list))
    file.close()


loops = int(input ("give number of loops (no more then 1000)"))
if loops <= 1000 and loops>0 :
    create_rnd_seq(loops)
else:
    print ("eror number not supported")