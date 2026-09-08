import os

path = r'c:\project\baekse-food\layouts\partials\apply-form.html'

translations = '''{{ $ctx := .page | default . }}
{{ $defaultInterest := .defaultInterest | default "닭한마리" }}
{{- $lang := $ctx.Lang -}}

{{- $title := "맛으로 먼저<br>증명합니다" -}}
{{- $lead := "무료 소스 샘플과 창업안내서를 보내드립니다. 신청 후 카카오톡 알림톡으로 안내드리며, 원치 않는 영업 전화는 하지 않습니다." -}}
{{- $lblFlagship := "본점" -}}
{{- $lblHours := "영업시간" -}}
{{- $lblContact := "문의" -}}
{{- $lblName := "이름" -}}
{{- $plName := "성함을 입력해 주세요" -}}
{{- $lblPhone := "연락처" -}}
{{- $lblStore := "현재 운영중인 매장" -}}
{{- $optYes := "있음" -}}
{{- $optNo := "없음 (신규 창업)" -}}
{{- $lblInterest := "관심 분야" -}}
{{- $btnText := "무료 상담 신청하기" -}}
{{- $disclaimer := "신청 시 개인정보 수집·이용(상담 목적)에 동의하는 것으로 간주합니다." -}}

{{- $boribapText := "보리밥 산채정식" -}}
{{- $dakText := "닭한마리" -}}
{{- $academyText := "전수교육" -}}
{{- $sauceText := "닭한마리 소스" -}}
{{- $pochaText := "백세포차" -}}

{{- if eq $lang "en" -}}
  {{- $title = "Taste It to<br>Believe It" -}}
  {{- $lead = "We'll send you free sauce samples and a franchise guide. After applying, you will be notified, and we promise no unwanted sales calls." -}}
  {{- $lblFlagship = "Flagship" -}}
  {{- $lblHours = "Hours" -}}
  {{- $lblContact = "Contact" -}}
  {{- $lblName = "Name" -}}
  {{- $plName = "Enter your name" -}}
  {{- $lblPhone = "Phone" -}}
  {{- $lblStore = "Current Store Status" -}}
  {{- $optYes = "Yes" -}}
  {{- $optNo = "No (New Business)" -}}
  {{- $lblInterest = "Area of Interest" -}}
  {{- $btnText = "Request Free Consultation" -}}
  {{- $disclaimer = "By submitting, you agree to the collection and use of personal information for consultation." -}}
  {{- $boribapText = "Barley Bibimbap" -}}
  {{- $dakText = "Dakhanmari" -}}
  {{- $academyText = "Recipe Academy" -}}
  {{- $sauceText = "Sauce Supply" -}}
  {{- $pochaText = "Night Pocha" -}}
{{- else if eq $lang "zh" -}}
  {{- $title = "用无可挑剔的<br>美味证明一切" -}}
  {{- $lead = "我们将为您寄送免费酱料样品和加盟指南。申请后会通过信息通知您，绝无推销骚扰电话。" -}}
  {{- $lblFlagship = "总店" -}}
  {{- $lblHours = "营业时间" -}}
  {{- $lblContact = "咨询" -}}
  {{- $lblName = "姓名" -}}
  {{- $plName = "请输入您的姓名" -}}
  {{- $lblPhone = "联系方式" -}}
  {{- $lblStore = "当前是否有门店" -}}
  {{- $optYes = "有" -}}
  {{- $optNo = "无（新创业）" -}}
  {{- $lblInterest = "意向项目" -}}
  {{- $btnText = "申请免费咨询" -}}
  {{- $disclaimer = "提交申请即视为同意收集并使用个人信息用于咨询目的。" -}}
  {{- $boribapText = "大麦饭定食" -}}
  {{- $dakText = "一只鸡" -}}
  {{- $academyText = "秘方传授" -}}
  {{- $sauceText = "酱料供应" -}}
  {{- $pochaText = "百世大排档" -}}
{{- else if eq $lang "ja" -}}
  {{- $title = "本物の美味しさで<br>証明します" -}}
  {{- $lead = "無料のソースサンプルと創業ガイドをお送りします。お申し込み後にお知らせをお送りしますが、しつこい営業電話は一切いたしません。" -}}
  {{- $lblFlagship = "本店" -}}
  {{- $lblHours = "営業時間" -}}
  {{- $lblContact = "お問い合わせ" -}}
  {{- $lblName = "名前" -}}
  {{- $plName = "お名前を入力してください" -}}
  {{- $lblPhone = "連絡先" -}}
  {{- $lblStore = "現在の店舗運営状況" -}}
  {{- $optYes = "あり" -}}
  {{- $optNo = "なし（新規開業）" -}}
  {{- $lblInterest = "関心分野" -}}
  {{- $btnText = "無料相談を申し込む" -}}
  {{- $disclaimer = "お申し込みにより、相談目的での個人情報の収集・利用に同意したものとみなされます。" -}}
  {{- $boribapText = "麦飯山菜定食" -}}
  {{- $dakText = "タッカンマリ" -}}
  {{- $academyText = "レシピ伝授" -}}
  {{- $sauceText = "ソース供給" -}}
  {{- $pochaText = "屋台ポチャ" -}}
{{- else if eq $lang "ru" -}}
  {{- $title = "Вкус, проверенный<br>годами" -}}
  {{- $lead = "Мы отправим вам бесплатные образцы соусов и руководство по франшизе. Никаких нежелательных звонков с предложениями." -}}
  {{- $lblFlagship = "Флагман" -}}
  {{- $lblHours = "Часы работы" -}}
  {{- $lblContact = "Контакты" -}}
  {{- $lblName = "Имя" -}}
  {{- $plName = "Введите ваше имя" -}}
  {{- $lblPhone = "Телефон" -}}
  {{- $lblStore = "Наличие ресторана" -}}
  {{- $optYes = "Есть" -}}
  {{- $optNo = "Нет (Новый бизнес)" -}}
  {{- $lblInterest = "Интересующее направление" -}}
  {{- $btnText = "Запросить консультацию" -}}
  {{- $disclaimer = "Отправляя заявку, вы соглашаетесь на сбор и использование личных данных для консультации." -}}
  {{- $boribapText = "Корейская кухня" -}}
  {{- $dakText = "Дакханмари" -}}
  {{- $academyText = "Обучение" -}}
  {{- $sauceText = "Поставки соусов" -}}
  {{- $pochaText = "Ночная Поча" -}}
{{- end -}}

<section id="apply" class="section alt">
  <div class="container grid grid-2" style="align-items:start">
    <div style="display:flex;flex-direction:column;gap:18px;max-width:480px">
      <span class="eyebrow">FREE CONSULTATION</span>
      <h2 class="h2">{{ $title | safeHTML }}</h2>
      <p class="lead">{{ $lead }}</p>
      <div style="display:flex;flex-direction:column;gap:10px;font-size:14px;color:var(--muted);border-top:1px solid var(--border);padding-top:20px;max-width:340px">
        <div style="display:flex;gap:14px"><span style="flex:0 0 68px;color:var(--dim);font-size:12.5px">{{ $lblFlagship }}</span><span>{{ $ctx.Site.Params.address }}</span></div>
        <div style="display:flex;gap:14px"><span style="flex:0 0 68px;color:var(--dim);font-size:12.5px">{{ $lblHours }}</span><span>{{ $ctx.Site.Params.hours }}</span></div>
        <div style="display:flex;gap:14px"><span style="flex:0 0 68px;color:var(--dim);font-size:12.5px">{{ $lblContact }}</span><a href="{{ $ctx.Site.Params.phoneHref | safeURL }}" style="border-bottom:1px solid rgba(245,241,232,.28)">{{ $ctx.Site.Params.phone }}</a></div>
      </div>
    </div>

    <form action="https://formsubmit.co/{{ $ctx.Site.Params.contactFormEmail }}" method="POST" style="border:1px solid var(--border);background:rgba(245,241,232,.05);padding:clamp(26px,3vw,40px);display:flex;flex-direction:column;gap:18px">
      <input type="hidden" name="_subject" value="[백세푸드 홈페이지] 창업 상담 신청">
      <input type="hidden" name="_template" value="table">
      <input type="hidden" name="_captcha" value="false">
      <label class="form-field"><span>{{ $lblName }}</span><input type="text" name="이름" placeholder="{{ $plName }}" required></label>
      <label class="form-field"><span>{{ $lblPhone }}</span><input type="tel" name="연락처" placeholder="010-0000-0000" required></label>
      <div class="form-field">
        <span>{{ $lblStore }}</span>
        <div class="chip-row">
          <label class="chip"><input type="radio" name="현재매장" value="있음"> {{ $optYes }}</label>
          <label class="chip"><input type="radio" name="현재매장" value="없음(신규창업)" checked> {{ $optNo }}</label>
        </div>
      </div>
      <div class="form-field">
        <span>{{ $lblInterest }}</span>
        <div class="chip-row">
          <label class="chip"><input type="radio" name="관심분야" value="보리밥 산채정식" {{ if eq $defaultInterest "보리밥 산채정식" }}checked{{ end }}> {{ $boribapText }}</label>
          <label class="chip"><input type="radio" name="관심분야" value="닭한마리" {{ if eq $defaultInterest "닭한마리" }}checked{{ end }}> {{ $dakText }}</label>
          <label class="chip"><input type="radio" name="관심분야" value="전수교육" {{ if eq $defaultInterest "전수교육" }}checked{{ end }}> {{ $academyText }}</label>
          <label class="chip"><input type="radio" name="관심분야" value="닭한마리 소스" {{ if eq $defaultInterest "닭한마리 소스" }}checked{{ end }}> {{ $sauceText }}</label>
          <label class="chip"><input type="radio" name="관심분야" value="백세포차" {{ if eq $defaultInterest "백세포차" }}checked{{ end }}> {{ $pochaText }}</label>
        </div>
      </div>
      <button type="submit" class="btn btn-primary" style="justify-content:center;margin-top:6px">{{ $btnText }}</button>
      <span style="font-size:11.5px;color:var(--dimmer);line-height:1.7">{{ $disclaimer }}</span>
    </form>
  </div>
</section>
'''

with open(path, 'w', encoding='utf-8') as f:
    f.write(translations)

print('Updated apply-form.html')
