# -*- coding: utf-8 -*-
"""
Generate 5 new blog posts in 5 languages (ko, en, ja, zh, ru) = 25 markdown files
Targeting high-traffic search terms:
1. タッカンマリ 食べ方, つけだれ, タテギ 本格 / 닭한마리 먹는법 & 다대기 황금비율
2. タッカンマリ 雑炊, 닭한마리 죽, 칼국수, 백세보리밥 누룽지죽 (계란 없이 누룽지+참기름+김치)
3. セントラルキッチン, central kitchen, セントラルキッチン とは / 센트럴키친 원팩 시스템
4. 닭곰탕 삼계탕 차이, タッコムタン サムゲタン 違い / 닭곰탕 삼계탕 닭한마리 비교
5. 닭한마리 육수, タッカンマリ スープ / 잡내 없는 4번 끓인 비법 육수
"""

import os

BLOG_DIR = r"c:\project\baekse-food\content\blog"

# Post definitions
POSTS = [
    # ----------------------------------------------------
    # POST 1: dakhanmari-how-to-eat
    # ----------------------------------------------------
    {
        "slug": "dakhanmari-how-to-eat",
        "image": "/img/bs-menu-2.webp",
        "translations": {
            "ko": {
                "title": "닭한마리 맛있게 먹는 법과 35년 전통 비법 다대기(양념장) 황금비율",
                "seoTitle": "닭한마리 먹는 법 & 다대기 양념장 황금비율 | 백세푸드 비법 가이드",
                "description": "닭한마리 맛있게 먹는 순서부터 백세푸드 35년 비법 다대기(양념장) 황금 비율, 겨자·식초·간장의 완벽한 배합까지 현지인이 즐기는 정통 방식을 공개합니다.",
                "heroEyebrow": "AUTHENTIC HOW-TO GUIDE",
                "heroTitle": "닭한마리 맛있게 먹는 법과<br>비법 다대기(양념장) 황금비율",
                "heroLead": "깊고 담백한 닭 육수와 쫄깃한 닭고기, 그리고 중독성 있는 특제 다대기의 조화! 백세푸드 35년 노하우가 담긴 정통 시식 가이드.",
                "heroImageAlt": "닭한마리 상차림과 특제 다대기 양념장",
                "tags": ["닭한마리", "닭한마리먹는법", "다대기황금비율", "양념장", "안산맛집"],
                "faq": [
                    {
                        "q": "닭한마리 다대기 양념장의 가장 이상적인 황금비율은 무엇인가요?",
                        "a": "백세푸드 정통 비율은 고춧가루 특제 다대기 1큰술, 진간장(맛간장) 1큰술, 식초 0.5큰술, 겨자 0.5큰술, 간마늘 0.3큰술입니다. 취향에 따라 겨자와 식초를 조절하며, 채 썬 양배추나 부추를 함께 버무려 고기와 곁들이면 최고의 풍미를 냅니다."
                    },
                    {
                        "q": "닭한마리는 어떤 순서로 건져 먹어야 가장 맛있나요?",
                        "a": "냄비가 끓기 시작하면 먼저 쫄깃하게 익은 떡과 포슬포슬한 감자를 소스에 찍어 드세요. 그 사이 닭고기 속까지 진한 육수가 배어들면 닭고기를 건져 야채 소스와 함께 즐기시면 됩니다."
                    },
                    {
                        "q": "냄비 육수에 다대기나 김치를 넣어서 끓여도 되나요?",
                        "a": "처음 절반은 맑은 닭 육수 본연의 담백하고 깊은 맛을 즐기신 후, 중간에 매콤한 다대기와 백세푸드의 시원한 물김치를 통째로 넣어 얼큰하고 칼칼한 전골 스타일로 변형해 드시는 것을 추천합니다."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / EATING SEQUENCE</span>
<h2 class="h2">닭한마리 200% 즐기는<br>완벽한 시식 순서</h2>
<p class="lead">닭한마리는 단순히 닭을 끓여 먹는 요리가 아닙니다. 맑은 육수가 점점 진국이 되어가는 과정 속에서 식재료가 익어가는 순서에 맞춰 최상의 식감을 즐기는 정통 코스 요리입니다.</p>

<div class="grid grid-3" style="margin-top:28px">
  <div class="card"><div class="body">
    <span class="tag">STEP 01</span>
    <h3 class="h3">말랑한 떡과 포슬한 감자</h3>
    <p>육수가 팔팔 끓어오르면 가장 먼저 위로 떠오르는 쫄깃한 떡 사리와 달큰한 감자를 건져 특제 소스에 살짝 찍어 입맛을 돋웁니다.</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">STEP 02</span>
    <h3 class="h3">육수 머금은 촉촉한 닭고기</h3>
    <p>불을 중불로 줄이고 깊은 육수가 속살까지 배어든 닭고기를 건집니다. 채 썬 양배추·부추를 소스에 듬뿍 적셔 닭고기와 한 쌈처럼 싸서 드세요.</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">STEP 03</span>
    <h3 class="h3">얼큰 김치 전골로의 변신</h3>
    <p>맑은 국물을 충분히 즐긴 뒤, 남은 육수에 칼칼한 다대기와 아삭한 김치를 넣고 한소끔 더 끓여내면 완전히 새로운 얼큰 전골이 완성됩니다.</p>
  </div></div>
</div>
</section>

<section>
<span class="eyebrow">02 / SECRET SAUCE RATIO</span>
<h2 class="h2">35년 전통 백세푸드<br>비법 다대기(양념장) 황금비율</h2>
<p class="lead">닭한마리의 맛을 결정짓는 핵심은 바로 테이블에서 즉석 제조하는 '특제 다대기 소스'입니다. 알싸한 매운맛, 감칠맛 나는 간장, 톡 쏘는 겨자와 상큼한 식초가 어우러져 닭고기의 기름진 맛을 완벽히 잡아줍니다.</p>

<div style="border:1px solid rgba(199,84,29,.25);background:rgba(199,84,29,.05);padding:24px;border-radius:8px;margin-top:24px">
  <h3 class="h3" style="margin:0 0 16px;color:#c7541d">백세푸드 추천 다대기 소스 황금 배합표</h3>
  <ul style="line-height:2;margin:0;padding-left:20px">
    <li><strong>특제 비법 다대기(붉은 양념):</strong> 1 큰술 (기본 칼칼한 감칠맛의 중심)</li>
    <li><strong>특제 맛간장:</strong> 1 큰술 (짜지 않고 풍미를 더해주는 베이스)</li>
    <li><strong>양조식초:</strong> 0.5 큰술 (뒷맛을 깔끔하고 산뜻하게 정돈)</li>
    <li><strong>연겨자:</strong> 0.3 ~ 0.5 큰술 (코끝을 맴도는 개운한 풍미)</li>
    <li><strong>간마늘:</strong> 0.3 큰술 (한국 정통의 깊고 알싸한 맛 완성)</li>
    <li><strong>신선한 채소:</strong> 채 썬 양배추와 부추를 소스 볼에 가득 넣어 버무리기</li>
  </ul>
</div>
</section>

<section>
<span class="eyebrow">03 / LOCAL SECRETS</span>
<h2 class="h2">단골들만 아는 현지 꿀팁</h2>
<p class="lead">안산 백세푸드 매장을 찾는 단골손님들이 입을 모아 극찬하는 숨은 꿀팁을 전수합니다.</p>
<ul style="line-height:1.9;color:var(--text);margin-top:16px">
  <li><strong>물김치 국물 활용:</strong> 제공되는 시원한 김치 국물을 냄비 육수에 2~3 국자 부어 끓이면 느끼함이 제로가 되고 국물이 극도로 시원해집니다.</li>
  <li><strong>소스에 닭가슴살 찢어 넣기:</strong> 퍽퍽할 수 있는 닭가슴살을 결대로 찢어 다대기 소스 볼에 버무려 두었다가 먹으면 촉촉하고 매콤새콤한 별미 요리가 됩니다.</li>
  <li><strong>칼국수와 누룽지죽 필수 코스:</strong> 고기를 다 드신 후 남은 진국 육수에 칼국수 사리를 끓여 드시고, 마지막에 구수한 누룽지죽으로 마무리하세요!</li>
</ul>

<div style="border:1px solid rgba(199,84,29,.35);background:linear-gradient(120deg,rgba(199,84,29,.14),rgba(245,241,232,.03));padding:clamp(26px,4vw,40px);margin-top:36px;display:flex;flex-direction:column;gap:16px">
  <h3 class="h3" style="margin:0">35년 전통의 손맛, 백세닭한마리 본점에서 직접 경험해보세요</h3>
  <p style="margin:0;color:var(--muted);line-height:1.8">
    <strong>본점 주소:</strong> 경기도 안산시 상록구 석호로 101, 1층<br>
    <strong>영업시간:</strong> 매일 10:00 ~ 22:00 (연중무휴)<br>
    <strong>예약 및 가맹 문의:</strong> 031-407-0103
  </p>
</div>
</section>
"""
            },
            "ja": {
                "title": "タッカンマリの美味しい食べ方＆本場秘伝タテギ（つけだれ）黄金比率レシピ",
                "seoTitle": "タッカンマリ 食べ方・つけだれ・本格タテギ黄金比率 | 百世フード公式",
                "description": "韓国本場のタッカンマリを200%美味しく食べる順番と、35年伝統の秘伝タテギ（唐辛子だれ）・酢・醤油・マスタードの黄金比率つけだれレシピを徹底解説。",
                "heroEyebrow": "AUTHENTIC HOW-TO GUIDE",
                "heroTitle": "タッカンマリの美味しい食べ方＆<br>本場秘伝タテギ（つけだれ）黄金比率",
                "heroLead": "澄んだ極上鶏スープとジューシーな鶏肉、そして病みつきになる特製タテギのハーモニー！35年のノウハウが詰まった本場の食べ方ガイド。",
                "heroImageAlt": "タッカンマリ鍋と秘伝のつけだれ（タテギ）",
                "tags": ["タッカンマリ食べ方", "タッカンマリつけだれ", "タッカンマリタテギ本格", "韓国料理レシピ"],
                "faq": [
                    {
                        "q": "タッカンマリのつけだれ（タテギ）の黄金比率は？",
                        "a": "基本は【特製タテギ 1】：【特製醤油 1】：【酢 0.5】：【からし（マスタード）0.3〜0.5】：【すりおろしニンニク 0.3】です。小皿でよく混ぜ、千切りキャベツやニラをたっぷり絡めて鶏肉と一緒に召し上がってください。"
                    },
                    {
                        "q": "具材を食べるおすすめの順番はありますか？",
                        "a": "スープが沸騰したら、まずは火の通りが早いお餅（トック）とホクホクのジャガイモからタレにつけて食べます。その間に鶏肉の芯まで旨味が染み込み、ふっくら柔らかくなった鶏肉を味わいます。"
                    },
                    {
                        "q": "途中でスープにタテギやキムチを入れても良いですか？",
                        "a": "はい！前半は澄んだ透明な鶏出汁のコクをストレートに楽しみ、中盤からタテギや白菜キムチを鍋に投入してピリ辛の赤いチゲ風に味変するのが本場韓国の王道スタイルです。"
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / EATING SEQUENCE</span>
<h2 class="h2">本場の味を満喫する<br>タッカンマリの正しい食べ方手順</h2>
<p class="lead">タッカンマリ（鶏一羽鍋）は、ただ煮込んで食べるだけの鍋料理ではありません。澄んだ出汁が煮詰まって濃厚になっていく過程の中で、食材ごとに最高の食感を味わう韓国伝統のコース料理です。</p>

<div class="grid grid-3" style="margin-top:28px">
  <div class="card"><div class="body">
    <span class="tag">STEP 01</span>
    <h3 class="h3">もちもちトックとジャガイモ</h3>
    <p>スープが沸騰したら、まずは浮き上がってきたお餅とジャガイモを取り出し、特製つけだれにつけて前菜代わりに楽しみます。</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">STEP 02</span>
    <h3 class="h3">出汁が染みたジューシーな鶏肉</h3>
    <p>弱火にして旨味が凝縮した鶏肉を取り出します。タレに千切りキャベツとニラをたっぷり絡め、鶏肉と一緒に頬張ります。</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">STEP 03</span>
    <h3 class="h3">キムチとタテギでピリ辛味変</h3>
    <p>澄んだスープを味わった後は、鍋にキムチとタテギを加えて一煮立ち。旨辛スープへと劇的な味変（あじへん）を堪能します。</p>
  </div></div>
</div>
</section>

<section>
<span class="eyebrow">02 / SECRET SAUCE RATIO</span>
<h2 class="h2">35年伝統 百世フード直伝<br>本格タテギ（つけだれ）の黄金比率</h2>
<p class="lead">タッカンマリの美味しさの決め手は、卓上で自分好みに調合する「特製つけだれ」です。ピリッとした辛み、まろやかな特製醤油、爽やかな酸味とツンとくるからしが、鶏肉のジューシーな脂を完璧に引き立てます。</p>

<div style="border:1px solid rgba(199,84,29,.25);background:rgba(199,84,29,.05);padding:24px;border-radius:8px;margin-top:24px">
  <h3 class="h3" style="margin:0 0 16px;color:#c7541d">プロ直伝！タテギつけだれ黄金配合比率</h3>
  <ul style="line-height:2;margin:0;padding-left:20px">
    <li><strong>本格タテギ（特製唐辛子ペースト）：</strong> 大さじ1（旨辛味のベース）</li>
    <li><strong>特製出汁醤油：</strong> 大さじ1（塩味がきつすぎない専用醤油）</li>
    <li><strong>お酢：</strong> 大さじ0.5（後味をさっぱりと引き締める）</li>
    <li><strong>練りからし（マスタード）：</strong> 小さじ1/2〜1（ピリッとしたアクセント）</li>
    <li><strong>すりおろしニンニク：</strong> 小さじ1/3（韓国料理らしい深いパンチ）</li>
    <li><strong>薬味野菜：</strong> 千切りキャベツ・ニラを器いっぱいに浸す</li>
  </ul>
</div>
</section>

<section>
<span class="eyebrow">03 / LOCAL SECRETS</span>
<h2 class="h2">常連が実践する本場韓国の裏技</h2>
<p class="lead">韓国ソウル・安山の百世フード本店で愛され続ける、常連客の美味しい食べ方テクニックをご紹介します。</p>
<ul style="line-height:1.9;color:var(--text);margin-top:16px">
  <li><strong>水キムチの汁を鍋に投入：</strong> 提供されるキムチの汁をお玉2〜3杯スープに入れると、酸味と乳酸菌のコクが加わり絶品スープに進化します。</li>
  <li><strong>鶏むね肉をタレに漬け込む：</strong> パサつきがちな胸肉は、細かく裂いてタテギのタレに2〜3分浸してからキャベツと一緒に食べると極上にしっとりします。</li>
  <li><strong>締めはカルグクスからヌルンジ雑炊へ：</strong> 鶏の出汁が極限まで溶け出したスープに麺を入れ、最後は名物の香ばしいおこげ雑炊（ヌルンジ雑炊）で完璧に締めくくります。</li>
</ul>

<div style="border:1px solid rgba(199,84,29,.35);background:linear-gradient(120deg,rgba(199,84,29,.14),rgba(245,241,232,.03));padding:clamp(26px,4vw,40px);margin-top:36px;display:flex;flex-direction:column;gap:16px">
  <h3 class="h3" style="margin:0">35年伝統の味を安山・百世フード本店でご体験ください</h3>
  <p style="margin:0;color:var(--muted);line-height:1.8">
    <strong>本店所在地：</strong> 京畿道安山市常緑区石湖路101、1階<br>
    <strong>営業時間：</strong> 毎日 10:00 〜 22:00 (年中無休)<br>
    <strong>ご予約・お問い合わせ：</strong> +82-31-407-0103
  </p>
</div>
</section>
"""
            },
            "en": {
                "title": "How to Eat Dakhanmari & The Golden Ratio of Authentic Tateki Dipping Sauce",
                "seoTitle": "How to Eat Dakhanmari & Secret Tateki Sauce Ratio | Baekse Food",
                "description": "Master the art of eating Korean whole chicken soup (Dakhanmari). Learn the ideal eating sequence, secret tateki spicy paste ratio, and local insider tips.",
                "heroEyebrow": "AUTHENTIC HOW-TO GUIDE",
                "heroTitle": "How to Eat Dakhanmari &<br>The Secret Tateki Sauce Ratio",
                "heroLead": "Rich, comforting chicken broth, tender chicken pieces, and the irresistible spicy-tangy dipping sauce. Experience authentic Korean dining culture.",
                "heroImageAlt": "Dakhanmari chicken soup with dipping sauce",
                "tags": ["Dakhanmari", "HowToEat", "KoreanSauce", "BaekseFood"],
                "faq": [
                    {
                        "q": "What is the secret ratio for the authentic dipping sauce?",
                        "a": "Combine 1 tbsp special red chili paste (Tateki), 1 tbsp seasoned soy sauce, 0.5 tbsp vinegar, 0.3-0.5 tbsp hot mustard, and 0.3 tbsp minced garlic. Mix well with finely shredded cabbage and chives."
                    },
                    {
                        "q": "What is the best order to eat the ingredients?",
                        "a": "Start with the chewy rice cakes and tender potatoes as soon as the pot boils. Then enjoy the juicy chicken pieces with the freshly tossed vegetable dipping sauce."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / EATING SEQUENCE</span>
<h2 class="h2">The Perfect Sequence to Enjoy Dakhanmari</h2>
<p class="lead">Dakhanmari is more than just chicken soup—it is a traditional multi-stage culinary experience cooked right at your table.</p>
<div class="grid grid-3" style="margin-top:28px">
  <div class="card"><div class="body">
    <span class="tag">STEP 01</span>
    <h3 class="h3">Rice Cakes & Potatoes</h3>
    <p>Enjoy floating soft rice cakes and tender potato slices first, dipping them lightly into the seasoned sauce.</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">STEP 02</span>
    <h3 class="h3">Tender Chicken & Vegetables</h3>
    <p>Ladle out tender chicken pieces and wrap them with shredded cabbage soaked in spicy tateki sauce.</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">STEP 03</span>
    <h3 class="h3">Noodles & Scorched Rice Finish</h3>
    <p>Add handmade kalguksu noodles, followed by Baekse Food's signature scorched rice porridge (Nurungji-juk).</p>
  </div></div>
</div>
</section>
<section>
<span class="eyebrow">02 / SECRET SAUCE RATIO</span>
<h2 class="h2">The Golden Ratio for Tateki Sauce</h2>
<p class="lead">The magical taste comes from balancing spicy, savory, tangy, and pungent flavors:</p>
<div style="border:1px solid rgba(199,84,29,.25);background:rgba(199,84,29,.05);padding:24px;border-radius:8px;margin-top:24px">
  <ul style="line-height:2;margin:0;padding-left:20px">
    <li><strong>Special Tateki Chili Paste:</strong> 1 Tablespoon</li>
    <li><strong>Seasoned Soy Sauce:</strong> 1 Tablespoon</li>
    <li><strong>Brewed Vinegar:</strong> 0.5 Tablespoon</li>
    <li><strong>Hot Mustard:</strong> 0.3 to 0.5 Tablespoon</li>
    <li><strong>Minced Garlic:</strong> 0.3 Tablespoon</li>
    <li><strong>Fresh Garnish:</strong> Shredded cabbage & Asian chives</li>
  </ul>
</div>
</section>
"""
            },
            "zh": {
                "title": "韩国一只鸡美味吃法与35年秘制辣椒酱(蘸料)黄金比例配方",
                "seoTitle": "韩国一只鸡吃法与秘制蘸料比例 | 百世食品正宗指南",
                "description": "详解韩国正宗一只鸡的品尝顺序，以及35年传承的特制辣椒酱（Tateki）、酱油、芥末、醋黄金搭配秘方，尽享原汁原味的韩国美食。",
                "heroEyebrow": "AUTHENTIC HOW-TO GUIDE",
                "heroTitle": "韩国一只鸡美味吃法与<br>秘制辣椒酱(蘸料)黄金比例",
                "heroLead": "清澈鲜美的高汤、鲜嫩多汁的鸡肉，搭配令人欲罢不能的特制秘酱！百世食品35年传承正宗品尝指南。",
                "heroImageAlt": "韩国一只鸡与秘制蘸料",
                "tags": ["一只鸡吃法", "一只鸡蘸料", "韩国料理", "百世食品"],
                "faq": [
                    {
                        "q": "正宗一只鸡蘸料的黄金比例是什么？",
                        "a": "特制辣椒酱1大勺、专用酱油1大勺、食醋0.5大勺、黄芥末0.3~0.5大勺、蒜泥0.3大勺。在碗中充分调匀后加入大量卷心菜丝和韭菜，夹着鸡肉一起食用。"
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / EATING SEQUENCE</span>
<h2 class="h2">一只鸡正宗享用顺序</h2>
<p class="lead">一只鸡不仅是一道鸡汤，更是一道随着高汤不断炖煮、滋味愈加浓郁的餐桌仪式。</p>
<div class="grid grid-3" style="margin-top:28px">
  <div class="card"><div class="body">
    <span class="tag">STEP 01</span>
    <h3 class="h3">软糯年糕与土豆</h3>
    <p>汤水沸腾后，先捞出浮起的年糕条和粉糯土豆，蘸少许秘制酱汁品尝。</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">STEP 02</span>
    <h3 class="h3">多汁鲜鸡肉搭配蔬菜</h3>
    <p>将充分吸收汤汁的鸡肉捞出，配上浸透特制酱料的爽口卷心菜和韭菜一同享用。</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">STEP 03</span>
    <h3 class="h3">刀削面与香脆锅巴粥</h3>
    <p>最后在浓郁鸡汤中煮入手工面条，接着加入百世食品特色的香脆锅巴熬成暖胃热粥。</p>
  </div></div>
</div>
</section>
"""
            },
            "ru": {
                "title": "Как правильно есть Дакханмари и золотая пропорция традиционного соуса Тадеги",
                "seoTitle": "Как есть Дакханмари & Рецепт соуса Тадеги | Baekse Food",
                "description": "Пошаговое руководство по употреблению корейского супа Дакханмари. Идеальные пропорции острого соуса тадеги, горчицы, уксуса и соевого соуса от Baekse Food.",
                "heroEyebrow": "AUTHENTIC HOW-TO GUIDE",
                "heroTitle": "Как правильно есть Дакханмари и<br>золотая пропорция соуса Тадеги",
                "heroLead": "Наваристый куриный бульон, нежное мясо и фирменный соус с яркой перчинкой. Откройте для себя культуру корейского застолья.",
                "heroImageAlt": "Блюдо Дакханмари и острый соус тадеги",
                "tags": ["Дакханмари", "КорейскийСоус", "Тадеги", "BaekseFood"],
                "faq": [
                    {
                        "q": "В чем секрет соуса для Дакханмари?",
                        "a": "1 ст.л. острой пасты тадеги, 1 ст.л. соевого соуса, 0.5 ст.л. уксуса, 0.3 ст.л. горчицы и 0.3 ст.л. чеснока. Смешайте со свежей капустой и зеленым луком."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / EATING SEQUENCE</span>
<h2 class="h2">Порядок употребления Дакханмари</h2>
<p class="lead">Дакханмари готовится прямо за вашим столом, раскрывая новые вкусовые грани с каждой минутой кипения.</p>
<div class="grid grid-3" style="margin-top:28px">
  <div class="card"><div class="body">
    <span class="tag">STEP 01</span>
    <h3 class="h3">Рисовые клецки и картофель</h3>
    <p>Сначала попробуйте мягкие рисовые клецки тток и картофель, обмакивая их в пикантный соус.</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">STEP 02</span>
    <h3 class="h3">Нежная курица с овощами</h3>
    <p>Достаньте курицу и заверните кусочки в хрустящую капусту, пропитанную соусом тадеги.</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">STEP 03</span>
    <h3 class="h3">Лапша и каша из нурунджи</h3>
    <p>Завершите трапезу домашней лапшой и ароматной кашей из поджаренного риса с кунжутным маслом.</p>
  </div></div>
</div>
</section>
"""
            }
        }
    },

    # ----------------------------------------------------
    # POST 2: dakhanmari-nurungji-juk (USER SPECIAL REFINED!)
    # ----------------------------------------------------
    {
        "slug": "dakhanmari-nurungji-juk",
        "image": "/img/bs-menu-7.webp",
        "translations": {
            "ko": {
                "title": "닭한마리의 꽃, 칼국수와 백세보리밥 시그니처 '누룽지죽' 맛있게 끓이는 법",
                "seoTitle": "닭한마리 칼국수 & 백세보리밥 누룽지죽(雑炊) 끓이는 법 | 계란 없이 깊은 맛",
                "description": "닭한마리 코스의 하이라이트! 칼국수 후 자작해진 육수에 계란 없이 구수한 누룽지와 참기름만으로 끓여 김치와 곁들이는 백세보리밥 닭한마리 시그니처 누룽지죽 비법을 공개합니다.",
                "heroEyebrow": "THE ULTIMATE FINISH",
                "heroTitle": "닭한마리의 꽃, 칼국수와<br>시그니처 '누룽지죽'의 비밀",
                "heroLead": "닭과 야채가 농축된 진국 육수에 쫄깃한 면발, 그리고 계란 없이 누룽지와 참기름으로 완성하는 극상의 구수함!",
                "heroImageAlt": "닭한마리 칼국수와 누룽지죽",
                "tags": ["닭한마리죽", "누룽지죽", "닭한마리칼국수", "타ッカンマリ雑炊", "백세보리밥"],
                "faq": [
                    {
                        "q": "백세보리밥 닭한마리의 누룽지죽에는 왜 계란이 들어가지 않나요?",
                        "a": "일반 샤브샤브 죽에는 계란을 풀어 부드럽게 하지만, 닭한마리에서는 닭 뼈와 살에서 우러난 진한 육수 본연의 맑고 깊은 감칠맛과 전통 가마솥 누룽지의 구수한 풍미를 온전히 살리기 위해 계란을 넣지 않습니다. 계란이 들어가지 않아야 텁텁함 없이 깔끔하고 개운한 맛이 완성됩니다."
                    },
                    {
                        "q": "누룽지죽은 어떻게 끓여야 가장 맛있나요?",
                        "a": "칼국수를 드신 후 남은 육수가 자작해질 정도로 졸아들었을 때 구수한 누룽지와 고소한 참기름을 넣습니다. 중불에서 누룽지 알갱이가 부드러워질 때까지 자작하게 저어가며 끓인 뒤, 시원하고 아삭한 김치를 얹어 드시면 최고의 궁합을 자랑합니다."
                    },
                    {
                        "q": "칼국수 사리를 넣을 때 육수 조절은 어떻게 하나요?",
                        "a": "면을 넣기 전 육수가 부족하면 본사에서 제공하는 맑은 비법 육수를 한 국자 보충한 뒤 센 불에서 팔팔 끓여 전분기가 면에 잘 감기도록 끓여주는 것이 좋습니다."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / THE NOODLE PHASE</span>
<h2 class="h2">1단계: 닭 육수의 정점을 품은<br>쫄깃한 칼국수 사리</h2>
<p class="lead">닭고기와 야채가 오랫동안 우러난 국물은 그 자체로 최고의 천연 육수입니다. 닭한마리의 1차 마무리는 바로 이 진국에 끓여내는 칼국수입니다.</p>

<div class="grid grid-2" style="margin-top:24px">
  <div class="card"><div class="body">
    <h3 class="h3">전분을 털어내고 강불에 끓이기</h3>
    <p>칼국수 생면의 겉가루를 살짝 털어낸 후 끓는 육수에 넣습니다. 3~4분간 센 불에서 끓여 면발이 닭 육수를 흠뻑 흡수하도록 합니다.</p>
  </div></div>
  <div class="card"><div class="body">
    <h3 class="h3">김치 국물과 다대기 추가 팁</h3>
    <p>맑은 칼국수로 반을 즐긴 뒤, 남은 반에 특제 다대기와 김치 국물을 풀어주면 칼칼하고 개운한 '장칼국수 스타일'로 즐길 수 있습니다.</p>
  </div></div>
</div>
</section>

<section>
<span class="eyebrow">02 / SIGNATURE NURUNGJI JUK</span>
<h2 class="h2">2단계: 백세보리밥 닭한마리의 독보적 인기 메뉴<br>계란 없이 끓이는 '누룽지죽'</h2>
<p class="lead">칼국수를 다 먹고 나면 바닥에 자작하게 남은 농축 육수가 기다립니다. 여기서 일반적인 밥과 계란을 넣은 죽 대신, 백세보리밥 닭한마리에서 가장 뜨거운 사랑을 받는 비밀 메뉴가 바로 <strong>'누룽지죽'</strong>입니다.</p>

<div style="border:1px solid rgba(199,84,29,.25);background:rgba(199,84,29,.05);padding:24px;border-radius:8px;margin-top:24px">
  <h3 class="h3" style="margin:0 0 16px;color:#c7541d">✨ 백세보리밥 누룽지죽만의 3가지 비법 원칙</h3>
  <ul style="line-height:2;margin:0;padding-left:20px">
    <li><strong>1. 계란은 절대 넣지 않습니다:</strong> 계란을 풀면 육수가 탁해지고 누룽지의 고소한 곡물향이 덮입니다. 닭 육수 본연의 맑고 깊은 감칠맛을 지키기 위해 오직 누룽지만을 넣습니다.</li>
    <li><strong>2. 참기름과 자작한 육수의 조화:</strong> 칼국수 후 자작해진 육수에 바삭한 전통 누룽지와 고소한 참기름을 두르고, 누룽지가 부드럽게 퍼질 때까지 중불에서 천천히 저어가며 끓입니다.</li>
    <li><strong>3. 아삭한 김치와의 완벽한 페어링:</strong> 겉은 부드럽고 속은 쫀득하게 풀어진 누룽지죽 한 숟가락 위에, 매장에서 직접 담근 시원한 김치를 얹어 드시면 고소함과 상큼함이 폭발합니다.</li>
  </ul>
</div>
</section>

<section>
<span class="eyebrow">03 / COMPARISON</span>
<h2 class="h2">일반 죽(雑炊) vs 백세보리밥 누룽지죽</h2>
<div style="overflow-x:auto;margin-top:20px">
  <table style="width:100%;border-collapse:collapse;text-align:left;line-height:1.8">
    <thead>
      <tr style="border-bottom:2px solid var(--border);color:var(--text)">
        <th style="padding:12px">구분</th>
        <th style="padding:12px">일반 닭죽 / 雑炊(조우스이)</th>
        <th style="padding:12px;color:#c7541d">백세보리밥 시그니처 누룽지죽</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom:1px solid var(--border)">
        <td style="padding:12px;font-weight:bold">주재료</td>
        <td style="padding:12px">일반 흰쌀밥, 김가루, 계란</td>
        <td style="padding:12px;font-weight:bold;color:#c7541d">전통 가마솥 누룽지 + 순수 참기름</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border)">
        <td style="padding:12px;font-weight:bold">계란 유무</td>
        <td style="padding:12px">계란을 풀어 부드럽게 만듦</td>
        <td style="padding:12px;font-weight:bold;color:#c7541d">계란 없음 (닭 육수 순수 감칠맛 보존)</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border)">
        <td style="padding:12px;font-weight:bold">식감 및 풍미</td>
        <td style="padding:12px">부드럽고 크리미한 계란죽 느낌</td>
        <td style="padding:12px;font-weight:bold;color:#c7541d">구수한 누룽지의 쫀득한 식감과 깔끔한 뒷맛</td>
      </tr>
    </tbody>
  </table>
</div>

<div style="border:1px solid rgba(199,84,29,.35);background:linear-gradient(120deg,rgba(199,84,29,.14),rgba(245,241,232,.03));padding:clamp(26px,4vw,40px);margin-top:36px;display:flex;flex-direction:column;gap:16px">
  <h3 class="h3" style="margin:0">속을 편안하게 채워주는 누룽지죽, 백세푸드에서 맛보세요</h3>
  <p style="margin:0;color:var(--muted);line-height:1.8">
    <strong>본점 주소:</strong> 경기도 안산시 상록구 석호로 101, 1층 (백세보리밥 & 닭한마리)<br>
    <strong>영업시간:</strong> 10:00 ~ 22:00 (연중무휴)<br>
    <strong>가맹 및 전수 문의:</strong> 031-407-0103
  </p>
</div>
</section>
"""
            },
            "ja": {
                "title": "タッカンマリの締めはこれ！絶品カルグクス＆百世名物「ヌルンジ（おこげ）雑炊」の作り方",
                "seoTitle": "タッカンマリ 雑炊（おじや）とカルグクス締め | 百世名物ヌルンジ雑炊",
                "description": "タッカンマリ（タッカンマリ 雑炊）の真髄！濃厚スープで作るカルグクスと、卵を入れず香ばしいおこげとごま油のみで煮込む百世麦飯・タッカンマリ名物ヌルンジ雑炊の秘密。",
                "heroEyebrow": "THE ULTIMATE FINISH",
                "heroTitle": "タッカンマリの締めはこれ！<br>名物「ヌルンジ（おこげ）雑炊」の秘密",
                "heroLead": "鶏の旨味が凝縮した極上スープで煮るカルグクス、そして卵を入れず香ばしいヌルンジとごま油で仕上げる感動の締め雑炊！",
                "heroImageAlt": "タッカンマリのカルグクスとヌルンジ雑炊",
                "tags": ["タッカンマリ雑炊", "タッカンマリ締め", "韓国鶏雑炊", "ヌルンジ雑炊"],
                "faq": [
                    {
                        "q": "百世フードのタッカンマリ雑炊にはなぜ卵を入れないのですか？",
                        "a": "一般的な日本の雑炊では卵をとじますが、タッカンマリでは長時間煮詰まった鶏出汁の澄んだ旨味と、香ばしいおこげ（ヌルンジ）本来の風味を損なわないよう、あえて卵を入れません。卵を入れないことで濁らず、すっきり深い香ばしさが際立ちます。"
                    },
                    {
                        "q": "ヌルンジ雑炊はどうやって作りますか？",
                        "a": "カルグクス（うどん）を食べ終えた後、出汁が少量残った鍋にヌルンジ（おこげ）と香り高いごま油を加えます。弱火でおこげが柔らかくなるまで煮込み、仕上げに自家製キムチを添えて食べるのが最高に美味しい食べ方です。"
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / THE NOODLE PHASE</span>
<h2 class="h2">第1段階：鶏出汁の極みを吸い込む<br>もちもちカルグクス（手打ち麺）</h2>
<p class="lead">鶏肉と野菜の旨味が極限まで溶け出したスープは、まさに天然の極上出汁。タッカンマリの第1の締めは、この黄金スープで煮込むカルグクスです。</p>

<div class="grid grid-2" style="margin-top:24px">
  <div class="card"><div class="body">
    <h3 class="h3">強火で一気に煮込む</h3>
    <p>麺の余分な粉を落とし、沸騰したスープに投入。強火で3〜4分煮込むことで、麺が出汁をたっぷり吸い込みモチモチになります。</p>
  </div></div>
  <div class="card"><div class="body">
    <h3 class="h3">タテギとキムチで旨辛アレンジ</h3>
    <p>半分は澄んだ鶏出汁で味わい、残り半分に特製タテギとキムチを投入すれば、パンチの効いた旨辛うどんへと進化します。</p>
  </div></div>
</div>
</section>

<section>
<span class="eyebrow">02 / SIGNATURE NURUNGJI JUK</span>
<h2 class="h2">第2段階：百世麦飯・タッカンマリの圧倒的人気メニュー<br>卵を入れない「ヌルンジ（おこげ）雑炊」</h2>
<p class="lead">麺を食べ終え、鍋底にわずかに残った濃厚な凝縮スープ。一般的な白ご飯と卵の雑炊ではなく、百世フードで熱狂的なファンを持つ名物こそが<strong>「ヌルンジ雑炊（おこげ雑炊）」</strong>です。</p>

<div style="border:1px solid rgba(199,84,29,.25);background:rgba(199,84,29,.05);padding:24px;border-radius:8px;margin-top:24px">
  <h3 class="h3" style="margin:0 0 16px;color:#c7541d">✨ 百世名物ヌルンジ雑炊 3つのこだわり</h3>
  <ul style="line-height:2;margin:0;padding-left:20px">
    <li><strong>1. 卵は絶対に入れません：</strong> 卵を入れるとスープが濁り、おこげの芳醇な穀物の香りが消えてしまいます。鶏出汁本来の深いコクを保つため、卵は使いません。</li>
    <li><strong>2. おこげと純ごま油の絶妙な調和：</strong> 煮詰まったスープに香ばしい釜焼きヌルンジと純ごま油を加え、おこげがとろりと柔らかくなるまで中火で煮込みます。</li>
    <li><strong>3. シャキシャキのキムチを添えて：</strong> 柔らかくほどけた香ばしいおこげ雑炊の上に、熟成キムチを乗せて食べれば、濃厚な旨味と酸味が口いっぱいに広がります。</li>
  </ul>
</div>
</section>

<section>
<span class="eyebrow">03 / COMPARISON</span>
<h2 class="h2">一般的な雑炊（おじや） vs 百世名物ヌルンジ雑炊</h2>
<div style="overflow-x:auto;margin-top:20px">
  <table style="width:100%;border-collapse:collapse;text-align:left;line-height:1.8">
    <thead>
      <tr style="border-bottom:2px solid var(--border);color:var(--text)">
        <th style="padding:12px">項目</th>
        <th style="padding:12px">一般的な鶏雑炊</th>
        <th style="padding:12px;color:#c7541d">百世名物 ヌルンジ雑炊</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom:1px solid var(--border)">
        <td style="padding:12px;font-weight:bold">主原料</td>
        <td style="padding:12px">白米、刻み海苔、卵</td>
        <td style="padding:12px;font-weight:bold;color:#c7541d">伝統釜焼きヌルンジ ＋ 純正ごま油</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border)">
        <td style="padding:12px;font-weight:bold">卵の使用</td>
        <td style="padding:12px">溶き卵でとじる</td>
        <td style="padding:12px;font-weight:bold;color:#c7541d">不使用（鶏出汁本来の旨味を凝縮）</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border)">
        <td style="padding:12px;font-weight:bold">食感と後味</td>
        <td style="padding:12px">ふんわりクリーミー</td>
        <td style="padding:12px;font-weight:bold;color:#c7541d">香ばしくモチモチ、後味すっきり</td>
      </tr>
    </tbody>
  </table>
</div>
</section>
"""
            },
            "en": {
                "title": "The Grand Finale of Dakhanmari: Kalguksu Noodles & Signature Scorched Rice Porridge",
                "seoTitle": "Dakhanmari Porridge & Noodles | Baekse Food Signature Nurungji-Juk",
                "description": "Discover the highlight of Korean whole chicken soup: rich broth noodles and Baekse Food's signature scorched rice porridge (Nurungji-juk), made without eggs for a pure savory finish.",
                "heroEyebrow": "THE ULTIMATE FINISH",
                "heroTitle": "The Grand Finale of Dakhanmari:<br>Kalguksu & Signature Scorched Rice Porridge",
                "heroLead": "Chewy knife-cut noodles in concentrated chicken broth, followed by the nutty aroma of crispy scorched rice cooked with sesame oil—without eggs!",
                "heroImageAlt": "Dakhanmari noodles and scorched rice porridge",
                "tags": ["Dakhanmari", "Porridge", "Nurungji", "KoreanFood"],
                "faq": [
                    {
                        "q": "Why is there no egg in Baekse Food's scorched rice porridge?",
                        "a": "Unlike ordinary porridges, we do not add eggs in order to preserve the crystal-clear chicken flavor and highlighting the natural nutty aroma of authentic scorched rice (nurungji)."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / FINISHING COURSE</span>
<h2 class="h2">From Chewy Noodles to Crispy Rice Porridge</h2>
<p class="lead">After the chicken is enjoyed, the concentrated broth becomes the base for two iconic finishes: fresh knife-cut noodles (kalguksu) and our signature Nurungji porridge.</p>
<div style="border:1px solid rgba(199,84,29,.25);background:rgba(199,84,29,.05);padding:24px;border-radius:8px;margin-top:24px">
  <h3 class="h3" style="margin:0 0 16px;color:#c7541d">The Secret of Egg-Free Nurungji-Juk</h3>
  <p>Traditional cauldrons create golden scorched rice. When cooked in the reduced chicken broth with aromatic sesame oil until tender, it delivers a clean, richly nutty taste that pairs perfectly with fermented kimchi.</p>
</div>
</section>
"""
            },
            "zh": {
                "title": "韩国一只鸡的压轴美味：刀削面与百世特色'香脆锅巴粥'煮法秘诀",
                "seoTitle": "一只鸡泡饭·刀削面与百世特色锅巴粥 | 不加鸡蛋的纯粹原香",
                "description": "一只鸡的精髓所在！在浓缩鸡汤中煮入手工刀削面，随后放入传统香脆锅巴与纯正芝麻油，不加鸡蛋直接炖煮至软糯，搭配泡菜食用绝配。",
                "heroEyebrow": "THE ULTIMATE FINISH",
                "heroTitle": "一只鸡的压轴美味：<br>刀削面与百世特色'香脆锅巴粥'",
                "heroLead": "在凝聚鸡肉精华的浓缩鲜汤中品味手工面条，接着以无蛋锅巴粥画上完美句号！",
                "heroImageAlt": "一只鸡刀削面与锅巴粥",
                "tags": ["一只鸡泡饭", "锅巴粥", "刀削面", "百世食品"],
                "faq": [
                    {
                        "q": "为什么百世食品的锅巴粥不加鸡蛋？",
                        "a": "为了完整保留长时间熬煮而成的纯净鸡汤鲜香，以及传统铁锅锅巴纯粹的谷物焦香，百世食品坚决不加鸡蛋，确保汤底清澈不发腻。"
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / FINISHING COURSE</span>
<h2 class="h2">从劲道刀削面到养胃锅巴粥</h2>
<p class="lead">吃完鸡肉后，锅底浓缩的高汤正是最珍贵的精华。第一步煮入爽滑筋道的手工刀削面，第二步加入百世大麦饭的招牌特色——香脆锅巴粥。</p>
<div style="border:1px solid rgba(199,84,29,.25);background:rgba(199,84,29,.05);padding:24px;border-radius:8px;margin-top:24px">
  <h3 class="h3" style="margin:0 0 16px;color:#c7541d">不加鸡蛋的纯粹焦香法则</h3>
  <p>在浓缩鸡汤中加入传统焦香锅巴与香油，文火慢熬至软糯，配上酸爽开胃的白菜泡菜，是百世食品顾客必点的经典收尾美味。</p>
</div>
</section>
"""
            },
            "ru": {
                "title": "Кульминация Дакханмари: Лапша Калгуксу и фирменная каша из хрустящего риса (Нурунджи)",
                "seoTitle": "Дакханмари каша и лапша Калгуксу | Фирменная каша Нурунджи без яиц",
                "description": "Финал корейского куриного супа Дакханмари! Как приготовить домашнюю лапшу и фирменную кашу из жареного риса нурунджи с кунжутным маслом без добавления яиц.",
                "heroEyebrow": "THE ULTIMATE FINISH",
                "heroTitle": "Кульминация Дакханмари:<br>Лапша и фирменная каша Нурунджи",
                "heroLead": "Упругая лапша в концентрированном курином бульоне, а затем нежная каша из нурунджи без яиц с чистым ореховым вкусом!",
                "heroImageAlt": "Лапша Калгуксу и каша Нурунджи",
                "tags": ["ДакханмариКаша", "Нурунджи", "Калгуксу", "BaekseFood"],
                "faq": [
                    {
                        "q": "Почему в кашу Нурунджи от Baekse Food не добавляют яйца?",
                        "a": "В отличие от обычных каш, мы не используем яйца, чтобы сохранить чистый, глубокий вкус куриного бульона и натуральный аромат традиционного поджаренного риса."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / FINISHING COURSE</span>
<h2 class="h2">Фирменная лапша и каша из риса Нурунджи</h2>
<p class="lead">После нежного куриного мяса оставшийся бульон становится основой для настоящих кулинарных шедевров.</p>
<div style="border:1px solid rgba(199,84,29,.25);background:rgba(199,84,29,.05);padding:24px;border-radius:8px;margin-top:24px">
  <h3 class="h3" style="margin:0 0 16px;color:#c7541d">Секрет чистого вкуса без яиц</h3>
  <p>Хрустящий рис нурунджи варится в оставшемся бульоне с кунжутным маслом до мягкости. В сочетании с кимчи это создает незабываемый гармоничный вкус.</p>
</div>
</section>
"""
            }
        }
    },

    # ----------------------------------------------------
    # POST 3: central-kitchen-system
    # ----------------------------------------------------
    {
        "slug": "central-kitchen-system",
        "image": "/img/bs-sys-ck.webp",
        "translations": {
            "ko": {
                "title": "센트럴 키친(CK)이란 무엇인가? 요식업 주방 인건비를 획기적으로 줄이는 외식업 원팩 시스템",
                "seoTitle": "센트럴 키친(central kitchen)이란? 외식업 원팩 시스템과 인건비 절감",
                "description": "외식업계의 대세인 센트럴 키친(Central Kitchen, CK)의 개념과 작동 원리, 매장 조리시간 10분 단축 및 인건비 80% 절감 효과를 백세푸드 원팩 직배송 시스템으로 분석합니다.",
                "heroEyebrow": "F&B INNOVATION",
                "heroTitle": "센트럴 키친(CK)이란 무엇인가?<br>요식업 인건비 혁신과 원팩 시스템",
                "heroLead": "주방장 없는 식당의 비밀! 본사 중앙 조리시설에서 완성되는 원팩 시스템이 외식업 가맹점의 생존율을 3배 높이는 이유를 공개합니다.",
                "heroImageAlt": "백세푸드 센트럴키친 자동화 시설",
                "tags": ["센트럴키친", "centralkitchen", "센트럴키친이란", "원팩시스템", "식당창업"],
                "faq": [
                    {
                        "q": "센트럴 키친(Central Kitchen, CK)이란 구체적으로 무엇인가요?",
                        "a": "센트럴 키친은 여러 외식 매장에 공급할 식자재를 본사의 대규모 전문 위생 조리 시설에서 집중 전처리·조리·가공·포장하는 '중앙 공급식 주방'입니다. 각 매장에서 일일이 육수를 끓이고 고기를 손질할 필요 없이, 표준화된 원팩 완제품 상태로 직배송받아 바로 조리할 수 있습니다."
                    },
                    {
                        "q": "외식 매장에서 센트럴 키친 원팩 시스템을 도입하면 어떤 이점이 있나요?",
                        "a": "첫째, 비싼 인건비의 전문 조리사(주방장)가 필요 없어 인건비가 최대 70~80% 절감됩니다. 둘째, 개별 점포의 조리 숙련도와 무관하게 365일 균일한 맛 품질이 유지됩니다. 셋째, 식자재 손질 과정의 음식물 쓰레기와 로스(Loss)율이 0%에 수렴하여 원가율이 대폭 개선됩니다."
                    },
                    {
                        "q": "백세푸드의 센트럴 키친 물류 시스템은 어떻게 운영되나요?",
                        "a": "백세푸드는 35년 비법의 닭한마리 4단 추출 육수와 보리밥 비빔장, 포차 안주류를 본사 CK에서 정밀 가공하여 진공 급속 포장 원팩으로 가맹점에 직배송합니다. 점주는 팩을 뜯어 냄비에 붓고 끓이기만 하면 10분 만에 전문점 수준의 요리를 완성할 수 있습니다."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / CONCEPT DEFINITION</span>
<h2 class="h2">센트럴 키친(Central Kitchen)이란?<br>외식업의 패러다임을 바꾼 중앙 조리 시스템</h2>
<p class="lead"><strong>센트럴 키친(Central Kitchen, CK)</strong>이란 여러 매장이나 프랜차이즈 가맹점에 공급할 음식을 한곳의 첨단 위생 시설에서 대량으로 일괄 조리·가공하여 반제품 또는 완제품 형태로 공급하는 '중앙 집중식 조리 주방'을 뜻합니다.</p>

<p>과거의 식당들은 매일 아침 주방장이 출근하여 몇 시간 동안 채소를 다듬고, 닭 뼈를 고아 육수를 내며, 계량 없이 양념장을 배합했습니다. 하지만 치솟는 인건비, 인력난, 그리고 주방장의 퇴사로 인한 맛의 변질 문제는 식당 폐업의 가장 큰 원인이 되었습니다. 센트럴 키친은 이러한 구조적 문제를 근본적으로 해결하는 현대 외식업의 핵심 인프라입니다.</p>
</section>

<section>
<span class="eyebrow">02 / CORE ADVANTAGES</span>
<h2 class="h2">가맹점주가 체감하는<br>센트럴 키친 원팩 시스템의 4대 혁신</h2>

<div class="grid grid-2" style="margin-top:28px">
  <div class="card"><div class="body">
    <span class="tag">BENEFIT 01</span>
    <h3 class="h3">고액 주방장 없는 1인 운영 (인건비 80% 절감)</h3>
    <p>본사에서 완벽히 조리된 원팩을 뜯어 냄비에 붓고 끓이기만 하면 끝납니다. 전문 조리 기술이 전혀 없는 초보 점주나 파트타임 아르바이트생도 10분 만에 최고급 맛을 재현합니다.</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">BENEFIT 02</span>
    <h3 class="h3">전국 어느 매장이나 100% 동일한 맛 유지</h3>
    <p>주방장의 컨디션이나 날씨에 따라 맛이 변하던 주먹구구식 운영이 사라집니다. 본사 CK의 엄격한 온도·염도·당도 제어로 365일 균일한 감칠맛을 고객에게 제공합니다.</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">BENEFIT 03</span>
    <h3 class="h3">식자재 로스(Loss)율 0%와 원가 혁신</h3>
    <p>매장에서 재료를 다듬다 버려지는 자투리 채소나 유통기한 임박 식자재 폐기가 발생하지 않습니다. 딱 필요한 정량만큼 원팩으로 공급되어 원가율을 극도로 낮춥니다.</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">BENEFIT 04</span>
    <h3 class="h3">주방 면적 최소화, 홀 매출 극대화</h3>
    <p>거대한 육수 솥과 복잡한 전처리 작업대가 필요 없습니다. 주방 면적을 1~2평 수준으로 압축하고, 그만큼 홀 테이블을 늘려 회전율과 총매출을 비약적으로 끌어올립니다.</p>
  </div></div>
</div>
</section>

<section>
<span class="eyebrow">03 / BAEKSE FOOD CK</span>
<h2 class="h2">백세푸드 센트럴키친 시스템만의 경쟁력</h2>
<p class="lead">백세푸드는 35년 외식업 가문의 손맛과 첨단 CK 제조 공정을 완벽히 결합했습니다.</p>
<ul style="line-height:1.9;color:var(--text);margin-top:16px">
  <li><strong>4단계 농축 닭한마리 육수 원팩:</strong> 4번에 걸쳐 끓여낸 잡내 제로의 황금빛 진국 육수를 급속 냉각 포장 공급.</li>
  <li><strong>보리밥 산채 12종 나물 & 특제 비빔장:</strong> 사계절 신선도를 유지하는 스마트 패키징 공급.</li>
  <li><strong>원팩 시스템 기반 3in1 매장 운영:</strong> 한 주방에서 점심(보리밥), 저녁(닭한마리), 심야(포차)를 혼자서도 너끈히 소화하는 복합 매출 모델.</li>
</ul>

<div style="border:1px solid rgba(199,84,29,.35);background:linear-gradient(120deg,rgba(199,84,29,.14),rgba(245,241,232,.03));padding:clamp(26px,4vw,40px);margin-top:36px;display:flex;flex-direction:column;gap:16px">
  <h3 class="h3" style="margin:0">주방 스트레스 없는 성공 창업, 백세푸드 원팩 시스템과 함께하세요</h3>
  <p style="margin:0;color:var(--muted);line-height:1.8">
    <strong>본사 주소:</strong> 경기도 안산시 상록구 석호로 101, 1층<br>
    <strong>가맹 및 소스 공급 상담:</strong> 031-407-0103 (인테리어 마진 0원, 거품 없는 실속 창업)
  </p>
</div>
</section>
"""
            },
            "ja": {
                "title": "セントラルキッチン（central kitchen）とは？飲食店の省人化と味の均一化を実現するワンパック調理システムの秘密",
                "seoTitle": "セントラルキッチン とは | 飲食店の省人化・人件費削減とワンパックシステム",
                "description": "外食業界のキーワード「セントラルキッチン（central kitchen）とは？」その仕組みとメリットを徹底解説。仕込み時間ゼロ、人件費80%削減を可能にする百世フードのワンパック物流システム。",
                "heroEyebrow": "F&B INNOVATION",
                "heroTitle": "セントラルキッチン（CK）とは？<br>飲食店の省人化とワンパック革命",
                "heroLead": "料理人いらずで繁盛店を作る！本部セントラルキッチンで一元調理されたワンパックが、飲食店の生存率を飛躍的に高める理由。",
                "heroImageAlt": "百世フード セントラルキッチン製造施設",
                "tags": ["セントラルキッチン", "セントラルキッチンとは", "centralkitchen", "飲食店開業", "省人化"],
                "faq": [
                    {
                        "q": "セントラルキッチン（Central Kitchen, CK）とは何ですか？",
                        "a": "セントラルキッチンとは、複数の店舗で提供する料理の仕込み・加熱調理・加工・包装を、本部の衛生管理された専門工場で一括集中して行う「集中調理施設」のことです。各店舗での仕込み作業が不要になり、届いた食材を温めて盛り付けるだけで最高品質の料理を提供できます。"
                    },
                    {
                        "q": "飲食店がワンパックシステムを導入するメリットは？",
                        "a": "高給な専門料理人が不要になり人件費を大幅に削減できる点、どの店舗でもブレのない均一な味を提供できる点、そして仕込みによる食材ロスやゴミがゼロになる点が最大の強みです。"
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / CONCEPT DEFINITION</span>
<h2 class="h2">セントラルキッチン（Central Kitchen）とは？<br>外食産業を劇的に変える集中調理システム</h2>
<p class="lead"><strong>セントラルキッチン（Central Kitchen / CK）</strong>とは、複数の外食店舗やフランチャイズ店で使用する食材を一箇所の大規模な衛生施設でまとめて下処理・調理・加工・パッケージングし、各店へ配送する「中央調理施設」のことです。</p>

<p>従来の飲食店では、毎朝料理長が出勤し、何時間もかけて鶏ガラを煮込み、野菜を刻み、独自の勘で調味していました。しかし、人件費の高騰、深刻な人手不足、そして料理人の退職による味の劣化は、飲食店の経営を揺るがす最大の原因となっています。セントラルキッチンは、これらすべての課題を一気に解決する現代外食ビジネスの必須インフラです。</p>
</section>

<section>
<span class="eyebrow">02 / CORE ADVANTAGES</span>
<h2 class="h2">店舗オーナーが実感する<br>セントラルキッチン・ワンパックの4大メリット</h2>

<div class="grid grid-2" style="margin-top:28px">
  <div class="card"><div class="body">
    <span class="tag">BENEFIT 01</span>
    <h3 class="h3">専任シェフ不要！人件費を最大80%削減</h3>
    <p>本部から届いたワンパックを開封して鍋に注ぎ、火にかけるだけ。未経験のアルバイトでも10分でプロの味を完璧に再現できます。</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">BENEFIT 02</span>
    <h3 class="h3">全店舗でブレのない100%均一な美味しさ</h3>
    <p>料理人の体調や経験による味のブレを完全に排除。温度・塩分・糖度を徹底管理された製品が届くため、常に最高の満足度をお客様に提供します。</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">BENEFIT 03</span>
    <h3 class="h3">食材ロス率0%で原価管理を最適化</h3>
    <p>店舗での仕込みによる野菜クズや余分な廃棄が一切出ません。必要な分だけをパック単位で使用できるため、無駄なコストを徹底排除します。</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">BENEFIT 04</span>
    <h3 class="h3">厨房面積を最小化し客席稼働率アップ</h3>
    <p>巨大なスープ寸胴や仕込み台が不要に。厨房スペースを極小化し客席を増やすことで、坪あたりの売上効率を劇的に向上させます。</p>
  </div></div>
</div>
</section>
"""
            },
            "en": {
                "title": "What is a Central Kitchen? Revolutionizing Restaurant Labor Costs with One-Pack Systems",
                "seoTitle": "What is a Central Kitchen? F&B One-Pack System | Baekse Food",
                "description": "Understand what a central kitchen (CK) is and how it saves up to 80% of kitchen labor costs through standardized one-pack logistics and effortless 10-minute cooking.",
                "heroEyebrow": "F&B INNOVATION",
                "heroTitle": "What is a Central Kitchen?<br>Labor Cost Optimization & One-Pack Systems",
                "heroLead": "No expensive chefs needed. Discover how centralized cooking infrastructure powers high-profit restaurant operations.",
                "heroImageAlt": "Central kitchen automation system",
                "tags": ["CentralKitchen", "OnePackSystem", "RestaurantFranchise", "BaekseFood"],
                "faq": [
                    {
                        "q": "What is a Central Kitchen (CK)?",
                        "a": "A central kitchen is a centralized food processing and cooking facility that supplies standardized, ready-to-cook packages to multiple retail restaurant outlets."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / CONCEPT DEFINITION</span>
<h2 class="h2">The Definition and Power of a Central Kitchen</h2>
<p class="lead">In an era of soaring minimum wages and labor shortages, relying on traditional skilled kitchen chefs is the leading cause of restaurant closures. Central Kitchens eliminate in-store prep work by delivering ready-to-heat packaged broths and pre-portioned ingredients directly to the kitchen.</p>
</section>
"""
            },
            "zh": {
                "title": "什么是中央厨房(Central Kitchen)？大幅削减餐饮厨房人工成本的一包料标准化系统",
                "seoTitle": "什么是中央厨房(CK)？餐饮标准化与人工成本控制 | 百世食品",
                "description": "深入解析中央厨房（Central Kitchen）的核心概念与运作原理，如何通过百世食品一包料中央配送体系，实现无厨师10分钟出餐，人工成本节约80%。",
                "heroEyebrow": "F&B INNOVATION",
                "heroTitle": "什么是中央厨房(CK)？<br>餐饮人工革命与一包料标准化",
                "heroLead": "告别高薪大厨依赖！百世食品总店中央厨房标准化加工体系，助力加盟店实现高利润轻运营。",
                "heroImageAlt": "中央厨房自动化设备",
                "tags": ["中央厨房", "centralkitchen", "餐饮标准化", "百世食品"],
                "faq": [
                    {
                        "q": "什么是中央厨房（Central Kitchen）？",
                        "a": "中央厨房是指由总部设立的集中采购、集中加工、统一配送的专业化食品生产中心。加盟店只需拆包加热出餐，无需复杂的后厨切配与熬汤工序。"
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / CONCEPT DEFINITION</span>
<h2 class="h2">中央厨房（Central Kitchen）的定义与价值</h2>
<p class="lead">在高房租、高人工的时代，传统餐厅对大厨经验的过度依赖是导致关店率居高不下的主要原因。中央厨房通过工业化、标准化的统一生产，彻底颠覆了传统餐饮模式。</p>
</section>
"""
            },
            "ru": {
                "title": "Что такое Центральная кухня (Central Kitchen)? Оптимизация затрат на персонал с системой One-Pack",
                "seoTitle": "Что такое Central Kitchen? Стандартизация ресторана | Baekse Food",
                "description": "Разбираем концепцию Центральной кухни (Central Kitchen): как заготовки One-Pack экономят до 80% затрат на персонал и обеспечивают стабильное качество блюд.",
                "heroEyebrow": "F&B INNOVATION",
                "heroTitle": "Что такое Центральная кухня?<br>Оптимизация расходов и система One-Pack",
                "heroLead": "Ресторан без дорогих шеф-поваров! Как централизованное производство готовых соусов и бульонов поднимает рентабельность бизнеса.",
                "heroImageAlt": "Центральная кухня и система заготовок",
                "tags": ["CentralKitchen", "РесторанныйБизнес", "Франшиза", "BaekseFood"],
                "faq": [
                    {
                        "q": "Что такое Центральная кухня (Central Kitchen)?",
                        "a": "Это централизованный производственный цех, где готовятся и фасуются соусы, бульоны и полуфабрикаты для доставки во все заведения сети."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / CONCEPT DEFINITION</span>
<h2 class="h2">Принцип работы Центральной кухни</h2>
<p class="lead">Центральная кухня берет на себя самую трудоемкую работу: многочасовую варку бульонов, подготовку соусов и нарезку ингредиентов, поставляя их в рестораны в готовом виде.</p>
</section>
"""
            }
        }
    },

    # ----------------------------------------------------
    # POST 4: dakgomtang-samgyetang-difference
    # ----------------------------------------------------
    {
        "slug": "dakgomtang-samgyetang-difference",
        "image": "/img/bs-menu-1.webp",
        "translations": {
            "ko": {
                "title": "닭곰탕과 삼계탕의 차이는? 닭한마리까지 한국 3대 닭요리 완벽 비교",
                "seoTitle": "닭곰탕 삼계탕 차이점 & 닭한마리 비교 | 한국 대표 보양 닭요리 총정리",
                "description": "닭곰탕과 삼계탕의 재료·조리법·육수의 결정적 차이점을 비교 분석하고, 테이블에서 즉석으로 끓여먹는 닭한마리만의 독보적 매력과 35년 백세푸드의 스토리를 소개합니다.",
                "heroEyebrow": "KOREAN CHICKEN COMPARISON",
                "heroTitle": "닭곰탕과 삼계탕의 차이는?<br>닭한마리까지 3대 닭요리 비교",
                "heroLead": "인삼과 찹쌀의 보양식 삼계탕, 맑고 담백한 국밥 닭곰탕, 그리고 여럿이 둘러앉아 코스로 즐기는 닭한마리의 모든 것!",
                "heroImageAlt": "한국 대표 닭요리 삼계탕과 닭한마리 비교",
                "tags": ["닭곰탕삼계탕차이", "닭한마리삼계탕차이", "한국닭요리", "백세푸드"],
                "faq": [
                    {
                        "q": "닭곰탕과 삼계탕의 가장 결정적인 차이는 무엇인가요?",
                        "a": "삼계탕은 어린 영계 뱃속에 찹쌀, 인삼, 대추, 마늘을 채워 넣고 뚝배기에 1인분씩 진하게 끓여내는 전통 '약선 보양식'입니다. 반면 닭곰탕은 큰 닭을 삶아 살코기를 결대로 찢고, 맑게 우려낸 육수에 밥을 말아먹는 일상적인 '맑은 고기 국밥'입니다."
                    },
                    {
                        "q": "닭한마리는 삼계탕이나 닭곰탕과 어떻게 다른가요?",
                        "a": "삼계탕과 닭곰탕이 조리 완료된 뚝배기/그릇으로 서빙되는 개인 식사라면, 닭한마리는 테이블 위 전골냄비에서 큰 닭을 토막 내어 즉석에서 끓여가며 먹는 '외식 전골 요리'입니다. 특제 다대기 소스, 떡·감자 사리, 칼국수, 그리고 누룽지죽까지 코스 요리처럼 즐기는 것이 독보적인 차별점입니다."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / 3-WAY COMPARISON</span>
<h2 class="h2">한눈에 정리하는<br>한국 3대 닭요리 핵심 비교표</h2>
<p class="lead">한국인뿐만 아니라 전 세계 미식가들이 가장 사랑하는 대표 닭요리 3가지—삼계탕, 닭곰탕, 닭한마리는 닭을 주재료로 한다는 공통점이 있지만 조리 방식과 식문화는 완전히 다릅니다.</p>

<div style="overflow-x:auto;margin-top:24px">
  <table style="width:100%;border-collapse:collapse;text-align:left;line-height:1.8">
    <thead>
      <tr style="border-bottom:2px solid var(--border);color:var(--text)">
        <th style="padding:12px">구분</th>
        <th style="padding:12px">삼계탕 (Samgyetang)</th>
        <th style="padding:12px">닭곰탕 (Dakgomtang)</th>
        <th style="padding:12px;color:#c7541d">닭한마리 (Dakhanmari)</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom:1px solid var(--border)">
        <td style="padding:12px;font-weight:bold">주요 형태</td>
        <td style="padding:12px">뚝배기 1인분 영양 보양식</td>
        <td style="padding:12px">그릇에 담아내는 맑은 국밥</td>
        <td style="padding:12px;font-weight:bold;color:#c7541d">테이블 즉석 조리 대형 전골</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border)">
        <td style="padding:12px;font-weight:bold">닭 크기/손질</td>
        <td style="padding:12px">어린 영계 (속에 찹쌀·인삼)</td>
        <td style="padding:12px">큰 닭 (삶아서 살을 찢음)</td>
        <td style="padding:12px;font-weight:bold;color:#c7541d">육질 좋은 중대닭 토막</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border)">
        <td style="padding:12px;font-weight:bold">국물/육수</td>
        <td style="padding:12px">인삼·약재 향이 진한 국물</td>
        <td style="padding:12px">기름기 걷어낸 깔끔한 맑은 탕</td>
        <td style="padding:12px;font-weight:bold;color:#c7541d">깊고 맑은 황금빛 농축 육수</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border)">
        <td style="padding:12px;font-weight:bold">즐기는 방식</td>
        <td style="padding:12px">소금에 살 찍어먹고 찹쌀밥</td>
        <td style="padding:12px">밥을 말아 깍두기와 취식</td>
        <td style="padding:12px;font-weight:bold;color:#c7541d">고기+특제소스 → 칼국수 → 누룽지죽</td>
      </tr>
    </tbody>
  </table>
</div>
</section>

<section>
<span class="eyebrow">02 / HISTORY & PHILOSOPHY</span>
<h2 class="h2">삼계탕 전문점에서 닭한마리로 진화한<br>백세푸드 35년의 철학</h2>
<p class="lead">백세푸드의 시작은 본래 35년 전 정통 삼계탕 전문점이었습니다. 매일 신선한 인삼과 약재를 달여내던 손맛에서 출발했습니다.</p>
<p>하지만 삼계탕은 '복날에 혼자 보양하는 음식'이라는 한계가 있었습니다. 가족, 동료, 친구들이 한 냄비에 둘러앉아 도란도란 이야기를 나누며, 맑은 육수에서 닭고기를 건져 먹고 칼국수와 구수한 누룽지죽까지 푸짐하게 즐길 수 있는 최고의 외식 문화를 만들고자 완성해 낸 요리가 바로 <strong>'백세 닭한마리'</strong>입니다.</p>
</section>
"""
            },
            "ja": {
                "title": "タッコムタンとサムゲタンの違いとは？タッカンマリまで知っておきたい韓国3大鶏料理の魅力",
                "seoTitle": "タッコムタン サムゲタン 違い・タッカンマリ比較 | 韓国3大鶏料理ガイド",
                "description": "韓国料理好き必見！「タッコムタンとサムゲタンの違いとは？」具材・スープ・食べ方の違いを徹底比較。さらに大人気タッカンマリとの決定的な差まで詳しく解説します。",
                "heroEyebrow": "KOREAN CHICKEN COMPARISON",
                "heroTitle": "タッコムタンとサムゲタンの違いとは？<br>タッカンマリまで3大鶏料理を徹底比較",
                "heroLead": "高麗人参ともち米の薬膳「サムゲタン」、澄んだクッパ「タッコムタン」、鍋を囲んで麺とおこげ雑炊まで楽しむ「タッカンマリ」のすべて！",
                "heroImageAlt": "タッコムタン・サムゲタン・タッカンマリの比較",
                "tags": ["タッコムタンサムゲタン違い", "サムゲタンタッカンマリ違い", "韓国鶏料理", "百世フード"],
                "faq": [
                    {
                        "q": "タッコムタンとサムゲタンの決定的な違いは何ですか？",
                        "a": "サムゲタン（参鶏湯）は、若鶏のお腹にもち米、高麗人参、ナツメを詰めて土鍋で濃厚に煮込んだ薬膳滋養強壮料理です。一方タッコムタン（鶏コムタン）は、丸鶏を煮て身をほぐし、澄んだスープにご飯を入れて食べる日常的なクリアスープクッパです。"
                    },
                    {
                        "q": "タッカンマリはそれらとどう違うのですか？",
                        "a": "サムゲタンやタッコムタンが調理済みで1人前ずつ提供される料理であるのに対し、タッカンマリ（鶏一羽鍋）は卓上コンロの大鍋で鶏肉を煮ながら、特製タテギ（辛味だれ）、トック、カルグクス、締めのおこげ雑炊までコース仕立てで大人数で楽しむ外食鍋料理です。"
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / 3-WAY COMPARISON</span>
<h2 class="h2">ひと目でわかる！<br>韓国3大鶏料理の徹底比較</h2>
<p class="lead">韓国旅行や外食で人気の3大鶏料理「サムゲタン」「タッコムタン」「タッカンマリ」。同じ鶏肉を主役としながらも、その調理法と楽しみ方は大きく異なります。</p>

<div style="overflow-x:auto;margin-top:24px">
  <table style="width:100%;border-collapse:collapse;text-align:left;line-height:1.8">
    <thead>
      <tr style="border-bottom:2px solid var(--border);color:var(--text)">
        <th style="padding:12px">料理名</th>
        <th style="padding:12px">サムゲタン（参鶏湯）</th>
        <th style="padding:12px">タッコムタン（鶏コムタン）</th>
        <th style="padding:12px;color:#c7541d">タッカンマリ（鶏一羽鍋）</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom:1px solid var(--border)">
        <td style="padding:12px;font-weight:bold">スタイル</td>
        <td style="padding:12px">1人前土鍋の薬膳滋養食</td>
        <td style="padding:12px">1人前の澄んだ鶏クッパ</td>
        <td style="padding:12px;font-weight:bold;color:#c7541d">卓上鍋を囲むコース外食</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border)">
        <td style="padding:12px;font-weight:bold">鶏の特徴</td>
        <td style="padding:12px">若鶏（腹にもち米・人参）</td>
        <td style="padding:12px">ほぐした鶏肉がスープイン</td>
        <td style="padding:12px;font-weight:bold;color:#c7541d">ぶつ切りの大ぶりジューシー鶏</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border)">
        <td style="padding:12px;font-weight:bold">スープ</td>
        <td style="padding:12px">人参や韓方の香る白濁出汁</td>
        <td style="padding:12px">脂を取り除いた透明な出汁</td>
        <td style="padding:12px;font-weight:bold;color:#c7541d">黄金色に澄んだ極上濃厚出汁</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border)">
        <td style="padding:12px;font-weight:bold">締め・食べ方</td>
        <td style="padding:12px">塩をつけて身を食べ粥へ</td>
        <td style="padding:12px">カクテキと一緒に飯を食す</td>
        <td style="padding:12px;font-weight:bold;color:#c7541d">特製タテギだれ → 麺 → ヌルンジ雑炊</td>
      </tr>
    </tbody>
  </table>
</div>
</section>
"""
            },
            "en": {
                "title": "Difference Between Dakgomtang and Samgyetang: Comparing Korea's Top 3 Chicken Dishes",
                "seoTitle": "Dakgomtang vs Samgyetang vs Dakhanmari | Korean Chicken Guide",
                "description": "Understand the culinary differences between Samgyetang (ginseng chicken soup), Dakgomtang (clear chicken soup with rice), and Dakhanmari (tabletop chicken hot pot).",
                "heroEyebrow": "KOREAN CHICKEN COMPARISON",
                "heroTitle": "Dakgomtang vs Samgyetang:<br>Comparing Korea's Top 3 Chicken Dishes",
                "heroLead": "From nourishing herbal Samgyetang to everyday clear soup Dakgomtang, and the ultimate social feast of Dakhanmari.",
                "heroImageAlt": "Korean chicken soups comparison",
                "tags": ["Dakgomtang", "Samgyetang", "Dakhanmari", "KoreanFoodGuide"],
                "faq": [
                    {
                        "q": "What is the key difference between Dakgomtang and Samgyetang?",
                        "a": "Samgyetang features a young whole chicken stuffed with sweet rice, ginseng, and dates, cooked in individual earthen pots. Dakgomtang consists of shredded chicken in a clear, soothing broth poured over rice."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / COMPARISON</span>
<h2 class="h2">The Three Pillars of Korean Chicken Soups</h2>
<p class="lead">While all three highlight chicken, their cooking methods, broth profiles, and dining rituals offer completely different experiences.</p>
</section>
"""
            },
            "zh": {
                "title": "鸡白汤(Dakgomtang)与参鸡汤的区别是什么？韩国3大经典鸡肉料理全景解析",
                "seoTitle": "鸡白汤与参鸡汤的区别 · 一只鸡对比 | 韩国三大鸡汤全解析",
                "description": "全面对比参鸡汤、鸡白汤泡饭与一只鸡的用料、汤底及吃法差异，感受从滋补参鸡汤到围炉共享一只鸡的韩国饮食魅力。",
                "heroEyebrow": "KOREAN CHICKEN COMPARISON",
                "heroTitle": "鸡白汤与参鸡汤的区别？<br>韩国3大经典鸡肉料理全景解析",
                "heroLead": "药膳滋补参鸡汤、清润鸡白汤泡饭、再到围炉共享的一只鸡火锅！",
                "heroImageAlt": "韩国三大鸡汤对比",
                "tags": ["鸡白汤与参鸡汤区别", "参鸡汤", "一只鸡", "百世食品"],
                "faq": [
                    {
                        "q": "鸡白汤（Dakgomtang）与参鸡汤有什么区别？",
                        "a": "参鸡汤在童子鸡腹内填入糯米、人参、红枣等药膳慢炖；鸡白汤则是将大鸡煮熟后手撕鸡肉，放入清澈高汤中泡饭食用。"
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / COMPARISON</span>
<h2 class="h2">韩国三大鸡汤料理对比</h2>
<p class="lead">虽然都以鸡肉为核心，但参鸡汤偏重药膳补身，鸡白汤偏重日常简餐，而一只鸡则是大家围炉欢聚、边煮边吃的殿堂级火锅。</p>
</section>
"""
            },
            "ru": {
                "title": "В чем разница между Дакгомтан и Самгетан? Полное сравнение 3 главных корейских блюд из курицы",
                "seoTitle": "Разница между Дакгомтан и Самгетан | Корейские куриные супы",
                "description": "Разбираем отличия Самгетан (суп с женьшенем), Дакгомтан (прозрачный куриный суп) и Дакханмари (куриный суп-хотпот на всю компанию).",
                "heroEyebrow": "KOREAN CHICKEN COMPARISON",
                "heroTitle": "В чем разница между Дакгомтан и Самгетан?<br>Сравнение 3 главных блюд из курицы",
                "heroLead": "Лечебный Самгетан с женьшенем, легкий суп Дакгомтан с рисом и легендарный банкетный Дакханмари!",
                "heroImageAlt": "Сравнение корейских куриных супов",
                "tags": ["Дакгомтан", "Самгетан", "Дакханмари", "КорейскаяКухня"],
                "faq": [
                    {
                        "q": "В чем основное отличие Дакгомтан от Самгетан?",
                        "a": "Самгетан — это цыпленок, фаршированный рисом и женьшенем. Дакгомтан — это суп с кусочками отварного куриного мяса и рисом в прозрачном бульоне."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / COMPARISON</span>
<h2 class="h2">Три столпа корейских куриных блюд</h2>
<p class="lead">Самгетан согревает тело лекарственными травами, Дакгомтан дарит ежедневный комфорт, а Дакханмари объединяет близких за одним большим столом.</p>
</section>
"""
            }
        }
    },

    # ----------------------------------------------------
    # POST 5: dakhanmari-secret-broth
    # ----------------------------------------------------
    {
        "slug": "dakhanmari-secret-broth",
        "image": "/img/bs-sys-logistics.webp",
        "translations": {
            "ko": {
                "title": "닭 비린내 없이 맑고 진한 닭한마리 육수의 비밀 (4번 끓인 비법 육수 노하우)",
                "seoTitle": "닭한마리 육수의 비밀 | 잡내 없이 맑고 깊은 4단 추출 레시피",
                "description": "닭 비린내와 잡내를 완벽히 잡고 맑으면서도 깊은 감칠맛을 내는 백세푸드 35년 전통 4번 끓인 닭한마리 비법 육수의 제조 원리와 비결을 공개합니다.",
                "heroEyebrow": "SECRET BROTH RECIPE",
                "heroTitle": "닭 비린내 없이 맑고 진한<br>닭한마리 육수의 비밀",
                "heroLead": "왜 집에서 끓이면 닭 냄새가 나고 국물이 탁해질까? 35년 외식 가문이 지켜온 4번 끓인 황금빛 비법 육수 노하우를 전수합니다.",
                "heroImageAlt": "4번 끓여낸 맑고 깊은 백세푸드 닭 육수",
                "tags": ["닭한마리육수", "닭육수만들기", "닭잡내제거", "백세푸드"],
                "faq": [
                    {
                        "q": "닭 육수를 끓일 때 국물이 탁해지고 비린내가 나는 이유는 무엇인가요?",
                        "a": "닭 뼈 속 잔여 핏물과 내장 불순물을 제대로 제거하지 않고 바로 끓이거나, 초벌 데치기 과정 없이 센 불에서 계속 끓여 기름과 단백질 찌꺼기가 육수에 유화(Emulsion)되기 때문입니다."
                    },
                    {
                        "q": "백세푸드의 '4번 끓인 육수'는 어떤 과정으로 만들어지나요?",
                        "a": "1단계 냉수 핏물 제거, 2단계 끓는 물 급속 데치기로 잡내 원인 완벽 차단, 3단계 신선 채소와 비법 한약재의 최적 배합 추출, 4단계 미세 지방 정제 및 저온 숙성을 거쳐 맑고도 깊은 감칠맛의 황금 육수가 완성됩니다."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / COMMON MISTAKES</span>
<h2 class="h2">닭 육수 끓일 때<br>가장 많이 범하는 3가지 실수</h2>
<p class="lead">닭한마리의 영혼은 국물입니다. 하지만 많은 이들이 육수를 우릴 때 다음과 같은 치명적인 실수를 저지릅니다.</p>

<div class="grid grid-3" style="margin-top:28px">
  <div class="card"><div class="body">
    <span class="tag">ERROR 01</span>
    <h3 class="h3">초벌 데치기 생략</h3>
    <p>생닭을 그대로 냄비에 넣고 끓이면 뼈 속 핏물과 불순물이 국물에 녹아들어 잡내와 거품의 주원인이 됩니다.</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">ERROR 02</span>
    <h3 class="h3">무리한 강불 유지</h3>
    <p>센 불로만 계속 끓이면 닭기름과 육수가 섞여 국물이 뿌옇게 탁해지고 텁텁한 맛이 납니다.</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">ERROR 03</span>
    <h3 class="h3">과도한 조미료 의존</h3>
    <p>채소와 닭 뼈에서 우러나는 자연스러운 단맛과 감칠맛 대신 조미료를 과용하면 첫맛만 강하고 뒷맛이 텁텁해집니다.</p>
  </div></div>
</div>
</section>

<section>
<span class="eyebrow">02 / 4-STAGE EXTRACTION</span>
<h2 class="h2">백세푸드 35년 비법<br>4번 끓여내는 4단 추출 공정</h2>
<div style="border:1px solid rgba(199,84,29,.25);background:rgba(199,84,29,.05);padding:24px;border-radius:8px;margin-top:24px">
  <h3 class="h3" style="margin:0 0 16px;color:#c7541d">황금빛 진국 육수를 완성하는 4단계</h3>
  <ol style="line-height:2;margin:0;padding-left:20px">
    <li><strong>1단계 (핏물 세척):</strong> 닭 뼈 사이사이의 잔여 핏물을 찬물에서 완벽히 침출 분리.</li>
    <li><strong>2단계 (순간 초벌 데치기):</strong> 끓는 물에 살짝 튀기듯 데쳐내어 표면 단백질 응고 및 잔여 잡내 원천 차단.</li>
    <li><strong>3단계 (신선 채수 & 비법 약재 추출):</strong> 대파 뿌리, 무, 양파, 통마늘과 황기 등 엄선된 약재를 황금 비율로 은근히 우려냄.</li>
    <li><strong>4단계 (유화 방지 정제 및 저온 숙성):</strong> 맑은 상층 기름을 걷어내고 저온 숙성하여 맑고도 깊은 감칠맛 확립.</li>
  </ol>
</div>
</section>

<section>
<span class="eyebrow">03 / READY TO DELIVER</span>
<h2 class="h2">가맹점에는 완벽한 원팩으로 공급</h2>
<p class="lead">이 복잡하고 정성스러운 4단 육수 추출 공정을 매장에서 매일 할 필요가 없습니다. 백세푸드 본사 센트럴키친에서 완벽한 상태로 원팩 포장 공급하므로, 가맹점은 불만 켜면 전국 어디서나 최고의 맛을 제공합니다.</p>
</section>
"""
            },
            "ja": {
                "title": "臭みゼロで澄んだ深み！タッカンマリ秘伝の極上スープ（出汁）の作り方と4段抽出の秘密",
                "seoTitle": "タッカンマリ スープ・出汁の秘密 | 臭みのない澄んだスープの作り方",
                "description": "鶏特有の生臭さを完全に消し、澄み切った黄金色と濃厚なコクを両立させる百世フード35年伝統「4度煮込み秘伝タッカンマリスープ」の全貌を公開。",
                "heroEyebrow": "SECRET BROTH RECIPE",
                "heroTitle": "臭みゼロで澄んだ深み！<br>タッカンマリ秘伝スープの秘密",
                "heroLead": "なぜ家庭で作ると濁り、臭みが出るのか？35年の外食名門が受け継いできた4段抽出黄金スープのノウハウを伝授。",
                "heroImageAlt": "澄み切った黄金色のタッカンマリ極上スープ",
                "tags": ["タッカンマリスープ", "鶏出汁レシピ", "タッカンマリ作り方", "百世フード"],
                "faq": [
                    {
                        "q": "鶏スープが白濁したり臭みが出る原因は？",
                        "a": "骨の中の血合いや内臓の残渣を処理せずに煮込んだり、下茹で（湯こぼし）をせずに強火で煮立てて脂とタンパク質が乳化してしまうことが原因です。"
                    },
                    {
                        "q": "百世フードのスープはどうやって作られていますか？",
                        "a": "冷水での血抜き、熱湯での瞬間下茹で、香味野菜と厳選韓方生薬による低温抽出、微細油脂の濾過と熟成の4段階を経て、澄み切った黄金出汁を完成させています。"
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / COMMON MISTAKES</span>
<h2 class="h2">鶏スープ作りで<br>初心者が陥りがちな3大失敗</h2>
<p class="lead">タッカンマリの命は「スープ（出汁）」です。しかし多くの方が下処理の基本を見落として失敗してしまいます。</p>
<div class="grid grid-3" style="margin-top:28px">
  <div class="card"><div class="body">
    <span class="tag">ERROR 01</span>
    <h3 class="h3">下茹での省略</h3>
    <p>生肉のまま煮込むと、骨の血合いやアクがスープ全体に溶け出し、生臭さの原因になります。</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">ERROR 02</span>
    <h3 class="h3">強火での過度な加熱</h3>
    <p>グラグラと沸騰させ続けると脂分が乳化し、澄んだ出汁ではなく濁った白湯になってしまいます。</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">ERROR 03</span>
    <h3 class="h3">過度な化学調味料</h3>
    <p>鶏と野菜本来の自然な甘みではなく調味料に頼ると、後味が悪く重たいスープになってしまいます。</p>
  </div></div>
</div>
</section>

<section>
<span class="eyebrow">02 / 4-STAGE EXTRACTION</span>
<h2 class="h2">百世フード直伝！4段抽出の黄金工程</h2>
<div style="border:1px solid rgba(199,84,29,.25);background:rgba(199,84,29,.05);padding:24px;border-radius:8px;margin-top:24px">
  <ol style="line-height:2;margin:0;padding-left:20px">
    <li><strong>第1段階（徹底した血抜き）：</strong> 冷水で骨周りの血や汚れを丁寧に洗い落とす。</li>
    <li><strong>第2段階（瞬間下茹で）：</strong> 熱湯にさっと潜らせて表面を固め、臭みのアクを完全遮断。</li>
    <li><strong>第3段階（香味野菜と薬膳抽出）：</strong> 長ネギの根、大根、玉ねぎ、ニンニクと生薬を絶妙な比率で煮出す。</li>
    <li><strong>第4段階（油脂分離と低温熟成）：</strong> 余分な油を丁寧に濾過し、澄んだ黄金スープを完成させる。</li>
  </ol>
</div>
</section>
"""
            },
            "en": {
                "title": "The Secret to Clear, Savory Dakhanmari Broth: Zero Gamy Odor, 4-Stage Extraction",
                "seoTitle": "Secret Dakhanmari Chicken Broth Recipe | Baekse Food",
                "description": "Learn the 35-year secrets of Baekse Food's crystal-clear golden chicken broth. How our 4-stage extraction process eliminates gamy smells completely.",
                "heroEyebrow": "SECRET BROTH RECIPE",
                "heroTitle": "Zero Odor, Crystal Clear:<br>The Secret of Dakhanmari Broth",
                "heroLead": "Discover the culinary science behind creating pure, comforting Korean chicken broth with rich umami.",
                "heroImageAlt": "Clear golden chicken broth",
                "tags": ["DakhanmariBroth", "ChickenSoupRecipe", "KoreanCulinarySecrets"],
                "faq": [
                    {
                        "q": "How do you achieve a crystal clear broth without chicken odor?",
                        "a": "Thoroughly rinse blood from the bone cavities, blanch briefly in boiling water, and simmer gently with aromatic root vegetables without boiling rapidly."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / THE SCIENCE OF BROTH</span>
<h2 class="h2">4-Stage Extraction Process</h2>
<p class="lead">By combining cold-water rinsing, rapid blanching, low-temperature simmering, and careful fat skimming, Baekse Food achieves unmatched broth clarity and deep umami.</p>
</section>
"""
            },
            "zh": {
                "title": "去腥增鲜、清澈醇厚的韩国一只鸡高汤秘方 (35年四重熬煮工艺)",
                "seoTitle": "一只鸡高汤秘方与熬制技巧 | 百世食品四重萃取工艺",
                "description": "揭秘百世食品35年传承的清亮金黄一只鸡鸡汤秘方，如何通过四重熬煮与控温工艺彻底去除鸡腥味，锁住极致浓鲜。",
                "heroEyebrow": "SECRET BROTH RECIPE",
                "heroTitle": "去腥增鲜、清澈醇厚：<br>一只鸡高汤的熬制秘方",
                "heroLead": "为什么自己熬汤容易浑浊有腥味？传授35年餐饮老店四重萃取黄金鸡汤的独家秘籍。",
                "heroImageAlt": "金黄澄澈的一只鸡高汤",
                "tags": ["一只鸡高汤", "去腥秘方", "鸡汤熬制", "百世食品"],
                "faq": [
                    {
                        "q": "如何熬出清澈无腥味的鸡高汤？",
                        "a": "关键在于提前清洗骨髓中的残血、沸水快速焯水去杂质，以及搭配大葱根、白萝卜等蔬菜小火慢炖，避免大火剧烈沸腾导致汤水浑浊。"
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / SECRET RECIPE</span>
<h2 class="h2">百世食品四重熬煮萃取工艺</h2>
<p class="lead">清洗残血、沸水焯烫、蔬菜与草本小火慢煨、低温油水分离四道严密工序，成就清亮金黄、鲜而不腻的极品高汤。</p>
</section>
"""
            },
            "ru": {
                "title": "Секрет прозрачного бульона для Дакханмари без запаха: 4 этапа варки от мастеров",
                "seoTitle": "Секрет идеального бульона для Дакханмари | Baekse Food",
                "description": "Узнайте секрет кристально чистого золотистого бульона Дакханмари от Baekse Food: как убрать специфический запах и добиться насыщенного вкуса умами.",
                "heroEyebrow": "SECRET BROTH RECIPE",
                "heroTitle": "Без запаха, прозрачный и наваристый:<br>Секрет бульона Дакханмари",
                "heroLead": "Как сварить идеальный куриный бульон золотистого цвета? Пошаговая технология от корейских мастеров с 35-летним стажем.",
                "heroImageAlt": "Прозрачный золотистый куриный бульон",
                "tags": ["БульонДляДакханмари", "КорейскийБульон", "КуриныйБульон"],
                "faq": [
                    {
                        "q": "Как сделать бульон прозрачным и без запаха?",
                        "a": "Обязательно промойте мясо от остатков крови, бланшируйте в кипятке 2 минуты и варите на медленном огне с овощами, снимая пену и жир."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / SECRET BROTH</span>
<h2 class="h2">Технология 4-ступенчатой варки</h2>
<p class="lead">Бланширование, медленное томление с кореньями и фильтрация позволяют получить кристально прозрачный бульон с непревзойденной глубиной вкуса.</p>
</section>
"""
            }
        }
    }
]

def format_frontmatter(t, image):
    tags_formatted = ", ".join(f'"{tag}"' for tag in t["tags"])
    faq_lines = []
    for item in t.get("faq", []):
        q_esc = item["q"].replace('"', '\\"')
        a_esc = item["a"].replace('"', '\\"')
        faq_lines.append(f'  - q: "{q_esc}"\n    a: "{a_esc}"')
    faq_block = "\n".join(faq_lines)

    cta_primary_label = {
        "ko": "무료 창업·전수 상담",
        "ja": "無料加盟・伝授相談",
        "en": "Free Consultation",
        "zh": "免费加盟咨询",
        "ru": "Бесплатная консультация"
    }

    cta_secondary_label = {
        "ko": "전화 문의",
        "ja": "お電話でのお問い合わせ",
        "en": "Call Us",
        "zh": "电话咨询",
        "ru": "Позвонить нам"
    }

    lang = t.get("lang", "ko")

    fm = f"""---
title: "{t['title']}"
seoTitle: "{t['seoTitle']}"
description: "{t['description']}"
heroEyebrow: "{t['heroEyebrow']}"
heroTitle: "{t['heroTitle']}"
heroLead: "{t['heroLead']}"
heroImage: "{image}"
heroImageAlt: "{t['heroImageAlt']}"
ctaPrimary:
  label: "{cta_primary_label.get(lang, '상담 신청')}"
  href: "#apply"
ctaSecondary:
  label: "{cta_secondary_label.get(lang, '전화 문의')}"
  href: "tel:031-407-0103"
interest: "닭한마리"
faq:
{faq_block}
tags: [{tags_formatted}]
---
"""
    return fm

def main():
    created_count = 0
    for post in POSTS:
        slug = post["slug"]
        image = post["image"]
        for lang, trans_data in post["translations"].items():
            trans_data["lang"] = lang
            filename = f"{slug}.md" if lang == "ko" else f"{slug}.{lang}.md"
            filepath = os.path.join(BLOG_DIR, filename)

            fm = format_frontmatter(trans_data, image)
            full_content = fm + trans_data["content"].strip() + "\n"

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(full_content)
            
            created_count += 1
            print(f"Created: {filename}")

    print(f"\nSuccessfully generated all {created_count} blog markdown files!")

if __name__ == "__main__":
    main()
