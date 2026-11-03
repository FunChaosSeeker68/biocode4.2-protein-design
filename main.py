import random
def create_rnd_seq(loops): 
    file=open('results/Out_RandProtSeq.txt','w')
    ran_loops=0
    length=150
    for ran_loops < loops:
        num_in=0
        ran_loops=ran_loops+1
        file.write("loop number:"+ran_loops)
        for num_in < length:
            if num_in ==0:
                file.write("M")
            else:
                




loops = input("give number of loops (no more then 1000)")
