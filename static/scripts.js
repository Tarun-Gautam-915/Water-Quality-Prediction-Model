// This script enables toggling the hidden content on hover of the flowchart buttons
const flowchartButtons = document.querySelectorAll('.flowchart-btn');

flowchartButtons.forEach(button => {
    button.addEventListener('mouseover', function() {
        const contentId = button.getAttribute('data-content');
        const content = document.getElementById(contentId);
        content.style.display = 'block'; // Show the content on hover
    });

    button.addEventListener('mouseout', function() {
        const contentId = button.getAttribute('data-content');
        const content = document.getElementById(contentId);
        content.style.display = 'none'; // Hide the content when hover is removed
    });
});
