homeApp.controller("CategoryController", 
	function ($scope, $http){
		$http.get('/books/categories').success(
				function (data) {
					$scope.categories=data;
				}
			);
	}
);