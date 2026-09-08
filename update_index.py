import os

path = r'c:\project\baekse-food\layouts\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

translations = '''{{ define "main" }}
{{- $lang := .Lang -}}
{{- $marquee := "점심 보리밥 · 저녁 닭한마리 · 야간 포차 · 식자재 80% 호환 · 로스율 제로 · 인테리어 마진 0원 · " -}}
{{- $calcTitle := "닭한마리 창업, 예상 수익 직접 계산해 보세요" -}}
{{- $calcLead := "인테리어 본사 마진 0원. 점주님이 장사가 잘되어 매일 시키는 물류비로만 수익을 냅니다." -}}
{{- $calcPyeong := "매장 평수" -}}
{{- $calcDaily := "예상 일매출" -}}
{{- $calcMonthly := "월 예상 매출" -}}
{{- $calcFood := "식자재 원가" -}}
{{- $calcRent := "월 임대료 추산" -}}
{{- $calcLabor := "인건비 추산" -}}
{{- $calcUtil := "공과금·기타" -}}
{{- $calcNote := "※ 업계 평균 기준 추산치이며 실제 수익은 상권·운영 방식에 따라 달라집니다. 상담 시 상권별 실측 데이터를 드립니다." -}}
{{- $calcBtn := "내 상권 수익 상담받기" -}}

{{- if eq $lang "en" -}}
  {{- $marquee = "Lunch Bibimbap · Dinner Dakhanmari · Night Pocha · 80% Ingredient Compatibility · Zero Waste · Zero Interior Margin · " -}}
  {{- $calcTitle = "Dakhanmari Franchise Profit Simulator" -}}
  {{- $calcLead = "Zero interior margin. We profit solely from the daily food supplies you order as your business grows." -}}
  {{- $calcPyeong = "Store Size" -}}
  {{- $calcDaily = "Expected Daily Sales" -}}
  {{- $calcMonthly = "Monthly Expected Sales" -}}
  {{- $calcFood = "Food Cost" -}}
  {{- $calcRent = "Est. Monthly Rent" -}}
  {{- $calcLabor = "Est. Labor Cost" -}}
  {{- $calcUtil = "Utilities & Misc." -}}
  {{- $calcNote = "※ Estimates are based on industry averages. Actual profits may vary depending on location and operation. Custom data provided during consultation." -}}
  {{- $calcBtn = "Get My Custom Profit Estimate" -}}
{{- else if eq $lang "zh" -}}
  {{- $marquee = "午餐大麦饭 · 晚餐一只鸡 · 深夜大排档 · 食材80%通用 · 零损耗 · 零装修加价 · " -}}
  {{- $calcTitle = "一只鸡加盟预期收益计算器" -}}
  {{- $calcLead = "总部零装修加价。我们仅通过您生意兴隆时每天订购的物流食材获取收益。" -}}
  {{- $calcPyeong = "店铺面积" -}}
  {{- $calcDaily = "预期日营业额" -}}
  {{- $calcMonthly = "月预期营业额" -}}
  {{- $calcFood = "食材成本" -}}
  {{- $calcRent = "预估月租金" -}}
  {{- $calcLabor = "预估人工费" -}}
  {{- $calcUtil = "水电杂费" -}}
  {{- $calcNote = "※ 此为行业平均估算值，实际收益因商圈与经营方式而异。咨询时将提供详细数据。" -}}
  {{- $calcBtn = "获取专属收益分析" -}}
{{- else if eq $lang "ja" -}}
  {{- $marquee = "昼は麦飯 · 夜はタッカンマリ · 深夜はポチャ · 食材80%互換 · ロス率ゼロ · インテリアマージン0円 · " -}}
  {{- $calcTitle = "タッカンマリ創業 予想収益シミュレーター" -}}
  {{- $calcLead = "本社のインテリアマージン0円。店舗が繁盛して発注される物流費のみで収益を得ます。" -}}
  {{- $calcPyeong = "店舗面積" -}}
  {{- $calcDaily = "予想日商" -}}
  {{- $calcMonthly = "月間予想売上" -}}
  {{- $calcFood = "食材原価" -}}
  {{- $calcRent = "予想月額家賃" -}}
  {{- $calcLabor = "予想人件費" -}}
  {{- $calcUtil = "水道光熱費・その他" -}}
  {{- $calcNote = "※ 業界平均基準の推計値であり、実際の収益は商圏や運営方式により異なります。ご相談時に詳細データを提供します。" -}}
  {{- $calcBtn = "収益シミュレーションを相談する" -}}
{{- else if eq $lang "ru" -}}
  {{- $marquee = "Обед: Пибимпап · Ужин: Дакханмари · Ночь: Поча · Совместимость ингредиентов 80% · Безотходное производство · Нулевая наценка на интерьер · " -}}
  {{- $calcTitle = "Калькулятор прибыли франшизы" -}}
  {{- $calcLead = "Нулевая наценка на интерьер. Наша прибыль зависит только от ежедневных поставок продуктов для вашего бизнеса." -}}
  {{- $calcPyeong = "Площадь магазина" -}}
  {{- $calcDaily = "Ожидаемые продажи в день" -}}
  {{- $calcMonthly = "Ожидаемые продажи в месяц" -}}
  {{- $calcFood = "Стоимость продуктов" -}}
  {{- $calcRent = "Оценка аренды" -}}
  {{- $calcLabor = "Оценка затрат на труд" -}}
  {{- $calcUtil = "Коммунальные услуги" -}}
  {{- $calcNote = "※ Оценки основаны на средних показателях по отрасли. Фактическая прибыль зависит от местоположения и способа управления." -}}
  {{- $calcBtn = "Получить расчет прибыли" -}}
{{- end -}}'''

content = content.replace('{{ define "main" }}', translations)
content = content.replace('<span>점심 보리밥 · 저녁 닭한마리 · 야간 포차 · 식자재 80% 호환 · 로스율 제로 · 인테리어 마진 0원 · </span>', '<span>{{ $marquee }}</span>')
content = content.replace('닭한마리 창업, 예상 수익 직접 계산해 보세요', '{{ $calcTitle }}')
content = content.replace('인테리어 본사 마진 0원. 점주님이 장사가 잘되어 매일 시키는 물류비로만 수익을 냅니다.', '{{ $calcLead }}')
content = content.replace('매장 평수', '{{ $calcPyeong }}')
content = content.replace('예상 일매출', '{{ $calcDaily }}')
content = content.replace('월 예상 매출 <span style="color:var(--dimmer)">(30일)</span>', '{{ $calcMonthly }} <span style="color:var(--dimmer)">(30 days)</span>')
content = content.replace('식자재 원가 <span style="color:var(--dimmer)">(32%)</span>', '{{ $calcFood }} <span style="color:var(--dimmer)">(32%)</span>')
content = content.replace('월 임대료 추산', '{{ $calcRent }}')
content = content.replace('인건비 추산', '{{ $calcLabor }}')
content = content.replace('공과금·기타 (매출 5%)', '{{ $calcUtil }} (5%)')
content = content.replace('※ 업계 평균 기준 추산치이며 실제 수익은 상권·운영 방식에 따라 달라집니다. 상담 시 상권별 실측 데이터를 드립니다.', '{{ $calcNote }}')
content = content.replace('내 상권 수익 상담받기', '{{ $calcBtn }}')

# Unit IDs for JS
content = content.replace('<span style="font-family:\'Gowun Batang\',serif;font-size:clamp(20px,2.4vw,30px);color:var(--accent-light);padding-bottom:6px">만원</span>', '<span id="calc-net-unit" style="font-family:\'Gowun Batang\',serif;font-size:clamp(20px,2.4vw,30px);color:var(--accent-light);padding-bottom:6px">만원</span>')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated layouts/index.html')
