from icecream import ic
import inspect

def menu(request):
    main_menu = [
        {'title': "About the site", 'url_name': 'about', 'class': ''},
        {'title': "Add article", 'url_name': 'add_page', 'class': ''},
        {'title': "Feedback", 'url_name': 'contact', 'class': ''},
        {'title': "Register", 'url_name': 'register', 'class': ''},
        {'title': "Login", 'url_name': 'login', 'class': 'last'},
        # {'title': "Logout", 'url_name': 'logout', 'class': 'last'},
    ]
    if request and request.user.is_authenticated:
        main_menu[4] = {
            'title': f"Logout {request.user.username}",
            "url_name": "logout",
            "class": "last"
        }
    # else:
    #     main_menu.pop(3)
    current_frame = inspect.currentframe()
    previous_frame = current_frame.f_back
    ic(previous_frame.f_code.co_name, request, request.user.username)
    return main_menu


# class Menumixin:

#     @staticmethod
#     def get_menu(request):
#         main_menu = [
#             {'title': "About the site", 'url_name': 'about', 'class': ''},
#             {'title': "Add article", 'url_name': 'add_page', 'class': ''},
#             {'title': "Feedback", 'url_name': 'contact', 'class': ''},
#             {'title': "Register", 'url_name': 'register', 'class': ''},
#             {'title': "Login", 'url_name': 'login', 'class': 'last'},
#         ]
#         if request and request.user.is_authenticated:
#             main_menu[4] = {
#                 'title': "Logout",
#                 "url_name": "logout",
#                 "class": "last"
#             }

#         return main_menu

#     def get_context_data(self, **kwargs):
#         self.extra_context['menu'] = Menumixin.get_menu(self.request)
#         return super().get_context_data(**kwargs)
