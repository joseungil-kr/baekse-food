# 백세푸드 IndexNow 자동 색인 가이드

본 문서는 새 글 또는 수정된 웹페이지가 네이버, Bing, Yandex 등 검색엔진에 즉시 알려져 빠르게 크롤링·상위 노출되도록 하는 **IndexNow 프로토콜 작업 지침**입니다.

---

## 1. IndexNow 개요 및 세팅 정보

- **도메인 (Host)**: `baeksefood.com`
- **인증 API 키**: `baekse9f82d44c80b572a1e038f87e21`
- **키 검증 파일**: [`static/baekse9f82d44c80b572a1e038f87e21.txt`](file:///c:/project/baekse-food/static/baekse9f82d44c80b572a1e038f87e21.txt)
  - 웹 접속 URL: `https://baeksefood.com/baekse9f82d44c80b572a1e038f87e21.txt`
  - Hugo 빌드 시 `public/` 루트로 복사되어 검색엔진이 자동으로 소유권을 인증합니다.
- **제출 엔드포인트**: `https://api.indexnow.org/indexnow`

---

## 2. 새 글 작성 시 작업 절차

1. **콘텐츠 파일 작성**
   - `content/blog/새파일.md` 생성 및 작성
2. **사이트 빌드**
   ```bash
   hugo --minify
   ```
3. **IndexNow 전송 실행 (선택 1 또는 2)**
   - **방법 A: 사이트맵 전체 일괄 전송 (추천)**
     ```powershell
     powershell -ExecutionPolicy Bypass -File .\scripts\submit-indexnow.ps1
     ```
     `public/sitemap.xml` 내의 전체 40여 개 페이지를 한 번에 검색엔진에 리프레시 요청합니다.
   - **방법 B: 특정 단일 URL만 전송**
     ```powershell
     powershell -ExecutionPolicy Bypass -File .\scripts\submit-indexnow.ps1 -Url "https://baeksefood.com/blog/새파일/"
     ```
4. **Git 커밋 및 배포**
   ```bash
   git add -A
   git commit -m "feat: 새 블로그 글 추가 및 IndexNow 제출"
   git push
   ```

---

## 3. 작동 원리 및 주의사항

- **연동 검색엔진**: IndexNow API로 전송하면 참여 검색엔진(네이버 검색엔진 크롤러, Bing, Yandex 등)에 자동으로 공유 전파됩니다.
- **전송 상태 코드**:
  - `HTTP 200`: 정상 전송 및 처리 완료
  - `HTTP 202`: 접수 완료 (크롤러 대기열에 정상 추가됨)
- **키 파일 삭제 주의**: `static/baekse9f82d44c80b572a1e038f87e21.txt` 파일이 삭제되면 인증이 실패하므로 항상 보존해야 합니다.
