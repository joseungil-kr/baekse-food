# 🔍 [적대적 검수 리포트] 백세푸드 (baekse-food)

## 1. 개요 및 아키텍처
- **기술 스택**: Hugo, 다국어 (한국어, 영어, 중국어, 일본어, 러시아어 5개 국어)
- **도메인**: `https://baeksefood.com/`
- **주요 기능**: 닭한마리, 보리밥 산채정식, 백세포차 가맹 및 전수창업 홍보

---

## 2. 적대적 관점 SEO & 다국어 태그 치명적 결함 (Critical)

### 🚨 결함 1: 다국어 `hreflang="x-default"` 자기 참조 모순
- **위치**: `layouts/partials/seo.html` 라인 10~13
- **코드**:
  ```html
  {{ range .AllTranslations }}
  <link rel="alternate" hreflang="{{ .Language.Lang }}" href="{{ .Permalink }}">
  {{ end }}
  <link rel="alternate" hreflang="x-default" href="{{ .Permalink }}">
  ```
- **문제점**:
  `x-default`는 사용자의 언어/지역이 일치하지 않을 때 보내줄 기본 언어 페이지(보통 한국어 메인 `https://baeksefood.com/`)를 하나로 고정해야 합니다.
  현재 코드는 영어 페이지에서는 영어 URL이 x-default가 되고, 러시아어 페이지에서는 러시아어 URL이 x-default가 되는 **상호 모순된 다국어 신호**를 구글 봇에게 전송합니다.
  결과적으로 구글 검색엔진이 다국어 인덱싱을 신뢰하지 못해 전 세계 검색 결과 노출 순위가 강등됩니다.
- **조치 방안**:
  ```html
  {{ with .Sites.Default }}
  <link rel="alternate" hreflang="x-default" href="{{ $.Permalink }}">
  {{ end }}
  <!-- 또는 기본 한국어 버전의 영구 주소로 고정 -->
  ```

---

## 3. 보안 & 개인정보 노출 취약점 (High / Medium)

### ⚠️ 취약점 1: 대표자 이메일 소스코드 평문 노출로 인한 스팸 수집
- **위치**: `hugo.toml` 라인 16: `contactFormEmail = "joseungil@Gmail.com"`
- **문제점**: 대문자가 섞인 개인 이메일 주소가 정적 HTML에 그대로 노출되어 자동화된 이메일 하베스터(Scraper)에게 크롤링되어 피싱, 스팸 공격 대상이 됩니다.
- **조치 방안**: 이메일을 Cloudflare Email Obfuscation으로 암호화하거나, 백엔드 폼 API(Turnstile 보호 적용)로 전환하십시오.

### ⚠️ 취약점 2: 마크다운 렌더러 `unsafe = true`
- **위치**: `hugo.toml` 라인 80: `unsafe = true`
- **문제점**: 마크다운 파일 내 원시 HTML 태그 삽입을 허용하고 있습니다. 다국어 번역본이나 외부 작성 콘텐츠가 유입될 때 악성 스크립트(XSS) 주입 위험이 있습니다.

---

## 4. 리소스 및 폰트 로딩 성능 (Performance)
1. **Google Web Fonts 렌더링 차단**:
   - `Cormorant Garamond` 및 `Gowun Batang` 구글 폰트를 `@import` 또는 동기 `<link>`로 로드하여 First Contentful Paint(FCP) 지연 유발.
   - 폰트 파일 자체를 `static/fonts/`에 woff2 형식으로 자체 호스팅(Self-hosting)하여 DNS 조회 및 외부 CDN 종속성을 제거할 것을 권장합니다.
2. **Pretendard CDN 종속성**:
   - `cdn.jsdelivr.net`에 의존하고 있어, jsdelivr 장애 시 국내 접속자의 텍스트 폰트가 깨질 수 있습니다.

---

## 5. 긴급 보완 권고사항 체크리스트
- [ ] `seo.html` 내 `hreflang="x-default"` 다국어 모순 수정
- [ ] 개인 이메일 평문 노출 제거 및 문의 폼 전환
- [ ] 웹폰트(고운바탕, 프리텐다드) woff2 로컬 자체 호스팅 전환
- [ ] `unsafe = true` 사용 시 콘텐츠 입력 검증 체계 확립
