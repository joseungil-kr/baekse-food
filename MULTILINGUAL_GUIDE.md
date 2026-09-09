# 백세푸드 다국어 사이트 운영 및 콘텐츠 작성 지침

본 문서는 백세푸드 공식 사이트(baeksefood.com)의 다국어(한국어, 영어, 중국어, 일본어, 러시아어) 사이트 운영 및 신규 콘텐츠 발행에 관한 **필수 작업 표준 지침**입니다.

---

## ⚠️ [핵심 원칙] 블로그 및 페이지 작성 시 다국어 페이지 동시 개설 의무

앞으로 `content/` 및 `content/blog/`에 새로운 글이나 페이지를 작성·발행할 때는 **반드시 한국어 원문과 함께 4개 외국어 번역본을 동시에 개설**해야 합니다.

### 1. 파일명 표준 규격 (Hugo Multilingual)
동일한 디렉토리 내에 언어 코드를 접미사로 붙여 파일을 생성합니다:

| 언어 | 언어 코드 | 파일명 형식 예시 (메인 페이지) | 파일명 형식 예시 (블로그 글) |
|------|-----------|-------------------------------|-----------------------------|
| **한국어** (기본) | `ko` | `content/academy.md` | `content/blog/post-name.md` |
| **영어** | `en` | `content/academy.en.md` | `content/blog/post-name.en.md` |
| **중국어** | `zh` | `content/academy.zh.md` | `content/blog/post-name.zh.md` |
| **일본어** | `ja` | `content/academy.ja.md` | `content/blog/post-name.ja.md` |
| **러시아어** | `ru` | `content/academy.ru.md` | `content/blog/post-name.ru.md` |

---

## 2. Front Matter 및 본문 작성 규칙

각 언어별 파일은 해당 국가의 외식·비즈니스 문화에 맞춘 자연스러운 표현으로 작성합니다:

- **title / seoTitle**: 해당 언어의 현지 검색 키워드 포함
- **description**: 해당 언어 메타 디스크립션 (120자 내외)
- **heroEyebrow / heroTitle / heroLead**: 해당 언어로 번역
- **faq**: 질문(`q`)과 답변(`a`) 모두 해당 언어로 번역
- **본문**: HTML 시맨틱 구조(`<section>`, `<h2>`, `<p>`, `<table>` 등)를 동일하게 유지하며 본문 텍스트 번역
- **이미지 경로**: 기존의 최적화된 이미지 경로(`/img/...`, `/assets/...`)를 그대로 공유 사용

---

## 3. 신규 콘텐츠 발행 워크플로우

1. **한국어 원문 작성**: `content/blog/[파일명].md` 작성
2. **4개 언어 번역본 동시 생성**: 
   - `content/blog/[파일명].en.md`
   - `content/blog/[파일명].zh.md`
   - `content/blog/[파일명].ja.md`
   - `content/blog/[파일명].ru.md`
3. **정적 빌드 검증**:
   ```powershell
   hugo --minify
   ```
4. **IndexNow 검색엔진 제출 (국내 및 글로벌)**:
   ```powershell
   powershell -ExecutionPolicy Bypass -File .\scripts\submit-indexnow.ps1
   ```
5. **Git 커밋 및 배포**:
   ```bash
   git add -A
   git commit -m "feat: [글 제목] 신규 콘텐츠 및 5개 국어 번역본 발행"
   git push
   ```

---

## 4. 기존 콘텐츠 수정 워크플로우

한국어 페이지를 수정할 때는 **모든 언어 버전을 동기화**해야 합니다:

1. **한국어 원문 수정**: `content/blog/[파일명].md` 또는 `content/[페이지명].md` 수정
2. **4개 언어 버전 동기화 수정**:
   - 구조, 이미지 경로, 메타데이터는 동일하게 유지
   - 수정 내용을 각 언어별로 자연스럽게 반영
   - `content/blog/[파일명].en.md`
   - `content/blog/[파일명].zh.md`
   - `content/blog/[파일명].ja.md`
   - `content/blog/[파일명].ru.md`
3. **정적 빌드 검증**:
   ```powershell
   hugo --minify
   ```
4. **Git 커밋 및 배포**:
   ```bash
   git add -A
   git commit -m "fix/style/docs: [설명] 콘텐츠 수정 및 5개 국어 동기화"
   git push
   ```

⚠️ **주의**: 한국어만 수정하고 외국어를 동기화하지 않으면 다국어 사이트의 정보 일관성이 깨집니다.

---

## 5. 다국어 URL 매핑 구조

- 한국어: `https://baeksefood.com/blog/[파일명]/`
- 영어: `https://baeksefood.com/en/blog/[파일명]/`
- 중국어: `https://baeksefood.com/zh/blog/[파일명]/`
- 일본어: `https://baeksefood.com/ja/blog/[파일명]/`
- 러시아어: `https://baeksefood.com/ru/blog/[파일명]/`

모든 페이지의 `<head>`에는 `hreflang` 태그가 자동 삽입되어 구글, 바이두, 얀덱스 등 글로벌 검색엔진에 정확하게 상호 링크됩니다.
