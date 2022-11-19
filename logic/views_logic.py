from rest_framework.exceptions import PermissionDenied


def permissions_only(permissions: set):
    def wrapper(func):
        def view_method(view, *args, **kwargs):
            for perm in permissions:
                if not view.request.user.has_perm(perm):
                    raise PermissionDenied()
            return func(view, *args, **kwargs)
        return view_method
    return wrapper

