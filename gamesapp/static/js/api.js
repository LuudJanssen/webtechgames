$(document).ready(function () {
    var getCookie = function (name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});

function Api(apiRoot, dummy) {
    this.apiRoot = apiRoot;
    this.dummy = dummy || false;
}

Api.prototype.getGames = function () {
    return this._request('games/', 'GET');
};

Api.prototype.getGame = function (gameId) {
    if (this.dummy) {
        return this._dummyRequest([
            {
                "url": "http://127.0.0.1:8000/games/1/",
                "gameId": "snakegame",
                "name": "Snake Game",
                "description": "A snake needs food",
                "location": "snakegame",
                "genre": "highscore",
                "timesPlayed": 5,
                "dateAdded": "2017-01-16T10:54:22"
            }
        ]);
    }
    return this._request('games/' + gameId, 'GET');
};

Api.prototype.getHighscores = function (gameId, userId) {
    return this._request('highscores/' + ( gameId ? ('/' + gameId + ( userId ? ('/' + userId) : '')) : ''), 'GET');
};

Api.prototype.setHighscore = function (gameId, userId, highscore) {
    return this._request('highscores/' + gameId + '/' + userId + '/', 'POST', {score: highscore});
};

Api.prototype.registerUser = function (data) {
    return this._request('user/register/', 'POST', data);
};

Api.prototype.loginUser = function (data) {
    return this._request('user/login/', 'POST', data);
};

Api.prototype.logoutUser = function () {
    return this._request('user/logout/', 'GET');
};

Api.prototype._request = function (url, method, data) {
    var fullUrl = this.apiRoot + '/' + url;

    if (method === 'GET') {
        return $.get(fullUrl);
    } else {
        return $.post(fullUrl, data);
    }
};

Api.prototype._dummyRequest = function (sendBackData) {
    return {
        then: function (fn) {
            setTimeout(function () {
                fn(sendBackData)
            }, 200);
        }
    }
};