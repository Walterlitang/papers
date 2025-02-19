import random
import time

# 鱼类配置（名称、稀有度、基础价格）
fish_data = {
    "小池塘": [
        {"name": "鲤鱼", "rarity": 1, "price": 10},
        {"name": "鲫鱼", "rarity": 1, "price": 15},
        {"name": "泥鳅", "rarity": 2, "price": 30},
    ],
    "湖泊": [
        {"name": "鲈鱼", "rarity": 2, "price": 50},
        {"name": "鳟鱼", "rarity": 3, "price": 100},
        {"name": "鲶鱼", "rarity": 2, "price": 40},
    ],
    "大海": [
        {"name": "金枪鱼", "rarity": 3, "price": 200},
        {"name": "鲨鱼", "rarity": 4, "price": 500},
        {"name": "旗鱼", "rarity": 3, "price": 150},
    ]
}

# 鱼饵配置（名称、价格、钓鱼加成）
baits = {
    "面包": {"price": 0, "power": 1},
    "蚯蚓": {"price": 20, "power": 2},
    "虾米": {"price": 50, "power": 3},
}

class Player:
    def __init__(self):
        self.gold = 100  # 初始金币
        self.backpack = []  # 背包存储钓到的鱼
        self.current_bait = "面包"  # 当前使用的鱼饵

# 游戏开场
def game_intro():
    print("欢迎来到可交易钓鱼游戏！")
    print("你可以钓鱼、出售鱼获，并用金币购买更好的鱼饵！\n")

# 显示玩家状态
def show_status(player):
    print(f"\n当前金币：{player.gold} | 当前鱼饵：{player.current_bait}")
    print("背包中的鱼：")
    if not player.backpack:
        print("空空如也...")
    else:
        for fish in player.backpack:
            print(f"- {fish['name']}（价值{fish['price']}金币）")

# 钓鱼逻辑
def go_fishing(player, location):
    print("\n开始钓鱼...")
    time.sleep(2)
    
    # 根据鱼饵计算成功率
    bait_power = baits[player.current_bait]["power"]
    success_rate = bait_power * 15  # 基础成功率
    
    if random.randint(1, 100) <= success_rate:
        fish = random.choice(fish_data[location])
        print(f"钓到了一条 {fish['name']}！价值{fish['price']}金币！")
        player.backpack.append(fish)
    else:
        print("这次一无所获...")

# 交易市场
def open_market(player):
    while True:
        print("\n===== 交易市场 =====")
        print("1. 出售所有鱼获")
        print("2. 购买鱼饵")
        print("3. 返回主菜单")
        choice = input("请输入选项：")
        
        if choice == "1":
            if not player.backpack:
                print("背包里没有鱼可出售！")
            else:
                total = sum(fish["price"] for fish in player.backpack)
                player.gold += total
                print(f"出售了所有鱼获，获得{total}金币！")
                player.backpack = []
        
        elif choice == "2":
            print("\n可购买的鱼饵：")
            for idx, (bait, info) in enumerate(baits.items(), 1):
                print(f"{idx}. {bait}（价格：{info['price']}金币，钓鱼加成：+{info['power']}）")
            try:
                bait_choice = int(input("请输入要购买的鱼饵编号："))
                bait = list(baits.keys())[bait_choice-1]
                if player.gold >= baits[bait]["price"]:
                    player.gold -= baits[bait]["price"]
                    player.current_bait = bait
                    print(f"已更换鱼饵为：{bait}！")
                else:
                    print("金币不足！")
            except:
                print("输入无效！")
        
        elif choice == "3":
            break

# 主游戏循环
def main_game():
    player = Player()
    game_intro()
    
    while True:
        show_status(player)
        print("\n===== 主菜单 =====")
        print("1. 去钓鱼")
        print("2. 交易市场")
        print("3. 退出游戏")
        choice = input("请输入选项：")
        
        if choice == "1":
            print("\n选择钓鱼地点：")
            locations = list(fish_data.keys())
            for idx, loc in enumerate(locations, 1):
                print(f"{idx}. {loc}")
            try:
                loc_choice = int(input("请输入地点编号："))
                location = locations[loc_choice-1]
                go_fishing(player, location)
            except:
                print("输入无效！")
        
        elif choice == "2":
            open_market(player)
        
        elif choice == "3":
            print("感谢游玩，再见！")
            break

# 启动游戏
if __name__ == "__main__":
    main_game()
