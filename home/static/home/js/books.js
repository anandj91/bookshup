homeApp.controller("CategoryController", 
	function ($scope, $http){
		// Populating Categories
		$http.get('/books/categories').success(
				function (data) {
					$scope.categories=data;
				}
			);

		// Auto-complete option in search
    $('#search').autocomplete({
		    source: '/books',
		    select: function (event,ui) {
					        $("#search").val(ui.item.label);
					        return false;
	  						}	
			}
		);
	}
);

homeApp.controller("SearchController",
	function ($scope) {
		$scope.searchPage="home";
	}
);