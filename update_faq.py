import os

path = r'c:\project\baekse-food\layouts\partials\faq.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

translations = '''{{ if .Params.faq }}
{{- $lang := .Lang -}}
{{- $faqTitle := "자주 묻는 질문" -}}
{{- $faqLead := "답을 찾지 못하셨다면 전화로 바로 물어보세요." -}}

{{- if eq $lang "en" -}}
  {{- $faqTitle = "Frequently Asked Questions" -}}
  {{- $faqLead = "Couldn't find the answer? Call us directly." -}}
{{- else if eq $lang "zh" -}}
  {{- $faqTitle = "常见问题解答" -}}
  {{- $faqLead = "没找到答案？欢迎直接致电咨询。" -}}
{{- else if eq $lang "ja" -}}
  {{- $faqTitle = "よくあるご質問" -}}
  {{- $faqLead = "解決しない場合は、直接お電話でお問い合わせください。" -}}
{{- else if eq $lang "ru" -}}
  {{- $faqTitle = "Часто задаваемые вопросы" -}}
  {{- $faqLead = "Не нашли ответ? Позвоните нам напрямую." -}}
{{- end -}}

<div class="section">
  <div class="container grid grid-2" style="align-items:start">
    <div style="display:flex;flex-direction:column;gap:18px">
      <span class="eyebrow">FAQ</span>
      <h2 class="h2">{{ $faqTitle }}</h2>
      <p class="lead" style="max-width:420px">{{ $faqLead }}</p>
      <a href="{{ .Site.Params.phoneHref | safeURL }}" class="btn btn-outline" style="align-self:flex-start">{{ .Site.Params.phone }}</a>
    </div>'''

content = content.replace('''{{ if .Params.faq }}
<div class="section">
  <div class="container grid grid-2" style="align-items:start">
    <div style="display:flex;flex-direction:column;gap:18px">
      <span class="eyebrow">FAQ</span>
      <h2 class="h2">자주 묻는 질문</h2>
      <p class="lead" style="max-width:420px">답을 찾지 못하셨다면 전화로 바로 물어보세요.</p>
      <a href="{{ .Site.Params.phoneHref }}" class="btn btn-outline" style="align-self:flex-start">{{ .Site.Params.phone }}</a>
    </div>''', translations)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated faq.html')
