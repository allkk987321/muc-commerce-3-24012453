// ========================================
// 校园轻集市 - Mock 数据层
// ========================================

// 当前用户
const currentUser = {
  id: 'u1',
  nickname: '小明同学',
  college: '计算机科学与技术学院',
  campus: '南校区',
  role: '本科生',
  creditScore: 95,
  avatar: ''
};

// 用户数据
const users = [
  { id: 'u1', nickname: '小明同学', college: '计算机科学与技术学院', campus: '南校区', role: '本科生', creditScore: 95 },
  { id: 'u2', nickname: '图书馆小助手', college: '人文学院', campus: '北校区', role: '研究生', creditScore: 88 },
  { id: 'u3', nickname: '篮球少年', college: '体育学院', campus: '南校区', role: '本科生', creditScore: 92 },
  { id: 'u4', nickname: '咖啡续命中', college: '艺术学院', campus: '东校区', role: '本科生', creditScore: 78 },
  { id: 'u5', nickname: '考研上岸', college: '法学院', campus: '北校区', role: '研究生', creditScore: 100 },
  { id: 'u6', nickname: '实验室搬砖', college: '物理学院', campus: '西校区', role: '研究生', creditScore: 85 },
];

// 校园信息数据
const items = [
  {
    id: 1, type: 'secondhand', title: '九成新《算法导论》第三版',
    description: '只用了一个学期，基本全新，没有笔记和折痕。适合计算机专业同学。原价128，现价68出。',
    campus: '南校区', location: '图书馆一楼', tags: ['教材', '计算机', '算法'],
    images: [], publisherId: 'u3', status: 'active',
    viewCount: 342, favoriteCount: 28,
    price: 68, condition: '九成新', allowBargain: true,
    createdAt: '2024-03-15 14:30', updatedAt: '2024-03-15 14:30'
  },
  {
    id: 2, type: 'secondhand', title: '索尼WH-1000XM4降噪耳机',
    description: '买了半年，使用频率不高，保护得很好，箱说全。降噪效果一流，图书馆自习神器。',
    campus: '南校区', location: '2号宿舍楼下', tags: ['耳机', '数码', '索尼'],
    images: [], publisherId: 'u6', status: 'active',
    viewCount: 580, favoriteCount: 45,
    price: 899, condition: '九五成新', allowBargain: true,
    createdAt: '2024-03-14 09:15', updatedAt: '2024-03-14 09:15'
  },
  {
    id: 3, type: 'secondhand', title: '27寸4K显示器 Dell U2723QE',
    description: '毕业出，使用一年半，无坏点无划痕。Type-C一线连，适合Mac用户。送支架。',
    campus: '西校区', location: '研究生公寓3栋', tags: ['显示器', '数码', 'Dell'],
    images: [], publisherId: 'u5', status: 'active',
    viewCount: 720, favoriteCount: 56,
    price: 2200, condition: '九成新', allowBargain: true,
    createdAt: '2024-03-13 16:45', updatedAt: '2024-03-13 16:45'
  },
  {
    id: 4, type: 'secondhand', title: '全新未拆封台灯 小米智能台灯1S',
    description: '年会抽奖中的，全新未拆封。支持米家APP控制，色温亮度可调。',
    campus: '北校区', location: '10号教学楼门口', tags: ['台灯', '小米', '智能'],
    images: [], publisherId: 'u2', status: 'active',
    viewCount: 156, favoriteCount: 12,
    price: 129, condition: '全新', allowBargain: false,
    createdAt: '2024-03-16 10:00', updatedAt: '2024-03-16 10:00'
  },
  {
    id: 5, type: 'lostfound', title: '丢失校园卡一张',
    description: '昨天在操场跑步时可能掉在跑道附近。学号2021开头，卡套是蓝色的。找到必有重谢！',
    campus: '南校区', location: '操场跑道附近', tags: ['校园卡', '蓝色卡套'],
    images: [], publisherId: 'u1', status: 'active',
    viewCount: 89, favoriteCount: 5,
    lostOrFound: 'lost', eventTime: '2024-03-15 18:00', itemFeature: '蓝色卡套，学号2021开头',
    createdAt: '2024-03-15 20:30', updatedAt: '2024-03-15 20:30'
  },
  {
    id: 6, type: 'lostfound', title: '捡到一副AirPods Pro',
    description: '在图书馆三楼自习区捡到的，带保护壳，壳上有贴纸。请失主联系我认领，需描述保护壳样式。',
    campus: '北校区', location: '图书馆三楼', tags: ['耳机', 'AirPods', '苹果'],
    images: [], publisherId: 'u2', status: 'active',
    viewCount: 210, favoriteCount: 8,
    lostOrFound: 'found', eventTime: '2024-03-14 15:00', itemFeature: '带保护壳，壳上有贴纸',
    createdAt: '2024-03-14 16:00', updatedAt: '2024-03-15 09:00'
  },
  {
    id: 7, type: 'lostfound', title: '钥匙串遗失 带U盘',
    description: '钥匙串上有三把钥匙和一个32G金士顿U盘（U盘里有重要资料），可能在食堂或教学楼之间丢失。',
    campus: '东校区', location: '食堂到教学楼之间', tags: ['钥匙', 'U盘', '金士顿'],
    images: [], publisherId: 'u4', status: 'active',
    viewCount: 134, favoriteCount: 3,
    lostOrFound: 'lost', eventTime: '2024-03-16 12:30', itemFeature: '三把钥匙+32G金士顿U盘',
    createdAt: '2024-03-16 13:30', updatedAt: '2024-03-16 13:30'
  },
  {
    id: 8, type: 'group', title: '奶茶拼单！一点点四季春',
    description: '想喝一点点，有没有人一起拼？满30减8，目前还差2人。预计下午3点下单。',
    campus: '南校区', location: '线上', tags: ['奶茶', '一点点', '拼单'],
    images: [], publisherId: 'u1', status: 'active',
    viewCount: 189, favoriteCount: 15,
    targetCount: 4, currentCount: 2, deadline: '2024-03-16 15:00',
    createdAt: '2024-03-16 14:00', updatedAt: '2024-03-16 14:00'
  },
  {
    id: 9, type: 'group', title: '寻找考研搭子 每天图书馆',
    description: '备战2025考研，想找个能一起每天早上8点到晚上10点泡图书馆的搭子，互相监督。',
    campus: '北校区', location: '图书馆', tags: ['考研', '搭子', '学习'],
    images: [], publisherId: 'u5', status: 'active',
    viewCount: 320, favoriteCount: 42,
    targetCount: 3, currentCount: 1, deadline: '2024-03-20 23:59',
    createdAt: '2024-03-13 08:30', updatedAt: '2024-03-15 08:30'
  },
  {
    id: 10, type: 'group', title: '水果团购 车厘子+草莓',
    description: '联系了水果批发商，车厘子5斤装180，草莓3斤装60。满10人成团，周五统一送到校门口。',
    campus: '东校区', location: '校门口', tags: ['水果', '团购', '车厘子'],
    images: [], publisherId: 'u4', status: 'active',
    viewCount: 450, favoriteCount: 67,
    targetCount: 10, currentCount: 7, deadline: '2024-03-17 18:00',
    createdAt: '2024-03-15 12:00', updatedAt: '2024-03-16 09:00'
  },
  {
    id: 11, type: 'errand', title: '代取快递 南门菜鸟驿站',
    description: '今天有个快递到了但我下午有课走不开。一个中等大小的盒子，不重。取完放3号宿舍楼下就行。',
    campus: '南校区', location: '南门菜鸟驿站', tags: ['快递', '代取'],
    images: [], publisherId: 'u1', status: 'active',
    viewCount: 56, favoriteCount: 2,
    reward: 8, taskPlace: '南门菜鸟驿站', expectedTime: '2024-03-16 17:00前',
    createdAt: '2024-03-16 10:30', updatedAt: '2024-03-16 10:30'
  },
  {
    id: 12, type: 'errand', title: '代买晚餐 食堂二楼',
    description: '晚上有实验走不开，帮我从食堂二楼带一份黄焖鸡米饭+可乐。加跑腿费一共25。',
    campus: '西校区', location: '食堂二楼', tags: ['晚餐', '代买', '食堂'],
    images: [], publisherId: 'u6', status: 'active',
    viewCount: 34, favoriteCount: 1,
    reward: 5, taskPlace: '食堂二楼', expectedTime: '2024-03-16 18:30前',
    createdAt: '2024-03-16 17:00', updatedAt: '2024-03-16 17:00'
  },
  {
    id: 13, type: 'secondhand', title: '二手自行车 捷安特ATX720',
    description: '大二买的，骑了两年，车况良好。前后轮胎刚换过，刹车灵敏。送车锁和打气筒。',
    campus: '东校区', location: '13号宿舍楼下', tags: ['自行车', '捷安特', '出行'],
    images: [], publisherId: 'u4', status: 'active',
    viewCount: 380, favoriteCount: 33,
    price: 450, condition: '七成新', allowBargain: true,
    createdAt: '2024-03-12 11:20', updatedAt: '2024-03-12 11:20'
  },
  {
    id: 14, type: 'errand', title: '代送文件到行政楼',
    description: '有一份申请材料需要交到行政楼教务处，但我人在校外。材料已经准备好放在信封里了。',
    campus: '北校区', location: '行政楼教务处', tags: ['文件', '代送', '行政楼'],
    images: [], publisherId: 'u2', status: 'active',
    viewCount: 22, favoriteCount: 0,
    reward: 10, taskPlace: '行政楼二楼教务处', expectedTime: '2024-03-17 12:00前',
    createdAt: '2024-03-16 08:00', updatedAt: '2024-03-16 08:00'
  },
  {
    id: 15, type: 'lostfound', title: '捡到一个钱包',
    description: '在校门口共享单车车筐里发现的，棕色皮质钱包，里面有少量现金和一张照片。请失主联系我。',
    campus: '东校区', location: '校门口共享单车停放区', tags: ['钱包', '棕色'],
    images: [], publisherId: 'u2', status: 'resolved',
    viewCount: 180, favoriteCount: 6,
    lostOrFound: 'found', eventTime: '2024-03-10 07:30', itemFeature: '棕色皮质钱包，有照片',
    createdAt: '2024-03-10 08:30', updatedAt: '2024-03-11 10:00'
  },
];

// 收藏数据
const favorites = [
  { id: 1, userId: 'u1', itemId: 2, createdAt: '2024-03-14 10:00' },
  { id: 2, userId: 'u1', itemId: 4, createdAt: '2024-03-16 11:00' },
  { id: 3, userId: 'u1', itemId: 9, createdAt: '2024-03-14 08:30' },
  { id: 4, userId: 'u1', itemId: 3, createdAt: '2024-03-13 20:00' },
];

// 会话数据
const conversations = [
  {
    id: 1, itemId: 2, buyerId: 'u1', publisherId: 'u6',
    lastMessage: '最低多少能出？', unreadCount: 1,
    updatedAt: '2024-03-15 15:30'
  },
  {
    id: 2, itemId: 6, buyerId: 'u1', publisherId: 'u2',
    lastMessage: '好的，我下午去找你', unreadCount: 0,
    updatedAt: '2024-03-15 10:00'
  },
  {
    id: 3, itemId: 8, buyerId: 'u4', publisherId: 'u1',
    lastMessage: '还差一个人就够啦！', unreadCount: 2,
    updatedAt: '2024-03-16 14:30'
  },
];

// 消息数据
const messages = [
  { id: 1, conversationId: 1, senderId: 'u1', receiverId: 'u6', content: '你好，耳机还在吗？', messageType: 'text', createdAt: '2024-03-15 15:00', read: true },
  { id: 2, conversationId: 1, senderId: 'u6', receiverId: 'u1', content: '在的，有什么想问的？', messageType: 'text', createdAt: '2024-03-15 15:05', read: true },
  { id: 3, conversationId: 1, senderId: 'u1', receiverId: 'u6', content: '最低多少能出？', messageType: 'text', createdAt: '2024-03-15 15:30', read: false },
  { id: 4, conversationId: 2, senderId: 'u1', receiverId: 'u2', content: '你好，请问AirPods还在吗？我好像在图书馆丢了一副', messageType: 'text', createdAt: '2024-03-15 09:30', read: true },
  { id: 5, conversationId: 2, senderId: 'u2', receiverId: 'u1', content: '在的！可以描述一下你的保护壳吗？', messageType: 'text', createdAt: '2024-03-15 09:35', read: true },
  { id: 6, conversationId: 2, senderId: 'u1', receiverId: 'u2', content: '是一个米白色的硅胶壳，上面贴了一张小狗贴纸', messageType: 'text', createdAt: '2024-03-15 09:40', read: true },
  { id: 7, conversationId: 2, senderId: 'u2', receiverId: 'u1', content: '对的！就是它。你什么时候方便来取？我在图书馆三楼', messageType: 'text', createdAt: '2024-03-15 09:45', read: true },
  { id: 8, conversationId: 2, senderId: 'u1', receiverId: 'u2', content: '好的，我下午去找你', messageType: 'text', createdAt: '2024-03-15 10:00', read: true },
  { id: 9, conversationId: 3, senderId: 'u4', receiverId: 'u1', content: '想加入奶茶拼单！', messageType: 'text', createdAt: '2024-03-16 14:20', read: false },
  { id: 10, conversationId: 3, senderId: 'u1', receiverId: 'u4', content: '欢迎欢迎！你喝什么？', messageType: 'text', createdAt: '2024-03-16 14:25', read: false },
  { id: 11, conversationId: 3, senderId: 'u4', receiverId: 'u1', content: '四季春玛奇朵，去冰三分糖', messageType: 'text', createdAt: '2024-03-16 14:28', read: false },
  { id: 12, conversationId: 3, senderId: 'u1', receiverId: 'u4', content: '还差一个人就够啦！', messageType: 'text', createdAt: '2024-03-16 14:30', read: false },
];

// 安全提醒
const notices = [
  { id: 1, title: '交易安全提醒', content: '请尽量选择校内公共区域（如图书馆、食堂、教学楼大厅）进行线下交易，注意人身和财物安全。', type: 'safety' },
  { id: 2, title: '贵重物品提醒', content: '购买贵重电子产品时建议当面验机，确认外观、功能和配件完整后再确认交易。', type: 'safety' },
  { id: 3, title: '隐私保护提醒', content: '请勿在公开信息中泄露个人手机号、宿舍号等隐私信息，建议通过平台消息进行初步沟通。', type: 'privacy' },
  { id: 4, title: '谨防诈骗', content: '警惕异常低价商品和提前转账要求。二手交易请坚持当面交易、一手交钱一手交货。', type: 'warning' },
];

// 工具函数
function getUserById(id) {
  return users.find(u => u.id === id) || null;
}

function getItemById(id) {
  return items.find(item => item.id === id) || null;
}

function getItemsByType(type) {
  return type === 'all' ? items : items.filter(item => item.type === type);
}

function getFavoriteItemIds(userId) {
  return favorites.filter(f => f.userId === userId).map(f => f.itemId);
}

function getUserPosts(userId) {
  return items.filter(item => item.publisherId === userId);
}

function getUserFavorites(userId) {
  const favIds = favorites.filter(f => f.userId === userId).map(f => f.itemId);
  return items.filter(item => favIds.includes(item.id));
}

function getConversationsByUser(userId) {
  return conversations.filter(c => c.buyerId === userId || c.publisherId === userId);
}

function getMessagesByConversation(conversationId) {
  return messages.filter(m => m.conversationId === conversationId);
}

function getTypeLabel(type) {
  const map = { secondhand: '二手交易', lostfound: '失物招领', group: '拼单搭子', errand: '跑腿委托' };
  return map[type] || type;
}

function getStatusLabel(status) {
  const map = { active: '进行中', completed: '已完成', closed: '已关闭', resolved: '已解决' };
  return map[status] || status;
}

function getCampusLabel(campus) {
  const map = { '南校区': '南校区', '北校区': '北校区', '东校区': '东校区', '西校区': '西校区' };
  return map[campus] || campus;
}

function formatTime(dateStr) {
  if (!dateStr) return '';
  const d = new Date(dateStr.replace(' ', 'T'));
  if (isNaN(d.getTime())) return dateStr;
  const now = new Date();
  const diff = now - d;
  if (diff < 60000) return '刚刚';
  if (diff < 3600000) return Math.floor(diff / 60000) + '分钟前';
  if (diff < 86400000) return Math.floor(diff / 3600000) + '小时前';
  if (diff < 604800000) return Math.floor(diff / 86400000) + '天前';
  return d.getFullYear() + '-' +
    String(d.getMonth() + 1).padStart(2, '0') + '-' +
    String(d.getDate()).padStart(2, '0');
}
