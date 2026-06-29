/**
 * PhotonEdge AI Chatbot
 * Rule-based chat widget for demand consultation, lead collection & after-sales support
 * ES5 only - no const, let, arrow functions, template literals
 */

var PhotonEdgeChatbot = (function() {

    /* ===== Configuration ===== */
    var CONFIG = {
        weakTriggerDelay: 40000,      // 40 seconds
        weakTriggerScroll: true,      // trigger on scroll to bottom
        exitIntentEnabled: true,      // mouse leaves viewport
        exitIntentCooldown: 86400000, // 24 hours in ms
        sessionCooldown: 3600000,     // 1 hour between exit intent shows
        leadFormFields: ['name', 'email', 'company', 'phone', 'requirement'],
        gaEvents: true
    };

    /* ===== State ===== */
    var state = {
        isOpen: false,
        currentStep: 'menu',
        userData: {},
        weakTriggerFired: false,
        exitTriggerFired: false,
        lastExitTime: 0,
        messageQueue: [],
        isTyping: false
    };

    /* ===== Knowledge Base ===== */
    var KB = {
        faq: {
            'lead-time': {
                en: 'Standard in-stock components ship within 3-5 business days. Custom manufactured optics typically take 2-4 weeks depending on specifications and coating requirements. Rush orders may be available for urgent requirements.',
                zh: '标准库存元件3-5个工作日发货。定制光学元件通常需要2-4周，具体取决于规格和镀膜要求。紧急订单可加急处理。'
            },
            'moq': {
                en: 'For standard catalog components, we have no minimum order quantity — you can order even a single piece. For custom manufactured optics, MOQ typically starts at 5-10 pieces depending on complexity.',
                zh: '标准目录产品无最低起订量，单片起订。定制光学元件最低起订量通常为5-10片，具体取决于复杂度。'
            },
            'payment': {
                en: 'We accept bank wire transfers (T/T), PayPal, and major credit cards. For established customers, net-30 payment terms may be available after credit approval.',
                zh: '我们接受银行电汇(T/T)、PayPal和主要信用卡。老客户经信用审核后可提供NET-30账期。'
            },
            'shipping': {
                en: 'We ship worldwide via DHL, FedEx, and UPS. Standard international delivery takes 3-7 business days. Import duties and taxes are the responsibility of the customer.',
                zh: '我们通过DHL、FedEx和UPS全球发货。标准国际快递3-7个工作日到达。进口关税由客户承担。'
            },
            'sample': {
                en: 'We can provide sample components for qualification testing at standard pricing, with credit applied toward future volume orders. Contact our sales team to discuss sample requirements.',
                zh: '我们可提供样品用于_qualification测试，按标准价格计费，后续批量订单可抵扣样品费用。请联系销售团队了解详情。'
            },
            'custom': {
                en: 'We specialize in custom precision optics. We can work from your drawings, specifications, or reverse engineer existing parts. Please share your requirements and our engineering team will provide a quote within 24-48 hours.',
                zh: '我们专注于定制精密光学元件，可根据您的图纸、规格书或现有样品进行逆向工程。请提供需求，我们的工程团队将在24-48小时内报价。'
            },
            'coating': {
                en: 'We offer AR coatings (VIS, NIR, SWIR, MWIR, LWIR), HR coatings, partial reflectors, broadband coatings, and laser line coatings. Custom coatings for specific wavelength ranges are available.',
                zh: '我们提供增透膜(可见光、近红外、短波红外、中波红外、长波红外)、高反膜、部分反射膜、宽带膜和激光线膜。支持特定波长的定制镀膜。'
            },
            'tolerance': {
                en: 'Standard precision: surface quality 40-20 scratch-dig, surface accuracy λ/4 @ 633nm, centration < 3 arc minutes. Precision options up to 10-5 scratch-dig, λ/20 surface accuracy available.',
                zh: '标准精度：面形质量40-20划痕 digs，面形精度λ/4 @ 633nm，偏心差< 3弧分。精密选项可达10-5划痕digs，λ/20面形精度。'
            },
            'certification': {
                en: 'PhotonEdge is ISO 9001:2015 certified. We provide inspection reports including interferometer surface maps, spectrophotometer curves, and dimensional data. Certificates of Compliance (CoC) are provided with every shipment.',
                zh: '恒鼎光通过ISO 9001:2015认证。我们提供干涉仪面形图、分光光度计曲线和尺寸检测数据等检验报告。每批货物附带合格证书(CoC)。'
            },
            'warranty': {
                en: 'All optical components come with a 12-month warranty against defects in materials and workmanship. Standard catalog items may be returned within 30 days in original packaging (15% restocking fee).',
                zh: '所有光学元件享有12个月材料和工艺质保。标准目录产品可在30天内原包装退货（收取15%重新入库费）。'
            }
        },

        products: {},  // Will be populated from products-data.js
        categories: [],

        applications: {
            'laser': { en: 'Laser Systems', zh: '激光系统', keywords: ['laser', 'cutting', 'welding', 'marking', 'engraving'] },
            'medical': { en: 'Medical Devices', zh: '医疗设备', keywords: ['medical', 'surgical', 'imaging', 'diagnostic', 'endoscope'] },
            'research': { en: 'Scientific Research', zh: '科研实验', keywords: ['research', 'laboratory', 'spectroscopy', 'microscopy', 'experiment'] },
            'telecom': { en: 'Telecommunications', zh: '电信通信', keywords: ['telecom', 'fiber', 'communication', 'optical network'] },
            'defense': { en: 'Defense & Aerospace', zh: '国防航天', keywords: ['defense', 'military', 'aerospace', 'satellite', 'surveillance'] },
            'industrial': { en: 'Industrial Automation', zh: '工业自动化', keywords: ['industrial', 'automation', 'machine vision', 'inspection', 'metrology'] },
            'semiconductor': { en: 'Semiconductor', zh: '半导体', keywords: ['semiconductor', 'wafer', 'lithography', 'cleanroom'] },
            'other': { en: 'Other Applications', zh: '其他应用', keywords: [] }
        }
    };

    /* ===== Conversation Flow ===== */
    var flow = {
        menu: {
            en: {
                greeting: 'Hello! I\'m the PhotonEdge Optical Assistant. How can I help you today?',
                options: [
                    { key: 'product_recommend', icon: '🔍', label: 'Product Recommendation' },
                    { key: 'custom_consult', icon: '🔧', label: 'Custom Solution Inquiry' },
                    { key: 'quote_delivery', icon: '💰', label: 'Pricing & Delivery' },
                    { key: 'other_question', icon: '❓', label: 'Other Questions' }
                ]
            },
            zh: {
                greeting: '您好！我是PhotonEdge光学助手，请问有什么可以帮您的？',
                options: [
                    { key: 'product_recommend', icon: '🔍', label: '产品选型推荐' },
                    { key: 'custom_consult', icon: '🔧', label: '定制方案咨询' },
                    { key: 'quote_delivery', icon: '💰', label: '报价/交期查询' },
                    { key: 'other_question', icon: '❓', label: '其他问题' }
                ]
            }
        },

        product_recommend: {
            steps: [
                {
                    key: 'application',
                    en: { question: 'What is your application scenario?', options: ['laser', 'medical', 'research', 'telecom', 'defense', 'industrial', 'semiconductor', 'other'] },
                    zh: { question: '请问您的应用场景是什么？', options: ['laser', 'medical', 'research', 'telecom', 'defense', 'industrial', 'semiconductor', 'other'] }
                },
                {
                    key: 'wavelength',
                    en: { question: 'What is your working wavelength range?', options: ['UV (200-400nm)', 'Visible (400-700nm)', 'NIR (700-1400nm)', 'SWIR (1400-3000nm)', 'MWIR (3-5μm)', 'LWIR (8-14μm)', 'Not sure'] },
                    zh: { question: '您的工作波长范围是多少？', options: ['紫外 (200-400nm)', '可见光 (400-700nm)', '近红外 (700-1400nm)', '短波红外 (1400-3000nm)', '中波红外 (3-5μm)', '长波红外 (8-14μm)', '不确定'] }
                },
                {
                    key: 'component_type',
                    en: { question: 'What type of component do you need?', options: ['Lens', 'Mirror', 'Window', 'Prism', 'Filter', 'Beamsplitter', 'Waveplate', 'Polarizer', 'Not sure - need recommendation'] },
                    zh: { question: '您需要什么类型的元件？', options: ['透镜', '反射镜', '窗口片', '棱镜', '滤光片', '分光镜', '波片', '偏振器', '不确定-需要推荐'] }
                }
            ],
            result_en: 'Based on your requirements, I recommend the following products:',
            result_zh: '根据您的需求，我推荐以下产品：',
            cta_en: 'Would you like me to send you the full specification sheet and sample pricing? Please leave your email and we\'ll contact you within 24 hours.',
            cta_zh: '需要我为您发送完整参数表和样品报价吗？请留下您的邮箱，我们会在24小时内联系您。'
        },

        custom_consult: {
            steps: [
                {
                    key: 'product_type',
                    en: { question: 'What type of product do you need customized?', options: ['Lens', 'Mirror', 'Window', 'Prism', 'Filter', 'Other optical component'] },
                    zh: { question: '请问需要定制的产品类型是？', options: ['透镜', '反射镜', '窗口片', '棱镜', '滤光片', '其他光学元件'] }
                },
                {
                    key: 'spec_level',
                    en: { question: 'What is your specification level?', options: ['Standard (λ/4, 40-20)', 'Precision (λ/10, 20-10)', 'High Precision (λ/20, 10-5)', 'Not sure - need guidance'] },
                    zh: { question: '您的精度要求是？', options: ['标准 (λ/4, 40-20)', '精密 (λ/10, 20-10)', '高精度 (λ/20, 10-5)', '不确定-需要指导'] }
                },
                {
                    key: 'quantity',
                    en: { question: 'What is your estimated order quantity?', options: ['1-10 pcs', '10-50 pcs', '50-100 pcs', '100-500 pcs', '500+ pcs'] },
                    zh: { question: '预计采购数量是？', options: ['1-10片', '10-50片', '50-100片', '100-500片', '500片以上'] }
                }
            ],
            result_en: 'Thank you for providing your requirements. Our optical engineers will review your specifications and provide a detailed quote.',
            result_zh: '感谢您提供需求信息。我们的光学工程师将审核您的规格并提供详细报价。',
            cta_en: 'Please leave your email and contact information, and our team will reach out within 24 hours.',
            cta_zh: '请留下您的邮箱和联系方式，我们的团队会在24小时内与您联系。'
        },

        quote_delivery: {
            en: {
                intro: 'Here are answers to common pricing and delivery questions:',
                topics: [
                    { key: 'lead-time', label: 'Lead Time & Delivery' },
                    { key: 'moq', label: 'Minimum Order Quantity' },
                    { key: 'payment', label: 'Payment Methods' },
                    { key: 'shipping', label: 'Shipping & Logistics' },
                    { key: 'sample', label: 'Sample Policy' }
                ],
                fallback: 'For specific pricing based on your requirements, please leave your contact details and we\'ll prepare a custom quote for you.'
            },
            zh: {
                intro: '以下是关于报价和交期的常见问题解答：',
                topics: [
                    { key: 'lead-time', label: '交期与发货' },
                    { key: 'moq', label: '最低起订量' },
                    { key: 'payment', label: '付款方式' },
                    { key: 'shipping', label: '运输物流' },
                    { key: 'sample', label: '样品政策' }
                ],
                fallback: '如需根据您的具体需求报价，请留下联系方式，我们将为您准备定制报价。'
            }
        },

        other_question: {
            en: {
                intro: 'I can help with these common topics:',
                topics: [
                    { key: 'coating', label: 'Coating Options' },
                    { key: 'tolerance', label: 'Precision & Tolerances' },
                    { key: 'certification', label: 'Quality & Certifications' },
                    { key: 'warranty', label: 'Warranty & Returns' },
                    { key: 'custom', label: 'Custom Manufacturing' }
                ],
                fallback: 'For detailed technical questions, our engineering team is best equipped to help. Please leave your contact details and we\'ll have a specialist reach out to you.'
            },
            zh: {
                intro: '我可以帮您解答以下常见问题：',
                topics: [
                    { key: 'coating', label: '镀膜选项' },
                    { key: 'tolerance', label: '精度与公差' },
                    { key: 'certification', label: '质量与认证' },
                    { key: 'warranty', label: '质保与退换' },
                    { key: 'custom', label: '定制生产' }
                ],
                fallback: '如需详细技术解答，我们的工程团队将为您提供专业支持。请留下联系方式，我们会安排专家与您对接。'
            }
        }
    };

    /* ===== Safety Boundary Messages ===== */
    var safetyMessages = {
        complex_custom: {
            en: 'This is a complex requirement that needs detailed review by our optical engineers. Please leave your contact information and we\'ll have a specialist get back to you within 24 hours.',
            zh: '这是一个需要光学工程师详细评估的复杂需求。请留下您的联系方式，我们的专家会在24小时内回复您。'
        },
        specific_price: {
            en: 'Pricing depends on specifications, coatings, and quantity. Please share your detailed requirements and we\'ll prepare a precise quote for you within 24 hours.',
            zh: '价格取决于规格、镀膜和数量。请提供详细需求，我们将在24小时内为您准备精确报价。'
        },
        uncertain_param: {
            en: 'To recommend the right product, I\'d suggest consulting with our technical team. Please leave your contact details and an engineer will help you determine the optimal specifications.',
            zh: '为了推荐合适的产品，建议您咨询我们的技术团队。请留下联系方式，工程师会帮您确定最佳规格。'
        }
    };

    /* ===== Lead Form ===== */
    var leadForm = {
        en: {
            title: 'Let us get back to you',
            subtitle: 'Leave your details and we\'ll respond within 24 hours',
            fields: {
                name: { label: 'Your Name', placeholder: 'John Smith', required: true },
                email: { label: 'Email Address', placeholder: 'john@company.com', required: true },
                company: { label: 'Company', placeholder: 'Company name', required: false },
                phone: { label: 'Phone / WhatsApp', placeholder: '+1-234-567-8900', required: false },
                requirement: { label: 'Requirements Summary', placeholder: 'Brief description of your needs...', required: false }
            },
            submit: 'Submit & Get Quote',
            success: 'Thank you! We\'ve received your information and will contact you within 24 hours.'
        },
        zh: {
            title: '让我们与您取得联系',
            subtitle: '请留下您的信息，我们将在24小时内回复',
            fields: {
                name: { label: '您的姓名', placeholder: '张先生', required: true },
                email: { label: '邮箱地址', placeholder: 'your@company.com', required: true },
                company: { label: '公司名称', placeholder: '公司名称', required: false },
                phone: { label: '电话 / WhatsApp', placeholder: '+86-138-0000-0000', required: false },
                requirement: { label: '需求概述', placeholder: '简要描述您的需求...', required: false }
            },
            submit: '提交并获取报价',
            success: '感谢！我们已收到您的信息，将在24小时内与您联系。'
        }
    };

    /* ===== DOM Elements ===== */
    var dom = {};

    /* ===== Initialization ===== */
    function init() {
        // Build knowledge base from products data
        if (typeof PRODUCTS !== 'undefined') {
            KB.products = PRODUCTS;
        }
        if (typeof PRODUCT_CATEGORIES !== 'undefined') {
            KB.categories = PRODUCT_CATEGORIES;
        }

        // Create DOM structure
        createWidget();
        
        // Bind events
        bindEvents();
        
        // Start trigger timers
        startTriggers();

        // Track initialization
        trackEvent('chatbot_initialized');
    }

    /* ===== Widget Creation ===== */
    function createWidget() {
        // Main container
        var container = document.createElement('div');
        container.id = 'pe-chatbot';
        container.className = 'pe-chatbot-container';
        
        container.innerHTML = 
            '<!-- Floating Ball -->' +
            '<div class="pe-chatbot-ball" id="peChatbotBall" title="Chat with us">' +
                '<div class="pe-chatbot-ball-icon">💬</div>' +
                '<div class="pe-chatbot-ball-badge" id="peChatbotBadge" style="display:none;">1</div>' +
            '</div>' +

            '<!-- Floating Message Bubble -->' +
            '<div class="pe-chatbot-bubble" id="peChatbotBubble" style="display:none;">' +
                '<span class="pe-chatbot-bubble-text" id="peChatbotBubbleText"></span>' +
                '<button class="pe-chatbot-bubble-close" id="peChatbotBubbleClose">&times;</button>' +
            '</div>' +

            '<!-- Exit Intent Overlay -->' +
            '<div class="pe-chatbot-exit" id="peChatbotExit" style="display:none;">' +
                '<div class="pe-chatbot-exit-content">' +
                    '<button class="pe-chatbot-exit-close" id="peChatbotExitClose">&times;</button>' +
                    '<div class="pe-chatbot-exit-icon">🔬</div>' +
                    '<h3 id="peChatbotExitTitle">Haven\'t found the right optical component?</h3>' +
                    '<p id="peChatbotExitDesc">Tell me your application scenario and I\'ll recommend the perfect component in 10 seconds.</p>' +
                    '<button class="pe-chatbot-exit-btn" id="peChatbotExitBtn">Start Chat</button>' +
                    '<button class="pe-chatbot-exit-dismiss" id="peChatbotExitDismiss">No thanks</button>' +
                '</div>' +
            '</div>' +

            '<!-- Chat Window -->' +
            '<div class="pe-chatbot-window" id="peChatbotWindow" style="display:none;">' +
                '<!-- Header -->' +
                '<div class="pe-chatbot-header">' +
                    '<div class="pe-chatbot-header-info">' +
                        '<div class="pe-chatbot-avatar">🔬</div>' +
                        '<div>' +
                            '<div class="pe-chatbot-name" id="peChatbotName">PhotonEdge Assistant</div>' +
                            '<div class="pe-chatbot-status"><span class="pe-chatbot-status-dot"></span> Online</div>' +
                        '</div>' +
                    '</div>' +
                    '<button class="pe-chatbot-close" id="peChatbotClose">&times;</button>' +
                '</div>' +
                
                '<!-- Messages Area -->' +
                '<div class="pe-chatbot-messages" id="peChatbotMessages"></div>' +
                
                '<!-- Quick Replies Area -->' +
                '<div class="pe-chatbot-quick-replies" id="peChatbotQuickReplies"></div>' +
                
                '<!-- Input Area (hidden by default, shown for free text) -->' +
                '<div class="pe-chatbot-input-area" id="peChatbotInputArea" style="display:none;">' +
                    '<input type="text" class="pe-chatbot-input" id="peChatbotInput" placeholder="Type your message..." />' +
                    '<button class="pe-chatbot-send" id="peChatbotSend">➤</button>' +
                '</div>' +
            '</div>';

        document.body.appendChild(container);

        // Cache DOM references
        dom.container = container;
        dom.ball = document.getElementById('peChatbotBall');
        dom.badge = document.getElementById('peChatbotBadge');
        dom.bubble = document.getElementById('peChatbotBubble');
        dom.bubbleText = document.getElementById('peChatbotBubbleText');
        dom.bubbleClose = document.getElementById('peChatbotBubbleClose');
        dom.exit = document.getElementById('peChatbotExit');
        dom.exitTitle = document.getElementById('peChatbotExitTitle');
        dom.exitDesc = document.getElementById('peChatbotExitDesc');
        dom.exitBtn = document.getElementById('peChatbotExitBtn');
        dom.exitClose = document.getElementById('peChatbotExitClose');
        dom.exitDismiss = document.getElementById('peChatbotExitDismiss');
        dom.window = document.getElementById('peChatbotWindow');
        dom.messages = document.getElementById('peChatbotMessages');
        dom.quickReplies = document.getElementById('peChatbotQuickReplies');
        dom.close = document.getElementById('peChatbotClose');
        dom.inputArea = document.getElementById('peChatbotInputArea');
        dom.input = document.getElementById('peChatbotInput');
        dom.send = document.getElementById('peChatbotSend');
        dom.name = document.getElementById('peChatbotName');
    }

    /* ===== Event Binding ===== */
    function bindEvents() {
        // Ball click
        dom.ball.onclick = function() {
            toggleChat();
        };

        // Close button
        dom.close.onclick = function() {
            closeChat();
        };

        // Bubble close
        dom.bubbleClose.onclick = function() {
            dom.bubble.style.display = 'none';
        };

        // Exit intent buttons
        dom.exitBtn.onclick = function() {
            dom.exit.style.display = 'none';
            openChat();
            trackEvent('exit_intent_accepted');
        };

        dom.exitClose.onclick = function() {
            dom.exit.style.display = 'none';
        };

        dom.exitDismiss.onclick = function() {
            dom.exit.style.display = 'none';
            trackEvent('exit_intent_dismissed');
        };

        // Send button
        dom.send.onclick = function() {
            handleUserInput();
        };

        // Enter key in input
        dom.input.onkeypress = function(e) {
            if (e.keyCode === 13) {
                handleUserInput();
            }
        };

        // Exit intent detection
        if (CONFIG.exitIntentEnabled) {
            document.onmouseout = function(e) {
                if (!e.toElement && !e.relatedTarget && e.clientY < 10) {
                    triggerExitIntent();
                }
            };
        }

        // Scroll to bottom detection
        if (CONFIG.weakTriggerScroll) {
            window.onscroll = function() {
                if (state.weakTriggerFired || state.isOpen) return;
                var scrollBottom = (window.innerHeight + window.scrollY) >= document.body.offsetHeight - 100;
                if (scrollBottom) {
                    fireWeakTrigger();
                }
            };
        }
    }

    /* ===== Trigger Logic ===== */
    function startTriggers() {
        // Weak trigger: delay
        setTimeout(function() {
            if (!state.isOpen && !state.weakTriggerFired) {
                fireWeakTrigger();
            }
        }, CONFIG.weakTriggerDelay);
    }

    function fireWeakTrigger() {
        if (state.weakTriggerFired || state.isOpen) return;
        state.weakTriggerFired = true;

        var lang = getCurrentLanguage();
        var msg = lang === 'zh' ? '有选型疑问？随时问我 💡' : 'Need help choosing? Ask me anytime 💡';
        
        dom.bubbleText.textContent = msg;
        dom.bubble.style.display = 'block';
        dom.badge.style.display = 'block';
        dom.badge.textContent = '1';

        // Auto-hide bubble after 10 seconds
        setTimeout(function() {
            if (!state.isOpen) {
                dom.bubble.style.display = 'none';
            }
        }, 10000);

        trackEvent('weak_trigger_fired');
    }

    function triggerExitIntent() {
        var now = new Date().getTime();
        
        // Check cooldowns
        if (state.isOpen) return;
        if (now - state.lastExitTime < CONFIG.sessionCooldown) return;
        
        // Check if dismissed in last 24 hours
        var dismissed = getLocalStorage('pe_chatbot_exit_dismissed');
        if (dismissed) {
            var dismissedTime = parseInt(dismissed, 10);
            if (now - dismissedTime < CONFIG.exitIntentCooldown) return;
        }

        state.exitTriggerFired = true;
        state.lastExitTime = now;

        var lang = getCurrentLanguage();
        if (lang === 'zh') {
            dom.exitTitle.textContent = '还没找到合适的光学元件？';
            dom.exitDesc.textContent = '告诉我您的应用场景，10秒为您推荐合适的产品';
            dom.exitBtn.textContent = '开始咨询';
            dom.exitDismiss.textContent = '不了，谢谢';
        }

        dom.exit.style.display = 'flex';
        trackEvent('exit_intent_triggered');
    }

    /* ===== Chat Open/Close ===== */
    function toggleChat() {
        if (state.isOpen) {
            closeChat();
        } else {
            openChat();
        }
    }

    function openChat() {
        state.isOpen = true;
        dom.window.style.display = 'flex';
        dom.ball.style.display = 'none';
        dom.bubble.style.display = 'none';
        dom.badge.style.display = 'none';

        // If first open, show greeting
        if (state.currentStep === 'menu') {
            showMenu();
        }

        trackEvent('chatbot_opened');
    }

    function closeChat() {
        state.isOpen = false;
        dom.window.style.display = 'none';
        dom.ball.style.display = 'flex';
        
        trackEvent('chatbot_closed');
    }

    /* ===== Message Rendering ===== */
    function addMessage(text, sender, isHtml) {
        var msgDiv = document.createElement('div');
        msgDiv.className = 'pe-chatbot-msg pe-chatbot-msg-' + sender;
        
        if (isHtml) {
            msgDiv.innerHTML = text;
        } else {
            msgDiv.textContent = text;
        }
        
        dom.messages.appendChild(msgDiv);
        scrollToBottom();
    }

    function showTyping() {
        state.isTyping = true;
        var typingDiv = document.createElement('div');
        typingDiv.className = 'pe-chatbot-msg pe-chatbot-msg-bot pe-chatbot-typing';
        typingDiv.id = 'peChatbotTyping';
        typingDiv.innerHTML = '<span class="pe-chatbot-dot"></span><span class="pe-chatbot-dot"></span><span class="pe-chatbot-dot"></span>';
        dom.messages.appendChild(typingDiv);
        scrollToBottom();
    }

    function hideTyping() {
        state.isTyping = false;
        var typing = document.getElementById('peChatbotTyping');
        if (typing) {
            typing.parentNode.removeChild(typing);
        }
    }

    function scrollToBottom() {
        dom.messages.scrollTop = dom.messages.scrollHeight;
    }

    /* ===== Quick Replies ===== */
    function showQuickReplies(options, callback) {
        dom.quickReplies.innerHTML = '';
        var lang = getCurrentLanguage();

        for (var i = 0; i < options.length; i++) {
            var opt = options[i];
            var btn = document.createElement('button');
            btn.className = 'pe-chatbot-quick-reply';
            
            if (typeof opt === 'object') {
                btn.textContent = (opt.icon ? opt.icon + ' ' : '') + (lang === 'zh' ? (opt.labelZh || opt.label) : opt.label);
                btn.setAttribute('data-key', opt.key);
            } else {
                btn.textContent = opt;
                btn.setAttribute('data-value', opt);
            }
            
            btn.onclick = (function(o, cb) {
                return function() {
                    // Show user's choice as message
                    var displayText = this.textContent;
                    addMessage(displayText, 'user');
                    dom.quickReplies.innerHTML = '';
                    cb(o);
                };
            })(opt, callback);
            
            dom.quickReplies.appendChild(btn);
        }
    }

    function clearQuickReplies() {
        dom.quickReplies.innerHTML = '';
    }

    /* ===== Conversation Flow ===== */
    function showMenu() {
        state.currentStep = 'menu';
        var lang = getCurrentLanguage();
        var menuData = flow.menu[lang] || flow.menu.en;

        showTyping();
        setTimeout(function() {
            hideTyping();
            addMessage(menuData.greeting, 'bot');
            
            var options = [];
            for (var i = 0; i < menuData.options.length; i++) {
                options.push(menuData.options[i]);
            }
            
            showQuickReplies(options, function(opt) {
                handleMenuChoice(opt.key);
            });
        }, 800);
    }

    function handleMenuChoice(choice) {
        trackEvent('menu_choice', { choice: choice });
        
        switch (choice) {
            case 'product_recommend':
                startProductRecommend();
                break;
            case 'custom_consult':
                startCustomConsult();
                break;
            case 'quote_delivery':
                showQuoteDelivery();
                break;
            case 'other_question':
                showOtherQuestions();
                break;
            default:
                showMenu();
        }
    }

    /* ===== Product Recommendation Flow ===== */
    function startProductRecommend() {
        state.currentStep = 'product_recommend';
        state.userData = { flow: 'product_recommend', step: 0 };
        askProductRecommendStep(0);
    }

    function askProductRecommendStep(stepIndex) {
        var lang = getCurrentLanguage();
        var steps = flow.product_recommend.steps;
        
        if (stepIndex >= steps.length) {
            showProductRecommendResult();
            return;
        }

        var step = steps[stepIndex];
        var stepData = step[lang] || step.en;

        showTyping();
        setTimeout(function() {
            hideTyping();
            addMessage(stepData.question, 'bot');
            
            var options = [];
            for (var i = 0; i < stepData.options.length; i++) {
                options.push(stepData.options[i]);
            }
            
            showQuickReplies(options, function(opt) {
                var value = typeof opt === 'object' ? opt : opt;
                state.userData[step.key] = value;
                state.userData.step = stepIndex + 1;
                askProductRecommendStep(stepIndex + 1);
            });
        }, 600);
    }

    function showProductRecommendResult() {
        var lang = getCurrentLanguage();
        var app = state.userData.application || 'other';
        var componentType = state.userData.component_type || '';
        
        // Find matching products from knowledge base
        var recommendations = findProducts(app, componentType);
        
        showTyping();
        setTimeout(function() {
            hideTyping();
            
            var resultMsg = lang === 'zh' ? flow.product_recommend.result_zh : flow.product_recommend.result_en;
            addMessage(resultMsg, 'bot');
            
            // Show product recommendations as cards
            if (recommendations.length > 0) {
                var html = '<div class="pe-chatbot-products">';
                for (var i = 0; i < Math.min(recommendations.length, 3); i++) {
                    var p = recommendations[i];
                    var name = lang === 'zh' ? (p.nameZh || p.name) : p.name;
                    html += '<div class="pe-chatbot-product-card">' +
                        '<div class="pe-chatbot-product-name">' + name + '</div>' +
                        '<div class="pe-chatbot-product-category">' + p.category + '</div>' +
                        '<a href="/contact.html?product=' + encodeURIComponent(p.slug) + '" class="pe-chatbot-product-link" onclick="PhotonEdgeChatbot.trackEvent(\'product_recommendation_click\', {product: \'' + p.slug + '\'})">' + 
                        (lang === 'zh' ? '查看详情 →' : 'View Details →') + '</a>' +
                    '</div>';
                }
                html += '</div>';
                addMessage(html, 'bot', true);
            } else {
                // Fallback: suggest contacting engineer
                var fallbackMsg = lang === 'zh' ? 
                    '根据您的需求，我建议您咨询我们的技术工程师获取专业推荐。' :
                    'Based on your requirements, I recommend consulting our technical team for personalized product recommendations.';
                addMessage(fallbackMsg, 'bot');
            }
            
            // Show CTA
            var ctaMsg = lang === 'zh' ? flow.product_recommend.cta_zh : flow.product_recommend.cta_en;
            addMessage(ctaMsg, 'bot');
            
            // Show lead form
            showLeadForm();
            
            trackEvent('product_recommendation_complete', {
                application: app,
                wavelength: state.userData.wavelength,
                component_type: componentType
            });
        }, 1000);
    }

    function findProducts(application, componentType) {
        var results = [];
        if (typeof PRODUCTS === 'undefined') return results;
        
        var appData = KB.applications[application];
        if (!appData) return results;
        
        // Map application to product categories
        var categoryMap = {
            'laser': ['Optical Mirrors', 'Optical Lenses', 'Optical Windows'],
            'medical': ['Optical Lenses', 'Optical Windows', 'Optical Filters'],
            'research': ['Optical Lenses', 'Optical Mirrors', 'Optical Prisms', 'Optical Wave Plates'],
            'telecom': ['Optical Lenses', 'Optical Filters', 'Optical Polarizers'],
            'defense': ['Optical Windows', 'Optical Mirrors', 'Optical Prisms'],
            'industrial': ['Optical Prisms', 'Optical Mirrors', 'Optical Lenses'],
            'semiconductor': ['Optical Lenses', 'Optical Windows', 'Optical Filters'],
            'other': []
        };
        
        // Map component type to category
        var typeMap = {
            'Lens': 'Optical Lenses',
            '透镜': 'Optical Lenses',
            'Mirror': 'Optical Mirrors',
            '反射镜': 'Optical Mirrors',
            'Window': 'Optical Windows',
            '窗口片': 'Optical Windows',
            'Prism': 'Optical Prisms',
            '棱镜': 'Optical Prisms',
            'Filter': 'Optical Filters',
            '滤光片': 'Optical Filters',
            'Beamsplitter': 'Optical Beamsplitters',
            '分光镜': 'Optical Beamsplitters',
            'Waveplate': 'Optical Wave Plates',
            '波片': 'Optical Wave Plates',
            'Polarizer': 'Optical Polarizers',
            '偏振器': 'Optical Polarizers'
        };
        
        var targetCategories = [];
        if (componentType && typeMap[componentType]) {
            targetCategories = [typeMap[componentType]];
        } else if (categoryMap[application]) {
            targetCategories = categoryMap[application];
        }
        
        // Find products in target categories
        for (var i = 0; i < PRODUCTS.length && results.length < 3; i++) {
            var p = PRODUCTS[i];
            for (var j = 0; j < targetCategories.length; j++) {
                if (p.category === targetCategories[j]) {
                    results.push(p);
                    break;
                }
            }
        }
        
        return results;
    }

    /* ===== Custom Consultation Flow ===== */
    function startCustomConsult() {
        state.currentStep = 'custom_consult';
        state.userData = { flow: 'custom_consult', step: 0 };
        askCustomConsultStep(0);
    }

    function askCustomConsultStep(stepIndex) {
        var lang = getCurrentLanguage();
        var steps = flow.custom_consult.steps;
        
        if (stepIndex >= steps.length) {
            showCustomConsultResult();
            return;
        }

        var step = steps[stepIndex];
        var stepData = step[lang] || step.en;

        showTyping();
        setTimeout(function() {
            hideTyping();
            addMessage(stepData.question, 'bot');
            
            showQuickReplies(stepData.options, function(opt) {
                state.userData[step.key] = opt;
                state.userData.step = stepIndex + 1;
                askCustomConsultStep(stepIndex + 1);
            });
        }, 600);
    }

    function showCustomConsultResult() {
        var lang = getCurrentLanguage();
        
        showTyping();
        setTimeout(function() {
            hideTyping();
            
            var resultMsg = lang === 'zh' ? flow.custom_consult.result_zh : flow.custom_consult.result_en;
            addMessage(resultMsg, 'bot');
            
            var ctaMsg = lang === 'zh' ? flow.custom_consult.cta_zh : flow.custom_consult.cta_en;
            addMessage(ctaMsg, 'bot');
            
            // Show lead form
            showLeadForm();
            
            trackEvent('custom_consult_complete', {
                product_type: state.userData.product_type,
                spec_level: state.userData.spec_level,
                quantity: state.userData.quantity
            });
        }, 800);
    }

    /* ===== Quote & Delivery ===== */
    function showQuoteDelivery() {
        state.currentStep = 'quote_delivery';
        var lang = getCurrentLanguage();
        var data = flow.quote_delivery[lang] || flow.quote_delivery.en;

        showTyping();
        setTimeout(function() {
            hideTyping();
            addMessage(data.intro, 'bot');
            
            showQuickReplies(data.topics, function(opt) {
                var key = typeof opt === 'object' ? opt.key : opt;
                showFaqAnswer(key);
            });
        }, 600);
    }

    /* ===== Other Questions ===== */
    function showOtherQuestions() {
        state.currentStep = 'other_question';
        var lang = getCurrentLanguage();
        var data = flow.other_question[lang] || flow.other_question.en;

        showTyping();
        setTimeout(function() {
            hideTyping();
            addMessage(data.intro, 'bot');
            
            showQuickReplies(data.topics, function(opt) {
                var key = typeof opt === 'object' ? opt.key : opt;
                showFaqAnswer(key);
            });
        }, 600);
    }

    /* ===== FAQ Answers ===== */
    function showFaqAnswer(key) {
        var lang = getCurrentLanguage();
        var answer = KB.faq[key];
        
        showTyping();
        setTimeout(function() {
            hideTyping();
            
            if (answer) {
                var text = lang === 'zh' ? (answer.zh || answer.en) : answer.en;
                addMessage(text, 'bot');
            } else {
                var safetyMsg = lang === 'zh' ? safetyMessages.complex_custom.zh : safetyMessages.complex_custom.en;
                addMessage(safetyMsg, 'bot');
            }
            
            // Offer more options
            setTimeout(function() {
                var moreLang = lang === 'zh' ? '还有其他问题吗？' : 'Any other questions?';
                addMessage(moreLang, 'bot');
                
                var moreOptions = lang === 'zh' ? [
                    { key: 'back_menu', label: '返回主菜单' },
                    { key: 'contact_engineer', label: '联系工程师' },
                    { key: 'no_more', label: '没有问题了' }
                ] : [
                    { key: 'back_menu', label: 'Back to Menu' },
                    { key: 'contact_engineer', label: 'Contact Engineer' },
                    { key: 'no_more', label: 'No more questions' }
                ];
                
                showQuickReplies(moreOptions, function(opt) {
                    var k = typeof opt === 'object' ? opt.key : opt;
                    if (k === 'back_menu') {
                        showMenu();
                    } else if (k === 'contact_engineer') {
                        showLeadForm();
                    } else {
                        var byeMsg = lang === 'zh' ? '感谢咨询！如有需要随时找我。祝您工作顺利！😊' : 'Thanks for chatting! Feel free to reach out anytime. Have a great day! 😊';
                        addMessage(byeMsg, 'bot');
                        trackEvent('chatbot_conversation_complete');
                    }
                });
            }, 500);
        }, 800);
    }

    /* ===== Lead Collection Form ===== */
    function showLeadForm() {
        var lang = getCurrentLanguage();
        var formData = leadForm[lang] || leadForm.en;
        
        var html = '<div class="pe-chatbot-lead-form">' +
            '<div class="pe-chatbot-lead-form-title">' + formData.title + '</div>' +
            '<div class="pe-chatbot-lead-form-subtitle">' + formData.subtitle + '</div>' +
            '<form id="peChatbotLeadForm">';
        
        var fieldKeys = CONFIG.leadFormFields;
        for (var i = 0; i < fieldKeys.length; i++) {
            var key = fieldKeys[i];
            var field = formData.fields[key];
            html += '<div class="pe-chatbot-form-group">' +
                '<label>' + field.label + (field.required ? ' *' : '') + '</label>' +
                (key === 'requirement' ? 
                    '<textarea class="pe-chatbot-form-input" name="' + key + '" placeholder="' + field.placeholder + '" rows="3"' + (field.required ? ' required' : '') + '></textarea>' :
                    '<input type="' + (key === 'email' ? 'email' : 'text') + '" class="pe-chatbot-form-input" name="' + key + '" placeholder="' + field.placeholder + '"' + (field.required ? ' required' : '') + ' />') +
            '</div>';
        }
        
        html += '<button type="submit" class="pe-chatbot-form-submit">' + formData.submit + '</button>' +
            '</form></div>';
        
        addMessage(html, 'bot', true);
        
        // Bind form submit
        setTimeout(function() {
            var form = document.getElementById('peChatbotLeadForm');
            if (form) {
                form.onsubmit = function(e) {
                    if (e.preventDefault) e.preventDefault();
                    handleLeadSubmit(formData);
                    return false;
                };
            }
        }, 100);
    }

    function handleLeadSubmit(formData) {
        var form = document.getElementById('peChatbotLeadForm');
        if (!form) return;
        
        var inputs = form.getElementsByTagName('input');
        var textareas = form.getElementsByTagName('textarea');
        var leadData = {};
        
        var i;
        for (i = 0; i < inputs.length; i++) {
            leadData[inputs[i].name] = inputs[i].value;
        }
        for (i = 0; i < textareas.length; i++) {
            leadData[textareas[i].name] = textareas[i].value;
        }
        
        // Validate required fields
        if (!leadData.name || !leadData.email) {
            var lang = getCurrentLanguage();
            var msg = lang === 'zh' ? '请填写姓名和邮箱（必填项）' : 'Please fill in name and email (required fields)';
            addMessage(msg, 'bot');
            return;
        }
        
        // Store lead data
        leadData.flow = state.userData.flow;
        leadData.userData = JSON.stringify(state.userData);
        leadData.timestamp = new Date().toISOString();
        leadData.page = window.location.href;
        
        // Save to localStorage for now (in production, this would POST to a server)
        saveLead(leadData);
        
        // Show success message
        var lang = getCurrentLanguage();
        showTyping();
        setTimeout(function() {
            hideTyping();
            addMessage(formData.success, 'bot');
            
            // Offer restart
            var options = lang === 'zh' ? [
                { key: 'back_menu', label: '继续咨询' },
                { key: 'close', label: '结束对话' }
            ] : [
                { key: 'back_menu', label: 'Continue Chat' },
                { key: 'close', label: 'End Chat' }
            ];
            
            showQuickReplies(options, function(opt) {
                var k = typeof opt === 'object' ? opt.key : opt;
                if (k === 'back_menu') {
                    showMenu();
                } else {
                    closeChat();
                }
            });
        }, 600);
        
        trackEvent('lead_submitted', {
            flow: leadData.flow,
            email_domain: leadData.email ? leadData.email.split('@')[1] : ''
        });
    }

    function saveLead(leadData) {
        // Save to localStorage
        try {
            var existing = getLocalStorage('pe_chatbot_leads');
            var leads = existing ? JSON.parse(existing) : [];
            leads.push(leadData);
            setLocalStorage('pe_chatbot_leads', JSON.stringify(leads));
        } catch (e) {
            // Silently fail
        }
        
        // In production, POST to server
        // For now, also send via email using FormSubmit
        sendLeadByEmail(leadData);
    }

    function sendLeadByEmail(leadData) {
        // Use FormSubmit to send lead notification email
        // This is a simple approach - in production you'd have a proper backend
        try {
            var formData = new FormData();
            formData.append('_subject', 'PhotonEdge Chatbot Lead - ' + (leadData.flow || 'general'));
            formData.append('_template', 'table');
            formData.append('Name', leadData.name || '');
            formData.append('Email', leadData.email || '');
            formData.append('Company', leadData.company || '');
            formData.append('Phone', leadData.phone || '');
            formData.append('Requirement', leadData.requirement || '');
            formData.append('Flow', leadData.flow || '');
            formData.append('Page', leadData.page || '');
            formData.append('Timestamp', leadData.timestamp || '');
            formData.append('User Data', leadData.userData || '');
            
            // Send via XMLHttpRequest (ES5 compatible)
            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'https://formsubmit.co/ajax/sales@photonedgeoptics.com', true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.setRequestHeader('Accept', 'application/json');
            xhr.send(JSON.stringify({
                '_subject': 'PhotonEdge Chatbot Lead - ' + (leadData.flow || 'general'),
                '_template': 'table',
                'Name': leadData.name || '',
                'Email': leadData.email || '',
                'Company': leadData.company || '',
                'Phone': leadData.phone || '',
                'Requirement': leadData.requirement || '',
                'Flow': leadData.flow || '',
                'Page': leadData.page || '',
                'Timestamp': leadData.timestamp || '',
                'User_Data': leadData.userData || ''
            }));
        } catch (e) {
            // Silently fail - lead is still saved in localStorage
        }
    }

    /* ===== User Input Handler ===== */
    function handleUserInput() {
        var text = dom.input.value.trim();
        if (!text) return;
        
        addMessage(text, 'user');
        dom.input.value = '';
        
        // Simple keyword matching for common questions
        var lang = getCurrentLanguage();
        var lowerText = text.toLowerCase();
        
        // Check for common keywords
        if (lowerText.indexOf('price') >= 0 || lowerText.indexOf('cost') >= 0 || lowerText.indexOf('quote') >= 0 ||
            lowerText.indexOf('价格') >= 0 || lowerText.indexOf('报价') >= 0) {
            showFaqAnswer('moq');
            return;
        }
        
        if (lowerText.indexOf('delivery') >= 0 || lowerText.indexOf('lead time') >= 0 || lowerText.indexOf('ship') >= 0 ||
            lowerText.indexOf('交期') >= 0 || lowerText.indexOf('发货') >= 0) {
            showFaqAnswer('lead-time');
            return;
        }
        
        if (lowerText.indexOf('sample') >= 0 || lowerText.indexOf('样品') >= 0) {
            showFaqAnswer('sample');
            return;
        }
        
        if (lowerText.indexOf('custom') >= 0 || lowerText.indexOf('oem') >= 0 || lowerText.indexOf('定制') >= 0) {
            startCustomConsult();
            return;
        }
        
        // Default: suggest contacting engineer
        var lang = getCurrentLanguage();
        var safetyMsg = lang === 'zh' ? safetyMessages.uncertain_param.zh : safetyMessages.uncertain_param.en;
        addMessage(safetyMsg, 'bot');
        showLeadForm();
    }

    /* ===== GA4 Event Tracking ===== */
    function trackEvent(eventName, params) {
        if (!CONFIG.gaEvents) return;
        try {
            if (typeof gtag === 'function') {
                gtag('event', eventName, params || {});
            }
        } catch (e) {
            // Silently fail
        }
    }

    /* ===== LocalStorage Helpers ===== */
    function getLocalStorage(key) {
        try {
            return localStorage.getItem(key);
        } catch (e) {
            return null;
        }
    }

    function setLocalStorage(key, value) {
        try {
            localStorage.setItem(key, value);
        } catch (e) {
            // Silently fail
        }
    }

    /* ===== Language Detection ===== */
    function getCurrentLanguage() {
        try {
            if (typeof getCurrentLang === 'function') {
                return getCurrentLang();
            }
            var lang = localStorage.getItem('photonedge_lang');
            return lang || 'en';
        } catch (e) {
            return 'en';
        }
    }

    /* ===== Public API ===== */
    return {
        init: init,
        open: openChat,
        close: closeChat,
        trackEvent: trackEvent,
        getState: function() { return state; },
        getLeads: function() {
            try {
                var leads = getLocalStorage('pe_chatbot_leads');
                return leads ? JSON.parse(leads) : [];
            } catch (e) {
                return [];
            }
        }
    };
})();

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
        PhotonEdgeChatbot.init();
    });
} else {
    PhotonEdgeChatbot.init();
}
