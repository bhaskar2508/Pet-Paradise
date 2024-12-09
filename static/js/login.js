    function showPopup(message) {
        const popup = document.createElement('div');
        popup.id = 'popupMessage';
        popup.textContent = message;

        document.body.appendChild(popup);

        popup.style.display = 'block';

        setTimeout(() => {
            popup.style.display = 'none';
            popup.remove();
        }, 4000); 
    }
