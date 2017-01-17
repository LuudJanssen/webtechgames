var gamesApp = angular.module('games', []);

gamesApp.controller('gamesController', function ($scope) {
    var api = new Api('/api');
    $scope.gameSorting = 'date_added';

    // Apply selectFX on all select elements with classes cs-select
    (function () {
        [].slice.call(document.querySelectorAll('select.cs-select')).forEach(function (el) {
            new SelectFx(el, {
                onChange: updateSort
            });
        });
    })();

    api.getGames().then(function (games) {
        $scope.games = games;

        $scope.games.forEach(function (game) {
            game.highscore = null;
        });

        $('.game').each(function (i, gameElement) {
            $(gameElement).find('.photo').one('load', function () {
                correctBackgroundBlur($(gameElement).find('.cover-photo'), $(gameElement));
            });
        });

        $scope.$apply();

        api.getHighscores().then(function (highscores) {

            setGameHighs(highscores);
            $scope.$apply();
        });
    });

    function setGameHighs(highscores) {
        highscores.forEach(function (highscore) {
            $scope.games.forEach(function (game) {
                if (highscore.game_id === game.game_id && highscore.score > game.highscore) {
                    game.highscore = highscore.score;
                }
            });
        });
    }

    function updateSort(value) {
        console.log(value);
        $scope.gameSorting = value;
        $scope.$apply();
        return true;
    }
});