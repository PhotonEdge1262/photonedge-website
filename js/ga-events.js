// ga-events.js - PhotonEdge GA4 Event Tracking Reference
// Add this file reference to all pages
var PHOTONEDGE_EVENTS = {
  // CTA Events
  'quote_click': { category: 'conversion', label: 'Request a Quote clicked' },
  'upload_drawing': { category: 'conversion', label: 'Upload Your Drawing clicked' },
  'ask_engineer': { category: 'conversion', label: 'Ask Engineer clicked' },
  'ai_engineer_click': { category: 'engagement', label: 'AI Optical Engineer clicked' },
  // Form Events
  'inquiry_submit': { category: 'conversion', label: 'Contact form submitted' },
  'file_upload': { category: 'conversion', label: 'File uploaded on form' },
  // Content Events
  'pdf_download': { category: 'content', label: 'Technical PDF downloaded' },
  'product_view': { category: 'content', label: 'Product page viewed' },
  // Product Advisor Events
  'advisor_recommendation': { category: 'engagement', label: 'AI recommendation received' },
  'advisor_chat_turn': { category: 'engagement', label: 'Chat conversation turn' }
};
