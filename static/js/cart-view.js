function updateSubtotal(element) {
    var row = element.closest('tr');

    var priceText = row.querySelector('td:nth-child(3)').textContent;
    var price = parseFloat(priceText.replace(/[^\d.]/g, '')); // Remove ₹ or other non-numeric characters

    var quantity = parseInt(element.value);

    var subtotal = price * quantity;

    row.querySelector('.subtotal').value = subtotal.toFixed(2);

    updateTotals();
}

function updateTotals() {
    var subtotals = document.querySelectorAll('.subtotal');

    var finalTotal = 0;

    subtotals.forEach(function (subtotal) {
        finalTotal += parseFloat(subtotal.value);
    });

    var gst = finalTotal * 0.18;

    var invoiceTotal = finalTotal + gst;

    document.getElementById('total-value').textContent = finalTotal.toFixed(2) + " /-";
    document.getElementById('gst-value').textContent = gst.toFixed(2) + " /-";
    document.getElementById('invoice-total-value').textContent = invoiceTotal.toFixed(2) + " /-";

    // If the final-amount field exists, update it
    var finalAmountField = document.getElementById('final-amount');
    if (finalAmountField) {
        finalAmountField.value = invoiceTotal.toFixed(2);
    }
}

document.addEventListener("DOMContentLoaded", function () {
    updateTotals(); // Ensure totals are calculated on page load
});
