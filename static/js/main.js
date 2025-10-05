// Main JavaScript for Iberdrola AI Marketing Suite - Fluent 2 Enhanced

// ==================== FLUENT 2 REVEAL EFFECT ====================
// Track mouse position for reveal effect
document.addEventListener('mousemove', (e) => {
    document.querySelectorAll('.btn, .card').forEach(element => {
        const rect = element.getBoundingClientRect();
        const x = ((e.clientX - rect.left) / rect.width) * 100;
        const y = ((e.clientY - rect.top) / rect.height) * 100;
        element.style.setProperty('--mouse-x', `${x}%`);
        element.style.setProperty('--mouse-y', `${y}%`);
    });
});

// ==================== INITIALIZATION ====================
document.addEventListener('DOMContentLoaded', function() {
    // Initialize Fluent animations
    initFluentAnimations();
    
    // Auto-hide flash messages after 5 seconds
    const flashMessages = document.querySelectorAll('.alert');
    flashMessages.forEach(function(message) {
        setTimeout(function() {
            message.style.transition = 'opacity 0.5s';
            message.style.opacity = '0';
            setTimeout(function() {
                message.remove();
            }, 500);
        }, 5000);
    });

    // Animate metric values on dashboard with stagger
    const metricValues = document.querySelectorAll('.metric-value');
    metricValues.forEach(function(el, index) {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        setTimeout(function() {
            el.style.transition = 'all 0.6s cubic-bezier(0, 0.5, 0.3, 1)';
            el.style.opacity = '1';
            el.style.transform = 'translateY(0)';
        }, 100 + (index * 50));
    });

    // Animate cards with stagger
    const cards = document.querySelectorAll('.card, .metric-card');
    cards.forEach(function(card, index) {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        setTimeout(function() {
            card.style.transition = 'all 0.6s cubic-bezier(0, 0.5, 0.3, 1)';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 150 + (index * 75));
    });

    // Smooth scroll for navigation
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add ripple effect to buttons
    addRippleEffect();
    
    // Initialize documentation panel
    initDocPanel();
});

// ==================== FLUENT ANIMATIONS ====================
function initFluentAnimations() {
    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe all cards and sections
    document.querySelectorAll('.card, .metric-card, section').forEach(el => {
        observer.observe(el);
    });
}

// ==================== RIPPLE EFFECT ====================
function addRippleEffect() {
    document.querySelectorAll('.btn').forEach(button => {
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;

            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.classList.add('ripple');

            this.appendChild(ripple);

            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });
}

// Add ripple CSS dynamically
const style = document.createElement('style');
style.textContent = `
    .ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.6);
        transform: scale(0);
        animation: ripple-animation 0.6s ease-out;
        pointer-events: none;
    }

    @keyframes ripple-animation {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Utility function to format numbers
function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}

// Utility function to format currency
function formatCurrency(num) {
    return '€' + formatNumber(num);
}

// Copy to clipboard function
function copyToClipboard(text) {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.style.position = 'fixed';
    textarea.style.opacity = '0';
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    
    // Show notification
    showNotification('Copiado al portapapeles', 'success');
}

// Show notification
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type}`;
    notification.innerHTML = `
        <span class="alert-icon">
            ${type === 'success' ? '✅' : type === 'error' ? '❌' : type === 'warning' ? '⚠️' : 'ℹ️'}
        </span>
        <span class="alert-message">${message}</span>
        <button class="alert-close" onclick="this.parentElement.remove()">×</button>
    `;
    
    const container = document.querySelector('.flash-messages') || document.querySelector('.content-wrapper');
    if (container) {
        container.insertBefore(notification, container.firstChild);
        setTimeout(() => {
            notification.style.transition = 'opacity 0.5s';
            notification.style.opacity = '0';
            setTimeout(() => notification.remove(), 500);
        }, 3000);
    }
}

// Loading state for buttons
function setButtonLoading(button, loading) {
    if (loading) {
        button.dataset.originalText = button.innerHTML;
        button.disabled = true;
        button.innerHTML = '<div class="loading-spinner" style="width: 20px; height: 20px; margin: 0 auto;"></div>';
    } else {
        button.disabled = false;
        button.innerHTML = button.dataset.originalText || button.innerHTML;
    }
}

// Confirm dialog
function confirmAction(message, callback) {
    if (confirm(message)) {
        callback();
    }
}

// Format date
function formatDate(date) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(date).toLocaleDateString('es-ES', options);
}

// Format time
function formatTime(date) {
    const options = { hour: '2-digit', minute: '2-digit' };
    return new Date(date).toLocaleTimeString('es-ES', options);
}

// Debounce function for search inputs
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Export functions to global scope
window.copyToClipboard = copyToClipboard;
window.showNotification = showNotification;
window.setButtonLoading = setButtonLoading;
window.confirmAction = confirmAction;
window.formatNumber = formatNumber;
window.formatCurrency = formatCurrency;
window.formatDate = formatDate;
window.formatTime = formatTime;
window.debounce = debounce;

// ==================== DOCUMENTATION PANEL ====================
function initDocPanel() {
    const toggleBtn = document.querySelector('.doc-panel-toggle');
    const panel = document.querySelector('.doc-panel');
    const closeBtn = document.querySelector('.doc-panel-close');
    const mainContent = document.querySelector('.main-content');
    const editBtn = document.querySelector('.doc-edit-btn');
    
    if (!panel) return;
    
    // Panel is open by default, toggle button shows/hides it
    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            const isClosed = panel.classList.contains('closed');
            
            if (isClosed) {
                panel.classList.remove('closed');
                toggleBtn.classList.remove('panel-closed');
                if (mainContent) mainContent.classList.remove('doc-panel-closed');
            } else {
                panel.classList.add('closed');
                toggleBtn.classList.add('panel-closed');
                if (mainContent) mainContent.classList.add('doc-panel-closed');
            }
        });
    }
    
    if (closeBtn) {
        closeBtn.addEventListener('click', () => {
            panel.classList.add('closed');
            if (toggleBtn) toggleBtn.classList.add('panel-closed');
            if (mainContent) mainContent.classList.add('doc-panel-closed');
        });
    }
    
    // Edit mode functionality
    if (editBtn) {
        let isEditMode = false;
        
        editBtn.addEventListener('click', () => {
            isEditMode = !isEditMode;
            toggleEditMode(isEditMode);
            
            if (isEditMode) {
                editBtn.classList.add('active');
                editBtn.innerHTML = '<span>💾</span> Guardar Cambios';
            } else {
                editBtn.classList.remove('active');
                editBtn.innerHTML = '<span>✏️</span> Editar';
                saveDocumentation();
            }
        });
    }
    
    // Close on ESC key (only if in edit mode, cancel edit)
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            const editBtn = document.querySelector('.doc-edit-btn');
            if (editBtn && editBtn.classList.contains('active')) {
                editBtn.click(); // Toggle off edit mode
            }
        }
    });
}

function toggleEditMode(enable) {
    const contentSections = document.querySelectorAll('.doc-section-content');
    
    contentSections.forEach(section => {
        if (enable) {
            section.setAttribute('contenteditable', 'true');
            section.style.cursor = 'text';
        } else {
            section.setAttribute('contenteditable', 'false');
            section.style.cursor = 'default';
        }
    });
}

function saveDocumentation() {
    // Show save indicator
    showSaveIndicator();
    
    // Get all content sections
    const sections = document.querySelectorAll('.doc-section');
    const docData = [];
    
    sections.forEach((section, index) => {
        const title = section.querySelector('.doc-section-title')?.textContent.trim();
        const content = section.querySelector('.doc-section-content')?.innerHTML;
        
        docData.push({
            index: index,
            title: title,
            content: content
        });
    });
    
    // Save to localStorage (you can change this to save to backend)
    const pageId = window.location.pathname;
    localStorage.setItem(`doc_content_${pageId}`, JSON.stringify(docData));
    
    console.log('Documentation saved:', docData);
}

function loadDocumentation() {
    const pageId = window.location.pathname;
    const savedData = localStorage.getItem(`doc_content_${pageId}`);
    
    if (savedData) {
        try {
            const docData = JSON.parse(savedData);
            const sections = document.querySelectorAll('.doc-section');
            
            docData.forEach((data, index) => {
                if (sections[index]) {
                    const contentDiv = sections[index].querySelector('.doc-section-content');
                    if (contentDiv && data.content) {
                        contentDiv.innerHTML = data.content;
                    }
                }
            });
            
            console.log('Documentation loaded from localStorage');
        } catch (e) {
            console.error('Error loading documentation:', e);
        }
    }
}

function showSaveIndicator() {
    // Create or get save indicator
    let indicator = document.querySelector('.doc-save-indicator');
    
    if (!indicator) {
        indicator = document.createElement('div');
        indicator.className = 'doc-save-indicator';
        indicator.innerHTML = '<span>✓</span> Cambios guardados';
        document.body.appendChild(indicator);
    }
    
    indicator.classList.add('show');
    
    setTimeout(() => {
        indicator.classList.remove('show');
    }, 3000);
}

// Load saved documentation on page load
document.addEventListener('DOMContentLoaded', () => {
    setTimeout(loadDocumentation, 100);
});
