// PhotonEdge Customer Service Chat Widget
// Pure frontend JS, no dependencies, compatible with legacy browsers

// Chat Widget translations
var chatWidgetTranslations = {
    en: {
        chatTitle: "Chat with Us",
        chatSubtitle: "How can we help you?",
        faqTitle: "Frequently Asked Questions",
        chatPlaceholder: "Type your message...",
        sendBtn: "Send",
        closeChat: "Close chat",
        openChat: "Chat with us",
        noAnswer: "Still need help?",
        contactWhatsApp: "Contact via WhatsApp",
        contactEmail: "Contact via Email",
        faq1Q: "What's your MOQ?",
        faq1A: "No minimum order for standard products. Custom orders typically start from 10 pieces.",
        faq2Q: "What's your lead time?",
        faq2A: "Standard products: 3-5 business days. Custom optics: 15-25 business days depending on complexity.",
        faq3Q: "Do you provide test reports?",
        faq3A: "Yes, every product ships with a Certificate of Conformance. Detailed test reports with interferometry data available upon request.",
        faq4Q: "Can you customize optics?",
        faq4A: "Absolutely. We offer custom sizes, coatings, and materials. Share your specs and we'll quote within 24 hours.",
        faq5Q: "How to request a quote?",
        faq5A: "Email sales@photonedgeoptics.com or use our RFQ form. We respond within 24 hours."
    },
    zh: {
        chatTitle: "在线咨询",
        chatSubtitle: "有什么可以帮您？",
        faqTitle: "常见问题",
        chatPlaceholder: "输入您的问题...",
        sendBtn: "发送",
        closeChat: "关闭聊天",
        openChat: "在线咨询",
        noAnswer: "还需要其他帮助？",
        contactWhatsApp: "通过微信联系",
        contactEmail: "通过邮件联系",
        faq1Q: "最小起订量是多少？",
        faq1A: "标准产品无最小起订量要求。定制产品通常从10件起订。",
        faq2Q: "交货周期多久？",
        faq2A: "标准产品：3-5个工作日。定制光学元件：15-25个工作日，视复杂程度而定。",
        faq3Q: "是否提供检测报告？",
        faq3A: "是的，每件产品都附带符合性证书。如有需要，可提供包含干涉仪数据的详细测试报告。",
        faq4Q: "可以定制光学元件吗？",
        faq4A: "当然可以。我们提供定制尺寸、镀膜和材料。请发送您的规格要求，我们将在24小时内提供报价。",
        faq5Q: "如何询价？",
        faq5A: "请发送邮件至 sales@photonedgeoptics.com 或填写询价表单。我们将在24小时内回复。"
    }
};

// Get current language
function getChatLanguage() {
    if (typeof getCurrentLanguage === 'function') {
        return getCurrentLanguage();
    }
    var lang = 'en';
    if (typeof localStorage !== 'undefined') {
        lang = localStorage.getItem('photonedge_lang') || 'en';
    }
    return lang;
}

// Get translation
function chatT(key) {
    var lang = getChatLanguage();
    var translations = chatWidgetTranslations[lang] || chatWidgetTranslations['en'];
    return translations[key] || key;
}

// Create chat widget HTML
function createChatWidget() {
    // Check if already exists
    if (document.getElementById('photonedge-chat-widget')) {
        return;
    }

    var widgetHTML = '\
        <div id="photonedge-chat-widget" class="chat-widget">\
            <button id="chat-toggle-btn" class="chat-toggle-btn" onclick="toggleChat()">\
                <svg id="chat-icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\
                    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>\
                </svg>\
                <svg id="chat-close-icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display:none">\
                    <line x1="18" y1="6" x2="6" y2="18"></line>\
                    <line x1="6" y1="6" x2="18" y2="18"></line>\
                </svg>\
            </button>\
            <div id="chat-window" class="chat-window">\
                <div class="chat-header">\
                    <div class="chat-header-info">\
                        <h4>' + chatT('chatTitle') + '</h4>\
                        <p>' + chatT('chatSubtitle') + '</p>\
                    </div>\
                    <button class="chat-minimize-btn" onclick="toggleChat()">\
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\
                            <line x1="5" y1="12" x2="19" y2="12"></line>\
                        </svg>\
                    </button>\
                </div>\
                <div class="chat-body">\
                    <div class="faq-section">\
                        <h5>' + chatT('faqTitle') + '</h5>\
                        <div class="faq-list">\
                            <button class="faq-item" onclick="showFaqAnswer(1)">\
                                <span class="faq-question">' + chatT('faq1Q') + '</span>\
                            </button>\
                            <button class="faq-item" onclick="showFaqAnswer(2)">\
                                <span class="faq-question">' + chatT('faq2Q') + '</span>\
                            </button>\
                            <button class="faq-item" onclick="showFaqAnswer(3)">\
                                <span class="faq-question">' + chatT('faq3Q') + '</span>\
                            </button>\
                            <button class="faq-item" onclick="showFaqAnswer(4)">\
                                <span class="faq-question">' + chatT('faq4Q') + '</span>\
                            </button>\
                            <button class="faq-item" onclick="showFaqAnswer(5)">\
                                <span class="faq-question">' + chatT('faq5Q') + '</span>\
                            </button>\
                        </div>\
                    </div>\
                    <div id="faq-answers" class="faq-answers" style="display:none;"></div>\
                    <div id="chat-messages" class="chat-messages"></div>\
                </div>\
                <div class="chat-footer">\
                    <p class="no-answer-text">' + chatT('noAnswer') + '</p>\
                    <div class="contact-buttons">\
                        <a href="https://wa.me/8613693009175" target="_blank" class="contact-btn whatsapp-btn">\
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">\
                                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>\
                            </svg>\
                            ' + chatT('contactWhatsApp') + '\
                        </a>\
                        <a href="mailto:sales@photonedgeoptics.com" class="contact-btn email-btn">\
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\
                                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>\
                                <polyline points="22,6 12,13 2,6"></polyline>\
                            </svg>\
                            ' + chatT('contactEmail') + '\
                        </a>\
                    </div>\
                </div>\
            </div>\
        </div>\
    ';

    // Insert before closing body tag
    var wrapper = document.createElement('div');
    wrapper.innerHTML = widgetHTML;
    document.body.appendChild(wrapper);
}

// Toggle chat window
function toggleChat() {
    var chatWindow = document.getElementById('chat-window');
    var chatIcon = document.getElementById('chat-icon');
    var closeIcon = document.getElementById('chat-close-icon');
    var toggleBtn = document.getElementById('chat-toggle-btn');

    if (!chatWindow) return;

    if (chatWindow.style.display === 'none' || !chatWindow.style.display) {
        chatWindow.style.display = 'flex';
        if (chatIcon) chatIcon.style.display = 'none';
        if (closeIcon) closeIcon.style.display = 'block';
        toggleBtn.classList.add('active');
    } else {
        chatWindow.style.display = 'none';
        if (chatIcon) chatIcon.style.display = 'block';
        if (closeIcon) closeIcon.style.display = 'none';
        toggleBtn.classList.remove('active');
    }
}

// Show FAQ answer
function showFaqAnswer(num) {
    var faqAnswers = document.getElementById('faq-answers');
    var faqSection = document.querySelector('.faq-section');
    if (!faqAnswers || !faqSection) return;

    var answers = {
        1: { q: chatT('faq1Q'), a: chatT('faq1A') },
        2: { q: chatT('faq2Q'), a: chatT('faq2A') },
        3: { q: chatT('faq3Q'), a: chatT('faq3A') },
        4: { q: chatT('faq4Q'), a: chatT('faq4A') },
        5: { q: chatT('faq5Q'), a: chatT('faq5A') }
    };

    var faq = answers[num];
    if (!faq) return;

    faqAnswers.innerHTML = '\
        <div class="faq-answer-item">\
            <div class="faq-answer-question">' + faq.q + '</div>\
            <div class="faq-answer-text">' + faq.a + '</div>\
        </div>\
        <button class="back-to-faq-btn" onclick="backToFaq()">\
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\
                <line x1="19" y1="12" x2="5" y2="12"></line>\
                <polyline points="12 19 5 12 12 5"></polyline>\
            </svg>\
            Back to FAQ\
        </button>\
    ';
    faqAnswers.style.display = 'block';
    faqSection.style.display = 'none';
    faqAnswers.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// Back to FAQ list
function backToFaq() {
    var faqAnswers = document.getElementById('faq-answers');
    var faqSection = document.querySelector('.faq-section');
    if (faqAnswers) faqAnswers.style.display = 'none';
    if (faqSection) faqSection.style.display = 'block';
}

// Initialize chat widget when DOM is ready
function initChatWidget() {
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', createChatWidget);
    } else {
        createChatWidget();
    }
}

// Run on load
initChatWidget();
