# -*- coding: utf-8 -*-
"""Add v142 translation keys to translations.js"""

import os

BASE = '/tmp/v142-build'
TRANS_PATH = os.path.join(BASE, 'js/translations.js')

with open(TRANS_PATH, 'r') as f:
    content = f.read()

# Find where to insert new keys - before the closing } of each language block
# The structure is: translations = { "en": { ... }, "zh": { ... } };
# followed by core functions

# Find the end of "en" block - look for last key before "zh" block
# Find the start of "zh" section
zh_start = content.find('  "zh": {')

# Find the line before "zh": { which should be the closing of en block
# We need to insert before the closing } of en and zh blocks

# New EN keys
en_keys = '''    "v142Title": "PhotonEdge | Precision Optical Components, Materials & Engineering Resources",
    "v142HeroTitle": "Precision Optical Components, Materials & Engineering Resources",
    "v142HeroSubtitle": "A sourcing and specification platform for engineers and procurement teams.",
    "v142HeroDesc": "PhotonEdge connects optical components, materials databases and coating resources in one platform. Whether you know exactly what you need or are still defining specifications, you can find relevant technical information and submit a request for quotation.",
    "v142HeroCTA1": "Request a Quote",
    "v142HeroCTA2": "Talk to an Engineer",
    "v142HeroCTA3": "Read Specification Guide",
    "v142S2Title": "What We Provide",
    "v142S2Subtitle": "PhotonEdge is an engineering-oriented platform for sourcing and specifying optical components.",
    "v142S2Card1Title": "Custom Optics",
    "v142S2Card1Desc": "Custom optical components based on your drawings and specifications. Material selection, coating requirements and manufacturing process review.",
    "v142S2Card2Title": "Standard Components",
    "v142S2Card2Desc": "Catalog optical components including lenses, mirrors, windows, filters, beamsplitters and prisms with defined specifications.",
    "v142S2Card3Title": "Application Review",
    "v142S2Card3Desc": "Help reviewing material suitability, coating selection and specification requirements before manufacturing.",
    "v142S2Card4Title": "Technical Documentation",
    "v142S2Card4Desc": "Material data sheets, coating specifications and application references for optical component selection.",
    "v142S3Title": "Why PhotonEdge",
    "v142S3Subtitle": "We focus on practical value for optical component sourcing and specification.",
    "v142S3Card1Title": "Qualified Supply",
    "v142S3Card1Desc": "Manufacturing resources are selected and qualified for optical component production. Each project is matched to appropriate manufacturing capability.",
    "v142S3Card2Title": "Engineering Review",
    "v142S3Card2Desc": "Every inquiry receives technical review. We check material suitability, coating feasibility and specification completeness before confirming production.",
    "v142S3Card3Title": "Application Matching",
    "v142S3Card3Desc": "Components are recommended based on application requirements including wavelength, power, environment and system integration.",
    "v142S3Card4Title": "Documentation Support",
    "v142S3Card4Desc": "Inspection reports, material certificates and coating specifications are provided according to project requirements.",
    "v142S5Title": "Core Product Categories",
    "v142S5Subtitle": "Standard and custom optical components across seven categories.",
    "v142S5Prod1": "Optical Lenses",
    "v142S5Prod1Desc": "Spherical, aspheric, cylindrical, achromatic and custom lenses for UV, visible and infrared applications.",
    "v142S5Prod2": "Optical Windows",
    "v142S5Prod2Desc": "Flat and curved windows in fused silica, BK7, sapphire, CaF\\u2082, ZnSe and other optical materials.",
    "v142S5Prod3": "Optical Mirrors",
    "v142S5Prod3Desc": "Flat, curved and dichroic mirrors with dielectric or metallic coatings.",
    "v142S5Prod4": "Optical Filters",
    "v142S5Prod4Desc": "Bandpass, longpass, shortpass, neutral density and dichroic filters.",
    "v142S5Prod5": "Beamsplitters",
    "v142S5Prod5Desc": "Plate and cube beamsplitters for beam splitting and combining.",
    "v142S5Prod6": "Optical Prisms",
    "v142S5Prod6Desc": "Beam steering, dispersion and polarization prisms.",
    "v142S5Prod7": "Waveplates & Polarizers",
    "v142S5Prod7Desc": "Zero-order, multi-order waveplates and polarizing beamsplitters.",
    "v142ViewAllProducts": "View All Products \\u2192",
    "v142S6Title": "Engineering Resources",
    "v142S6Subtitle": "Technical references for optical component selection and specification.",
    "v142S6Res1": "Materials Database",
    "v142S6Res1Desc": "Optical, thermal and mechanical properties of common optical materials. Use this database to compare materials and understand application suitability.",
    "v142S6Res2": "Coating Database",
    "v142S6Res2Desc": "Optical coating types, specifications and application references. Understand coating selection for your wavelength and power requirements.",
    "v142S6Res3": "Application Guides",
    "v142S6Res3Desc": "Application-specific references for laser systems, scientific research, semiconductor equipment, imaging and medical optics.",
    "v142S6Res4": "AI Optical Assistant",
    "v142S6Res4Desc": "Get preliminary optical component recommendations and material suggestions based on your application requirements.",
    "v142ExploreResources": "Explore All Resources \\u2192",
    "v142S7Title": "Custom Optics",
    "v142S7Subtitle": "If your application requires non-standard optical components, PhotonEdge can help coordinate custom manufacturing.",
    "v142S7Desc1": "Custom optical components are manufactured based on your drawings or specifications. We review your requirements including material, dimensions, surface quality, coating and quantity, then match appropriate manufacturing resources.",
    "v142S7Desc2": "Before production begins, we confirm:",
    "v142S7Item1": "Material and coating feasibility",
    "v142S7Item2": "Manufacturing process route",
    "v142S7Item3": "Inspection method and acceptance criteria",
    "v142S7Item4": "Documentation requirements",
    "v142S7CTA": "Discuss Your Custom Requirements \\u2192",
    "v142FinalTitle": "Have an Optical Requirement?",
    "v142FinalDesc": "Whether you have a complete drawing or just an application description, send us what you have. We will help identify the right component and manufacturing approach.",
    "v142FinalCTA1": "Request a Quote",
    "v142FinalCTA2": "Upload Your Drawing",
    "v142FinalCTA3": "Ask AI Assistant",
    "navAIAssistant": "AI Optical Assistant",
    "v142aiHeroTitle": "AI Optical Assistant",
    "v142aiHeroDesc": "Get preliminary component and material suggestions based on your application requirements. This tool provides starting-point recommendations for engineering review.",
    "v142aiFormTitle": "Describe Your Application",
    "v142aiSubmitBtn": "Get Preliminary Recommendation \\u2192",
    "v142aiFeat1Title": "Material Suggestions",
    "v142aiFeat1Desc": "Preliminary material suggestions based on wavelength, power and environment. Final selection requires engineering review.",
    "v142aiFeat2Title": "Coating Guidance",
    "v142aiFeat2Desc": "General coating type recommendations for common application requirements. Specific designs require detailed specification review.",
    "v142aiFeat3Title": "Specification Guidance",
    "v142aiFeat3Desc": "General guidance on specification parameters. Detailed tolerance analysis is available through our engineering review process.",
    "v142aiDisclaimer": "\\u26a0 This tool provides preliminary suggestions only. Final specifications and production decisions require professional engineering review. Contact us for detailed technical consultation.",
    "v142aiAdvisorTitle": "Prefer Guided Selection?",
    "v142aiAdvisorDesc": "Use our step-by-step Smart Product Advisor for component-by-component selection from our catalog.",
    "v142aiAdvisorCTA": "Open Smart Product Advisor \\u2192",
    "v142aiResultTitle": "\\U0001f4cb Preliminary Recommendation",
    "v142aiResultReviewTitle": "Get Detailed Engineering Review",
    "v142aiResultReviewDesc": "For detailed specification review, material analysis and custom quotes, contact our team directly.",
'''

# New ZH keys
zh_keys = '''    "v142Title": "PhotonEdge | \\u7cbe\\u5bc6\\u5149\\u5b66\\u5143\\u4ef6\\u3001\\u6750\\u6599\\u4e0e\\u5de5\\u7a0b\\u8d44\\u6e90",
    "v142HeroTitle": "\\u7cbe\\u5bc6\\u5149\\u5b66\\u5143\\u4ef6\\u3001\\u6750\\u6599\\u4e0e\\u5de5\\u7a0b\\u8d44\\u6e90",
    "v142HeroSubtitle": "\\u9762\\u5411\\u5de5\\u7a0b\\u5e08\\u548c\\u91c7\\u8d2d\\u56e2\\u961f\\u7684\\u5149\\u5b66\\u5143\\u4ef6\\u9009\\u578b\\u4e0e\\u89c4\\u683c\\u5e73\\u53f0\\u3002",
    "v142HeroDesc": "PhotonEdge\\u5c06\\u5149\\u5b66\\u5143\\u4ef6\\u3001\\u6750\\u6599\\u6570\\u636e\\u5e93\\u548c\\u9540\\u819c\\u8d44\\u6e90\\u96c6\\u6210\\u5728\\u4e00\\u4e2a\\u5e73\\u53f0\\u4e0a\\u3002\\u65e0\\u8bba\\u60a8\\u662f\\u660e\\u786e\\u9700\\u6c42\\u8fd8\\u662f\\u6b63\\u5728\\u786e\\u5b9a\\u89c4\\u683c\\uff0c\\u90fd\\u53ef\\u4ee5\\u627e\\u5230\\u76f8\\u5173\\u6280\\u672f\\u4fe1\\u606f\\u5e76\\u63d0\\u4ea4\\u62a5\\u4ef7\\u8bf7\\u6c42\\u3002",
    "v142HeroCTA1": "\\u8bf7\\u6c42\\u62a5\\u4ef7",
    "v142HeroCTA2": "\\u4e0e\\u5de5\\u7a0b\\u5e08\\u4ea4\\u6d41",
    "v142HeroCTA3": "\\u9605\\u8bfb\\u89c4\\u683c\\u6307\\u5357",
    "v142S2Title": "\\u6211\\u4eec\\u63d0\\u4f9b\\u4ec0\\u4e48",
    "v142S2Subtitle": "PhotonEdge\\u662f\\u4e00\\u4e2a\\u9762\\u5411\\u5de5\\u7a0b\\u7684\\u5149\\u5b66\\u5143\\u4ef6\\u9009\\u578b\\u4e0e\\u89c4\\u683c\\u5e73\\u53f0\\u3002",
    "v142S2Card1Title": "\\u5b9a\\u5236\\u5149\\u5b66",
    "v142S2Card1Desc": "\\u57fa\\u4e8e\\u60a8\\u7684\\u56fe\\u7eb8\\u548c\\u89c4\\u683c\\u7684\\u5b9a\\u5236\\u5149\\u5b66\\u5143\\u4ef6\\u3002\\u6750\\u6599\\u9009\\u62e9\\u3001\\u9540\\u819c\\u8981\\u6c42\\u548c\\u5236\\u9020\\u5de5\\u827a\\u5ba1\\u67e5\\u3002",
    "v142S2Card2Title": "\\u6807\\u51c6\\u5143\\u4ef6",
    "v142S2Card2Desc": "\\u76ee\\u5f55\\u5149\\u5b66\\u5143\\u4ef6\\uff0c\\u5305\\u62ec\\u900f\\u955c\\u3001\\u53cd\\u5c04\\u955c\\u3001\\u7a97\\u53e3\\u3001\\u6ee4\\u5149\\u7247\\u3001\\u5206\\u675f\\u955c\\u548c\\u68f1\\u955c\\uff0c\\u5177\\u6709\\u660e\\u786e\\u89c4\\u683c\\u3002",
    "v142S2Card3Title": "\\u5e94\\u7528\\u5ba1\\u67e5",
    "v142S2Card3Desc": "\\u5728\\u5236\\u9020\\u4e4b\\u524d\\u5e2e\\u52a9\\u5ba1\\u67e5\\u6750\\u6599\\u9002\\u7528\\u6027\\u3001\\u9540\\u819c\\u9009\\u62e9\\u548c\\u89c4\\u683c\\u8981\\u6c42\\u3002",
    "v142S2Card4Title": "\\u6280\\u672f\\u6587\\u6863",
    "v142S2Card4Desc": "\\u6750\\u6599\\u6570\\u636e\\u8868\\u3001\\u9540\\u819c\\u89c4\\u683c\\u548c\\u5e94\\u7528\\u53c2\\u8003\\uff0c\\u7528\\u4e8e\\u5149\\u5b66\\u5143\\u4ef6\\u9009\\u578b\\u3002",
    "v142S3Title": "\\u4e3a\\u4ec0\\u4e48\\u9009\\u62e9 PhotonEdge",
    "v142S3Subtitle": "\\u6211\\u4eec\\u4e13\\u6ce8\\u4e8e\\u5149\\u5b66\\u5143\\u4ef6\\u91c7\\u8d2d\\u548c\\u89c4\\u683c\\u7684\\u5b9e\\u9645\\u4ef7\\u503c\\u3002",
    "v142S3Card1Title": "\\u5408\\u683c\\u4f9b\\u5e94",
    "v142S3Card1Desc": "\\u5236\\u9020\\u8d44\\u6e90\\u7ecf\\u8fc7\\u5149\\u5b66\\u5143\\u4ef6\\u751f\\u4ea7\\u7684\\u7b5b\\u9009\\u548c\\u8d44\\u8d28\\u8ba4\\u5b9a\\u3002\\u6bcf\\u4e2a\\u9879\\u76ee\\u90fd\\u5339\\u914d\\u5408\\u9002\\u7684\\u5236\\u9020\\u80fd\\u529b\\u3002",
    "v142S3Card2Title": "\\u5de5\\u7a0b\\u5ba1\\u67e5",
    "v142S3Card2Desc": "\\u6bcf\\u4e2a\\u8be2\\u4ef7\\u90fd\\u4f1a\\u63a5\\u53d7\\u6280\\u672f\\u5ba1\\u67e5\\u3002\\u6211\\u4eec\\u5728\\u786e\\u8ba4\\u751f\\u4ea7\\u524d\\u68c0\\u67e5\\u6750\\u6599\\u9002\\u7528\\u6027\\u3001\\u9540\\u819c\\u53ef\\u884c\\u6027\\u548c\\u89c4\\u683c\\u5b8c\\u6574\\u6027\\u3002",
    "v142S3Card3Title": "\\u5e94\\u7528\\u5339\\u914d",
    "v142S3Card3Desc": "\\u6839\\u636e\\u5e94\\u7528\\u8981\\u6c42\\u63a8\\u8350\\u5143\\u4ef6\\uff0c\\u5305\\u62ec\\u6ce2\\u957f\\u3001\\u529f\\u7387\\u3001\\u73af\\u5883\\u548c\\u7cfb\\u7edf\\u96c6\\u6210\\u3002",
    "v142S3Card4Title": "\\u6587\\u6863\\u652f\\u6301",
    "v142S3Card4Desc": "\\u6839\\u636e\\u9879\\u76ee\\u8981\\u6c42\\u63d0\\u4f9b\\u68c0\\u6d4b\\u62a5\\u544a\\u3001\\u6750\\u6599\\u8bc1\\u4e66\\u548c\\u9540\\u819c\\u89c4\\u683c\\u3002",
    "v142S5Title": "\\u6838\\u5fc3\\u4ea7\\u54c1\\u5206\\u7c7b",
    "v142S5Subtitle": "\\u4e03\\u5927\\u7c7b\\u522b\\u7684\\u6807\\u51c6\\u548c\\u5b9a\\u5236\\u5149\\u5b66\\u5143\\u4ef6\\u3002",
    "v142S5Prod1": "\\u5149\\u5b66\\u900f\\u955c",
    "v142S5Prod1Desc": "\\u7403\\u9762\\u3001\\u975e\\u7403\\u9762\\u3001\\u5706\\u67f1\\u3001\\u6d88\\u8272\\u5dee\\u548c\\u5b9a\\u5236\\u900f\\u955c\\uff0c\\u9002\\u7528\\u4e8e\\u7d2b\\u5916\\u3001\\u53ef\\u89c1\\u5149\\u548c\\u7ea2\\u5916\\u5e94\\u7528\\u3002",
    "v142S5Prod2": "\\u5149\\u5b66\\u7a97\\u53e3",
    "v142S5Prod2Desc": "\\u5e73\\u9762\\u548c\\u66f2\\u9762\\u7a97\\u53e3\\uff0c\\u63d0\\u4f9b\\u7d2b\\u5916\\u7194\\u878d\\u77f3\\u82f1\\u3001BK7\\u3001\\u84dd\\u5b9d\\u77f3\\u3001CaF\\u2082\\u3001ZnSe\\u7b49\\u5149\\u5b66\\u6750\\u6599\\u3002",
    "v142S5Prod3": "\\u5149\\u5b66\\u53cd\\u5c04\\u955c",
    "v142S5Prod3Desc": "\\u5e73\\u9762\\u3001\\u66f2\\u9762\\u548c\\u4e8c\\u5411\\u8272\\u53cd\\u5c04\\u955c\\uff0c\\u5177\\u6709\\u4ecb\\u8d28\\u6216\\u91d1\\u5c5e\\u9540\\u819c\\u3002",
    "v142S5Prod4": "\\u5149\\u5b66\\u6ee4\\u5149\\u7247",
    "v142S5Prod4Desc": "\\u5e26\\u901a\\u3001\\u957f\\u901a\\u3001\\u77ed\\u901a\\u3001\\u4e2d\\u6027\\u5bc6\\u5ea6\\u548c\\u4e8c\u5411\\u8272\\u6ee4\\u5149\\u7247\\u3002",
    "v142S5Prod5": "\\u5206\\u675f\\u955c",
    "v142S5Prod5Desc": "\\u677f\\u5f0f\\u548c\\u7acb\\u65b9\\u4f53\\u5206\\u675f\\u955c\\uff0c\\u7528\\u4e8e\\u5149\\u675f\\u5206\\u5272\\u548c\\u5408\\u675f\\u3002",
    "v142S5Prod6": "\\u5149\\u5b66\\u68f1\\u955c",
    "v142S5Prod6Desc": "\\u5149\\u675f\\u8f6c\\u5411\\u3001\\u8272\\u6563\\u548c\\u504f\\u632f\\u68f1\\u955c\\u3002",
    "v142S5Prod7": "\\u6ce2\\u7247\\u4e0e\\u504f\\u632f\\u5668",
    "v142S5Prod7Desc": "\\u96f6\\u7ea7\\u3001\\u591a\\u7ea7\\u6ce2\\u7247\\u548c\\u504f\\u632f\\u5206\\u675f\\u955c\\u3002",
    "v142ViewAllProducts": "\\u67e5\\u770b\\u5168\\u90e8\\u4ea7\\u54c3 \\u2192",
    "v142S6Title": "\\u5de5\\u7a0b\\u8d44\\u6e90",
    "v142S6Subtitle": "\\u5149\\u5b66\\u5143\\u4ef6\\u9009\\u578b\\u548c\\u89c4\\u683c\\u7684\\u6280\\u672f\\u53c2\\u8003\\u8d44\\u6599\\u3002",
    "v142S6Res1": "\\u6750\\u6599\\u6570\\u636e\\u5e93",
    "v142S6Res1Desc": "\\u5e38\\u7528\\u5149\\u5b66\\u6750\\u6599\\u7684\\u5149\\u5b66\\u3001\\u70ed\\u5b66\\u548c\\u673a\\u68b0\\u6027\\u80fd\\u3002\\u4f7f\\u7528\\u6570\\u636e\\u5e93\\u6bd4\\u8f83\\u6750\\u6599\\u5e76\\u4e86\\u89e3\\u5e94\\u7528\\u9002\\u7528\\u6027\\u3002",
    "v142S6Res2": "\\u9540\\u819c\\u6570\\u636e\\u5e93",
    "v142S6Res2Desc": "\\u5149\\u5b66\\u9540\\u819c\\u7c7b\\u578b\\u3001\\u89c4\\u683c\\u548c\\u5e94\\u7528\\u53c2\\u8003\\u3002\\u4e86\\u89e3\\u9488\\u5bf9\\u60a8\\u7684\\u6ce2\\u957f\\u548c\\u529f\\u7387\\u8981\\u6c42\\u7684\\u9540\\u819c\\u9009\\u62e9\\u3002",
    "v142S6Res3": "\\u5e94\\u7528\\u6307\\u5357",
    "v142S6Res3Desc": "\\u6fc0\\u5149\\u7cfb\\u7edf\\u3001\\u79d1\\u5b66\\u7814\\u7a76\\u3001\\u534a\\u5bfc\\u4f53\\u8bbe\\u5907\\u3001\\u6210\\u50cf\\u548c\\u533b\\u7528\\u5149\\u5b66\\u7684\\u5e94\\u7528\\u53c2\\u8003\\u3002",
    "v142S6Res4": "AI \\u5149\\u5b66\\u52a9\\u624b",
    "v142S6Res4Desc": "\\u6839\\u636e\\u60a8\\u7684\\u5e94\\u7528\\u8981\\u6c42\\u83b7\\u53d6\\u521d\\u6b65\\u7684\\u5149\\u5b66\\u5143\\u4ef6\\u63a8\\u8350\\u548c\\u6750\\u6599\\u5efa\\u8bae\\u3002",
    "v142ExploreResources": "\\u63a2\\u7d22\\u6240\\u6709\\u8d44\\u6e90 \\u2192",
    "v142S7Title": "\\u5b9a\\u5236\\u5149\\u5b66",
    "v142S7Subtitle": "\\u5982\\u679c\\u60a8\\u7684\\u5e94\\u7528\\u9700\\u8981\\u975e\\u6807\\u5149\\u5b66\\u5143\\u4ef6\\uff0cPhotonEdge \\u53ef\\u4ee5\\u5e2e\\u52a9\\u534f\\u8c03\\u5b9a\\u5236\\u5236\\u9020\\u3002",
    "v142S7Desc1": "\\u5b9a\\u5236\\u5149\\u5b66\\u5143\\u4ef6\\u57fa\\u4e8e\\u60a8\\u7684\\u56fe\\u7eb8\\u6216\\u89c4\\u683c\\u5236\\u9020\\u3002\\u6211\\u4eec\\u5ba1\\u67e5\\u60a8\\u7684\\u8981\\u6c42\\uff0c\\u5305\\u62ec\\u6750\\u6599\\u3001\\u5c3a\\u5bf8\\u3001\\u8868\\u9762\\u8d28\\u91cf\\u3001\\u9540\\u819c\\u548c\\u6570\\u91cf\\uff0c\\u7136\\u540e\\u5339\\u914d\\u5408\\u9002\\u7684\\u5236\\u9020\\u8d44\\u6e90\\u3002",
    "v142S7Desc2": "\\u751f\\u4ea7\\u5f00\\u59cb\\u524d\\uff0c\\u6211\\u4eec\\u786e\\u8ba4\\uff1a",
    "v142S7Item1": "\\u6750\\u6599\\u548c\\u9540\\u819c\\u53ef\\u884c\\u6027",
    "v142S7Item2": "\\u5236\\u9020\\u5de5\\u827a\\u8def\\u7ebf",
    "v142S7Item3": "\\u68c0\\u6d4b\\u65b9\\u6cd5\\u548c\\u9a8c\\u6536\\u6807\\u51c6",
    "v142S7Item4": "\\u6587\\u6863\\u8981\\u6c42",
    "v142S7CTA": "\\u8ba8\\u8bba\\u60a8\\u7684\\u5b9a\\u5236\\u9700\\u6c42 \\u2192",
    "v142FinalTitle": "\\u6709\\u5149\\u5b66\\u9700\\u6c42\\uff1f",
    "v142FinalDesc": "\\u65e0\\u8bba\\u60a8\\u6709\\u5b8c\\u6574\\u56fe\\u7eb8\\u8fd8\\u662f\\u53ea\\u6709\\u5e94\\u7528\\u63cf\\u8ff0\\uff0c\\u8bf7\\u53d1\\u9001\\u7ed9\\u6211\\u4eec\\u3002\\u6211\\u4eec\\u5c06\\u5e2e\\u52a9\\u60a8\\u786e\\u5b9a\\u5408\\u9002\\u7684\\u5143\\u4ef6\\u548c\\u5236\\u9020\\u65b9\\u6848\\u3002",
    "v142FinalCTA1": "\\u8bf7\\u6c42\\u62a5\\u4ef7",
    "v142FinalCTA2": "\\u4e0a\\u4f20\\u60a8\\u7684\\u56fe\\u7eb8",
    "v142FinalCTA3": "\\u54a8\\u8be2 AI \\u52a9\\u624b",
    "navAIAssistant": "AI \\u5149\\u5b66\\u52a9\\u624b",
    "v142aiHeroTitle": "AI \\u5149\\u5b66\\u52a9\\u624b",
    "v142aiHeroDesc": "\\u6839\\u636e\\u60a8\\u7684\\u5e94\\u7528\\u8981\\u6c42\\u83b7\\u53d6\\u521d\\u6b65\\u7684\\u5143\\u4ef6\\u548c\\u6750\\u6599\\u5efa\\u8bae\\u3002\\u6b64\\u5de5\\u5177\\u63d0\\u4f9b\\u8d77\\u6b65\\u5efa\\u8bae\\uff0c\\u4f9b\\u5de5\\u7a0b\\u5ba1\\u67e5\\u3002",
    "v142aiFormTitle": "\\u63cf\\u8ff0\\u60a8\\u7684\\u5e94\\u7528",
    "v142aiSubmitBtn": "\\u83b7\\u53d6\\u521d\\u6b65\\u5efa\\u8bae \\u2192",
    "v142aiFeat1Title": "\\u6750\\u6599\\u5efa\\u8bae",
    "v142aiFeat1Desc": "\\u57fa\\u4e8e\\u6ce2\\u957f\\u3001\\u529f\\u7387\\u548c\\u73af\\u5883\\u7684\\u521d\\u6b65\\u6750\\u6599\\u5efa\\u8bae\\u3002\\u6700\\u7ec8\\u9009\\u62e9\\u9700\\u8981\\u5de5\\u7a0b\\u5ba1\\u67e5\\u3002",
    "v142aiFeat2Title": "\\u9540\\u819c\\u6307\\u5bfc",
    "v142aiFeat2Desc": "\\u5e38\\u89c1\\u5e94\\u7528\\u7684\\u901a\\u7528\\u9540\\u819c\\u7c7b\\u578b\\u5efa\\u8bae\\u3002\\u5177\\u4f53\\u8bbe\\u8ba1\\u9700\\u8981\\u8be6\\u7ec6\\u89c4\\u683c\\u5ba1\\u67e5\\u3002",
    "v142aiFeat3Title": "\\u89c4\\u683c\\u6307\\u5bfc",
    "v142aiFeat3Desc": "\\u89c4\\u683c\\u53c2\\u6570\\u7684\\u901a\\u7528\\u6307\\u5bfc\\u3002\\u8be6\\u7ec6\\u516c\\u5dee\\u5206\\u6790\\u53ef\\u901a\\u8fc7\\u5de5\\u7a0b\\u5ba1\\u67e5\\u6d41\\u7a0b\\u83b7\\u5f97\\u3002",
    "v142aiDisclaimer": "\\u26a0 \\u6b64\\u5de5\\u5177\\u4ec5\\u63d0\\u4f9b\\u521d\\u6b65\\u5efa\\u8bae\\u3002\\u6700\\u7ec8\\u89c4\\u683c\\u548c\\u751f\\u4ea7\\u51b3\\u7b56\\u9700\\u8981\\u4e13\\u4e1a\\u5de5\\u7a0b\\u5ba1\\u67e5\\u3002\\u8bf7\\u8054\\u7cfb\\u6211\\u4eec\\u83b7\\u53d6\\u8be6\\u7ec6\\u6280\\u672f\\u54a8\\u8be2\\u3002",
    "v142aiAdvisorTitle": "\\u504f\\u597d\\u5f15\\u5bfc\\u9009\\u62e9\\uff1f",
    "v142aiAdvisorDesc": "\\u4f7f\\u7528\\u6211\\u4eec\\u7684\\u9010\\u6b65\\u667a\\u80fd\\u4ea7\\u54c1\\u987e\\u95ee\\uff0c\\u4ece\\u76ee\\u5f55\\u4e2d\\u9010\\u4e2a\\u5143\\u4ef6\\u9009\\u62e9\\u3002",
    "v142aiAdvisorCTA": "\\u6253\\u5f00\\u667a\\u80fd\\u4ea7\\u54c1\\u987e\\u95ee \\u2192",
    "v142aiResultTitle": "\\U0001f4cb \\u521d\\u6b65\\u5efa\\u8bae",
    "v142aiResultReviewTitle": "\\u83b7\\u53d6\\u8be6\\u7ec6\\u5de5\\u7a0b\\u5ba1\\u67e5",
    "v142aiResultReviewDesc": "\\u5982\\u9700\\u8be6\\u7ec6\\u89c4\\u683c\\u5ba1\\u67e5\\u3001\\u6750\\u6599\\u5206\\u6790\\u548c\\u5b9a\\u5236\\u62a5\\u4ef7\\uff0c\\u8bf7\\u76f4\\u63a5\\u8054\\u7cfb\\u6211\\u4eec\\u7684\\u56e2\\u961f\\u3002",
'''

# Insert EN keys before the end of the EN block
# Find the position of "zh": { and go back to insert before the closing }
en_insert_pos = content.find('  "zh": {')
# Go back to find the last } that closes the EN block
# Look backwards from en_insert_pos for the closing
# Actually, we need to find the line just before "zh" block starts
# which should be "  }," closing the en block

# Find the last key-value pair in EN block
# Insert before the closing } of EN
en_close = content.rfind('}', 0, en_insert_pos)
# We want to insert before that closing }
# Find the actual last key in en block
last_en_comma = content.rfind(',', 0, en_close)

# Insert new EN keys after the last existing EN key
insert_point_en = last_en_comma + 1

# Build the insertion
content = content[:insert_point_en] + '\n' + en_keys + content[insert_point_en:]

# Now find zh block end
# After insertion, zh block moved. Find it again.
zh_start_new = content.find('  "zh": {')
zh_close = content.find('  }', zh_start_new + 10)
# Find the last comma before zh_close
last_zh_comma = content.rfind(',', zh_start_new, zh_close)

insert_point_zh = last_zh_comma + 1
content = content[:insert_point_zh] + '\n' + zh_keys + content[insert_point_zh:]

with open(TRANS_PATH, 'w') as f:
    f.write(content)

print("Translation keys added. New line count: %d" % content.count('\n'))
