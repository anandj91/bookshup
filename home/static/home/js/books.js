homeApp.controller("CategoryController", 
	function ($scope, $http){
		/*
		  Populating Categories
		*/
		$http.get('/books/categories').success(
			function (data) {
				$scope.categories = data;
			}
		);

		/*
		  Auto-complete option in search
		*/
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
		/*
			Search page tabs. Book,Shop etc
		*/
		$scope.searchPage = "";
	}
);

homeApp.controller("BookSearchController",
	function ($scope, $http) {
		/*
			Tab selection
		*/
		$scope.isTabSet = function (t) {
			return $scope.tab === t;
		};
		$scope.setTab = function (t) {
			$scope.tab = t;

			/*
				Populating books
			*/
			function setTabContent(url){
				$http.get(url).success(
					function (data) {
						$scope.books = data;
					}
				);
			}
			if (t === 'bs0') {
				setTabContent('/books/?order=rating');
			} else if (t === 'bs1') {
				setTabContent('/books/?order=price');
			}
			
		}

		/*
			Initializations
		*/
		$scope.setTab("bs0");
		
	}
);