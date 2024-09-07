// Disappear the Flashy Messages after their Animation is DONE.

document.addEventListener('DOMContentLoaded', function () {
    const messages = document.querySelectorAll('.messages .alert-message');
    
    messages.forEach((message) => {
        setTimeout(function () {
            message.remove();
        }, 6000);
    });
});