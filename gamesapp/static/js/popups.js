function showPopup(type) {
    $('.popup-selected').removeClass('popup-selected');
    $('.popup-blur').addClass('popup-active');

    var $popupContainer = $('.popup-container');
    $popupContainer.addClass('popup-show');
    $popupContainer.find('.popup-' + type).addClass('popup-selected');
}

function closePopup() {
    $('.popup-container').removeClass('popup-show');
    $('.popup-blur').removeClass('popup-active');
}

function preventPopupClosing(event) {
    event.stopPropagation();
}

$(document).ready(function () {
    var api = new Api('/api');

    $('.popup-container').click(closePopup);
    $('.popup').click(preventPopupClosing);

    var registerForm = $('#register_form');
    var loginForm = $('#login_form');

    registerForm.submit(function (event) {

        // Stop form from submitting normally
        event.preventDefault();

        // Register the user
        api.registerUser(registerForm.serialize()).then(function (result) {
            console.log('Registered', result);
        });
    });

    loginForm.submit(function (event) {

        // Stop form from submitting normally
        event.preventDefault();

        // Log the user in
        api.loginUser(loginForm.serialize()).then(function (result) {
            closePopup();
            setTimeout(function () {
                location.reload();
            }, 200);
        });
    });

    window.logoutUser = function () {
        api.logoutUser().then(function() {
            location.reload();
        });
    }
});