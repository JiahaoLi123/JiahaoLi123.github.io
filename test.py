print("请输入该业务员等级\n")
grad=input() #输入等级
print("请输入业务员姓名\n")
name = input()
if grad =='A' :
    print(name+"一级,应发奖金10000元")
elif grad =="B" :
    print(name+"二级,应发奖金9000元") 
elif grad =='C' :
    print(name + "三级,应发奖金8000元")
elif grad=='D' :
    print(name+ "四级，应发奖金7000元")   

