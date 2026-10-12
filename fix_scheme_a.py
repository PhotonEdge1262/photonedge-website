import os
import re

BASE = '/tmp/v162-work'

# Scheme A: the correct light blue card for blog/news/knowledge/application-notes
SCHEME_A_CORRECT = '''<!-- Upload Your Drawing CTA -->
<div style="background:#f0f9ff;border:1px solid #bfdbfe;border-radius:12px;padding:32px;margin:40px 0;text-align:center;">
  <h3 style="font-size:20px;font-weight:700;color:#1e293b;margin-bottom:8px;">Need Help Specifying Your Requirements?</h3>
  <p style="color:#475569;font-size:14px;line-height:1.7;margin-bottom:16px;">Upload your drawing or describe your application. Our engineering team will review and recommend the right solution.</p>
  <a href="/contact.html" style="display:inline-block;padding:12px 28px;background:#2563eb;color:white;font-weight:600;border-radius:8px;text-decoration:none;font-size:14px;">Upload Your Drawing</a>
</div>'''

# Scheme B: the correct gradient for materials/coatings
SCHEME_B_CORRECT = '''<!-- Upload Your Drawing CTA -->
<section style="padding:60px 0;background:linear-gradient(135deg,#1e40af,#3b82f6);text-align:center;">
  <div style="max-width:800px;margin:0 auto;padding:0 24px;">
    <h2 style="font-size:28px;font-weight:700;color:white;margin-bottom:12px;">Need This Material for Your Project?</h2>
    <p style="font-size:16px;color:rgba(255,255,255,0.9);margin-bottom:24px;">Upload your drawing with material specifications. We'll review and respond within 24 business hours.</p>
    <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;">
      <a href="/contact.html" style="display:inline-block;padding:14px 32px;background:white;color:#1e40af;font-weight:600;border-radius:8px;text-decoration:none;font-size:15px;">Upload Your Drawing</a>
      <a href="/contact.html" style="display:inline-block;padding:14px 32px;background:transparent;color:white;font-weight:600;border-radius:8px;text-decoration:none;font-size:15px;border:2px solid rgba(255,255,255,0.5);">Request a Quote</a>
    </div>
  </div>
</section>'''

# What was incorrectly applied (Scheme C) to blog/news/knowledge/app-notes and materials/coatings
SCHEME_C_WRONG = '''<!-- Upload Your Drawing CTA -->
<section style="padding:60px 0;background:linear-gradient(135deg,#1e40af,#3b82f6);text-align:center;">
  <div style="max-width:800px;margin:0 auto;padding:0 24px;">
    <h2 style="font-size:28px;font-weight:700;color:white;margin-bottom:12px;">Have an Optical Project in Mind?</h2>
    <p style="font-size:16px;color:rgba(255,255,255,0.9);margin-bottom:24px;">Upload your drawing or describe your requirements. Our engineering team will review and respond within 24 business hours.</p>
    <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;">
      <a href="/contact.html" style="display:inline-block;padding:14px 32px;background:white;color:#1e40af;font-weight:600;border-radius:8px;text-decoration:none;font-size:15px;">Upload Your Drawing</a>
      <a href="/contact.html" style="display:inline-block;padding:14px 32px;background:transparent;color:white;font-weight:600;border-radius:8px;text-decoration:none;font-size:15px;border:2px solid rgba(255,255,255,0.5);">Request a Quote</a>
    </div>
  </div>
</section>'''

def correct_scheme(filepath):
    rel = filepath.replace(BASE + '/', '').replace('./', '')
    if rel.startswith('blog/') or rel.startswith('news/') or rel.startswith('application-notes/') or rel.startswith('knowledge-center/'):
        return 'A'
    elif rel.startswith('materials/') or rel.startswith('coatings/'):
        return 'B'
    return 'C'

fixed_a = 0
fixed_b = 0

# Fix blog/news/knowledge-center/application-notes: replace Scheme C with Scheme A
import subprocess
for prefix in ['blog', 'news', 'application-notes', 'knowledge-center']:
    result = subprocess.run(
        ['find', './' + prefix, '-name', '*.html'],
        capture_output=True, text=True, cwd=BASE
    )
    for f in result.stdout.strip().split('\n'):
        if not f: continue
        full_path = os.path.join(BASE, f)
        with open(full_path, 'r', encoding='utf-8') as fh:
            content = fh.read()
        if SCHEME_C_WRONG in content:
            content = content.replace(SCHEME_C_WRONG, SCHEME_A_CORRECT)
            with open(full_path, 'w', encoding='utf-8') as fh:
                fh.write(content)
            fixed_a += 1

# Fix materials/coatings: replace Scheme C with Scheme B
for prefix in ['materials', 'coatings']:
    result = subprocess.run(
        ['find', './' + prefix, '-name', '*.html'],
        capture_output=True, text=True, cwd=BASE
    )
    for f in result.stdout.strip().split('\n'):
        if not f: continue
        full_path = os.path.join(BASE, f)
        with open(full_path, 'r', encoding='utf-8') as fh:
            content = fh.read()
        if SCHEME_C_WRONG in content:
            content = content.replace(SCHEME_C_WRONG, SCHEME_B_CORRECT)
            with open(full_path, 'w', encoding='utf-8') as fh:
                fh.write(content)
            fixed_b += 1

print(f"Fixed Scheme A (blog/news/knowledge/app-notes): {fixed_a} pages")
print(f"Fixed Scheme B (materials/coatings): {fixed_b} pages")

# Verify
print("\nVerification:")
for prefix in ['blog', 'news', 'application-notes', 'knowledge-center']:
    result = subprocess.run(
        ['grep', '-rl', 'Need Help Specifying Your Requirements', './' + prefix],
        capture_output=True, text=True, cwd=BASE
    )
    cnt = len([f for f in result.stdout.strip().split('\n') if f])
    print(f"  {prefix}: {cnt} pages with Scheme A")

for prefix in ['materials', 'coatings']:
    result = subprocess.run(
        ['grep', '-rl', 'Need This Material for Your Project', './' + prefix],
        capture_output=True, text=True, cwd=BASE
    )
    cnt = len([f for f in result.stdout.strip().split('\n') if f])
    print(f"  {prefix}: {cnt} pages with Scheme B")

# Check if any blog/news pages still have wrong Scheme C
result = subprocess.run(
    ['grep', '-rl', 'Have an Optical Project in Mind', '.'],
    capture_output=True, text=True, cwd=BASE
)
remaining_c = [f for f in result.stdout.strip().split('\n') if f and './zh/' not in f]
print(f"\n  Remaining Scheme C pages: {len(remaining_c)}")
for f in remaining_c:
    print(f"    {f}")
