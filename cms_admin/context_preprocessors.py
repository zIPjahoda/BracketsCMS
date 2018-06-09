def full_user_name(request):
    result_dictionary = {}
    if request.user.is_authenticated():
        result_dictionary["user_full_name"] = request.user.first_name + " " + request.user.last_name
        result_dictionary["logged_in"] = True
    else:
        result_dictionary["logged_in"] = False

    return result_dictionary

