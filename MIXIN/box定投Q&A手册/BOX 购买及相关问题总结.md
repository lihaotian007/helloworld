



# BOX 购买及相关问题总结

阅读本内容笔者将默认您已经完成以下知识积累：

1. 您已经了解过 BOX 是什么，若没有请查阅 [BOX 官网](https://b.watch/#/) 或 在公开课中查看
2. 您已经下载 mixin APP，且加入“定投公开课”，若没有请参考此[文章链接](https://www.jianshu.com/p/975da55575f5)下载并在 mixin 搜索 7000102093 



本文大部分内容笔者都自己跑过一遍，部分没有跑过的内容会在文中做注释。文章内容会做持续更新，有任何疑问可以在 mixin 搜索 37322432 添加笔者，帮你答疑



## 本文件内容目录

* 购买前的准备：添加 mixin 钱包

* BOX 申购与赎回

  > * 申购
  > * 兑换
  > * 赎回

* BOX 购买与卖出

  > * 实名认证
  > * 购买
  > * 卖出

* 其他相关问题

  > * USDT 相关
  >
  >   > * USDT 是什么
  >   > * USDT 为什么还有版本
  >
  > * ExinOne 相关
  >
  >   > * 如何使用 ExinOne 进行版本转换
  >   > * 如何使用 Exinone 设置定投
  >   > * 关于 Exinone 的安全性问题
  >
  > * BOX 相关
  >
  >   > * 关于 box 奖励的问题
  >   > * 关于 box 真伪的问题
  >
  > * 闪电交易使用方法（数字货币间兑换）



（注：此图方便大家明确公开课的各种功能操作）

![功能页面](https://raw.githubusercontent.com/lihaotian007/helloworld/master/MIXIN/box定投Q%26A手册/picture/公开课机器人.PNG)



## 购买前的准备



### 一个 mixin 钱包

* mixin 钱包只针对数字资产进行存储，所以即便你有了 mixin 钱包也无法完成人民币、美元等货币与数字货币的兑换。但是有了 mixin 钱包你就可以抢红包了呀，而且后续 BOX 的存储可以用到
* mixin 钱包如果你是完整版，那么主页面左上角就有。如果你是畅聊版（即左上角没有钱包），请搜索 7000101425 然后添加并授权
* 另外，授权成功后进入 钱包界面，点击下方机器人即可看到自己当前的数字资产状况



## BOX 的申购与赎回

### 申购

申购是通过一定比例的 BTC 、EOS、XIN 购买 BOX 的一种方式，需要申购者同时持有上述三种数字货币，并按以下比例申购 [官网链接](https://box.xue.cn/#/zh_CN/)

* 每 `0.0001 个 BTC` + `0.15 个 EOS` + `0.0008 个 XIN` 可申购 `1 份 BOX`
* 数量要求：申购 **`1 份起购`**，额度为基本配置数量的整数倍。
* 时效要求：提交申请后，30分钟内完成订单支付；超时订单会自动取消，并原路退回已打入的数字货币
* 费用：申购免手续费；基金免管理费

* 操作方法：

  > 1. 点击公开课下方机器人选择 b.watch，进入官网
  >
  > 2. 点击申购，填入所需申购份数（系统会根据你当前 BTC 、EOS、XIN 给出一个最大可申请份数，如果有一种数字货币不足，可以参考 “其他相关问题” 中的 `闪电交易使用方法` 完成数字货币间兑换）
  >
  >    ![申购1](https://raw.githubusercontent.com/lihaotian007/helloworld/master/MIXIN/box定投Q%26A手册/picture/申购1.PNG)
  >
  > 3. 申购成功后在三个数字货币后分别点击转账，转账完成后点击刷新
  >
  > 4. 完成后你会看到 b.watch 给你发来的消息
  >
  >    ![申购2](https://raw.githubusercontent.com/lihaotian007/helloworld/master/MIXIN/box定投Q%26A手册/picture/申购2.PNG)



### 兑换

兑换是官方给出的一个便捷方式，不用你去分别按比例购买三种数字货币，可以直接用 USTD 购买。但此方式只能使用 ERC-20 的 USDT 来兑换（关于 USDT 版本问题 请参考下方 “相关问题及注意事项” 的内容）

* 操作方法：

  > 1. 点击公开课下方机器人选择 BOX 兑换机，进入操作界面
  >
  > 2. 核对你的 USDT 版本是否为 “ERC-20”（关于 USDT 的版本问题请参考下方 “相关问题及注意事项” 的内容）
  >
  >    > * 若你是使用 EXinone 购买的 USDT ，则版本更可能是 “Omni" 需要在 Exinone 中进行版本转换（如何版本转换请参考下方 “相关问题及注意事项” 的内容）
  >    >
  >    > * 若你是使用 Z-OTC 购买的 USDT，则可直接使用（Z-OTC实名认证后可直接购买）
  >    >
  >    > * 若非以上两个渠道，笔者给你提供两者图片的差异可以自行判断或联系笔者( mixin 搜索 37322432 )
  >    >
  >    >   ![版本样式例子](https://raw.githubusercontent.com/lihaotian007/helloworld/master/MIXIN/box定投Q%26A手册/picture/版本样式例子.png)
  >    >
  >    > * 核对及转换完成之后，输入你要使用的 USDT 数量，点击转账，完成后转账后即可
  >    >
  >    > * 完成之后，BOX兑换机 将会通过 mixin 发送给你交易信息。包括购买的 BTC、EOS、XIN 的数量，以及兑换的 BOX 的数量，并且如果有没有使用的 USDT 也会显示并退还。（BOX兑换机会保障你兑换的 BOX 为整数，所以如果有未用完的 USDT ，BOX 兑换机会原路退还）
  >    >
  >    >   ![兑换](https://raw.githubusercontent.com/lihaotian007/helloworld/master/MIXIN/box定投Q%26A手册/picture/兑换.PNG)

### 赎回

赎回是类似卖出的一种方式，但是被赎回的 BOX 会被销毁。此流程笔者还没有跑过（因为没达到赎回要求），把官方内容和链接放在这里，对内容做一些解释说明。[官方链接](https://bwatch.zendesk.com/hc/zh-cn/articles/360032542872-BOX-简介)

* 赎回条件：

  > * 累计申购份额净值超过 **100,000 USDT**，可直接赎回对应 BOX 份额的数字货币
  >
  > * 解释：请注意是 `净值`，举例如下
  >
  >   > 1. 假设你买了 1000 USDT 的 BOX ，后来涨到了 100,000 USDT 也是可以赎回的
  >   > 2. 假设你买了 200,000 USDT 的 BOX ，后来跌倒了 90,000 USDT 也是不能赎回的

* 费用：赎回需扣除赎回 `数字货币数量` 的 1% 作为手续费

* 赎回流程：

  > 1. b.watch 对于符合赎回条件的用户会开放赎回入口；
  > 2. 确定赎回份额；
  > 3. 在结算日前提交赎回申请，将 BOX 代币提交给系统；
  > 4. b.watch 于结算日将对应份额的 BTC、EOS、XIN 转入 Mixin Messenger 钱包，赎回结束。



##  BOX 购买与卖出

BOX 的购买与卖出是使用 人民币 直接购买，由于监管问题，在 2017 年 9 月 4 日之后，在中国境内并不允许直接提供法币充值交易，因此现在所有的法币交易基本都是 C2C 交易，即由平台担保，用户和商户之间通过手动转账进行交易。基本所有使用 法币交易的平台，都需要完成实名认证，然后才可以进行交易。本例以 ExinOne 为场景完成，至于 FoxOne 之类的二级市场交易，由于并不适合新手，读者可以后期自行探索完成



### ExinOne 实名认证

Mixin Network 官网对于 Mixin 的定义是：“Mixin is a publicly distributed ledger aimed to help other publicly distributed ledgers gain trillions of TPS, achieve sub second final confirmations, zero transaction fees, enhanced privacy, and unlimited extensibility.” 简单来说 MiXin 是支持全币种的钱包，同时也是端对端加密的聊天工具，本身没有交易属性，因而实名认证是交易平台所必须的，并非 MiXin 所必须的，这点需要明白 [官网链接](https://mixin.one/) 

* 操作方法

  > 1. 点击公开课下方机器人选择 Exin，进入并授权
  > 2. 点击 “我的” 界面，进入后选择 “实名认证” ，之后按引导操作完成即可
  > 3. 可以顺道在 mixin 搜索 7000101276 ，关注 ExinOne ，反正以后用的到



### BOX 购买

BOX 的购买是 ExinOne 平台统一定价，无溢价，转账的承兑商仅负责做市商，完成交易（关于 ExinOne 的安全性问题，可以参考 “其他相关问题” 中的 `ExinOne 安全性问题` 的解答）

* 操作方法（通过 Exinone完成）：

  > 1. 点击公开课下方机器人选择 Exin，进入Exin的操作界面
  >
  > 2. 在 “C2C” 界面找到 BOX 并点击 “交易” ，进入交易界面
  >
  > 3. 输入你要购买的金额，下方选择 “Mixin 钱包” ，点击 “提交订单” ，进入支付方式选择
  >
  >    ![](https://raw.githubusercontent.com/lihaotian007/helloworld/master/box定投Q%26A手册/picture/购买1.PNG)
  >
  > 4. 选择完成后，点击 “确认购买”，进入支付界面（笔者使用是是支付宝，其他如果你选择了其他方式有什么差异也请告诉笔者）
  >
  > 5. 点击 “收款码” 后面的 “点击展示” ，将图片保存后在支付宝扫描转账即可
  >
  > 6. 转账完成后点击 “我已付款” ，即可。完成之后，Exinone 将会通过 mixin 发送给你交易信息
  >
  >    ![](https://raw.githubusercontent.com/lihaotian007/helloworld/master/box定投Q%26A手册/picture/购买2.PNG)



### BOX卖出

BOX 的卖出是卖给 ExinOne 平台，平台统一定价，卖给承兑商的过程（笔者本着坚守践行群的基本信念 BOX 在两个大周期以内只有购买的操作，在这里将 BOX 替换为了 BTC，请谅解）

操作方法（通过 Exinone完成）：

> 1. 点击公开课下方机器人选择 Exin，进入Exin的操作界面
>
> 2. 在 “C2C” 界面找到 BOX 并点击 “交易” ，进入交易界面
>
> 3. 输入你要卖出的 数量，下方选择 所在的钱包，点击 “提交订单” ，进入支付方式选择（笔者选择的是支付宝）
>
> 4. 选择完成后，点击 “支付 BOX”，会将对应的 BOX 支付给平台
>
> 5. 在支付之后，会受到承兑商的支付宝转账，确认收到后点击 “确认已收到转账” 即可
>
> 6. 完成之后，Exinone 将会通过 mixin 发送给你交易信息
>
>    ![](https://raw.githubusercontent.com/lihaotian007/helloworld/master/box定投Q%26A手册/picture/卖出.PNG)



## 其他相关问题

### USDT 是什么

USDT 是 Tether 公司推出的基于稳定价值货币美元（USD）的代币 TetherUSD ，1USDT=1美元，用户可以随时使用 USDT 与 USD 进行1:1兑换。 Tether公司严格遵守1:1准备金保证，即每发行1个 USDT 代币，其银行账户都会有1美元的资金保障



### USDT 为什么还有版本

USDT 目前有三个版本 ：OMNI、ERC-20、TRC-20

* OMNI USDT：

  > * 2014年，在比特币网络上上基于OMNI Layer协议，发行USDT，其以1:1的比例与美元锚定

* ERC-20 USDT：

  > * 2018年，在以太坊网络上基于ERC-20协议发行的USDT出现

* TRC-20 USDT

  > * 2019年3月，波场TRON宣布与Tether泰达公司合作，利用智能合约在波场网络中发行与美元1:1锚定的USDT，使用TRC20协议

这三类 USDT 最明显的区别在于 OMNI 地址是以 ’1‘ 或者 ’3‘ 开头；ERC-20 地址是以 ’0x‘ 开头；TRC-20 地址是以 ’T‘ 开头



### 如何使用 ExinOne 进行版本转换

1. 点击公开课下方机器人选择 Exin，进入Exin的操作界面

2. 在 “我的” 界面找到 工具箱 并点击进入

   ​	![](https://raw.githubusercontent.com/lihaotian007/helloworld/master/box定投Q%26A手册/picture/USDT版本转换1.PNG)

3. 选择来源钱包后，选择你 “想要兑换的版本” 和 “用来兑换的版本” ，并输入金额点击支付即可

   ![](https://raw.githubusercontent.com/lihaotian007/helloworld/master/box定投Q%26A手册/picture/USDT版本转换2.PNG)

4. **说明：转换有0.05%的手续费**



### 如何用 ExinOne 设置定投

1. 点击公开课下方机器人选择 Exin，进入Exin的操作界面
2. 在 “定投” 界面打开 ”定投开关“ 之后单机定投编辑进入编辑界面

3. 选择定投放入的钱包、定投时间、定投的货币及金额，之后点击保存即可（Exinone只支持按周 / 天定投）

4. 在定投选择的时间，选择定投支付，进入支付界面支付即可（支付操作见上方 “BOX 购买” 中的内容）
5. **另外，笔者理解定投的核心在于长期持有和定期投入，不要 “贪杯” 哦**

![](https://raw.githubusercontent.com/lihaotian007/helloworld/master/box定投Q%26A手册/picture/定投设置.PNG)



### 关于 ExinOne 安全性问题

ExinOne 的安全性问题，官网已经给了相关的解答，笔者给出如下概述，完整内容可以参考最后的四个链接

概述来说由于国家监管政策要求在中国境内不允许直接提供法币充值交易，所以 ExinOne 将法币充值交易放到 C2C板块，由平台定价、平台担保、通过用户和承兑商（平台认可且培训）之间的交易来完成。

*  [什么是 C2C（场外）交易？](https://support.exinone.com/hc/zh-cn/articles/360019637132-什么是-C2C-场外-交易-) 

*  [关于 ExinOne 平台承兑商的说明](https://support.exinone.com/hc/zh-cn/articles/360025310491-关于-ExinOne-平台承兑商的说明) 
*  [平台定价规则](https://support.exinone.com/hc/zh-cn/articles/360029105712-ExinOne-定价规则) 
*  [关于 Mixin 和 ExinOne 的关系](https://support.exinone.com/hc/zh-cn/articles/360025013992-关于-Mixin-和-ExinOne-的关系) 



### 关于 BOX 奖励的问题

* 奖励类型

  > * 在开放二级市场交易后，BOX 持有者将享有 50% 二级市场手续费分红。也就是说，与此同时，b.watch 作为提供交易的平台，将会有 50% 手续费留存
  > * 对于那些长期持有 BOX 的人，以及那些能够完成定投计划的人，b.watch 向这两种人发放 b.watch 的股份作为激励，目前计划 7 年发放完毕

* 我把目前问到的问题罗列一下，当前的情况会具体说明

  > * 两种奖励是否均与 BOX 持有者挂钩，与渠道无关：是的，但是必须在践行群
  > * 二级市场手续费分红以什么渠道发放？：暂不明确
  > * 定投计划是否有一定要求：暂不明确





### 关于 BOX 真伪的问题

其实主要是看图标，如果没有图标，或者图标不是如下这样，那么就是假的 BOX Token。官方链接放到下面可以参考

*  [验证真伪 BOX Token](https://bwatch.zendesk.com/hc/zh-cn/articles/360032542912-验证真伪-BOX-Token)

![](https://raw.githubusercontent.com/lihaotian007/helloworld/master/box定投Q%26A手册/picture/box.png)



### 闪电交易使用方法（数字货币间兑换）

1. 点击公开课下方机器人选择 闪电交易，进入操作界面

2. 选择你 “想要兑换的” 和 “用来兑换的” 数字货币，并输入数量，点击转账后完成转账即可

3. 完成之后，闪电交易 将会通过 mixin 发送给你交易信息

   ![](https://raw.githubusercontent.com/lihaotian007/helloworld/master/box定投Q%26A手册/picture/转换.PNG)