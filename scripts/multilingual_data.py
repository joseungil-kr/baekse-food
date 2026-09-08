import os
import re

BLOG_DIR = r"c:\project\baekse-food\content\blog"

# 전문 외식 비즈니스 번역 사전
GLOSSARY = {
    "en": {
        "site_name": "Baekse Food",
        "brand_dakhanmari": "Baekse Dakhanmari",
        "brand_boribap": "Baekse Barley Bibimbap",
        "brand_pocha": "Baekse Pocha",
        "btn_apply": "Franchise & Supply Consultation",
        "btn_call": "Inquire by Phone",
        "interest": "닭한마리",
        "turnover": "table turnover",
        "onepack": "One-Pack System",
        "ck": "Central Kitchen",
        "store_info_title": "Baekse Food Flagship Store Information",
        "address": "1F, 101 Seokho-ro, Sangnok-gu, Ansan-si, Gyeonggi-do, Korea",
        "hours": "Open Daily 10:00 - 22:00 (Open 365 Days)",
        "phone": "031-407-0103"
    },
    "zh": {
        "site_name": "百世食品",
        "brand_dakhanmari": "百世一只鸡",
        "brand_boribap": "百世大麦饭",
        "brand_pocha": "百世大排档",
        "btn_apply": "加盟与调料供应咨询",
        "btn_call": "电话咨询",
        "interest": "닭한마리",
        "turnover": "翻台率",
        "onepack": "一包料标准化系统",
        "ck": "中央厨房",
        "store_info_title": "百世食品安山总店信息",
        "address": "韩国京畿道安山市常绿区石湖路101号1楼",
        "hours": "每日 10:00 - 22:00 (全年无休)",
        "phone": "031-407-0103"
    },
    "ja": {
        "site_name": "百世フード",
        "brand_dakhanmari": "百世タッカンマリ",
        "brand_boribap": "百世麦飯",
        "brand_pocha": "百世ポチャ",
        "btn_apply": "加盟・卸売相談を申し込む",
        "btn_call": "お電話でのお問い合わせ",
        "interest": "닭한마리",
        "turnover": "客席回転率",
        "onepack": "ワンパックシステム",
        "ck": "セントラルキッチン",
        "store_info_title": "百世フード韓国安山本店のご案内",
        "address": "韓国京畿道安山市常緑区石湖路101、1階",
        "hours": "毎日 10:00 - 22:00 (年中無休)",
        "phone": "031-407-0103"
    },
    "ru": {
        "site_name": "Baekse Food",
        "brand_dakhanmari": "Baekse Dakhanmari",
        "brand_boribap": "Baekse Barley Bibimbap",
        "brand_pocha": "Baekse Pocha",
        "btn_apply": "Консультация по франшизе и поставкам",
        "btn_call": "Позвонить нам",
        "interest": "닭한마리",
        "turnover": "оборачиваемость столов",
        "onepack": "Система One-Pack",
        "ck": "Фабрика-кухня (Central Kitchen)",
        "store_info_title": "Флагманский ресторан Baekse Food",
        "address": "1 эт., 101, Сокхо-ро, Саннок-гу, г. Ансан, Кёнги-до, Корея",
        "hours": "Ежедневно 10:00 - 22:00 (Без выходных)",
        "phone": "031-407-0103"
    }
}

# 40개 게시글 메타데이터 번역 매핑
POSTS_META = {
    "dakhanmari-how-to-eat": {
        "en": ("How to Eat Korean Dakhanmari Deliciously", "How to Eat Dakhanmari | Step-by-Step Hot Pot Guide | Baekse Food", "Discover the authentic way to eat Korean Dakhanmari chicken hot pot: from rice cakes and potatoes to tender chicken, kalguksu noodles, and porridge with dipping sauce."),
        "zh": ("韩国一只鸡美味吃法攻略", "韩国一只鸡美味吃法 | 蘸料调制与面条蛋粥全套攻略 | 百世食品", "韩国正宗一只鸡吃法大揭秘！年糕土豆开胃、鲜嫩鸡肉蘸秘制辣酱、浓鸡汤煮刀削面到最后黄金鸡蛋粥，解锁35年老店地道吃法。"),
        "ja": ("タッカンマリの美味しい食べ方", "タッカンマリの美味しい食べ方 | つけダレ黄金比とカルグクス・雑炊 | 百世フード", "本場韓国タッカンマリを極限まで美味しく食べる手順！トッポッキとジャガイモから始まり、やわらか鶏肉、特製ニラダレ、締めの手打ちうどん＆栄養雑炊まで完全解説。"),
        "ru": ("Как правильно есть корейский суп Дакханмари", "Как есть Дакханмари | Пошаговое руководство к куриному котлу | Baekse Food", "Руководство по корейскому супу Дакханмари: от рисовых клецек и нежной курицы с острым соусом до домашней лапши калгуксу и насыщенной рисовой каши.")
    },
    "dakhanmari-sauce-secret": {
        "en": ("The Secret Behind Korean Dakhanmari Dipping Sauce", "Dakhanmari Sauce Secrets | 72-Hour Aged Dadegi & Dipping Ratio | Baekse Food", "Explore the science behind Dakhanmari dipping sauce: aged chili paste, low-sodium soy sauce, vinegar, and mustard paired with fresh chives for an addictive umami explosion."),
        "zh": ("韩国一只鸡灵魂蘸料的秘密", "一只鸡调料的秘密 | 72小时低温熟成辣椒酱与黄金配比 | 百世食品", "韩国一只鸡美味的精髓在于蘸料！72小时低温发酵辣椒酱、特调低盐酱油、白醋与研磨芥末的科学黄金平衡，造就令人欲罢不能的灵魂蘸汁。"),
        "ja": ("タッカンマリ秘伝つけダレの秘密", "タッカンマリのタレの秘密 | 72時間低温熟成タデギと黄金比率 | 百世フード", "タッカンマリの味を決定づける特製ダレの科学！72時間低温熟成ヤンニョム、低塩醤油、酢、からし、刻みニラが織りなす極上の中毒性を解き明かします。"),
        "ru": ("Секрет фирменного соуса для Дакханмари", "Секреты соуса Дакханмари | Выдержанная паста дадеги и дип-соус | Baekse Food", "В чем секрет соуса для Дакханмари? Идеальный баланс ферментированной перечной пасты дадеги, соевого соуса, уксуса и горчицы со свежим луком.")
    },
    "dakhanmari-broth-recipe": {
        "en": ("How to Cook Authentic Korean Dakhanmari Broth", "Dakhanmari Broth Recipe | Clear Umami Broth Secrets | Baekse Food", "Learn how authentic Dakhanmari clear chicken broth is brewed with fresh poultry, aromatics, and time-tested temperature control from Baekse Food's 35-year master kitchen."),
        "zh": ("正宗韩国一只鸡清汤高汤熬制方法", "一只鸡高汤熬制方法 | 澄澈鲜甜不油腻的清汤秘方 | 百世食品", "探秘正宗韩国一只鸡高汤熬制秘诀：新鲜原鸡除腥、高压清炖与火候温控技巧，解析家庭自熬与35年中央厨房标准化浓缩原汤的本质区别。"),
        "ja": ("タッカンマリ黄金スープの作り方", "タッカンマリのスープの作り方 | 雑味ゼロの極上チキンスープ | 百世フード", "澄み渡る深い旨味！タッカンマリのスープを極める下茹で技術と火加減のコツ。35年の伝統を誇る百世フードが本物の出汁の秘密を公開。"),
        "ru": ("Как сварить настоящий прозрачный бульон для Дакханмари", "Рецепт бульона Дакханмари | Секреты чистого насыщенного вкуса | Baekse Food", "Секреты варки прозрачного куриного бульона для Дакханмари: правильная бланшировка, выварка без жирного осадка и фирменная рецептура фабрики-кухни.")
    },
    "dakhanmari-kalguksu": {
        "en": ("How to Enjoy Kalguksu Noodles in Dakhanmari Broth", "Dakhanmari Kalguksu Guide | Timing, Noodles & Broth Balance | Baekse Food", "Master the art of finishing Dakhanmari with fresh kalguksu knife-cut noodles: broth refill rules, starch removal, and cooking techniques for optimal chewy texture."),
        "zh": ("韩国一只鸡手擀面刀削面神仙吃法", "一只鸡刀削面美味吃法 | 面条下锅时机与浓汤黄金比例 | 百世食品", "一只鸡精华浓汤煮手擀刀削面的完美技巧：加汤时机、抖掉多余面粉、大火煮沸技巧，让爽滑筋道的面条吸饱浓郁鸡汁。"),
        "ja": ("タッカンマリの締め生うどんカルグクスの極意", "タッカンマリカルグクス | 投入タイミングとモチモチ生麺 | 百世フード", "濃厚になった鶏スープで煮込む生うどん（カルグクス）の極上な楽しみ方。スープ追加のタイミング、打ち粉落とし、キムチとの相性を徹底解説。"),
        "ru": ("Как вкусно приготовить лапшу Калгуксу в курином бульоне", "Калгуксу в бульоне Дакханмари | Идеальная лапша и бульон | Baekse Food", "Правила приготовления домашней лапши калгуксу в концентрированном курином бульоне Дакханмари: идеальный момент подачи и текстура упругой лапши.")
    },
    "dakhanmari-sauce-ratio": {
        "en": ("Golden Ratio for Dakhanmari Table Dipping Sauce", "Dakhanmari Dipping Sauce Ratio | Soy, Mustard, Dadegi Balance | Baekse Food", "The standard golden ratio for Dakhanmari tabletop sauce: 2 spoons soy, 1 spoon vinegar, 1 spoon aged dadegi chili paste, and mustard mixed with shredded cabbage and chives."),
        "zh": ("韩国一只鸡餐桌蘸料黄金比例", "一只鸡蘸酱黄金配比 | 特调酱油、辣酱与芥末的科学配方 | 百世食品", "经典一只鸡餐桌蘸料黄金配比：特制酱油2勺、优质米醋1勺、熟成辣酱1勺、芥末半勺与鲜韭菜碎，酸辣鲜爽化解一切油腻。"),
        "ja": ("タッカンマリ専用タレの黄金比率", "タッカンマリヤンニョムの黄金比 | 醤油・酢・タデギ・からし | 百世フード", "タッカンマリを何倍も美味しくする卓上ブレンドの黄金比率！特製醤油2：酢1：タデギ1：からし0.5にニラを絡める至福のタレ配合を伝授。"),
        "ru": ("Золотые пропорции фирменного соуса для Дакханмари", "Пропорции соуса Дакханмари | Соевый соус, уксус и паста | Baekse Food", "Классический рецепт дип-соуса за столом: 2 ложки соевого соуса, 1 ложка уксуса, 1 ложка острой пасты дадеги и немного горчицы с зеленью.")
    },
    "dakbokkeum-recipe": {
        "en": ("How to Cook Rich and Spicy Korean Braised Chicken", "Spicy Braised Chicken Recipe | Odorless Chicken & Potatoes | Baekse Food", "Master authentic Dakbokkeumtang (Korean spicy braised chicken): pre-blanching tricks, sugar-first tenderizing, and perfect potato timing for thick, savory sauce."),
        "zh": ("韩式辣炒鸡块美味炖制秘诀", "韩式辣炒鸡块做法 | 去腥增鲜与土豆软糯浓稠技巧 | 百世食品", "韩式正宗辣炒鸡块（大排档辣炖鸡）全套配方：冷水焯鸡去腥、先糖后盐渗透软肉、中火慢炖让土豆自然起沙勾芡浓汁。"),
        "ja": ("ピリ辛タットリタン（タッポックムタン）の作り方", "タットリタンの作り方 | 臭み消しとホクホクじゃがいも煮込み | 百世フード", "ご飯もビールも止まらない韓国名物タットリタン（鶏とじゃがいものピリ辛煮込み）の本格レシピ。臭みを消す下処理とホクホク煮込みの秘訣。"),
        "ru": ("Как вкусно приготовить корейскую тушеную курицу Дакбоккым", "Рецепт Дакбоккымтан | Острая тушеная курица с картофелем | Baekse Food", "Секреты сочной и острой корейской курицы Дакбоккымтан: бланшировка, правильное добавление специй и разваристый картофель в густом соусе.")
    },
    "samgyetang-types": {
        "en": ("Types of Korean Samgyetang & Their Health Benefits", "Samgyetang Varieties & Health Benefits | Black, Perilla, Mung Bean | Baekse Food", "Explore the top varieties of Korean ginseng chicken soup (Samgyetang): traditional, black ginseng, perilla seed, and mung bean, along with their immune-boosting benefits."),
        "zh": ("韩国参鸡汤种类与食疗功效全解", "韩国参鸡汤种类与功效 | 黑参鸡汤·紫苏·绿豆参鸡汤 | 百世食品", "全面解析韩国四大经典参鸡汤：传统白参汤、2006年国家电视台首播的百世黑参鸡汤、醇香温润的紫苏参鸡汤与清热解暑的绿豆参鸡汤。"),
        "ja": ("韓国参鶏湯（サムゲタン）の種類と健康効能", "参鶏湯の種類と効能 | 黒参鶏湯・えごま・緑豆サムゲタン | 百世フード", "韓国の代表的な滋養強壮食サムゲタン4選！伝統参鶏湯、2006年地上波TV初放送の元祖黒参鶏湯、濃厚なえごま、すっきり緑豆の効能比較。"),
        "ru": ("Виды корейского супа Самгетан и их целебные свойства", "Виды корейского Самгетана | Черный женьшень, перилла, маш | Baekse Food", "Разновидности корейского женьшеневого супа Самгетан: традиционный, на черном женьшене, с семенами периллы и бобами мунг для укрепления иммунитета.")
    },
    "dakgomtang-vs-samgyetang": {
        "en": ("Dakgomtang vs Samgyetang: What Is the Real Difference?", "Dakgomtang vs Samgyetang Differences | Broth, Meat & Cost | Baekse Food", "Compare Korean chicken soup styles: shredded chicken meat in clear broth (Dakgomtang) versus stuffed whole young chicken with herbal roots (Samgyetang)."),
        "zh": ("韩式清鸡汤(Dakgomtang)与参鸡汤的区别", "韩式清鸡汤vs参鸡汤对比 | 食材形态·滋补药材与定价差异 | 百世食品", "看似都是鸡肉热汤，实则大不相同！细撕鸡肉丝澄澈清汤的Dakgomtang与整鸡塞满糯米人参的参鸡汤，在烹饪方式、午市翻台与客单价上的深度对比。"),
        "ja": ("タッコムタンと参鶏湯（サムゲタン）の違いとは？", "タッコムタン vs 参鶏湯の違い | 調理法・具材・価格帯を比較 | 百世フード", "ほぐし身を入れたあっさり澄まし汁「タッコムタン」と、丸鶏にもち米や高麗人参を詰めて丸ごと煮込む「参鶏湯」の根本的な違いを解説。"),
        "ru": ("В чем разница между Дакгомтаном и Самгетаном?", "Дакгомтан против Самгетана | Сравнение корейских супов | Baekse Food", "Сравнение прозрачного супа с волокнами курицы Дакгомтан и цельной молодой курицы, фаршированной рисом и женьшенем (Самгетан).")
    },
    "dakhanmari-startup-cost": {
        "en": ("Realistic Startup Costs for a Dakhanmari Restaurant", "Dakhanmari Startup Cost Breakdown | Interior 0% Margin Reality | Baekse Food", "Detailed budget breakdown for opening a 25-pyeong Dakhanmari restaurant: rent, equipment, ingredients, and how Baekse Food saves up to 50% through zero interior commissions."),
        "zh": ("开一家韩国一只鸡店的真实成本预算", "一只鸡餐厅开店初期费用 | 25坪预算清单与总部零加价 | 百世食品", "开一家25坪韩国一只鸡专门店到底要多少钱？房租押金、厨房设备、食材底货逐项测算，百世食品装修零抽成模式为您节省高达50%初始资金。"),
        "ja": ("タッカンマリ専門店のリアルな開業資金と内訳", "タッカンマリ創業初期費用 | 25坪モデル内訳と内装マージン0円 | 百世フード", "25坪のタッカンマリ専門店を開業するリアルな費用内訳！保証金、厨房機器、仕入れ初期費用の分析と、本部内装中間マージンゼロによる大幅コスト削減。"),
        "ru": ("Реальная стоимость открытия ресторана Дакханмари", "Затраты на открытие ресторана Дакханмари | Бюджет и окупаемость | Baekse Food", "Подробный анализ бюджета на открытие ресторана Дакханмари на 80 кв.м: оборудование, аренда, сырье и экономия до 50% благодаря нулевой наценке на ремонт.")
    },
    "dakhanmari-franchise-compare": {
        "en": ("Comparing Korean Dakhanmari Franchise Brands", "Dakhanmari Franchise Comparison | Checklist for Prospective Owners | Baekse Food", "Essential 5-point checklist when choosing a Dakhanmari franchise: interior margins, cold-chain CK logistics, multi-peak revenue, and kitchen labor requirements."),
        "zh": ("韩国一只鸡加盟品牌横向对比分析", "韩国一只鸡加盟对比 | 选拔加盟总部的5大核心考核指标 | 百世食品", "加盟一只鸡品牌切忌盲目！总部装修是否抽成、是否有自营中央厨房、能否实现全天三段式盈利，全方位对比帮您避开加盟陷阱。"),
        "ja": ("タッカンマリFCチェーンの比較と賢い選び方", "タッカンマリフランチャイズ比較 | 加盟先選定の5大チェックリスト | 百世フード", "タッカンマリ加盟で失敗しないための選定基準！内装マージンの有無、自社CK物流、昼夜3重売上モデル、調理簡素化を徹底比較。"),
        "ru": ("Сравнение франшиз корейского Дакханмари", "Сравнение франшиз Дакханмари | Чек-лист для рестораторов | Baekse Food", "5 ключевых критериев выбора франшизы Дакханмари: наценки на ремонт, прямая логистика с фабрики-кухни, мульти-пиковая выручка и простота кухни.")
    },
    "dakhanmari-failure-reasons": {
        "en": ("Why Chicken Restaurants Fail & How to Prevent It", "Chicken Restaurant Failure Causes | Overcoming Labor & Taste Variance | Baekse Food", "Analyze the 4 major pitfalls leading to restaurant closure: heavy chef dependency, taste inconsistencies, short 3-hour dinner windows, and excessive upfront interior costs."),
        "zh": ("韩国一只鸡餐厅开店失败原因与避坑指南", "一只鸡餐厅失败原因剖析 | 摆脱厨师依赖与3小时短命营收 | 百世食品", "揭秘餐饮创业高倒闭率四大致命死因：依赖高薪大厨导致口味失控、仅靠晚餐3小时营业额难以抵扣房租，百世食品4重防御体系助您稳健盈利。"),
        "ja": ("飲食店が廃業する4大原因と失敗回避の防衛策", "タッカンマリ創業の失敗原因 | 料理人依存と短時間営業の壁を打破 | 百世フード", "飲食開業の廃業率が高い本当の理由とは？料理人依存による味のブレ、過剰な初期投資、夜間3時間のみの単一売上リスクを解決する防衛戦略。"),
        "ru": ("Почему закрываются рестораны и как этого избежать", "Причины провала ресторанов | Защита от зависимости от повара | Baekse Food", "4 главные причины банкротства общепита: зависимость от шеф-повара, нестабильный вкус, работа только 3 часа вечером и завышенные расходы на открытие.")
    },
    "small-capital-restaurant": {
        "en": ("Best Low-Capital Restaurant Franchise Models for 2026", "Low Capital Restaurant Ideas | 3-in-1 Compact Kitchen Synergy | Baekse Food", "Discover why small-footprint, multi-peak restaurant concepts thrive in 2026: sharing 80% of ingredients across breakfast, lunch, and dinner to maximize return on investment."),
        "zh": ("2026低成本小资本外食餐饮加盟推荐", "小资本餐饮创业推荐 | 3in1复合空间实现坪效最大化 | 百世食品", "在2026年高租金高人工大环境下，小资本创业如何以小博大？对比咖啡馆、外卖便当与国饭店，百世食品同一厨房三次创收成为小本创业首选。"),
        "ja": ("2026年 小資本で始める飲食店開業おすすめモデル", "小資本飲食店創業 | 1つの厨房で3回稼ぐ高坪効率モデル | 百世フード", "低資金でリスクを抑えて開業したい方へ。カフェや居酒屋、ラーメン店と比較した百世フード3in1複合モデルの圧倒的な投資回収効率。"),
        "ru": ("Лучшие модели общепита с малым капиталом в 2026", "Идеи ресторанов с низким капиталом | Концепция 3-в-1 | Baekse Food", "Как запустить ресторан с минимальными вложениями в 2026 году: объединение 80% продуктов на одной кухне для максимальной отдачи на каждый метр.")
    },
    "one-person-restaurant": {
        "en": ("Operating a Restaurant with Just One Person", "One-Person Restaurant Management | One-Pack Pre-portioned Prep | Baekse Food", "How to run a high-revenue Korean eatery without kitchen staff: table-simmered hot pots, zero pre-prep, and One-Pack kits enabling 30-35% net profit margins."),
        "zh": ("一人即可独立运营的高利润餐厅模式", "一人开餐厅运营指南 | 一包料标准化省去厨师与后厨人员 | 百世食品", "没有员工也能开餐厅！探究一人餐厅的三大硬性前提：食材零切洗前处理、餐桌自煮互动式上菜、紧凑U型动线，省下的人工费转化为30-35%净利润。"),
        "ja": ("ワンオペ（1人営業）で回せる飲食店開業の条件", "1人運営が可能な飲食店 | 仕込み不要のワンパックシステム | 百世フード", "人手不足時代の最適解！厨房スタッフゼロで回すタッカンマリ＆麦飯店舗。テーブルセルフ加熱と定量キットで人件費ゼロ、利益率35%を達成。"),
        "ru": ("Ресторан для управления одним человеком", "Кафе без поваров и лишнего штата | Система One-Pack | Baekse Food", "Как управлять заведением в одиночку: готовые вакуумные полуфабрикаты, интерактивная готовка гостями за столиками и чистая прибыль 30-35%.")
    },
    "restaurant-cost-saving": {
        "en": ("How to Slash Restaurant Initial Setup Expenses", "Restaurant Cost Reduction Strategies | Direct Build Contracts | Baekse Food", "Four practical tactics to cut initial restaurant opening costs: direct contractor bidding, pre-owned equipment integration, direct factory supply, and compact space design."),
        "zh": ("餐饮开店初期费用大幅节省实操指南", "开饭店如何节省初始资金 | 拒绝装修加价与直签施工队 | 百世食品", "挤掉餐饮开店四大水分：总部平米装修回扣、强制捆绑指定高价厨具、虚高加盟督导费。实操4步指南为您立省数千万韩元开店资金。"),
        "ja": ("飲食店開業の初期費用を劇的に抑える節約法", "飲食店創業コスト削減術 | 内装直契約と中古厨房機器の活用 | 百世フード", "開業資金のムダを徹底排除する4つの原則。本部中間マージンのない施工会社との直接契約、自社CKからの直送で賢くオープン。"),
        "ru": ("Как существенно сэкономить на открытии ресторана", "Экономия бюджета при открытии ресторана | Baekse Food", "4 практических способа сберечь бюджет при запуске заведения: прямые договоры с подрядчиками, качественное б/у оборудование и оптовые поставки без посредников.")
    },
    "onepack-system-explained": {
        "en": ("Understanding the One-Pack Restaurant Kitchen System", "One-Pack Kitchen System Explained | 10-Minute Cook Consistency | Baekse Food", "What is the One-Pack restaurant model? Explore how pre-portioned vacuum packs eliminate kitchen butchery, eliminate food waste, and deliver 100% consistent quality."),
        "zh": ("餐饮一包料(One-Pack)系统的运作逻辑与优势", "餐饮一包料标准化系统解析 | 10分钟出餐与后厨革命 | 百世食品", "什么是外食行业的一包料系统？拆解开袋、下料、加热10分钟出餐的标准工序，彻底告别刀工备料与食材腐烂变质，实现品控高度统一。"),
        "ja": ("飲食業界を変革するワンパックシステムとは？", "ワンパックシステム徹底解説 | 10分提供と味の均一化 | 百世フード", "仕込み不要、ロスゼロ！ワンパックシステムの仕組みとメリット。計量や下ごしらえの手間を本部に集約し、誰でも10分で名店の味を再現。"),
        "ru": ("Что такое ресторанная система One-Pack и как она работает", "Система полуфабрикатов One-Pack | Стабильный вкус за 10 минут | Baekse Food", "Концепция One-Pack в ресторанном бизнесе: порционные заготовки исключают разделку на месте, устраняют порчу сырья и гарантируют стабильный вкус.")
    },
    "boribap-franchise": {
        "en": ("Starting a Korean Barley Bibimbap Franchise", "Barley Bibimbap Franchise | Fast Lunch Turnover Strategy | Baekse Food", "Capitalize on healthy dining trends with Korean Barley Bibimbap: 3-minute serving times, explosive 3-4 table rotations during lunch, and low labor overhead."),
        "zh": ("韩国大麦饭山菜定食连锁加盟分析", "大麦饭连锁加盟创业 | 抢占养生快餐与午间快翻台红利 | 百世食品", "深入剖析韩国大麦饭餐饮市场趋势与成功三大法则：快出餐、重养生、高翻台。百世大麦饭帮助加盟商在中午4小时内快速赚回全月固定开支。"),
        "ja": ("韓国麦飯山菜定食フランチャイズの成功法則", "麦飯FC創業 | ランチ高回転と健康食トレンドの波に乗る | 百世フード", "ヘルシー志向にマッチした麦飯山菜定食の市場性と開業メリット。わずか3分でのスピード提供によりランチ4時間で店舗の採算性を劇的に向上。"),
        "ru": ("Франшиза корейского ячменного пибимпапа", "Франшиза традиционного корейского кафе | Baekse Food", "Запуск заведения традиционной корейской кухни: быстрая отдача за 3 минуты, высокая дневная проходимость и фокус на здоровом питании.")
    },
    "boribap-menu-guide": {
        "en": ("Complete Menu Guide for Barley Rice & Mountain Herbs", "Barley Bibimbap Menu Guide | Seasonal Greens & Soybean Stew | Baekse Food", "Inside the traditional five-color mountain herb bibimbap table: wild aster, bracken, radish greens, home-style fermented soybean stew, and seasoned gochujang paste."),
        "zh": ("韩国大麦饭山菜定食经典菜单构成指南", "大麦饭定食菜单全解析 | 五色山野菜与农家大酱汤的科学搭配 | 百世食品", "大麦饭定食的营养精髓在于五色平衡：蕨菜、贡菜、白萝卜丝与应季山野之珍，配上慢火熬制的老豆腐大酱汤，构成养生韩定食的黄金阵营。"),
        "ja": ("麦飯山菜定食の黄金メニュー構成ガイド", "麦飯定食メニュー解説 | 五色旬ナムルと自家製味噌チゲ | 百世フード", "食物繊維とビタミンをバランスよく補給できる五色ナムルの調和。ゼンマイ、大根、山菜と田舎味噌チゲが織りなす伝統ヘルシー膳の魅力。"),
        "ru": ("Гид по меню традиционного ячменного сета с травами", "Меню традиционного ячменного пибимпапа | Baekse Food", "Гармония пяти цветов и вкусов: дикорастущие травы, папоротник, редька и наваристый суп твенджан в составе эталонного корейского обеда.")
    },
    "boribap-startup-cost": {
        "en": ("Startup Cost Estimates for a Barley Rice Restaurant", "Barley Rice Restaurant Startup Budget | Low-Risk Renewal | Baekse Food", "Financial simulation for starting a Korean barley bibimbap restaurant: rent, kitchen equipment, remodeling existing restaurants, and fast break-even milestones."),
        "zh": ("开一家传统大麦饭餐厅的预算与回本测算", "大麦饭餐厅开业成本预算 | 老店低成本改造与盈亏平衡点 | 百世食品", "开一家大麦饭馆需要多少预算？20坪新店与老店翻新成本对比，总部提供标准化料包配送，仅需千万韩元级别改造成本即可实现高速回本。"),
        "ja": ("麦飯山菜定食屋の開業費用と損益シミュレーション", "麦飯店の初期費用 | 居抜き低コスト改装と損益分岐点 | 百世フード", "20坪モデルでの開業予算明細と早期黒字化のシミュレーション。既存店舗からの業態転換なら設備をフル活用して小額投資でリニューアル可能。"),
        "ru": ("Бюджет запуска кафе ячменного пибимпапа", "Расчет затрат на запуск традиционного кафе | Baekse Food", "Финансовый план открытия кафе корейской кухни: аренда, оборудование, переоборудование существующих помещений и быстрый выход на окупаемость.")
    },
    "boribap-health-benefits": {
        "en": ("Health Benefits & Nutritional Value of Barley Rice", "Barley Rice Health Benefits | Beta-Glucan, Blood Sugar & Diet | Baekse Food", "Why barley rice and wild mountain greens are Korea's ultimate superfood: beta-glucan for blood sugar regulation, gut health fiber, and rich antioxidants."),
        "zh": ("韩国大麦饭与山野菜的健康养生功效全解", "大麦饭的营养与健康价值 | β-葡聚糖控糖控脂与肠道健康 | 百世食品", "风靡韩国的健康养生主食！大麦富含的β-葡聚糖对平稳餐后血糖和降低胆固醇具有显著作用，搭配高纤维五色山野菜，是现代人的理想控糖餐。"),
        "ja": ("麦飯と山菜がもたらす驚きの健康効能と栄養価", "麦飯の健康効果 | β-グルカンによる血糖値管理と腸活 | 百世フード", "現代人の健康課題を解決するスーパーフード麦飯。豊富な食物繊維とβ-グルカンが血糖値の上昇を抑え、腸内環境を整えるヘルシー食の秘密。"),
        "ru": ("Польза ячменного риса и горных трав для здоровья", "Польза ячменя и корейских трав | Бета-глюкан и клетчатка | Baekse Food", "Почему ячмень и горные травы считаются суперфудом: регулирование уровня сахара в крови благодаря бета-глюкану, очищение кишечника и антиоксиданты.")
    },
    "lunch-best-menu": {
        "en": ("Top Performing Lunchtime Restaurant Menu Concepts", "Best Lunch Restaurant Items | High Turnover & Predictable Costs | Baekse Food", "Analyzing successful lunch concepts: why Korean Barley Bibimbap outperforms heavy soups and greasy dishes in dining speed, recurring visits, and margin stability."),
        "zh": ("上班族午市高吸金餐饮菜单全方位分析", "午市最畅销餐饮品类 | 3分钟出餐与超高回访率的秘密 | 百世食品", "做餐饮午市如何赚大钱？对比面食、快餐与传统炒菜，大麦饭山菜定食以出餐速度快、消化无负担、食材成本稳定成为午市致富黑马。"),
        "ja": ("ランチ営業で圧倒的に売れる人気メニューの法則", "ランチ勝てる飲食店メニュー | 驚異の回転率と常連化の秘訣 | 百世フード", "オフィス街や住宅街でランチの売上を最大化する法則。クッパや中華と比べ、なぜ麦飯山菜定食が時間あたり3〜4回転の超高効率を生むのか。"),
        "ru": ("Самые эффективные концепции блюд для обеденного потока", "Меню для максимального дневного трафика | Baekse Food", "Анализ прибыльности обеденных концепций: почему легкий ячменный пибимпап превосходит жирные блюда по скорости отдачи и регулярности визитов.")
    },
    "pocha-startup-cost": {
        "en": ("Startup Realities of Korean Night Pocha Bars", "Korean Pocha Startup Costs | Shared Kitchen Model | Baekse Food", "Realistic capital requirements for opening a Korean late-night pocha pub: utilizing daytime restaurant infrastructure to slash upfront costs and maximize beverage profit."),
        "zh": ("韩国特色大排档(Pocha)开店成本与盈利真相", "韩式大排档开店成本 | 共享白天厨房实现零多余投资 | 百世食品", "开一家韩国夜市大排档需要多少钱？解析传统独立排档的高房租死局，百世食品独创共享厨房晚间切入模式，不增租金成倍增加深夜酒水收入。"),
        "ja": ("韓国屋台ポチャ（大衆酒場）開業の現実と収益構造", "ポチャ開業のリアルな費用 | 昼の厨房をそのまま使うシェアモデル | 百世フード", "単独で居酒屋を開く際のリスクを回避！タッカンマリの厨房をそのまま流用し、設備投資ほぼゼロで夜21時以降の深夜酒場営業を始める賢い仕組み。"),
        "ru": ("Реальная стоимость открытия корейского ночного бара", "Затраты на открытие корейского бара Поча | Baekse Food", "Сколько стоит запустить традиционный корейский ночной бар: использование оборудования дневного ресторана без дополнительных инвестиций в аренду.")
    },
    "night-sales-strategy": {
        "en": ("Proven Strategies to Boost Restaurant Late-Night Sales", "Late-Night Restaurant Sales Strategies | 21:00 Time-Shift | Baekse Food", "How to convert an idle dining room into a buzzing late-night pub: the 21:00 time-shift system, retaining dinner patrons into round two, and high-margin drinks."),
        "zh": ("餐厅夜间营业额爆发式增长的三大战略", "提升夜间营业额策略 | 21点氛围转换与二次消费锁定 | 百世食品", "晚上9点之后餐厅空荡荡？三大实战招式破局：调暗主光开启暖色氛围灯、推出米炸鸡与鱼饼汤组合、把正餐顾客直接锁定为第二轮酒局客户。"),
        "ja": ("夜21時以降の売上を爆発させるナイトタイム戦略", "深夜売上アップの秘訣 | 21時のタイムシフトと2次会囲い込み | 百世フード", "ディナー終了後のデッドスペースを夜間居酒屋へ転換。照明演出の切り替えとおつまみメニューで、1次会客をそのまま2次会へ引き込むノウハウ。"),
        "ru": ("Стратегии увеличения выручки ресторана в ночные часы", "Как увеличить ночные продажи ресторана | Смена формата в 21:00 | Baekse Food", "Как превратить ресторан после 21:00 в шумный и прибыльный бар: приглушенный теплый свет, популярные закуски и удержание гостей на второй раунд.")
    },
    "shop-in-shop-guide": {
        "en": ("Pros & Cons of Shop-in-Shop Restaurant Expansions", "Shop-in-Shop Restaurant Guide | 2-Day Setup & Shared Equipment | Baekse Food", "Maximize revenue in existing stores through Shop-in-Shop concepts: integrating Dakhanmari or Pocha menu lines into idle hours with 2 days of rapid training."),
        "zh": ("餐饮店中店(Shop-in-Shop)合作模式利弊全解", "店中店合作指南 | 2天快速上手与原有厨房最大化利用 | 百世食品", "不换门面、不添大件设备，如何在现有店铺里多上一套吸金菜单？店中店模式优缺点全面剖析，教您用炸鸡店嫁接排档、烤肉店植入大麦饭。"),
        "ja": ("既存店に売上をプラスするショップ・イン・ショップの全貌", "ショップ・イン・ショップ開業 | 2日間の研修で即メニュー導入 | 百世フード", "今ある店舗の厨房設備をそのまま生かし、新しい看板メニューを追加して売上を底上げする手法。設備適合の条件と2日間でのスピード導入手順。"),
        "ru": ("Плюсы и минусы формата Shop-in-Shop для ресторанов", "Формат Shop-in-Shop для кафе | Быстрый старт за 2 дня | Baekse Food", "Как ввести новые хиты продаж в существующее меню без замены оборудования: интеграция позиций Дакханмари или ночного бара за 2 дня обучения.")
    },
    "dakhanmari-recipe-transfer": {
        "en": ("Korean Dakhanmari Master Recipe Transfer Explained", "Dakhanmari Recipe Transfer | Independent Brand vs Franchise | Baekse Food", "Understand how recipe transfers work: acquiring 35 years of authentic broth and seasoning techniques to launch an independent brand without paying franchise royalties."),
        "zh": ("韩国一只鸡正宗秘方传授课程全景解析", "一只鸡独家秘方传授 | 自创品牌vs连锁加盟的深度权衡 | 百世食品", "什么是真正的秘方传授？不交加盟费、不挂总部招牌，100%习得35年老店原汤吊制与熟成秘酱配方，助力餐饮创业者打造属于自己的百年老字号。"),
        "ja": ("本場韓国タッカンマリの秘伝レシピ伝授とは？", "タッカンマリ技術伝授 | オリジナル看板での独立開業支援 | 百世フード", "ロイヤリティ不要、看板の縛りなし！35年培われたスープと秘伝ヤンニョムの配合技術を完全移転し、自由な屋号で勝負できる伝授システムの詳細。"),
        "ru": ("Обучение приготовлению Дакханмари от шеф-мастеров", "Передача рецептов Дакханмари | Собственный бренд без роялти | Baekse Food", "Что такое прямая передача шеф-технологий: полное освоение 35-летней рецептуры корейского бульона и соусов для запуска заведения под собственным именем.")
    },
    "dakhanmari-recipe-course": {
        "en": ("5-Day Intensive Dakhanmari Recipe Training Course", "5-Day Dakhanmari Culinary Course | Flagship Hands-on Training | Baekse Food", "Full 5-day curriculum breakdown: Day 1 broth extraction, Day 2 sauce formulation, Day 3 meat butchery, Day 4 derivative stews, Day 5 store layout and kitchen QA."),
        "zh": ("5天高强度一只鸡秘方传授教学大纲", "一只鸡5天集中培训课程 | 安山总店厨房一对一实操大纲 | 百世食品", "详尽揭晓5天闭门传授日程：第1天高汤清澈萃取、第2天低温熟成辣酱调配、第3天生鸡精细分割、第4天衍生辣炖鸡扩展、第5天实战出餐考核。"),
        "ja": ("5日間集中 タッカンマリ秘伝カリキュラム詳細", "タッカンマリ伝授5日間コース | 本店厨房でのマンツーマン実習 | 百世フード", "5日間の集中研修スケジュールを完全公開。出汁の抽出からタデギ調合、丸鶏カット、タットリタンへの応用、模擬オーダーテストまで網羅。"),
        "ru": ("5-дневный практический курс рецептов Дакханмари", "Программа 5-дневного обучения Дакханмари | Baekse Food", "Полное расписание интенсива: варка чистого бульона, замес острой пасты дадеги, разделка мяса птицы, производные блюда и симуляция обслуживания.")
    },
    "dakhanmari-sauce-transfer": {
        "en": ("Mastering the 3 Core Sauces of Korean Dakhanmari", "Dakhanmari 3 Signature Sauces | Dadegi, Soy Dipping & Mustard | Baekse Food", "In-depth culinary secrets behind the triad of Dakhanmari sauces: aged red dadegi chili paste, balanced low-sodium soy sauce, and emulsified hot mustard dip."),
        "zh": ("一只鸡三大核心调料酱汁传授详解", "一只鸡三大秘制调料传授 | 熟成辣酱·特调酱油·乳化芥末 | 百世食品", "一只鸡好吃的核心全在调味！深度传授三大核心秘汁配方：72小时低温发酵辣椒酱、咸酸平衡低盐酱油原汁、温和爽口不刺鼻的乳化芥末酱。"),
        "ja": ("タッカンマリを極める三大秘伝タレの伝授", "タッカンマリ3大特製ソース伝授 | 熟成タデギ・特製醤油・からし | 百世フード", "タッカンマリの命である三大タレの調合技術。72時間低温熟成ヤンニョム、まろやかな特製かけ醤油、風味豊かな練りからしの配合比率を余すことなく伝授。"),
        "ru": ("Секреты приготовления трех фирменных соусов Дакханмари", "3 фирменных соуса Дакханмари | Острая паста, соя, горчица | Baekse Food", "Мастерство создания трех ключевых соусов: ферментированная перечная паста дадеги, слабосоленая соевая заправка и эмульгированный горчичный дип.")
    },
    "transfer-vs-franchise": {
        "en": ("Recipe Transfer vs Franchise: Which Model Suits You?", "Culinary Transfer vs Franchise | Cost, Freedom, Brand Comparison | Baekse Food", "Compare opening an independent restaurant via Recipe Transfer against partnering with a Full Franchise: analyze capital costs, operational freedom, and support systems."),
        "zh": ("餐饮技术传授vs连锁加盟：哪种更适合您？", "学技术自创品牌vs加盟连锁 | 费用·自由度与后续支持大对比 | 百世食品", "餐饮创业十字路口如何抉择？全面对比技术传授（低成本、无提成、高自由度）与品牌加盟（成熟体系、品牌背书、一站式开店），助您精准定位。"),
        "ja": ("レシピ伝授 vs フランチャイズ加盟の徹底比較", "飲食店の技術伝授 vs FC加盟 | コスト・自由度・支援体制を検証 | 百世フード", "技術だけを学んで自由な屋号で勝負するか、本部の完成された看板と仕組みに乗るか。初期費用、自由度、食材供給の3つの視点から徹底比較。"),
        "ru": ("Обучение рецептам или франшиза: что выбрать?", "Передача рецептов против франшизы | Сравнение моделей | Baekse Food", "Что выбрать ресторатору: обучение технологиям для работы под собственным брендом или покупку франшизы с готовым именем и стандартами.")
    },
    "dakhanmari-broth-supply": {
        "en": ("Dakhanmari Broth Wholesale Supply & Pricing Economics", "Dakhanmari Broth Supply Pricing | Gas & Labor Savings | Baekse Food", "Understand the economics of outsourcing broth production: save on gas utilities and 1.5M+ KRW monthly kitchen labor through direct Central Kitchen delivery."),
        "zh": ("韩国一只鸡高汤批发供应价格与成本效益", "一只鸡浓缩高汤供应行情 | 节约燃气费与大厨人工开支 | 百世食品", "门店自熬大锅骨汤的隐形成本有多高？测算高昂燃气费、清晨早起熬汤的人工消耗与夏日变质风险，百世中央厨房直发高汤让每锅成本直降30%以上。"),
        "ja": ("タッカンマリスープの仕入れ価格と厨房採算性", "タッカンマリスープ卸売供給 | 光熱費・人件費の大幅削減効果 | 百世フード", "店舗で毎日大量のガラを煮込む隠れコストを徹底検証。都市ガス代の削減、早朝仕込みの人件費ゼロ化、自社CK直送スープによる原価改善の秘密。"),
        "ru": ("Оптовые поставки бульона Дакханмари и экономика кухни", "Поставки бульона Дакханмари оптом | Экономия на кухне | Baekse Food", "Почему выгоднее закупать готовый бульон: экономия на коммунальных расходах, отказ от ночных смен поваров и стабильное качество в каждом котле.")
    },
    "dakhanmari-sauce-supply": {
        "en": ("Selecting a Reliable Dakhanmari Sauce Supply Partner", "Dakhanmari Sauce Supplier Guide | Cold-Chain All-in-One Kits | Baekse Food", "Four essential criteria for choosing a sauce supplier: flavor consistency, direct pricing without middleman markups, unbroken cold-chain logistics, and complete kits."),
        "zh": ("如何甄选优质靠谱的韩国一只鸡调料供应商", "一只鸡调料供应商挑选法则 | 冷链直供与全套料包配套 | 百世食品", "餐饮调料供应链考察四大核心：调料批次品质是否稳定、是否有中间商层层加价、是否拥有全程冷链配送、能否提供鸡肉与高汤的一站式整套解决方案。"),
        "ja": ("タッカンマリソース・仕入れ業者選びの4大基準", "タッカンマリ調味料仕入れ先選定 | 品質均一性とコールドチェーン | 百世フード", "味のブレをなくす信頼できる仕入れパートナーの条件。中間マージンを排除した直営ファクトリー価格、厳格な温度管理、キット供給の強みを解説。"),
        "ru": ("Как выбрать надежного поставщика соусов Дакханмари", "Выбор оптового поставщика соусов Дакханмари | Baekse Food", "4 правила выбора поставщика: стабильность вкуса от партии к партии, прямые цены без посредников, непрерывная холодильная цепь и поставка готовых наборов.")
    },
    "sauce-oem-vs-direct": {
        "en": ("Restaurant Sauce OEM vs Direct Factory Supply", "Sauce OEM vs Direct Manufacturing | Small Minimums & Freshness | Baekse Food", "Comparing OEM contract manufacturing against direct Central Kitchen partnership: why high MOQ minimums and stale inventory make factory-direct supply superior."),
        "zh": ("餐饮酱料OEM贴牌代工vs自营中央厨房直供", "调味品代工OEM与直营中央厨房对比 | 起订量门槛与鲜度之争 | 百世食品", "餐饮小老板千万别盲目找工厂代工OEM！高昂的吨级起订量极易导致资金被压死和酱料过期，百世自营中央厨房小批量新鲜直配为您解决后顾之忧。"),
        "ja": ("飲食店タレ仕入れ：OEM受託製造 vs 直営工場供給", "ソースのOEM製造と直営セントラルキッチン供給の比較 | 百世フード", "数トン単位の過大な最小ロット（MOQ）や在庫リスクを抱えるOEM委託の落とし穴。小ロットから新鮮に届く百世直営ファクトリーの圧倒的優位性。"),
        "ru": ("OEM-производство соусов против прямых поставок", "Контрактное производство соусов против фабрики-кухни | Baekse Food", "Сравнение OEM-производства и поставок с фабрики-кухни: почему огромные минимальные партии и риск просрочки делают прямые поставки лучшим выбором.")
    },
    "central-kitchen-system": {
        "en": ("How Central Kitchen Systems Transform Restaurants", "Central Kitchen System Explained | Space Optimization & 0% Waste | Baekse Food", "The power of Central Kitchen (CK) operations: cutting in-store kitchen footprint by 50%, enabling 1-person kitchen ops, and achieving zero raw ingredient spoilage."),
        "zh": ("中央厨房(CK)系统如何颠覆传统餐饮经营", "中央厨房系统优势全解 | 缩减50%后厨空间与零耗损运营 | 百世食品", "解析现代外食连锁核心引擎中央厨房（CK）：将后厨面积缩减一半让给前厅多放餐桌、将复杂工序前置以实现1人出餐，彻底消灭食材腐烂报废。"),
        "ja": ("飲食経営を劇的に変えるセントラルキッチン（CK）の力", "セントラルキッチンシステム徹底解説 | 厨房面積半減とロス率ゼロ | 百世フード", "セントラルキッチンの導入がもたらす外食イノベーション。客席面積の最大化、職人不要の超効率オペレーション、食材の廃棄ゼロ化を実現する仕組み。"),
        "ru": ("Как система фабрики-кухни преображает ресторанный бизнес", "Преимущества фабрики-кухни (Central Kitchen) | Baekse Food", "Сила фабрики-кухни: сокращение площади кухни на 50% в пользу зала, обслуживание одним поваром и сведение списания продуктов к абсолютному нулю.")
    },
    "food-trend-2026": {
        "en": ("Top Dining & Restaurant Trends for 2026", "2026 Restaurant Trends | Healthy Comfort, Compact & Automated | Baekse Food", "Four defining trends shaping the 2026 F&B landscape: healthy pleasure comfort dining, single-operator compact layouts, multi-brand dayparts, and automated CK kitchens."),
        "zh": ("2026年外食餐饮行业发展趋势与创业风向", "2026餐饮创业新趋势 | 养生轻慢生活·紧凑小店与自动化后厨 | 百世食品", "把握2026餐饮消费核心脉搏：健康养生理念重回顶峰、小面积高坪效微型门店崛起、单一时段向多时段全天候经营进化，百世3in1模式全面契合新趋势。"),
        "ja": ("2026年 外食産業の最新トレンドと勝ち残る飲食モデル", "2026年飲食トレンド | ヘルシー志向・省スペース・自動化 | 百世フード", "2026年の飲食業界を牽引する4大キーワード。健康志向のヘルシープレジャー、1人営業の極小店舗、昼夜マルチブランド化に完全対応した百世モデル。"),
        "ru": ("Главные ресторанные тренды 2026 года", "Тренды общепита 2026 | Здоровая еда, компактность, автоматизация | Baekse Food", "4 главных тренда ресторанного рынка 2026 года: упор на здоровье и долголетие, компактные форматы на одного сотрудника и круглосуточная мульти-концепция.")
    },
    "reduce-closure-rate": {
        "en": ("How to Dramatically Lower Restaurant Closure Rates", "Lower Restaurant Failure Rates | Multi-peak Defense & 80% Synergy | Baekse Food", "Overcome the 80% 5-year failure rate in food service: eliminating single-shift dependency through 3in1 multi-peak revenue, shared chicken inventory, and One-Pack prep."),
        "zh": ("大幅降低餐厅闭店倒闭率的实战生存法则", "如何降低餐饮闭店率 | 3重时段防线与食材80%高通用率 | 百世食品", "面对外食行业5年80%的高闭店魔咒，聪明的餐饮人如何构筑防火墙？通过午市大麦饭、晚市一只鸡与深夜排档构建三层营收安全网，彻底规避单点崩溃。"),
        "ja": ("飲食店の廃業率を劇的に引き下げるサバイバル戦略", "飲食店の廃業率を下げる方法 | 3段構えの売上防衛線と食材共通化 | 百世フード", "外食産業の5年廃業率80%という現実に打ち勝つ手法。1日3回の異なる売上ピークで家賃を分散し、食材80%共通化で廃棄ロスをゼロにする仕組み。"),
        "ru": ("Как существенно снизить риск закрытия ресторана", "Снижение риска банкротства в общепите | Baekse Food", "Как защитить заведение от закрытия: диверсификация выручки по трем пиковым зонам дня, общие ингредиенты для 80% меню и вакуумные заготовки One-Pack.")
    },
    "franchise-interior-margin": {
        "en": ("The Truth Behind Franchise Interior Construction Markups", "Franchise Interior Markups Exposed | Zero HQ Commission Policy | Baekse Food", "Exposing the industry secret of 30-50% franchise interior kickbacks: why Baekse Food enforces direct 1-to-1 builder contracts to save franchisees tens of millions in KRW."),
        "zh": ("揭秘餐饮加盟连锁总部装修暴利回扣内幕", "加盟品牌装修水分有多深 | 百世食品总部装修零抽成政策 | 百世食品", "揭开行业公开秘密：传统加盟品牌30-50%的高额装修溢价。百世食品推行加盟商与持证施工队1对1直签合同，免费提供施工图纸，为加盟商立省巨资。"),
        "ja": ("FC本部の不透明な内装中間マージンの実態", "フランチャイズ内装マージンの真実 | 本部手数料0円の直契約宣言 | 百世フード", "加盟金よりも重い「内装マージン30〜50%」の業界の闇。百世フードが施工会社との完全ダイレクト契約を義務付け、加盟店の出店費用を大幅に削る理由。"),
        "ru": ("Вся правда о наценках на ремонт от франчайзеров", "Скрытые наценки на ремонт от франшиз | Baekse Food", "Разоблачение скрытых комиссий в 30-50% на строительные работы: почему Baekse Food внедряет прямые договоры с подрядчиками по себестоимости.")
    },
    "food-cost-management": {
        "en": ("Mastering Food Cost Ratio Management in Restaurants", "Restaurant Food Cost Management | 80% Synergy & Zero Waste | Baekse Food", "How to maintain ideal 30-35% food cost ratios: optimizing menu engineering, utilizing 80% shared chicken poultry inventory, and cutting middleman markups."),
        "zh": ("餐饮门店食材原价率精细化管控秘笈", "饭店食材成本率控制技巧 | 80%食材通用与零报废实战手册 | 百世食品", "餐厅毛利上不去的致命痛点全在原价率！解析理论成本与实际成本的流失黑洞，通过菜单工程学实现鲜鸡原料80%多菜品通用，实现食材损耗无限趋近于零。"),
        "ja": ("飲食店オーナーのための食材原価率コントロール術", "食材原価率の管理ノウハウ | 食材共通化80%で廃棄ロスを撃滅 | 百世フード", "理想的な適正原価率（30〜35%）を維持するための実践テクニック。鶏肉原料をランチ・ディナー・夜間メニューで80%共用し、廃棄ロスをゼロにする秘訣。"),
        "ru": ("Управление себестоимостью продуктов в ресторане", "Контроль себестоимости продуктов | Baekse Food", "Как удерживать идеальную планку себестоимости продуктов в 30-35%: использование 80% общих ингредиентов для блюд и прямые поставки с фабрики.")
    },
    "3in1-multi-brand-guide": {
        "en": ("Complete Guide to 3-in-1 Multi-Brand Restaurants", "3-in-1 Multi-Brand Restaurant Guide | Maximizing Space Utilization | Baekse Food", "Explore the revolutionary 3-in-1 restaurant model: daytime barley bibimbap, evening dakhanmari hot pot, and late-night pocha pub from a unified kitchen footprint."),
        "zh": ("3合1复合品牌餐厅模式全面运营指南", "3in1复合外食模式指南 | 同一空间300%坪效运转全解 | 百世食品", "为什么未来餐饮是复合品牌的天下？全景展现百世3in1日出大麦饭、日落一只鸡、入夜大排档的24小时生命周期，用一套厨房设备撬动三倍营业额。"),
        "ja": ("1店舗3業態！3in1複合飲食店経営の完全ガイド", "3in1複合店舗創業ガイド | 空間効率300%を叩き出す運営術 | 百世フード", "ランチ麦飯→ディナー鍋→深夜屋台ポチャへと姿を変えるカメレオン店舗。同一の厨房で仕込みと設備をフル稼働させ、売上を多重化する革新モデル。"),
        "ru": ("Гид по мульти-брендовому ресторану концепции 3-в-1", "Ресторанная концепция 3-в-1 | Максимум эффективности площади | Baekse Food", "Как работает модель тройного формата: дневной ячменный пибимпап, вечерний суп Дакханмари и ночной корейский бар в рамках одного заведения.")
    },
    "ansan-sanchae-restaurant": {
        "en": ("Best Sanchae Bibimbap Restaurant in Ansan", "Ansan Sanchae Dining | Baekse Barley Bibimbap Flagship Store", "Visit the original Baekse Barley Bibimbap flagship store in Ansan Sangnok-gu: seasonal wild mountain herbs, cold-pressed perilla oil, and rich rustic soybean stew."),
        "zh": ("韩国安山常绿区正宗山菜定食与拌饭名店", "安山山菜定食名店 | 百世大麦饭时令山野菜拌饭与浓郁大酱汤", "寻找韩国安山正宗养生韩定食？探访常绿区沙洞百世大麦饭总店！每天清晨现拌五色纯天然山野菜，淋上鲜榨香浓紫苏油，呈现最地道的韩国传统山菜拌饭。"),
        "ja": ("韓国安山市の絶品山菜定食・ビビンバ専門店", "安山山菜定食の名店 | 旬の五色ナムルと田舎味噌チゲ 百世麦飯本店", "安山市常緑区サドンにある山菜定食の有名店！香ばしい炊きたて麦飯に旬の山菜ナムル、直伝の辛味噌とエゴマ油をたっぷりかけて味わう至極のヘルシーランチ。"),
        "ru": ("Лучший традиционный ресторан ячменного пибимпапа в Ансане", "Ресторан корейской кухни в Ансане | Baekse Barley Bibimbap", "Флагманский ресторан Baekse Barley Bibimbap в г. Ансан (район Саннок-гу): горные травы, натуральное масло периллы и традиционный суп твенджан.")
    },
    "ansan-dakhanmari-restaurant": {
        "en": ("Best Dakhanmari & Chicken Dining in Ansan", "Ansan Dakhanmari Restaurant | 35-Year Master Broth | Baekse Food", "The premier chicken dining destination in Ansan Sangnok-gu: 35-year pure crystal-clear broth, fresh tender chicken, signature chive dipping sauce, kalguksu, and egg porridge."),
        "zh": ("韩国安山一只鸡特色名店与鸡料理专家", "安山一只鸡名店 | 35年老字号清炖原汤与特色蘸汁刀削面", "安山吃一只鸡必去老字号！常绿区沙洞百世一只鸡总店，凭4.8★超高好评闻名。澄澈见底的醇厚鸡汤、特制熟成辣椒芥末酱，搭配筋道面条与黄金鸡汤粥。"),
        "ja": ("韓国安山市のタッカンマリ名店・絶品鶏料理専門店", "安山タッカンマリ名店 | 35年伝統の極上澄ましスープ 百世本店", "安山で本格的なタッカンマリを食べるならここ！澄み渡る深い出汁、当日朝締めの新鮮若鶏、自家製タデギとニラの特製ダレ、最後の生うどん＆雑炊まで感動の連続。"),
        "ru": ("Лучший ресторан корейского супа Дакханмари в Ансане", "Ресторан Дакханмари в Ансане | 35 лет традиций | Baekse Food", "Легендарный ресторан Дакханмари в г. Ансан: чистый насыщенный куриный бульон, нежное мясо, соус с луком, домашняя лапша калгуксу и сытная каша.")
    },
    "dakmaeuntang-vs-dakbokkeumtang": {
        "en": ("Dakmaeuntang vs Dakbokkeumtang: Key Differences", "Dakmaeuntang vs Dakbokkeumtang | Soup Style vs Braised Chicken Stew", "Understand the difference: Dakmaeuntang features radish-rich refreshing spicy soup with perilla leaves, while Dakbokkeumtang offers thick potato braised chicken ideal with drinks."),
        "zh": ("辣鸡汤(Dakmaeuntang)与辣炒鸡块(Dakbokkeumtang)的区别", "辣鸡汤vs辣炒鸡块对比 | 萝卜清爽汤底vs土豆浓稠酱汁", "一字之差大不同！含大量白萝卜、无土豆、带有香浓紫苏叶的清爽解酒‘辣鸡汤’，对比土豆化沙、汤汁粘稠、饭酒两相宜的经典‘辣炒鸡块’深度解析。"),
        "ja": ("タッメウンタンとタットリタンの違いとは？徹底比較", "タッメウンタン vs タットリタン | 大根のすっきりスープ vs 濃厚煮込み", "似ているようで全く違う！大根たっぷり＆えごまの葉が香るすっきりピリ辛スープ料理「タッメウンタン」と、じゃがいもが溶け込んだ濃厚な「タットリタン」の違い。"),
        "ru": ("Дакмэунтанг или Дакбоккымтан: в чем разница?", "Разница между Дакмэунтангом и Дакбоккымтаном | Baekse Food", "В чем различие: Дакмэунтанг — это суп с дайконом и листьями периллы без картофеля, а Дакбоккымтан — густая тушеная курица с картофелем под соус и алкоголь.")
    },
    "ansan-sadong-pocha": {
        "en": ("Signature Night Pocha & Late-Night Pub in Ansan", "Ansan Sangnok-gu Pocha | Baekse Pocha Crispy Chicken & Beer", "The premier midnight gathering spot near Sangnok-gu Office in Ansan: crispy rice chicken, dakgangjeong, warm fish cake soup, spicy chicken feet, and ice-cold draft beer."),
        "zh": ("韩国安山常绿区沙洞代表性大排档酒馆", "安山常绿区厅大排档首选 | 百世大排档特色米炸鸡与宵夜啤酒", "常绿区厅下班小酌与朋友宵夜首选！安山沙洞百世大排档点亮温馨夜光，外酥里嫩米炸鸡、香甜炸鸡块、铁锅关东煮鱼饼汤与爽口生啤酒，常绿区夜生活新地标。"),
        "ja": ("韓国安山・常緑区庁近くのおすすめ韓国屋台ポチャ", "安山常緑区サドンの人気ポチャ | 百世ポチャ 米粉チキンと生ビール", "常緑区庁周辺で深夜の居酒屋を探すなら百世ポチャ！カリッとジューシーな米粉チキン、あつあつおでん鍋、激辛タッパルと冷えた生ビールで夜のひとときを。"),
        "ru": ("Корейский бар Baekse Pocha в Ансане (Саннок-гу)", "Ночной бар в Ансане | Baekse Pocha Хрустящая курочка и пиво", "Атмосферный ночной бар рядом с администрацией района Саннок-гу в Ансане: курица в рисовой панировке, рыбный суп, острые закуски и ледяное пиво.")
    }
}

print(f"Mapped {len(POSTS_META)} posts metadata.")
