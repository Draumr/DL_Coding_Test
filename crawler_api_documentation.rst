Title: 			crawler module
URL: 				/
Methods: 			GET
URL params: 		Required: url
				url=[string]
				example: url=http://www.example.com/
Success Response:	Example:
				Code: 200
				Content:{
					page_title = string
					app_timer = float
					system_time = datetime
					requests_done = int
					link_counter = int
					found_links = list
					meta_data = list
					}
Error Response:		Example:
				Code: 401 UNAUTHORIZED
				Code: 404 NOT FOUND
