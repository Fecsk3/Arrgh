document.addEventListener('DOMContentLoaded', function() {
    var membersSelect = document.getElementById('members');
    var titleInput = document.getElementById('title');
    var messageTextarea = document.getElementById('message');
    var submitButton = document.querySelector('button[type="submit"]');

    // Ha a felhasználó nem staff vagy superuser, letiltjuk az űrlap elemeit
    if (!is_staff || !is_superuser) {
        membersSelect.disabled = true;
        titleInput.disabled = true;
        messageTextarea.disabled = true;
        submitButton.disabled = true;
    }
});

