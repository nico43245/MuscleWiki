console.log('🛠 scripts.js încărcat!');
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.hotspot').forEach(el => {
    el.addEventListener('click', () => {
        window.location.href = el.getAttribute('data-url');
    });
  });
});