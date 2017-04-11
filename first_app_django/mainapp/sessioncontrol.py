class MySession:

    @staticmethod
    def get_hobby_index(request):
        x = request.session.get('hobby_index')
        if x is None:
            request.session['hobby_index'] = 0

        return request.session['hobby_index']

    @staticmethod
    def set_hobby_index(request, val):
        request.session['hobby_index'] = val