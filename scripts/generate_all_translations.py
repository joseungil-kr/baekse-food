import os
import sys
import re
from multilingual_data import POSTS_META, GLOSSARY

BLOG_DIR = r"c:\project\baekse-food\content\blog"

SECTION_TITLES = {
    "en": {
        "eyebrow_1": "01 / CORE FOUNDATIONS",
        "eyebrow_2": "02 / OPERATIONAL SECRETS",
        "eyebrow_3": "03 / SYSTEM & PROFITABILITY",
        "eyebrow_4": "04 / STORE INFORMATION",
        "step_1": "STEP 01",
        "step_2": "STEP 02",
        "step_3": "STEP 03",
        "faq_title": "Frequently Asked Questions",
        "inquiry_box_title": "Baekse Food Headquarter & Store Information",
        "cta_label": "Apply for Consultation"
    },
    "zh": {
        "eyebrow_1": "01 / 核心基础与原理",
        "eyebrow_2": "02 / 实战运营秘籍",
        "eyebrow_3": "03 / 系统化高收益保障",
        "eyebrow_4": "04 / 门店及合作信息",
        "step_1": "步骤 01",
        "step_2": "步骤 02",
        "step_3": "步骤 03",
        "faq_title": "常见问题解答 (FAQ)",
        "inquiry_box_title": "百世食品总部及总店信息",
        "cta_label": "申请加盟咨询"
    },
    "ja": {
        "eyebrow_1": "01 / 核心となる基本原理",
        "eyebrow_2": "02 / 実戦オペレーションの極意",
        "eyebrow_3": "03 / システム化による高収益モデル",
        "eyebrow_4": "04 / 店舗および仕入れ案内",
        "step_1": "STEP 01",
        "step_2": "STEP 02",
        "step_3": "STEP 03",
        "faq_title": "よくあるご質問 (FAQ)",
        "inquiry_box_title": "百世フード本部・本店のご案内",
        "cta_label": "加盟・仕入れ相談"
    },
    "ru": {
        "eyebrow_1": "01 / ОСНОВНЫЕ ПРИНЦИПЫ",
        "eyebrow_2": "02 / СЕКРЕТЫ ЭКСПЛУАТАЦИИ",
        "eyebrow_3": "03 / СИСТЕМНОСТЬ И ДОХОДНОСТЬ",
        "eyebrow_4": "04 / ИНФОРМАЦИЯ О РЕСТОРАНЕ",
        "step_1": "ШАГ 01",
        "step_2": "ШАГ 02",
        "step_3": "ШАГ 03",
        "faq_title": "Часто задаваемые вопросы (FAQ)",
        "inquiry_box_title": "Флагманский ресторан и фабрика-кухня Baekse Food",
        "cta_label": "Записаться на консультацию"
    }
}

def translate_content(text, lang, slug):
    meta = POSTS_META.get(slug, {}).get(lang)
    if not meta:
        return text

    title, seo_title, desc = meta
    g = GLOSSARY[lang]
    st = SECTION_TITLES[lang]

    # 링크 다국어 치환
    text = re.sub(r'href="/academy/"', f'href="/{lang}/academy/"', text)
    text = re.sub(r'href="/boribap/"', f'href="/{lang}/boribap/"', text)
    text = re.sub(r'href="/sanchae/"', f'href="/{lang}/sanchae/"', text)
    text = re.sub(r'href="/sauce/"', f'href="/{lang}/sauce/"', text)
    text = re.sub(r'href="/blog/"', f'href="/{lang}/blog/"', text)
    text = re.sub(r'href="/"', f'href="/{lang}/"', text)

    return text

def process_file(filename):
    if not filename.endswith(".md"):
        return
    if any(filename.endswith(f".{l}.md") for l in ["en", "zh", "ja", "ru"]):
        return
    if filename == "_index.md":
        return

    slug = filename[:-3]
    filepath = os.path.join(BLOG_DIR, filename)

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Front matter 분리
    parts = content.split("---", 2)
    if len(parts) < 3:
        return

    front_raw = parts[1]
    body_raw = parts[2]

    # heroImage, heroImageAlt, interest 추출
    img_match = re.search(r'heroImage:\s*"([^"]+)"', front_raw)
    hero_image = img_match.group(1) if img_match else "/img/bs-menu-3.webp"

    interest_match = re.search(r'interest:\s*"([^"]+)"', front_raw)
    interest = interest_match.group(1) if interest_match else "닭한마리"

    # 4개 언어 생성
    for lang in ["en", "zh", "ja", "ru"]:
        meta = POSTS_META.get(slug, {}).get(lang)
        if not meta:
            continue

        title, seo_title, desc = meta
        g = GLOSSARY[lang]
        st = SECTION_TITLES[lang]

        target_file = os.path.join(BLOG_DIR, f"{slug}.{lang}.md")

        # 본문 링크 변환
        trans_body = body_raw
        trans_body = re.sub(r'href="/academy/"', f'href="/{lang}/academy/"', trans_body)
        trans_body = re.sub(r'href="/boribap/"', f'href="/{lang}/boribap/"', trans_body)
        trans_body = re.sub(r'href="/sanchae/"', f'href="/{lang}/sanchae/"', trans_body)
        trans_body = re.sub(r'href="/sauce/"', f'href="/{lang}/sauce/"', trans_body)
        trans_body = re.sub(r'href="/blog/"', f'href="/{lang}/blog/"', trans_body)
        trans_body = re.sub(r'href="/"', f'href="/{lang}/"', trans_body)

        # 공통 매장 정보 박스 텍스트 현지화
        store_box = f"""
<div style="border:1px solid rgba(199,84,29,.35);background:linear-gradient(120deg,rgba(199,84,29,.14),rgba(245,241,232,.03));padding:clamp(26px,4vw,40px);margin-top:36px;display:flex;flex-direction:column;gap:16px">
  <h3 class="h3" style="margin:0">{g['store_info_title']}</h3>
  <p style="margin:0;color:var(--muted);line-height:1.8">
    <strong>Address:</strong> {g['address']}<br>
    <strong>Hours:</strong> {g['hours']}<br>
    <strong>Inquiries:</strong> {g['phone']}
  </p>
</div>
"""
        # 마지막 섹션의 매장 정보 안내 박스 교체
        if 'id="store"' in trans_body or '상록구 석호로 101' in trans_body:
            trans_body = re.sub(r'<div style="border:1px solid rgba\(199,84,29,\.35\)[^>]*>[\s\S]*?</div>\s*</section>', f'{store_box}\n</section>', trans_body)

        new_content = f"""---
title: "{title}"
seoTitle: "{seo_title}"
description: "{desc}"
heroEyebrow: "baekse food global"
heroTitle: "{title}"
heroLead: "{desc}"
heroImage: "{hero_image}"
heroImageAlt: "{title}"
ctaPrimary:
  label: "{g['btn_apply']}"
  href: "#apply"
ctaSecondary:
  label: "{g['btn_call']}"
  href: "tel:{g['phone']}"
interest: "{interest}"
---
{trans_body}
"""
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(new_content)

    print(f"Generated multilingual files for: {slug}")

def main():
    count = 0
    for fname in os.listdir(BLOG_DIR):
        if fname.endswith(".md") and not any(fname.endswith(f".{l}.md") for l in ["en", "zh", "ja", "ru"]) and fname != "_index.md":
            process_file(fname)
            count += 1
    print(f"Total processed original posts: {count}")

if __name__ == "__main__":
    main()
