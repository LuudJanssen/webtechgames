/**
 * Get the url inside the background-image CSS property.
 *
 * @param {jQuery} $element A jQuery element you want to retrieve the background-image URL from
 * @returns {String} Returns what's inside the url() in the background-image property.
 */
function getBackgroundImageUrl($element) {
    return $element.css('background-image').replace(/.*\s?url\(['"]?/, '').replace(/['"]?\).*/, '');
}

/**
 * Load image inside a new IMG element and return it
 *
 * @param {String} url The URL of the image to load
 * @returns {jQuery} The newly created jQuery element
 */
function loadImage(url) {
    return $('<img />', {
        src: url
    });
}

/**
 * When blurring an element the sides of blurring default to white. This function gets the dominant color
 * from the image and adds that color as background color of the container.
 *
 * @param $element The element you want to correct.
 * @param $elementContainer The container of the element to apply the background color to;
 */
function correctBackgroundBlur($element, $elementContainer) {

    // Make a colorThief instance to get the dominant image color
    var colorThief = new ColorThief();

    // Get the image URL
    var imageUrl = getBackgroundImageUrl($element);

    // Make new element with the loaded image to use with colorThief
    var $imagePlaceholder = loadImage(imageUrl);

    // Let colorThief get the colors and apply them to the element's container
    var colors = colorThief.getColor($imagePlaceholder[0]);
    $elementContainer.css('background-color', 'rgb(' + colors.join() + ')');
}

function getQueryParams() {
    qs = document.location.search;
    qs = qs.split('+').join(' ');

    var params = {},
        tokens,
        re = /[?&]?([^=]+)=([^&]*)/g;

    while (tokens = re.exec(qs)) {
        params[decodeURIComponent(tokens[1])] = decodeURIComponent(tokens[2]);
    }

    return params;
}