import os

path = r'c:\project\baekse-food\layouts\partials\sticky-cta.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

translations = '''{{- $lang := .Lang -}}
{{- $callText := "전화 상담" -}}
{{- $applyText := "무료 상담 신청" -}}

{{- if eq $lang "en" -}}
  {{- $callText = "Call Us" -}}
  {{- $applyText = "Free Consultation" -}}
{{- else if eq $lang "zh" -}}
  {{- $callText = "电话咨询" -}}
  {{- $applyText = "免费咨询" -}}
{{- else if eq $lang "ja" -}}
  {{- $callText = "電話相談" -}}
  {{- $applyText = "無料相談" -}}
{{- else if eq $lang "ru" -}}
  {{- $callText = "Позвонить" -}}
  {{- $applyText = "Консультация" -}}
{{- end -}}

<div class="sticky-cta">
  <a href="{{ .Site.Params.phoneHref | safeURL }}" class="call">{{ $callText }}</a>
  <a href="#apply" class="apply">{{ $applyText }}</a>
</div>'''

with open(path, 'w', encoding='utf-8') as f:
    f.write(translations)

print('Updated sticky-cta.html')
