(function(angular){
	'use strict';

	angular.module('myApp', [])
		.config(function($interpolateProvider){
    			$interpolateProvider.startSymbol('//');
   	 		$interpolateProvider.endSymbol('//');
		}).controller('DemoController', function($scope){
      			$scope.label = "This binding is brought you by // interpolation symbols.";
  		});

})(window.angular);