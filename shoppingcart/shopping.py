product_list=[
    ('Iphone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',31),
    ('Python',120),
]
shopping_list = []
salary=input("Input you salary:")   #让用户输入工资
if salary.isdigit():         #判断用户输入是否为int类型
    salary=int(salary)
    while True:         #进入死循环
        for index, item in enumerate(product_list):       #使用enumerate将商品和他的下标取出来   index是他的下标,item是他的数据
            print(index,item)                             #打印商品列表和下标
        '''
        for item in product_list:
            print(product_list.index(item),item)
            '''
        #break
        user_choice = input("选择要买的是东西>>>:")       #用户选择买的商品
        if user_choice.isdigit():              #判断用户的输入是否为数字类型
            user_choice=int(user_choice)       #如果用户输入的不是数字类型,将其转换为数字类型
            if user_choice<len(product_list) and user_choice>=0:    #判断用户输入的商品的值是否在商品范围内
                p_item=product_list[user_choice]  #通过用户输入的下标将商品取出来
                if p_item[1]<=salary:       #如果价格<工资  代表买得起
                    shopping_list.append(p_item)     #能买的起后将商品添加到商品的list中
                    salary -=p_item[1]         #扣钱
                    print("Added %s into shopping cart,you currect balance is \033[31;1m%s\033[0m" % (p_item,salary))    #将商品打印出来
                else:
                    print("\033[41;1m你的余额不足,只剩[%s]元]\033[0m" % salary)    #如果钱不够的话  打印出error massage
            else:
                print("product code [%s] is not exist!" %user_choice)      #如果用户输入的商品的下标不在商品列表中的话 打印出的error massage
        elif user_choice=='q':
            print('---------shopping list ---------')       #用户退出时 打印出购买完成后的剩下的余额
            for p in shopping_list:
                print("you current balance: ",salary)
                exit()
        else:
            print('invalid option')   #如果用户一开始输入的工资不是数字时,输出报错信息
