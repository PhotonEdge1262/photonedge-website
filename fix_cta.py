import os
import re

BASE = '/tmp/v162-work'

# ===== CTA Templates =====

# Scheme A: Blog/News/Knowledge/Article pages
SCHEME_A = '''
<!-- Upload Your Drawing CTA -->
<div style="background:#f0f9ff;border:1px solid #bfdbfe;border-radius:12px;padding:32px;margin:40px 0;text-align:center;">
  <h3 style="font-size:20px;font-weight:700;color:#1e293b;margin-bottom:8px;">Need Help Specifying Your Requirements?</h3>
  <p style="color:#475569;font-size:14px;line-height:1.7;margin-bottom:16px;">Upload your drawing or describe your application. Our engineering team will review and recommend the right solution.</p>
  <a href="/contact.html" style="display:inline-block;padding:12px 28px;background:#2563eb;color:white;font-weight:600;border-radius:8px;text-decoration:none;font-size:14px;">Upload Your Drawing</a>
</div>
'''

# Scheme B: Materials/Coatings pages
SCHEME_B = '''
<!-- Upload Your Drawing CTA -->
<section style="padding:60px 0;background:linear-gradient(135deg,#1e40af,#3b82f6);text-align:center;">
  <div style="max-width:800px;margin:0 auto;padding:0 24px;">
    <h2 style="font-size:28px;font-weight:700;color:white;margin-bottom:12px;">Need This Material for Your Project?</h2>
    <p style="font-size:16px;color:rgba(255,255,255,0.9);margin-bottom:24px;">Upload your drawing with material specifications. We'll review and respond within 24 business hours.</p>
    <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;">
      <a href="/contact.html" style="display:inline-block;padding:14px 32px;background:white;color:#1e40af;font-weight:600;border-radius:8px;text-decoration:none;font-size:15px;">Upload Your Drawing</a>
      <a href="/contact.html" style="display:inline-block;padding:14px 32px;background:transparent;color:white;font-weight:600;border-radius:8px;text-decoration:none;font-size:15px;border:2px solid rgba(255,255,255,0.5);">Request a Quote</a>
    </div>
  </div>
</section>
'''

# Scheme C: Other root pages (about, evidence, engineering, etc.)
SCHEME_C = '''
<!-- Upload Your Drawing CTA -->
<section style="padding:60px 0;background:linear-gradient(135deg,#1e40af,#3b82f6);text-align:center;">
  <div style="max-width:800px;margin:0 auto;padding:0 24px;">
    <h2 style="font-size:28px;font-weight:700;color:white;margin-bottom:12px;">Have an Optical Project in Mind?</h2>
    <p style="font-size:16px;color:rgba(255,255,255,0.9);margin-bottom:24px;">Upload your drawing or describe your requirements. Our engineering team will review and respond within 24 business hours.</p>
    <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;">
      <a href="/contact.html" style="display:inline-block;padding:14px 32px;background:white;color:#1e40af;font-weight:600;border-radius:8px;text-decoration:none;font-size:15px;">Upload Your Drawing</a>
      <a href="/contact.html" style="display:inline-block;padding:14px 32px;background:transparent;color:white;font-weight:600;border-radius:8px;text-decoration:none;font-size:15px;border:2px solid rgba(255,255,255,0.5);">Request a Quote</a>
    </div>
  </div>
</section>
'''

# Three-entry block for homepage
THREE_ENTRY_HOME = '''
<!-- ============ HOW CAN WE HELP YOU - THREE ENTRY POINTS ============ -->
<section style="padding:60px 0;background:#f8fafc;">
  <div style="max-width:1000px;margin:0 auto;padding:0 24px;text-align:center;">
    <h2 style="font-size:28px;font-weight:700;color:#1e293b;margin-bottom:8px;">How Can We Help You?</h2>
    <p style="color:#64748b;font-size:16px;margin-bottom:32px;">Choose the path that matches your current stage</p>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;text-align:left;">
      <div style="background:white;border:1px solid #e2e8f0;border-radius:12px;padding:24px;">
        <div style="font-size:32px;margin-bottom:12px;">&#128208;</div>
        <h3 style="font-size:18px;font-weight:700;color:#1e293b;margin-bottom:8px;">I Have a Drawing</h3>
        <p style="color:#64748b;font-size:14px;line-height:1.6;margin-bottom:16px;">Upload your drawing with specifications. Get a detailed quote within 24 business hours.</p>
        <a href="/contact.html" style="display:inline-block;padding:10px 20px;background:#2563eb;color:white;font-weight:600;border-radius:6px;text-decoration:none;font-size:14px;">Upload Your Drawing</a>
      </div>
      <div style="background:white;border:1px solid #e2e8f0;border-radius:12px;padding:24px;">
        <div style="font-size:32px;margin-bottom:12px;">&#128269;</div>
        <h3 style="font-size:18px;font-weight:700;color:#1e293b;margin-bottom:8px;">I Know the Product Type</h3>
        <p style="color:#64748b;font-size:14px;line-height:1.6;margin-bottom:16px;">Select product type and describe your requirements. Our team will review and suggest specifications.</p>
        <a href="/contact.html" style="display:inline-block;padding:10px 20px;background:white;color:#2563eb;font-weight:600;border-radius:6px;text-decoration:none;font-size:14px;border:2px solid #2563eb;">Request Engineering Review</a>
      </div>
      <div style="background:white;border:1px solid #e2e8f0;border-radius:12px;padding:24px;">
        <div style="font-size:32px;margin-bottom:12px;">&#128161;</div>
        <h3 style="font-size:18px;font-weight:700;color:#1e293b;margin-bottom:8px;">I'm Not Sure What I Need</h3>
        <p style="color:#64748b;font-size:14px;line-height:1.6;margin-bottom:16px;">Describe your system and technical challenge. Get material and component selection guidance.</p>
        <a href="/ai-optical-engineer.html" style="display:inline-block;padding:10px 20px;background:white;color:#2563eb;font-weight:600;border-radius:6px;text-decoration:none;font-size:14px;border:2px solid #2563eb;">Ask AI Optical Engineer</a>
      </div>
    </div>
  </div>
</section>
'''

# Three-entry block for custom-optics
THREE_ENTRY_CUSTOM = '''
<!-- Start Your Custom Project - Three Entry Points -->
<section style="padding:60px 0;background:#f8fafc;">
  <div style="max-width:1000px;margin:0 auto;padding:0 24px;text-align:center;">
    <h2 style="font-size:28px;font-weight:700;color:#1e293b;margin-bottom:8px;">Start Your Custom Project</h2>
    <p style="color:#64748b;font-size:16px;margin-bottom:32px;">Choose the path that matches your current stage</p>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;text-align:left;">
      <div style="background:white;border:1px solid #e2e8f0;border-radius:12px;padding:24px;">
        <div style="font-size:32px;margin-bottom:12px;">&#128208;</div>
        <h3 style="font-size:18px;font-weight:700;color:#1e293b;margin-bottom:8px;">I Have a Drawing</h3>
        <p style="color:#64748b;font-size:14px;line-height:1.6;margin-bottom:16px;">Upload your drawing with specifications. Get a detailed quote within 24 business hours.</p>
        <a href="/contact.html" style="display:inline-block;padding:10px 20px;background:#2563eb;color:white;font-weight:600;border-radius:6px;text-decoration:none;font-size:14px;">Upload Your Drawing</a>
      </div>
      <div style="background:white;border:1px solid #e2e8f0;border-radius:12px;padding:24px;">
        <div style="font-size:32px;margin-bottom:12px;">&#128269;</div>
        <h3 style="font-size:18px;font-weight:700;color:#1e293b;margin-bottom:8px;">I Know the Product Type</h3>
        <p style="color:#64748b;font-size:14px;line-height:1.6;margin-bottom:16px;">Select product type and describe your requirements. Our team will review and suggest specifications.</p>
        <a href="/contact.html" style="display:inline-block;padding:10px 20px;background:white;color:#2563eb;font-weight:600;border-radius:6px;text-decoration:none;font-size:14px;border:2px solid #2563eb;">Request Engineering Review</a>
      </div>
      <div style="background:white;border:1px solid #e2e8f0;border-radius:12px;padding:24px;">
        <div style="font-size:32px;margin-bottom:12px;">&#128161;</div>
        <h3 style="font-size:18px;font-weight:700;color:#1e293b;margin-bottom:8px;">I'm Not Sure What I Need</h3>
        <p style="color:#64748b;font-size:14px;line-height:1.6;margin-bottom:16px;">Describe your system and technical challenge. Get material and component selection guidance.</p>
        <a href="/ai-optical-engineer.html" style="display:inline-block;padding:10px 20px;background:white;color:#2563eb;font-weight:600;border-radius:6px;text-decoration:none;font-size:14px;border:2px solid #2563eb;">Ask AI Optical Engineer</a>
      </div>
    </div>
  </div>
</section>
'''

# Pages to skip (no marketing CTA appropriate)
SKIP_PAGES = {'404.html', 'cart.html', 'calculator.html'}

def categorize_page(filepath):
    """Determine which scheme to use based on path"""
    rel = filepath.replace(BASE + '/', '')
    if rel.startswith('blog/') or rel.startswith('news/') or rel.startswith('application-notes/') or rel.startswith('knowledge-center/'):
        return 'A'
    elif rel.startswith('materials/') or rel.startswith('coatings/'):
        return 'B'
    else:
        return 'C'

def insert_before_footer(content, cta_block):
    """Insert CTA block before <footer"""
    # Check if already has Upload Your Drawing
    if 'Upload Your Drawing' in content:
        return content, False
    
    # Find footer tag
    footer_match = re.search(r'\n(<footer)', content)
    if footer_match:
        pos = footer_match.start()
        new_content = content[:pos] + cta_block + '\n' + content[pos:]
        return new_content, True
    
    # Fallback: insert before </body>
    body_match = re.search(r'\n(</body>)', content)
    if body_match:
        pos = body_match.start()
        new_content = content[:pos] + cta_block + '\n' + content[pos:]
        return new_content, True
    
    return content, False

def process_file(filepath):
    """Process a single HTML file"""
    rel = filepath.replace(BASE + '/', '')
    
    if rel in SKIP_PAGES:
        return 'skipped', rel
    
    scheme = categorize_page(filepath)
    if scheme == 'A':
        cta = SCHEME_A
    elif scheme == 'B':
        cta = SCHEME_B
    else:
        cta = SCHEME_C
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content, modified = insert_before_footer(content, cta)
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return 'modified', rel
    else:
        return 'failed', rel

def process_index():
    """Add three-entry block to index.html"""
    filepath = os.path.join(BASE, 'index.html')
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has the three-entry block
    if 'How Can We Help You?' in content:
        print("  index.html: three-entry block already exists")
        return False
    
    # Insert before SECTION 4: CORE PRODUCT CATEGORIES
    marker = '<!-- ============ SECTION 4: CORE PRODUCT CATEGORIES ============ -->'
    if marker in content:
        new_content = content.replace(marker, THREE_ENTRY_HOME + '\n' + marker)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("  index.html: three-entry block added before Product Categories")
        return True
    else:
        print("  index.html: WARNING - could not find insertion marker")
        return False

def process_custom_optics():
    """Add three-entry block to custom-optics.html"""
    filepath = os.path.join(BASE, 'custom-optics.html')
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'Start Your Custom Project' in content:
        print("  custom-optics.html: three-entry block already exists")
        return False
    
    # Insert after the Hero section (before Standard vs Custom)
    marker = '<!-- Standard vs Custom -->'
    if marker in content:
        new_content = content.replace(marker, THREE_ENTRY_CUSTOM + '\n' + marker)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("  custom-optics.html: three-entry block added after Hero")
        return True
    else:
        print("  custom-optics.html: WARNING - could not find insertion marker")
        return False

# ===== Main execution =====
print("=" * 60)
print("TASK 1: Upload Your Drawing - Expand to all EN pages")
print("=" * 60)

# Get missing pages
import subprocess
result = subprocess.run(
    ['find', '.', '-name', '*.html', '-not', '-path', './zh/*', '-exec', 'grep', '-L', 'Upload Your Drawing', '{}', ';'],
    capture_output=True, text=True, cwd=BASE
)
missing = [f.strip() for f in result.stdout.strip().split('\n') if f.strip()]

modified_count = 0
skipped_count = 0
failed_count = 0

for f in sorted(missing):
    full_path = os.path.join(BASE, f)
    status, rel = process_file(full_path)
    if status == 'modified':
        modified_count += 1
    elif status == 'skipped':
        skipped_count += 1
        print(f"  SKIP: {rel}")
    else:
        failed_count += 1
        print(f"  FAIL: {rel}")

print(f"\n  Results: {modified_count} modified, {skipped_count} skipped, {failed_count} failed")

print("\n" + "=" * 60)
print("TASK 2: Three-entry blocks")
print("=" * 60)
process_index()
process_custom_optics()

print("\n" + "=" * 60)
print("VERIFICATION")
print("=" * 60)

# Verify Upload Your Drawing count
result2 = subprocess.run(
    ['find', '.', '-name', '*.html', '-not', '-path', './zh/*', '-exec', 'grep', '-l', 'Upload Your Drawing', '{}', ';'],
    capture_output=True, text=True, cwd=BASE
)
ud_count = len([f for f in result2.stdout.strip().split('\n') if f.strip()])

result3 = subprocess.run(
    ['find', '.', '-name', '*.html', '-not', '-path', './zh/*'],
    capture_output=True, text=True, cwd=BASE
)
total_en = len([f for f in result3.stdout.strip().split('\n') if f.strip()])

print(f"  Upload Your Drawing: {ud_count}/{total_en} EN pages")

# Verify three-entry blocks
with open(os.path.join(BASE, 'index.html'), 'r') as f:
    idx = f.read()
print(f"  Homepage three-entry: {'YES' if 'How Can We Help You?' in idx else 'NO'}")

with open(os.path.join(BASE, 'custom-optics.html'), 'r') as f:
    co = f.read()
print(f"  Custom-optics three-entry: {'YES' if 'Start Your Custom Project' in co else 'NO'}")

# Check remaining missing
result4 = subprocess.run(
    ['find', '.', '-name', '*.html', '-not', '-path', './zh/*', '-exec', 'grep', '-L', 'Upload Your Drawing', '{}', ';'],
    capture_output=True, text=True, cwd=BASE
)
still_missing = [f.strip() for f in result4.stdout.strip().split('\n') if f.strip()]
print(f"  Still missing Upload Your Drawing: {len(still_missing)} pages")
for f in still_missing:
    print(f"    - {f}")

