var homeApp = angular.module("homeApp", []);

homeApp.controller("MainController", 
	function ($scope){
		$scope.mainPage = "home";
});

// For Breadcrumbs
function pushPath($scope, path){

}

function popPath($scope){

}

