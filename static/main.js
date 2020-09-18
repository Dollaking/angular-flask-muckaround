(function () {
  'use strict';

  angular.module('JAJACInc', [])

  .controller('JAJACController', ['$scope', '$log' '$http',
    function($scope, $log, $http) {
      $scope.getResults = function() {
        $log.log("test");

        // get the firstname and colour input variables
        var first_name = $scope.first_name;
        var colour = $scope.favourite_colour;

        // fire the API request
        $http.post('/start', {"first_name": first_name}).success(function(results) {
            $log.log(results);
        })
        error(function(error) {
            $log.log(error);
        });
      };
    }
  ]);

}());

