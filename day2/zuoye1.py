# 课后作业练习 - 第一题：个人信息卡

# 定义变量
name = "张三"          # 姓名
age = 20               # 年龄
height = 175.5         # 身高（厘米）
is_student = True      # 是否为学生（布尔值）

# 1. 输出所有变量的值

print("个人信息卡")

print(f"姓名：{name}")
print(f"年龄：{age}")
print(f"身高：{height}")
print(f"是否为学生：{is_student}")
print()

# 2. 使用 type() 查看每个变量的数据类型

print("变量数据类型")
print(f"姓名的类型：{type(name)}")
print(f"年龄的类型：{type(age)}")
print(f"身高的类型：{type(height)}")
print(f"是否为学生的类型：{type(is_student)}")
print()

# 3. 将年龄转换为字符串，与姓名拼接输出
print("拼接输出")
age_str = str(age)  # 将年龄转换为字符串
result = name + "的年龄是：" + age_str + "岁"
print(result)

# 第二题：购物小票

# 定义商品价格
cola_price = 3.5    # 可乐价格
bread_price = 5     # 面包价格
milk_price = 8      # 牛奶价格

# 1. 计算商品总价
total_price = cola_price + bread_price + milk_price

# 2. 计算找零金额
payment = 20        # 顾客支付金额
change = payment - total_price  # 找零

# 3. 输出购物小票
print()
print("======== 购物小票 ========")
print(f"可乐：{cola_price}元")
print(f"面包：{bread_price}元")
print(f"牛奶：{milk_price}元")
print("-------------------------")
print(f"总计：{total_price}元")
print(f"实付：{payment}元")
print(f"找零：{change}元")
print("==========================")

#第三题

print(bool(""))
print(bool(" "))
print(int(True))
print("abc" * 3)
print(10 // 3)
print(10 % 3)