# -*- coding: utf-8 -*-
"""
Generate 3 Dak-Kalguksu blog posts in 5 languages (ko, en, ja, zh, ru) = 15 files
for baekse-food Hugo website:
1. dak-kalguksu-startup
2. dak-kalguksu-recipe-manual
3. dak-kalguksu-broth-supply
"""

import os

BLOG_DIR = r"c:\project\baekse-food\content\blog"

POSTS = [
    # ----------------------------------------------------
    # POST 1: dak-kalguksu-startup
    # ----------------------------------------------------
    {
        "slug": "dak-kalguksu-startup",
        "image": "/img/bs-menu-7.webp",
        "translations": {
            "ko": {
                "title": "기존 식당 매출을 올리는 가장 쉬운 방법, 닭칼국수 샵인샵 & 부메뉴 창업 전수",
                "seoTitle": "닭칼국수 창업 전수 | 식당 부메뉴·샵인샵 도입 가이드 | 백세푸드",
                "description": "별도 설비 없이 10배 농축 육수로 6분 만에 조리하는 닭칼국수 샵인샵 & 부메뉴 창업. 원가율 18~29%, 가맹비 0원, 1박스 소량 발주 및 사업자 무료 샘플 지원.",
                "heroEyebrow": "SHOP-IN-SHOP STARTUP",
                "heroTitle": "기존 식당 매출을 올리는 가장 쉬운 방법,<br>닭칼국수 샵인샵 & 부메뉴 창업 전수",
                "heroLead": "거창한 주방 설비나 육수 끓이는 번거로움 없이, 검증된 10배 농축 육수로 내 매장에 확실한 점심 효자 메뉴를 추가하세요.",
                "heroImageAlt": "닭칼국수 상차림과 샵인샵 조리",
                "tags": ["닭칼국수창업", "식당부메뉴", "샵인샵", "닭칼국수전수", "백세푸드"],
                "faq": [
                    {
                        "q": "현재 운영 중인 고깃집이나 분식집에 닭칼국수를 부메뉴로 바로 추가할 수 있나요?",
                        "a": "네, 가능합니다. 기존 주방 화구 1구와 냄비만 있으면 즉시 시작할 수 있습니다. 10배 농축 육수를 희석하여 주문 즉시 6분 만에 끓여내는 시스템이므로 별도의 대형 가마솥이나 전문 조리 인력이 전혀 필요하지 않습니다."
                    },
                    {
                        "q": "닭칼국수의 1인분 원가율과 마진율은 어떻게 되나요?",
                        "a": "시중 판매가 8,000원~12,000원 기준, 1:10 희석 육수와 칼국수 생면, 닭고기 고명, 신선 채소를 모두 포함한 1인분 총 원가는 2,100원~2,300원 수준으로 원가율 18%~29%를 달성합니다. 마진율 70% 이상의 초고수익 부메뉴입니다."
                    },
                    {
                        "q": "초기 도입 시 최소 주문 수량과 샘플 지원 조건은 무엇인가요?",
                        "a": "사업자등록증을 보유하신 외식업 대표님께는 실제 매장에서 맛과 농도를 테스트해보실 수 있도록 무료 테스트 샘플 키트를 지원해 드립니다. 정식 발주 시에도 1박스(1L × 6병) 소량부터 주문 가능하여 재고 부담이 없습니다."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / WHY DAK-KALGUKSU</span>
<h2 class="h2">식당 사장님들의 고민을 해결하는<br>가장 확실한 점심 효자 메뉴</h2>
<p class="lead">"점심 매출을 끌어올릴 든든한 식사 메뉴가 없을까?", "새로운 메뉴를 넣고 싶은데 주방 인력도 가스비도 걱정입니다." 많은 식당 사장님들이 마주하는 현실적인 문제입니다. 백세푸드가 제안하는 <strong>닭칼국수 샵인샵 & 부메뉴 창업</strong>은 별도의 설비 투자 없이 검증된 10배 농축 육수를 도입해 누구나 6분 만에 전문점 수준의 맛을 완성하는 고수익 솔루션입니다.</p>

<div class="grid grid-3" style="margin-top:28px">
  <div class="card"><div class="body">
    <span class="tag">POINT 01</span>
    <h3 class="h3">기존 화구 1구로 즉시 시작</h3>
    <p>대형 솥에서 하루 종일 육수를 우릴 필요가 없습니다. 일반 화구 하나와 냄비만 있으면 주문 즉시 조리 가능합니다.</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">POINT 02</span>
    <h3 class="h3">사계절 호불호 없는 대중성</h3>
    <p>남녀노소 누구나 좋아하는 맑고 깊은 닭 육수 기반으로, 여름 복날 보양식부터 겨울철 따뜻한 한 끼까지 365일 안정적인 매출을 보장합니다.</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">POINT 03</span>
    <h3 class="h3">1인분 원가율 18~29%</h3>
    <p>판매가 8,000~12,000원 기준 총 재료비 2,100~2,300원 수준으로, 매장 순이익률을 비약적으로 개선해 줍니다.</p>
  </div></div>
</div>
</section>

<section>
<span class="eyebrow">02 / PROFITABILITY ANALYSIS</span>
<h2 class="h2">투명한 원가 구조 및 마진율 분석</h2>
<p class="lead">고물가 시대에 식당의 생존은 철저한 원가 경쟁력에서 나옵니다.</p>

<div style="overflow-x:auto;margin-top:20px">
  <table style="width:100%;border-collapse:collapse;text-align:left;line-height:1.8">
    <thead>
      <tr style="border-bottom:2px solid var(--border);color:var(--text)">
        <th style="padding:12px">항목</th>
        <th style="padding:12px">투입 규격 / 용량</th>
        <th style="padding:12px">1인분 원가 (추정치)</th>
        <th style="padding:12px;color:#c7541d">비고</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom:1px solid var(--border)">
        <td style="padding:12px;font-weight:bold">10배 농축 닭 육수</td>
        <td style="padding:12px">1:10 희석 후 800ml</td>
        <td style="padding:12px">약 450원 ~ 500원</td>
        <td style="padding:12px">가스비·인건비 0원 절감</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border)">
        <td style="padding:12px;font-weight:bold">칼국수 생면</td>
        <td style="padding:12px">1인분 180~200g</td>
        <td style="padding:12px">약 500원 ~ 600원</td>
        <td style="padding:12px">쫄깃한 고급 생면 기준</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border)">
        <td style="padding:12px;font-weight:bold">닭고기 고명</td>
        <td style="padding:12px">삶아 찢은 살코기 40~50g</td>
        <td style="padding:12px">약 700원 ~ 800원</td>
        <td style="padding:12px">잡내 제거 비법 밑간</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border)">
        <td style="padding:12px;font-weight:bold">신선 채소 및 양념</td>
        <td style="padding:12px">양파, 당근, 호박, 대파 등</td>
        <td style="padding:12px">약 400원</td>
        <td style="padding:12px">기존 주방 식자재 호환</td>
      </tr>
      <tr style="border-bottom:2px solid var(--border);background:rgba(199,84,29,.05)">
        <td style="padding:12px;font-weight:bold;color:#c7541d">총 원가 합계</td>
        <td style="padding:12px;font-weight:bold">1인분 정량 기준</td>
        <td style="padding:12px;font-weight:bold;color:#c7541d">약 2,100원 ~ 2,300원</td>
        <td style="padding:12px;font-weight:bold;color:#c7541d">판매가 9,000원 기준 원가율 24.4% (마진 75.6%)</td>
      </tr>
    </tbody>
  </table>
</div>
</section>

<section>
<span class="eyebrow">03 / APPLICATION PROCESS</span>
<h2 class="h2">가맹비 0원 & 사업자 무료 샘플 지원 절차</h2>
<p class="lead">백세푸드는 가맹비, 로열티, 인테리어 강제 변경을 일절 요구하지 않습니다.</p>
<ul style="line-height:2;margin-top:16px;color:var(--text)">
  <li><strong>1단계 (유선 및 온라인 상담):</strong> 매장 형태(고깃집, 분식점, 배달 등)와 상권 분석 상담 진행.</li>
  <li><strong>2단계 (무료 테스트 샘플 발송):</strong> 사업자등록증 확인 시 1:10 농축 육수 테스트 샘플 키트 즉시 발송.</li>
  <li><strong>3단계 (매장 시식 및 농도 세팅):</strong> 점주님이 직접 시식 후 상권에 맞는 최적의 희석 비율(1:10) 확정.</li>
  <li><strong>4단계 (1박스 소량 발주 & 출시):</strong> 부담 없이 1박스(1L × 6병)부터 발주하여 다음 날 바로 메뉴판에 추가!</li>
</ul>

<div style="border:1px solid rgba(199,84,29,.35);background:linear-gradient(120deg,rgba(199,84,29,.14),rgba(245,241,232,.03));padding:clamp(26px,4vw,40px);margin-top:36px;display:flex;flex-direction:column;gap:16px">
  <h3 class="h3" style="margin:0">식당 부메뉴 도입 및 무료 샘플 신청</h3>
  <p style="margin:0;color:var(--muted);line-height:1.8">
    <strong>본사 상담 직통:</strong> 031-407-0103<br>
    <strong>운영 시간:</strong> 매일 10:00 ~ 22:00 (주말 상담 가능)<br>
    <strong>본사 위치:</strong> 경기도 안산시 상록구 석호로 101, 1층
  </p>
</div>
</section>
"""
            },
            "ja": {
                "title": "飲食店の売上を伸ばす最も簡単な方法！タッカルグクス（鶏うどん）ショップインショップ導入",
                "seoTitle": "タッカルグクス開業・サイドメニュー導入 | 10倍濃縮スープ＆原価率18% | 百世フード",
                "description": "厨房設備追加なし、10倍濃縮スープで6分調理！焼肉店・居酒屋・粉食店のランチ売上を劇的に伸ばすタッカルグクス（鶏カルグクス）導入ガイド。サンプル無償提供。",
                "heroEyebrow": "SHOP-IN-SHOP STARTUP",
                "heroTitle": "飲食店の売上を伸ばす最も簡単な方法！<br>タッカルグクス ショップインショップ導入",
                "heroLead": "大鍋で長時間スープを煮込む必要ゼロ！検証された10倍濃縮チキンスープで、既存店舗にランチの人気看板メニューを追加しませんか？",
                "heroImageAlt": "タッカルグクスの盛り付けと簡単調理",
                "tags": ["タッカルグクス開業", "飲食店サイドメニュー", "ショップインショップ", "百世フード"],
                "faq": [
                    {
                        "q": "既存の飲食店にタッカルグクスをすぐ追加できますか？",
                        "a": "はい！既存のコンロ1口と鍋さえあれば当日から導入可能です。10倍濃縮スープを希釈して注文後6分で提供できるため、専用の調理器具や職人は一切不要です。"
                    },
                    {
                        "q": "原価率とマジン率はどのくらいですか？",
                        "a": "販売価格800〜1,200円に対し、1人前の食材原価は約210〜230円（原価率18〜29%）です。粗利70%以上の極めて高い収益性を誇ります。"
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / WHY DAK-KALGUKSU</span>
<h2 class="h2">既存飲食店のランチ売上を救う<br>最高の高収益サイドメニュー</h2>
<p class="lead">「ランチタイムの集客を強化したい」「仕込みに手間のかからないメニューが欲しい」という飲食店オーナー様へ。百世フードの10倍濃縮スープを導入すれば、未経験のスタッフでも6分で専門店レベルのタッカルグクスを提供できます。</p>
</section>
"""
            },
            "en": {
                "title": "The Easiest Way to Boost Restaurant Sales: Chicken Kalguksu Shop-in-Shop Setup",
                "seoTitle": "Chicken Kalguksu Shop-in-Shop & Side Menu Guide | Baekse Food",
                "description": "Add authentic Chicken Kalguksu to your restaurant without new kitchen equipment. 10x concentrated broth, 6-minute cooking, 18-29% food cost, and free business samples.",
                "heroEyebrow": "SHOP-IN-SHOP STARTUP",
                "heroTitle": "The Easiest Way to Boost Restaurant Sales:<br>Chicken Kalguksu Shop-in-Shop Setup",
                "heroLead": "No all-day simmering required. Expand your lunch menu with proven 10x concentrated broth and achieve up to 75% profit margins.",
                "heroImageAlt": "Chicken Kalguksu noodle dish",
                "tags": ["KalguksuFranchise", "RestaurantMenuExpansion", "ShopInShop", "BaekseFood"],
                "faq": [
                    {
                        "q": "Can I add Chicken Kalguksu to my existing menu immediately?",
                        "a": "Yes! All you need is a single gas burner. Our 10x concentrated broth allows you to prepare authentic, piping-hot chicken noodle soup in just 6 minutes."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / OVERVIEW</span>
<h2 class="h2">High-Margin, Labor-Free Menu Expansion</h2>
<p class="lead">Chicken Kalguksu offers universally loved, comforting flavors with an exceptional food cost ratio of only 18% to 29%.</p>
</section>
"""
            },
            "zh": {
                "title": "提升现有餐厅营收的最简途径：鸡肉刀削面店中店与副菜单加盟传授",
                "seoTitle": "鸡肉刀削面店中店加盟传授 | 10倍浓缩高汤 6分钟出餐 | 百世食品",
                "description": "无需增添厨房大设备，利用10倍浓缩高汤6分钟极速出餐。烤肉店、小吃店午餐引流爆款，成本率仅18~29%，免费样品支持与小批量订货。",
                "heroEyebrow": "SHOP-IN-SHOP STARTUP",
                "heroTitle": "提升现有餐厅营收的最简途径：<br>鸡肉刀削面店中店与副菜单加盟传授",
                "heroLead": "告别长时间熬汤繁琐！凭借10倍高浓缩鸡汤包，为您的餐厅轻松引入高毛利午餐招牌菜。",
                "heroImageAlt": "鸡肉刀削面与店中店烹饪",
                "tags": ["鸡肉刀削面加盟", "餐厅副菜单", "店中店", "百世食品"],
                "faq": [
                    {
                        "q": "现有烤肉店或小吃店可以立即添加鸡肉刀削面吗？",
                        "a": "完全可以。只需后厨1个普通灶台，将10倍浓缩高汤按比例稀释后，6分钟即可出餐，无需专业大厨。"
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / OVERVIEW</span>
<h2 class="h2">低成本、高毛利的午餐爆单利器</h2>
<p class="lead">一份售价约8,000~12,000韩元，综合食材成本仅占18~29%，毛利率高达70%以上。</p>
</section>
"""
            },
            "ru": {
                "title": "Самый простой способ поднять выручку ресторана: Франшиза Дак-Калгуксу (куриная лапша)",
                "seoTitle": "Куриная лапша Калгуксу для ресторанов | Меню Shop-in-Shop | Baekse Food",
                "description": "Внедрите сытную куриную лапшу Калгуксу в меню своего ресторана. 10-кратный концентрированный бульон, варка за 6 минут, себестоимость 18-29%, бесплатные образцы.",
                "heroEyebrow": "SHOP-IN-SHOP STARTUP",
                "heroTitle": "Самый простой способ поднять выручку ресторана:<br>Франшиза Дак-Калгуксу",
                "heroLead": "Без сложного кухонного оборудования! Добавьте популярное блюдо в меню за 6 минут с помощью концентрированного бульона.",
                "heroImageAlt": "Корейская куриная лапша Калгуксу",
                "tags": ["КалгуксуФраншиза", "РесторанноеМеню", "ShopInShop", "BaekseFood"],
                "faq": [
                    {
                        "q": "Можно ли ввести блюдо в действующий ресторан?",
                        "a": "Да, достаточно одной обычной конфорки. Блюдо готовится ровно за 6 минут благодаря 10-кратному концентрату бульона."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / OVERVIEW</span>
<h2 class="h2">Идеальное блюдо для обеденного меню</h2>
<p class="lead">Себестоимость порции составляет всего 18-29% от цены продажи, что обеспечивает маржинальность свыше 70%.</p>
</section>
"""
            }
        }
    },

    # ----------------------------------------------------
    # POST 2: dak-kalguksu-recipe-manual
    # ----------------------------------------------------
    {
        "slug": "dak-kalguksu-recipe-manual",
        "image": "/img/bs-menu-4.webp",
        "translations": {
            "ko": {
                "title": "누구나 6분이면 전문점 깊은 맛! 표준 닭칼국수 초간단 조리 매뉴얼 & 닭고기 삶는 비법 팁",
                "seoTitle": "닭칼국수 표준 조리 레시피 | 6분 완성 매뉴얼 & 닭고기 삶는 팁 | 백세푸드",
                "description": "10배 농축 육수를 활용한 닭칼국수 6분 초간단 조리 매뉴얼. 닭 잡내 없이 부드럽게 결대로 삶아 찢는 비법과 면 3분, 야채 3분 표준화 레시피를 전수합니다.",
                "heroEyebrow": "6-MINUTE STANDARD RECIPE",
                "heroTitle": "누구나 6분이면 전문점 깊은 맛!<br>표준 닭칼국수 초간단 조리 매뉴얼",
                "heroLead": "알바생도 첫날부터 맛집 주방장처럼! 1:10 희석 육수 800ml와 닭고기 손질 노하우로 완성하는 흔들림 없는 표준 레시피.",
                "heroImageAlt": "6분 조리 완성 닭칼국수와 닭고기 고명",
                "tags": ["닭칼국수레시피", "닭칼국수조리법", "닭고기삶는팁", "조리표준화", "백세푸드"],
                "faq": [
                    {
                        "q": "닭칼국수 조리 시간 6분은 어떻게 구성되나요?",
                        "a": "1:10 희석 육수 800ml에 닭고기 고명을 넣고 불을 올린 뒤, 육수가 끓어오르면 생면을 넣고 3분간 끓입니다. 그 후 썰어둔 야채(양파, 당근, 감자, 호박, 파)를 한 번에 넣고 3분간 더 끓여내면 정확히 6분 만에 완성됩니다."
                    },
                    {
                        "q": "고명으로 쓸 닭고기는 어떻게 삶아야 잡내가 없고 부드러운가요?",
                        "a": "끓는 물에 대파 뿌리, 통마늘, 생강 편 한 조각을 넣고 닭가슴살이나 안심을 15~18분간 삶아냅니다. 삶은 직후 찬물이나 얼음물에 살짝 담가 표면을 수축시킨 뒤 결대로 찢어내고, 참기름과 소금, 백후추로 살짝 밑간해 보관하면 잡내 없이 하루 종일 촉촉합니다."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / DILUTION & PREP</span>
<h2 class="h2">기본 배합: 1:10 황금 희석 비율</h2>
<p class="lead">백세푸드의 전용 닭칼국수 육수는 10배 고농축 소스입니다. 물 10L에 농축액 1L를 붓고 저어주면 즉시 11L의 진국 육수가 완성됩니다.</p>

<div style="border:1px solid rgba(199,84,29,.25);background:rgba(199,84,29,.05);padding:24px;border-radius:8px;margin-top:24px">
  <h3 class="h3" style="margin:0 0 16px;color:#c7541d">✨ 주방 필수 팁: 닭고기 고명 삶는 특급 노하우</h3>
  <ul style="line-height:2;margin:0;padding-left:20px">
    <li><strong>부위 선택:</strong> 퍽퍽하지 않고 담백한 닭가슴살 또는 닭안심, 통닭 순살을 사용합니다.</li>
    <li><strong>잡내 제거 향신채:</strong> 끓는 물에 대파 파란 잎, 통마늘 5알, 생강 편 한 조각을 넣고 15~18분간 속까지 알맞게 익힙니다.</li>
    <li><strong>찬물 텐션 수축:</strong> 익은 닭고기를 건져 찬물/얼음물에 30초간 살짝 담가 육즙을 가두고 표면을 쫄깃하게 조입니다.</li>
    <li><strong>결대로 찢기 & 밑간:</strong> 손이나 포크로 결대로 먹기 좋게 찢은 뒤, 참기름 반 큰술, 맛소금 약간, 백후추 톡톡 뿌려 버무려 소분 보관합니다.</li>
  </ul>
</div>
</section>

<section>
<span class="eyebrow">02 / 6-MINUTE TIMER</span>
<h2 class="h2">1인분 표준 조리 매뉴얼 (타이머 6분)</h2>

<div class="grid grid-3" style="margin-top:24px">
  <div class="card"><div class="body">
    <span class="tag">00:00 - 육수 가열</span>
    <h3 class="h3">희석 육수 + 닭고기 투입</h3>
    <p>1:10 희석 육수 800ml와 밑간해 둔 닭고기 고명(40~50g)을 전골 냄비에 넣고 센 불에 올립니다.</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">03:00 - 면 투하</span>
    <h3 class="h3">칼국수 생면 3분간 끓이기</h3>
    <p>육수가 끓으면 겉가루를 털어낸 칼국수 생면을 넣고, 면이 뭉치지 않게 젓가락으로 저으며 3분간 끓입니다.</p>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">06:00 - 야채 마무리</span>
    <h3 class="h3">손질 채소 투하 후 3분 완성</h3>
    <p>양파 채, 당근, 감자 슬라이스, 애호박, 파를 넣고 3분간 센 불에 끓여 면기에 담아내면 조리 완료!</p>
  </div></div>
</div>
</section>
"""
            },
            "ja": {
                "title": "誰でも6分で専門店の深い味！タッカルグクス標準調理マニュアル＆鶏肉の下処理テクニック",
                "seoTitle": "タッカルグクス レシピ・6分調理マニュアル | 鶏肉の茹で方秘伝 | 百世フード",
                "description": "10倍濃縮スープで作るタッカルグクス（鶏うどん）の6分調理法。臭みを完全に消す鶏肉の茹で方と、アルバイトでも味のブレが出ない標準化マニュアルを公開。",
                "heroEyebrow": "6-MINUTE STANDARD RECIPE",
                "heroTitle": "誰でも6分で専門店の深い味！<br>タッカルグクス標準調理マニュアル",
                "heroLead": "新人アルバイトでも初日から一流の味！希釈スープ800mlと鶏肉の仕込みテクニックで実現するブレない標準レシピ。",
                "heroImageAlt": "タッカルグクス調理工程と完成写真",
                "tags": ["タッカルグクスレシピ", "調理マニュアル", "韓国料理調理法", "百世フード"],
                "faq": [
                    {
                        "q": "調理時間6分の内訳は？",
                        "a": "希釈スープに鶏肉を入れて火にかけ、沸騰したら生麺を入れて3分。刻んだ野菜（玉ねぎ、人参、じゃがいも、ズッキーニ、長ネギ）を投入してさらに3分煮込むだけで完成します。"
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / DILUTION & PREP</span>
<h2 class="h2">1:10の黄金希釈比率と鶏肉の下処理</h2>
<p class="lead">百世フードのタッカルグクス用スープは10倍高濃縮。水10Lに対してスープ1Lを混ぜるだけで、黄金色の絶品鶏出汁が完成します。</p>
</section>
"""
            },
            "en": {
                "title": "Master Authentic Chicken Kalguksu in 6 Minutes: Standardized Cooking Manual & Chicken Prep Tips",
                "seoTitle": "6-Minute Chicken Kalguksu Recipe Manual | Chicken Prep Tips | Baekse Food",
                "description": "Cook restaurant-quality Chicken Kalguksu in just 6 minutes with 10x concentrated broth. Professional chicken boiling secrets, zero gamy smell, and foolproof kitchen instructions.",
                "heroEyebrow": "6-MINUTE STANDARD RECIPE",
                "heroTitle": "Master Authentic Chicken Kalguksu in 6 Minutes:<br>Standardized Cooking Manual",
                "heroLead": "Even part-time staff can cook like a master chef on day one. A precise 6-minute procedure using 800ml diluted broth.",
                "heroImageAlt": "Chicken Kalguksu cooking steps",
                "tags": ["KalguksuRecipe", "6MinuteCooking", "ChickenPrepTips", "BaekseFood"],
                "faq": [
                    {
                        "q": "What is the breakdown of the 6-minute cooking time?",
                        "a": "Bring 800ml of diluted broth with shredded chicken to a boil. Add fresh noodles and cook for 3 minutes. Add prepped vegetables (onion, carrot, potato, zucchini, scallions) and cook for another 3 minutes. Total: 6 minutes."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / THE 6-MINUTE METHOD</span>
<h2 class="h2">Standardized Operations for Fast Turnover</h2>
<p class="lead">By preparing seasoned shredded chicken in advance, your kitchen can churn out bowls of piping-hot chicken kalguksu in exactly 6 minutes.</p>
</section>
"""
            },
            "zh": {
                "title": "任何人只需6分钟即可复刻专业名店风味！标准鸡肉刀削面超简烹饪手册与煮鸡秘诀",
                "seoTitle": "鸡肉刀削面6分钟标准烹饪手册 | 鸡肉去腥手撕技巧 | 百世食品",
                "description": "基于10倍高浓缩鸡汤包的鸡肉刀削面6分钟出餐手册。详解鸡肉彻底去腥滑嫩煮制秘诀，面条3分钟、蔬菜3分钟极速出餐标准化指南。",
                "heroEyebrow": "6-MINUTE STANDARD RECIPE",
                "heroTitle": "任何人只需6分钟即可复刻专业风味！<br>标准鸡肉刀削面超简烹饪手册",
                "heroLead": "零厨艺新手也能第一天出餐如大厨！1:10稀释高汤800ml搭配鸡肉前处理秘方，确保每碗品质如一。",
                "heroImageAlt": "6分钟出餐鸡肉刀削面",
                "tags": ["鸡肉刀削面配方", "6分钟出餐", "鸡肉去腥秘诀", "百世食品"],
                "faq": [
                    {
                        "q": "6分钟烹饪时间是如何分配的？",
                        "a": "800ml稀释高汤加鸡肉丝大火烧开，下面条煮3分钟，随后倒入配菜（洋葱、胡萝卜、土豆、西葫芦、大葱）再煮3分钟即可装碗出餐。"
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / PREP SECRETS</span>
<h2 class="h2">1:10黄金稀释与鸡肉去腥秘诀</h2>
<p class="lead">沸水中加入葱根、生姜、大蒜将鸡胸肉煮15分钟，迅速放入冷水中收缩肉质并顺纹手撕，加香油盐预调味，整天鲜嫩爽口。</p>
</section>
"""
            },
            "ru": {
                "title": "Вкус ресторанного уровня всего за 6 минут! Стандартная инструкция варки Дак-Калгуксу",
                "seoTitle": "Рецепт Дак-Калгуксу за 6 минут | Как варить курицу без запаха | Baekse Food",
                "description": "Готовьте традиционную корейскую куриную лапшу Дак-Калгуксу всего за 6 минут с 10-кратным концентратом бульона. Секреты варки нежной курицы без запаха.",
                "heroEyebrow": "6-MINUTE STANDARD RECIPE",
                "heroTitle": "Вкус ресторанного уровня за 6 минут!<br>Стандартная инструкция Дак-Калгуксу",
                "heroLead": "Даже стажер с первого дня сварит идеальный суп! Пошаговый 6-минутный регламент на основе 800 мл разведенного бульона.",
                "heroImageAlt": "Варка корейской куриной лапши за 6 минут",
                "tags": ["РецептКалгуксу", "КулинарнаяИнструкция", "КорейскийСуп", "BaekseFood"],
                "faq": [
                    {
                        "q": "Как распределяются 6 минут варки?",
                        "a": "В кипящий бульон с курицей закладывается свежая лапша на 3 минуты, затем овощи (лук, морковь, картофель, кабачок) еще на 3 минуты."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / INSTRUCTION</span>
<h2 class="h2">Быстрое приготовление без потери качества</h2>
<p class="lead">Четкий 6-минутный тайминг гарантирует максимальную скорость обслуживания гостей в обеденный пик.</p>
</section>
"""
            }
        }
    },

    # ----------------------------------------------------
    # POST 3: dak-kalguksu-broth-supply
    # ----------------------------------------------------
    {
        "slug": "dak-kalguksu-broth-supply",
        "image": "/img/bs-sys-ck.webp",
        "translations": {
            "ko": {
                "title": "식당 사장님을 위한 고농축 10배 닭칼국수 육수 소스 납품 안내",
                "seoTitle": "고농축 10배 닭칼국수 육수 소스 납품 | 1L PET 규격 & 무료 샘플 지원 | 백세푸드",
                "description": "식당 가스비와 인건비를 획기적으로 줄여주는 1:10 고농축 닭칼국수 육수 B2B 납품 안내. 1L PET 1병으로 13~14인분 조리, 원가율 18~29%, 사업자 무료 샘플 및 1박스 소량 주문 가능.",
                "heroEyebrow": "10X CONCENTRATED BROTH SUPPLY",
                "heroTitle": "식당 사장님을 위한 고농축 10배<br>닭칼국수 육수 소스 납품 안내",
                "heroLead": "매일 닭 뼈를 우리고 기름을 걷어내는 새벽 노동은 이제 그만! 1리터 1병으로 11리터의 진국 육수를 완성하는 혁신적인 B2B 소스 공급망.",
                "heroImageAlt": "백세푸드 10배 고농축 닭칼국수 육수와 물류 공급",
                "tags": ["닭칼국수육수납품", "업소용육수소스", "10배농축육수", "소스납품", "백세푸드"],
                "faq": [
                    {
                        "q": "10배 농축 육수 1L 한 병으로 몇 그릇의 닭칼국수를 만들 수 있나요?",
                        "a": "물 10 : 농축육수 1로 희석하면 1L 한 병으로 총 11리터(11,000ml)의 진국 육수가 완성됩니다. 1인분 조리 시 정량 800ml를 사용할 경우 약 13~14그릇을 넉넉히 조리할 수 있습니다."
                    },
                    {
                        "q": "포장 규격과 유통기한, 보관 방법은 어떻게 되나요?",
                        "a": "슬림하고 견고한 1L 전용 PET 보틀(1박스 6병 포장)로 생산되어 좁은 업소용 냉장고나 선반에도 수십 병 단위로 적재 보관이 용이합니다. 미개봉 시 실온에서 1년간 보관 가능하며, 개봉 후에는 냉장 보관하시면 됩니다. 대형 식당을 위한 5L/10L 벌크 규격도 지원합니다."
                    },
                    {
                        "q": "최소 주문 수량(MOQ)과 샘플 신청 절차는 어떻게 되나요?",
                        "a": "식당 운영 사업자등록증을 보유하신 대표님께는 1~2인분 분량의 무료 테스트 샘플 키트를 지원해 드립니다. 정식 발주 시에도 1박스(1L × 6병)부터 전국 택배 발송이 가능하므로 재고 부담 없이 편리하게 도입하실 수 있습니다."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / PACKAGING & EFFICIENCY</span>
<h2 class="h2">포장 규격 및 1:10 고농축 배합 효율</h2>
<p class="lead">무겁고 공간을 많이 차지하는 액상 말통 육수는 식당 주방의 골칫거리였습니다. 백세푸드의 10배 고농축 닭칼국수 육수는 컴팩트한 1리터(1L) 규격으로 보관성과 조리 편의성을 극대화했습니다.</p>

<div class="grid grid-2" style="margin-top:24px">
  <div class="card"><div class="body">
    <span class="tag">SPECIFICATION</span>
    <h3 class="h3">포장 규격 및 생산성</h3>
    <ul style="line-height:1.9;margin:8px 0 0;padding-left:18px">
      <li><strong>포장 단위:</strong> 1L 슬림 PET 보틀 (1박스 = 6병 포장)</li>
      <li><strong>대용량 옵션:</strong> 대형 매장 및 급식용 5L / 10L 벌크 주문 가능</li>
      <li><strong>유효 기간:</strong> 미개봉 실온 12개월 (개봉 후 냉장 보관)</li>
      <li><strong>생산 그릇 수:</strong> 1병으로 800ml 1인분 기준 약 13~14그릇 조리</li>
    </ul>
  </div></div>
  <div class="card"><div class="body">
    <span class="tag">COST ADVANTAGE</span>
    <h3 class="h3">비용 및 노동력 획기적 절감</h3>
    <ul style="line-height:1.9;margin:8px 0 0;padding-left:18px">
      <li><strong>가스비 절감:</strong> 매일 4~5시간 닭 뼈를 우리는 가스비 0원화</li>
      <li><strong>인건비 절감:</strong> 새벽 출근 및 육수 관리 전문 인력 불필요</li>
      <li><strong>음식물 쓰레기 절감:</strong> 닭 뼈 잔여물 및 채소 찌꺼기 폐기 0%</li>
      <li><strong>원가율 18~29%:</strong> 그릇당 육수 원가 450~500원 선으로 극대화된 마진</li>
    </ul>
  </div></div>
</div>
</section>

<section>
<span class="eyebrow">02 / SAMPLES & LOGISTICS</span>
<h2 class="h2">최소 주문 수량(MOQ) & 사업자 무료 샘플 신청</h2>
<div style="border:1px solid rgba(199,84,29,.25);background:rgba(199,84,29,.05);padding:24px;border-radius:8px;margin-top:24px">
  <h3 class="h3" style="margin:0 0 16px;color:#c7541d">📦 백세푸드 B2B 공급 파트너십 원칙</h3>
  <ul style="line-height:2;margin:0;padding-left:20px">
    <li><strong>사업자 무료 샘플 제공:</strong> 사업자등록증 사본 접수 시 1~2인분 분량의 테스트 육수 샘플을 즉시 택배 발송해 드립니다.</li>
    <li><strong>부담 없는 1박스 발주:</strong> 첫 거래부터 무리하게 대량 주문을 강요하지 않습니다. 1박스(1L × 6병)부터 전국 택배 출고됩니다.</li>
    <li><strong>상권별 농도 컨설팅:</strong> 담백한 국물을 선호하는 오피스 상권(1:11 권장)부터 진한 감칠맛을 원하는 주택/골목 상권(1:9.5 권장)까지 맞춤 가이드를 제공합니다.</li>
  </ul>
</div>

<div style="border:1px solid rgba(199,84,29,.35);background:linear-gradient(120deg,rgba(199,84,29,.14),rgba(245,241,232,.03));padding:clamp(26px,4vw,40px);margin-top:36px;display:flex;flex-direction:column;gap:16px">
  <h3 class="h3" style="margin:0">육수 납품 상담 및 무료 샘플 신청</h3>
  <p style="margin:0;color:var(--muted);line-height:1.8">
    <strong>직통 상담 전화:</strong> 031-407-0103<br>
    <strong>운영 시간:</strong> 매일 10:00 ~ 22:00 (연중무휴)<br>
    <strong>본사 주소:</strong> 경기도 안산시 상록구 석호로 101, 1층 백세푸드 본사 CK 지원팀
  </p>
</div>
</section>
"""
            },
            "ja": {
                "title": "飲食店オーナー様必見！高濃縮10倍タッカルグクス（鶏うどん）専用スープ卸売のご案内",
                "seoTitle": "高濃縮10倍タッカルグクススープ卸売 | 1Lボトル＆無料サンプル提供 | 百世フード",
                "description": "ガス代と人件費を大幅削減する1:10高濃縮タッカルグクススープのB2B卸売案内。1Lペットボトル1本で13〜14人前調理、原価率18〜29%、1ケース（6本）から小ロット発注可能。飲食店様向け無料サンプル提供中。",
                "heroEyebrow": "10X CONCENTRATED BROTH SUPPLY",
                "heroTitle": "飲食店オーナー様必見！高濃縮10倍<br>タッカルグクス専用スープ卸売のご案内",
                "heroLead": "毎朝の鶏ガラ煮込みと油切り労働はもう不要！1リットル1本で11リットルの極上鶏出汁が完成する画期的なB2Bスープ供給システム。",
                "heroImageAlt": "百世フード 10倍高濃縮スープ物流供給",
                "tags": ["タッカルグクススープ卸売", "業務用チキンスープ", "10倍濃縮スープ", "百世フード"],
                "faq": [
                    {
                        "q": "1Lボトル1本で何人前作れますか？",
                        "a": "水10：濃縮スープ1で希釈すると合計11Lのスープが完成します。1人前800ml基準で約13〜14人前を調理可能です。"
                    },
                    {
                        "q": "最小発注単位とサンプル提供は？",
                        "a": "飲食店営業許可をお持ちの事業者様には無料テイスティングサンプルを提供します。通常発注も1ケース（1L×6本）から対応可能です。"
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / SPECIFICATION</span>
<h2 class="h2">保管性抜群の1Lスリムボトル仕様</h2>
<p class="lead">場所を取る大型寸胴や業務用ポリタンクと異なり、扱いやすい1LスリムPETボトル規格を採用。未開封常温で1年間長期保管が可能です。</p>
</section>
"""
            },
            "en": {
                "title": "B2B Supply of 10x Concentrated Chicken Kalguksu Broth for Restaurant Owners",
                "seoTitle": "10x Concentrated Chicken Kalguksu Broth Supply | 1L PET & Free Samples | Baekse Food",
                "description": "Cut gas utility and kitchen prep labor with 1:10 high-concentration chicken broth. 1L makes 13-14 servings, 18-29% food cost, 1-case minimum order, and free business samples.",
                "heroEyebrow": "10X CONCENTRATED BROTH SUPPLY",
                "heroTitle": "B2B Supply of 10x Concentrated<br>Chicken Kalguksu Broth for Restaurants",
                "heroLead": "Stop waking up at dawn to simmer chicken bones. One 1-liter bottle yields 11 liters of rich, umami-packed authentic chicken broth.",
                "heroImageAlt": "10x concentrated chicken broth packaging and delivery",
                "tags": ["ChickenBrothSupply", "ConcentratedStock", "RestaurantB2B", "BaekseFood"],
                "faq": [
                    {
                        "q": "How many servings does one 1L bottle produce?",
                        "a": "Diluting 1 bottle of concentrate with 10 parts water produces 11 liters of ready-to-use broth—yielding approximately 13 to 14 generous 800ml bowls."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / SPECIFICATION</span>
<h2 class="h2">Compact Storage, Uncompromising Flavor</h2>
<p class="lead">Stored at room temperature with a 12-month shelf life, our 1L slim PET bottles maximize small kitchen storage without bulky containers.</p>
</section>
"""
            },
            "zh": {
                "title": "面向餐厅店主的高浓缩10倍鸡肉刀削面专用高汤酱汁批发供应指南",
                "seoTitle": "10倍高浓缩鸡肉刀削面高汤批发 | 1L瓶装与免费样品支持 | 百世食品",
                "description": "大幅节省燃气费与熬汤人工的1:10高浓缩鸡汤B2B供应指南。1L装可做13~14份，成本率仅18~29%，支持1箱（6瓶）起订及营业执照商家免费样品发放。",
                "heroEyebrow": "10X CONCENTRATED BROTH SUPPLY",
                "heroTitle": "面向餐厅店主的高浓缩10倍<br>鸡肉刀削面专用高汤供应指南",
                "heroLead": "无需每天清晨早起熬鸡骨撇浮油！1瓶1升兑出11升浓鲜鸡汤，颠覆传统餐饮后厨的高效供应链。",
                "heroImageAlt": "百世食品10倍浓缩鸡汤物流配送",
                "tags": ["鸡肉刀削面高汤批发", "商用鸡汤包", "10倍浓缩高汤", "百世食品"],
                "faq": [
                    {
                        "q": "1升浓缩高汤可以做多少碗刀削面？",
                        "a": "水与浓缩液按10:1稀释，1L可兑出11L高汤，按每碗800ml计算可制作约13~14碗刀削面。"
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / SPECIFICATION</span>
<h2 class="h2">1L精巧PET瓶装，空间利用率极高</h2>
<p class="lead">摆脱传统笨重大塑料桶的困扰，未开封常温保质期长达12个月，1箱（6瓶）起订发货，无压仓风险。</p>
</section>
"""
            },
            "ru": {
                "title": "Оптовые поставки 10-кратного концентрированного бульона для лапши Дак-Калгуксу",
                "seoTitle": "Концентрат куриного бульона 10x для ресторанов | 1л PET и образцы | Baekse Food",
                "description": "Сократите расходы на газ и поваров с 10-кратным концентратом куриного бульона 1:10. 1 бутылка = 13-14 порций, себестоимость 18-29%, доставка от 1 коробки (6 бутылок), бесплатные образцы.",
                "heroEyebrow": "10X CONCENTRATED BROTH SUPPLY",
                "heroTitle": "Оптовые поставки 10-кратного концентрированного<br>бульона для ресторанов",
                "heroLead": "Забудьте о многочасовой варке куриных костей! 1 литр концентрата дает 11 литров наваристого прозрачного бульона.",
                "heroImageAlt": "Концентрат куриного бульона для ресторанов",
                "tags": ["ПоставкиБульона", "КуриныйКонцентрат", "РесторанныйB2B", "BaekseFood"],
                "faq": [
                    {
                        "q": "Сколько порций получается из 1 литра?",
                        "a": "При разведении 1 к 10 получается 11 литров готового бульона — около 13–14 полноценных порций по 800 мл."
                    }
                ],
                "content": """
<section>
<span class="eyebrow">01 / SPECIFICATION</span>
<h2 class="h2">Компактное хранение и стабильный вкус</h2>
<p class="lead">Бутылки объемом 1л хранятся при комнатной температуре 12 месяцев, экономя место в холодильниках ресторана.</p>
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
        "ko": "무료 샘플 & 상담 신청",
        "ja": "無料サンプル・相談申込",
        "en": "Free Sample & Consultation",
        "zh": "免费样品与咨询申请",
        "ru": "Бесплатный образец и консультация"
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
  label: "{cta_primary_label.get(lang, '무료 샘플 신청')}"
  href: "#apply"
ctaSecondary:
  label: "{cta_secondary_label.get(lang, '전화 문의')}"
  href: "tel:031-407-0103"
interest: "닭한마리 소스"
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

    print(f"\nSuccessfully generated all {created_count} Dak-Kalguksu blog markdown files!")

if __name__ == "__main__":
    main()
