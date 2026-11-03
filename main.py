import random
def create_rnd_seq(loops): 
    file=open('results/Out_RandProtSeq.txt','w')
    ran_loops=0
    length=150
    while ran_loops < loops:
        num_in=0
        ran_loops=ran_loops+1
        amino_attrabute_list = ["non_poler", "positive_charge", "negative_charge","poler"]
        file.write("loop number:"+ran_loops)
        while num_in < length:
            if num_in ==0:
                file.write("M")
            else:
                choise=random.choice(amino_attrabute_list)
                if 
                




loops = input("give number of loops (no more then 1000)")
if loops < 1000 and loops>0 :
    create_rnd_seq(loops)