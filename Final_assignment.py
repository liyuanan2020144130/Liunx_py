from random import randint
import time,sys

# 玩家
class Player:

    def __init__(self,stoneNumber):
        self.stoneNumber = stoneNumber # 灵石数量
        self.warriors = {}  # 拥有的战士，包括弓箭兵和斧头兵

# 战士
class Warrior:

    # 初始化参数是生命值
    def __init__(self, strength):
        self.strength = strength

    # 用灵石疗伤
    def healing(self, stoneCount):
        # 如果已经到达最大生命值，灵石不起作用，浪费了
        if self.strength == self.maxStrength:
            return

        self.strength =self.strength + stoneCount

        # 不能超过最大生命值
        if self.strength > self.maxStrength:
            self.strength = self.maxStrength


# 弓箭兵 是 战士的子类
class Archer(Warrior):
    # 种类名称
    typeName = '弓箭兵'

    # 雇佣价 100灵石，属于静态属性
    price = 100

    # 最大生命值 ，属于静态属性
    maxStrength = 100


    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength =self.strength - 20
        elif monster.typeName== '狼妖':
            self.strength = self.strength - 80
        else:
            print('未知类型的妖怪！！！')



# 斧头兵 是 战士的子类
class Axeman(Warrior):
    # 种类名称
    typeName = '斧头兵'

    # 雇佣价 120灵石
    price = 120

    # 最大生命值
    maxStrength = 120


    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength = self.strength - 80
        elif monster.typeName== '狼妖':
            self.strength -=self.strength - 20
        else:
            print('未知类型的妖怪！！！')

# 鹰妖
class Eagle():
    typeName = '鹰妖'

# 狼妖
class Wolf():
    typeName = '狼妖'

# 森林
class Forest():
    def __init__(self,monster):
        # 该森林里面的妖怪
        self.monster = monster

print('***********************************\n')
print('***          游戏开始           ***\n')
print('***********************************\n')


# 森林数量
forest_num = 7

# 森林 列表
forestList = []

# 为每座森林随机产生 鹰妖或者 狼妖
notification = '前方森林里的妖怪是：'  # 显示在屏幕上的内容
for i in range(forest_num):
    typeName = randint(0,1)
    if typeName == 0:
        forestList.append( Forest(Eagle()) )
    else:
        forestList.append( Forest(Wolf()) )

    notification += \
        f'第{i+1}座森林里面是---{forestList[i].monster.typeName} '

# 显示 妖怪信息
print(notification)
#print(notification,end='')
i=0
while i<10:
    time.sleep(1)
    i+=1
  
for i in range(1,20):
    print('\n')
#创建玩家
Player1 = Player(1000)
print('你现在有灵石：',Player1.stoneNumber)

#雇佣战士流程
def hire_warrions():
    print('---------------------------')
    print('请选择雇佣的兵种：')
    print('1---弓箭兵')
    print('2---斧头兵')
    print('3---选择完成退出！')
    print('---------------------------')
    while 1:
        hire = input('请选择兵种：')
        if hire == '1':
            hireWarrion = Archer
        elif hire == '2':
            hireWarrion = Axeman
        elif hire == '3':
            return
        else:
            print('输入错误，请重新输入：')
            continue

        if Player1.stoneNumber < hireWarrion.price:
            print('你的灵石不足，只有:',Player1.stoneNumber)
            continue

   #给战士命名
        while 1:

            warrionName = input('输入战士名字：')
            if len(warrionName) == 0 :
                print('重新输入')
                continue
            elif warrionName in Player1.warriors :
                print('名字以存在！')
                continue

            break



        #招收战士
        Player1.warriors[warrionName] = hireWarrion(warrionName)

        #支付宝石
        Player1.stoneNumber -= hireWarrion.price
        print('雇佣成功！剩余宝石数为：',Player1.stoneNumber)

#雇佣兵
hire_warrions()

#打印出战士和宝石情况
def printinfo():
    print('战士情况如下：')
    for name,warrions in Player1.warriors.items():
        print(name,':',warrions.typeName,'生命值：',warrions.strength )

print('出发了！')

#每个森林关卡
for i,forest in enumerate(forestList):
    if not Player1.warriors:
        print('你没有战士')
        exit()

    print('现在到了第',i,1,'座森林')

    while 1:
        while 1:
            warrionName = input('输入派出的战士')

            if warrionName not in Player1.warriors:
                print('没有这个战士')
                continue
            break

        warrion = Player1.warriors[warrionName]
        print('当前森林里面是',forest.monster.typeName)

        warrion.fightWithMonster(forest.monster)
        print('经过战斗，你的战士',warrionName,'生命值还有',warrion.strength)

        #如果生命值小于0，该战士就牺牲了，从队伍中消失

        if warrion.strength <= 0:
            print('该战士牺牲')
            Player1.warriors.pop(warrionName)
            #没有战胜怪物，本关未过

            continue

            #战士生还，过关
        else:
            break
    input('过关，按回车建继续!!!')
    #过关后，选择给战士疗伤
    while 1:
        printinfo()

        op = input('输入疗伤的姓名和宝石数量，格式为：姓名+所要加宝石数回车')

        if not op:
            break

        if op.count('+')!=1:
            print('输入格式错误')
            continue

        name,stoneCount = op.split('+')
        if Player1.stoneNumber > int(stoneCount):
            Player1.warriors[warrionName].strength +=int(stoneCount)
            Player1.stoneNumber -=int(stoneCount)

        else:
            print('所剩余宝石数不足！')
        name = name.strip()

